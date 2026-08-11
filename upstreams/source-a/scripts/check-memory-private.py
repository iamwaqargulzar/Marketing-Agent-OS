#!/usr/bin/env python3
"""Fail closed before writing operational memory into a Git worktree."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys


class PrivacyError(ValueError):
    pass


MAX_HOOK_INPUT_BYTES = 4_000_000
MAX_NAMESPACE_ENTRIES = 4096
MAX_JSON_DEPTH = 64
MAX_JSON_NODES = 10_000
DIRECT_WRITERS = {"Write", "Edit", "NotebookEdit"}
PATH_KEYS = {
    "destination", "destinationpath", "dir", "directory", "file", "filename",
    "filepath", "newpath", "notebookpath", "oldpath", "outputdir", "outputfile",
    "outputpath", "path", "root", "sourcepath", "target", "targetpath",
}
COMMAND_KEYS = {"chars", "code", "command", "script"}
# Path-shaped references into the memory namespace: "memory/…" as a token
# start, "/memory" as a path component, or a shell variable assignment of the
# bare namespace name (the "d=memory; … $d/file" indirection). Deliberately
# narrower than a bare word scan so pattern arguments ("grep memory README.md",
# "--grep=memory") and prose ("in-memory") stay out of scope; renames of the
# bare directory itself are caught by the post-state namespace audit instead.
MEMORY_PATH_REFERENCE = re.compile(
    r"(?:^|[\s\"'`=:;(|&<>])\.?[/\\]?memory[/\\]"
    r"|[/\\]memory(?:[/\\]|[\s\"'`;|&<>)]|$)"
    r"|(?:^|[\s;&|(])[A-Za-z_][A-Za-z0-9_]*=([\"']?)memory\1(?=[\s;&|)]|$)",
    re.I,
)


def _has_git_marker(path: Path) -> bool:
    return any(
        (candidate / ".git").exists() or (candidate / ".git").is_symlink()
        for candidate in (path, *path.parents)
    )


def _run_git(arguments, cwd: Path):
    try:
        return subprocess.run(
            ["git", "-C", str(cwd), *arguments],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        if _has_git_marker(cwd):
            raise PrivacyError("cannot verify Git-ignore protection: %s" % exc) from exc
        return None


def _run_git_stdin(arguments, cwd: Path, value):
    try:
        return subprocess.run(
            ["git", "-C", str(cwd), *arguments],
            input=value,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise PrivacyError("cannot audit memory Git-ignore protection: %s" % exc) from exc


def _project_root(root):
    supplied_root = Path(root)
    if supplied_root.is_symlink():
        raise PrivacyError("project root cannot be a symlink")
    root_lexical = Path(os.path.abspath(supplied_root))
    root_path = supplied_root.resolve(strict=True)
    if not root_path.is_dir():
        raise PrivacyError("project root must be a directory")
    return root_lexical, root_path


def _git_root(root_path):
    probe = _run_git(["rev-parse", "--show-toplevel"], root_path)
    if probe is None:
        return None
    if probe.returncode:
        if _has_git_marker(root_path):
            raise PrivacyError(
                "cannot verify Git-ignore protection: %s"
                % (probe.stderr.strip() or "git rev-parse failed")
            )
        return None
    return Path(probe.stdout.strip()).resolve(strict=True)


def require_private_memory_path(root, raw_path):
    root_lexical, root_path = _project_root(root)

    supplied_target = Path(raw_path)
    target_lexical = supplied_target if supplied_target.is_absolute() else root_lexical / supplied_target
    target_lexical = Path(os.path.abspath(target_lexical))
    try:
        project_relative = target_lexical.relative_to(root_lexical)
    except ValueError:
        # Outside the project root: not this plugin's namespace. Deny only a
        # path that aliases back into memory/ through links; every other
        # destination is out of jurisdiction for a memory-privacy preflight.
        resolved_candidate = target_lexical.resolve(strict=False)
        try:
            outside_relative = resolved_candidate.relative_to(root_path)
        except ValueError:
            return
        if outside_relative.parts and outside_relative.parts[0].casefold() == "memory":
            raise PrivacyError("memory write target cannot use a symlink or alias path")
        return
    resolved_candidate = target_lexical.resolve(strict=False)
    try:
        resolved_candidate_relative = resolved_candidate.relative_to(root_path)
    except ValueError:
        resolved_candidate_relative = None
    lexical_memory = bool(
        project_relative.parts and project_relative.parts[0].casefold() == "memory"
    )
    resolved_memory = bool(
        resolved_candidate_relative is not None
        and resolved_candidate_relative.parts
        and resolved_candidate_relative.parts[0].casefold() == "memory"
    )
    if not lexical_memory and not resolved_memory:
        return
    if lexical_memory and project_relative.parts[0] != "memory":
        raise PrivacyError("memory namespace must use the canonical lowercase path")
    if resolved_memory and not lexical_memory:
        raise PrivacyError("memory write target cannot use a symlink or alias path")
    cursor = root_path
    last_index = len(project_relative.parts) - 1
    for index, part in enumerate(project_relative.parts):
        if part in {"", ".", ".."}:
            raise PrivacyError("memory write target contains an unsafe path component")
        cursor = cursor / part
        try:
            metadata = os.lstat(cursor)
        except FileNotFoundError:
            continue
        except OSError as exc:
            raise PrivacyError("cannot inspect memory write target: %s" % exc) from exc
        if stat.S_ISLNK(metadata.st_mode):
            raise PrivacyError("memory write target cannot traverse a symlink")
        if index < last_index and not stat.S_ISDIR(metadata.st_mode):
            raise PrivacyError("memory write target parent must be a directory")
        if index == last_index:
            if stat.S_ISREG(metadata.st_mode) and metadata.st_nlink != 1:
                raise PrivacyError("memory write target cannot be a hard-linked file")
            if not (stat.S_ISREG(metadata.st_mode) or stat.S_ISDIR(metadata.st_mode)):
                raise PrivacyError("memory write target must be a regular file or directory")
    target = (root_path / project_relative).resolve(strict=False)
    try:
        resolved_relative = target.relative_to(root_path)
    except ValueError as exc:
        raise PrivacyError("write target escapes the project root") from exc
    if not resolved_relative.parts or resolved_relative.parts[0].casefold() != "memory":
        raise PrivacyError("memory write target resolves outside memory/")

    git_root = _git_root(root_path)
    if git_root is None:
        return
    try:
        git_relative = target.relative_to(git_root)
    except ValueError as exc:
        raise PrivacyError("memory target escapes the containing Git worktree") from exc
    ignored = _run_git(["check-ignore", "--quiet", "--", str(git_relative)], git_root)
    if ignored is None or ignored.returncode != 0:
        detail = "path is tracked or is not ignored"
        if ignored is not None and ignored.returncode > 1 and ignored.stderr.strip():
            detail = ignored.stderr.strip()
        raise PrivacyError(
            "refusing memory write because %s is not Git-ignored: %s"
            % (git_relative, detail)
        )


def require_private_memory_namespace(root):
    """Verify current operational files plus a future memory path are protected."""
    audit_private_memory_namespace(root)
    require_private_memory_path(root, "memory/.aaron-private-write-probe")


def _static_memory_path(relative):
    parts = relative.parts
    return parts == ("README.md",) or bool(parts and parts[0] == "templates")


def audit_private_memory_namespace(root):
    """Fail if an existing operational memory file is tracked, unignored, or unsafe."""
    _, root_path = _project_root(root)
    git_root = _git_root(root_path)
    if git_root is not None:
        try:
            memory_git_relative = (root_path / "memory").relative_to(git_root)
        except ValueError as exc:
            raise PrivacyError("memory namespace escapes the containing Git worktree") from exc
        tracked = _run_git(["ls-files", "-z", "--", str(memory_git_relative)], git_root)
        if tracked is None or tracked.returncode:
            detail = tracked.stderr.strip() if tracked is not None else "git unavailable"
            raise PrivacyError("cannot audit tracked memory paths: %s" % detail)
        for tracked_path in (item for item in tracked.stdout.split("\0") if item):
            try:
                relative = Path(tracked_path).relative_to(memory_git_relative)
            except ValueError as exc:
                raise PrivacyError("Git returned a memory path outside the project root") from exc
            if not _static_memory_path(relative):
                raise PrivacyError("Git index tracks operational memory: %s" % tracked_path)
    try:
        memory_roots = [
            Path(entry.path) for entry in os.scandir(root_path)
            if entry.name.casefold() == "memory"
        ]
    except OSError as exc:
        raise PrivacyError("cannot inspect project root for memory: %s" % exc) from exc
    if not memory_roots:
        return
    if len(memory_roots) != 1 or memory_roots[0].name != "memory":
        raise PrivacyError("memory namespace must use the canonical lowercase path")
    memory_root = memory_roots[0]
    try:
        root_metadata = os.lstat(memory_root)
    except OSError as exc:
        raise PrivacyError("cannot inspect memory namespace: %s" % exc) from exc
    if stat.S_ISLNK(root_metadata.st_mode) or not stat.S_ISDIR(root_metadata.st_mode):
        raise PrivacyError("memory namespace must be a real directory")

    stack = [memory_root]
    entry_count = 0
    operational_git_paths = []
    while stack:
        directory = stack.pop()
        try:
            with os.scandir(directory) as iterator:
                entries = list(iterator)
        except OSError as exc:
            raise PrivacyError("cannot traverse memory namespace: %s" % exc) from exc
        for entry in entries:
            entry_count += 1
            if entry_count > MAX_NAMESPACE_ENTRIES:
                raise PrivacyError(
                    "memory namespace exceeds %d-entry audit limit" % MAX_NAMESPACE_ENTRIES
                )
            path = Path(entry.path)
            try:
                metadata = entry.stat(follow_symlinks=False)
            except OSError as exc:
                raise PrivacyError("cannot inspect memory entry: %s" % exc) from exc
            relative = path.relative_to(memory_root)
            if stat.S_ISLNK(metadata.st_mode):
                raise PrivacyError("memory namespace cannot contain symlinks: %s" % relative)
            if stat.S_ISDIR(metadata.st_mode):
                stack.append(path)
                continue
            if not stat.S_ISREG(metadata.st_mode):
                raise PrivacyError("memory namespace contains a special file: %s" % relative)
            if metadata.st_nlink != 1:
                raise PrivacyError("memory namespace contains a hard-linked file: %s" % relative)
            if git_root is None or _static_memory_path(relative):
                continue
            try:
                git_relative = path.relative_to(git_root)
            except ValueError as exc:
                raise PrivacyError("memory entry escapes the containing Git worktree") from exc
            operational_git_paths.append(str(git_relative))
    if operational_git_paths:
        payload = "\0".join(operational_git_paths) + "\0"
        ignored = _run_git_stdin(["check-ignore", "-z", "--stdin"], git_root, payload)
        if ignored.returncode not in (0, 1):
            raise PrivacyError(
                "cannot audit memory Git-ignore protection: %s"
                % (ignored.stderr.strip() or "git check-ignore failed")
            )
        protected = {item for item in ignored.stdout.split("\0") if item}
        missing = [path for path in operational_git_paths if path not in protected]
        if missing:
            raise PrivacyError(
                "operational memory file is tracked or not Git-ignored: %s" % missing[0]
            )


def _string_leaves(value, key=""):
    stack = [(value, key, 0)]
    nodes = 0
    while stack:
        current, current_key, depth = stack.pop()
        nodes += 1
        if nodes > MAX_JSON_NODES or depth > MAX_JSON_DEPTH:
            raise PrivacyError("hook input exceeds bounded JSON traversal limits")
        if isinstance(current, str):
            yield current_key, current
        elif isinstance(current, dict):
            for child_key, child in current.items():
                normalized = re.sub(r"[^a-z]", "", str(child_key).lower())
                stack.append((child, normalized, depth + 1))
        elif isinstance(current, list):
            stack.extend((child, current_key, depth + 1) for child in current)


def _path_lands_in_memory(root, raw_path):
    """Lexically decide whether a path field points into <root>/memory."""
    if "\0" in str(raw_path):
        raise PrivacyError("path field contains an unsupported control byte")
    root_lexical, root_path = _project_root(root)
    supplied = Path(raw_path)
    target_lexical = supplied if supplied.is_absolute() else root_lexical / supplied
    target_lexical = Path(os.path.abspath(target_lexical))
    try:
        relative = target_lexical.relative_to(root_lexical)
    except ValueError:
        relative = None
    if relative is not None and relative.parts and relative.parts[0].casefold() == "memory":
        return True
    resolved = target_lexical.resolve(strict=False)
    try:
        resolved_relative = resolved.relative_to(root_path)
    except ValueError:
        return False
    return bool(resolved_relative.parts and resolved_relative.parts[0].casefold() == "memory")


def preflight_hook_input(root, hook_input):
    if not isinstance(hook_input, dict):
        raise PrivacyError("hook input must be a JSON object")
    tool_name = hook_input.get("tool_name")
    tool_input = hook_input.get("tool_input")
    if not isinstance(tool_name, str) or not isinstance(tool_input, dict):
        raise PrivacyError("hook input requires tool_name and object tool_input")
    leaves = list(_string_leaves(tool_input))
    path_values = [value for key, value in leaves if key in PATH_KEYS]
    if tool_name in DIRECT_WRITERS and not path_values:
        raise PrivacyError("cannot determine the direct write target")
    if tool_name in DIRECT_WRITERS:
        for raw_path in path_values:
            require_private_memory_path(root, raw_path)
    else:
        command_values = [value for key, value in leaves if key in COMMAND_KEYS]
        if any(MEMORY_PATH_REFERENCE.search(value) for value in command_values) or any(
            _path_lands_in_memory(root, value) for value in path_values
        ):
            raise PrivacyError(
                "opaque shell/MCP memory mutations are unsupported; use an exact-path direct "
                "writer or the registry runtime"
            )


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Verify that a memory/** write target is outside Git tracking before writing."
    )
    parser.add_argument("--root", required=True, help="Host project root.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--path", help="Prospective write path, absolute or project-relative.")
    mode.add_argument(
        "--hook-input", action="store_true",
        help="Read one PreToolUse JSON object from stdin and inspect all supported path fields.",
    )
    mode.add_argument(
        "--namespace", action="store_true",
        help="Verify current operational memory plus a representative future path.",
    )
    mode.add_argument(
        "--audit-namespace", action="store_true",
        help="Audit every existing operational memory file after a write-capable call.",
    )
    args = parser.parse_args(argv)
    try:
        if args.hook_input:
            raw = sys.stdin.buffer.read(MAX_HOOK_INPUT_BYTES + 1)
            if len(raw) > MAX_HOOK_INPUT_BYTES:
                raise PrivacyError("hook input exceeds size limit")
            try:
                hook_input = json.loads(raw.decode("utf-8"))
            except (UnicodeDecodeError, ValueError, RecursionError) as exc:
                raise PrivacyError("hook input must be UTF-8 JSON") from exc
            preflight_hook_input(args.root, hook_input)
        elif args.namespace:
            require_private_memory_namespace(args.root)
        elif args.audit_namespace:
            audit_private_memory_namespace(args.root)
        else:
            require_private_memory_path(args.root, args.path)
    except (OSError, PrivacyError, subprocess.SubprocessError) as exc:
        print("memory privacy preflight failed: %s" % exc, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
