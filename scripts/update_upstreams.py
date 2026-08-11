#!/usr/bin/env python3
"""Check or atomically refresh the four pinned upstream source snapshots."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
LOCK_PATH = ROOT / "upstreams.lock.json"
SOURCES = {
    "source-a": {
        "repository": "aaron-he-zhu/aaron-marketing-skills",
        "url": "https://github.com/aaron-he-zhu/aaron-marketing-skills.git",
        "path": "upstreams/source-a",
        "license": "Apache-2.0",
    },
    "source-b": {
        "repository": "AgriciDaniel/claude-seo",
        "url": "https://github.com/AgriciDaniel/claude-seo.git",
        "path": "upstreams/source-b",
        "license": "MIT",
    },
    "source-c": {
        "repository": "zubair-trabzada/geo-seo-claude",
        "url": "https://github.com/zubair-trabzada/geo-seo-claude.git",
        "path": "upstreams/source-c",
        "license": "MIT",
    },
    "source-d": {
        "repository": "coreyhaines31/marketingskills",
        "url": "https://github.com/coreyhaines31/marketingskills.git",
        "path": "upstreams/source-d",
        "license": "MIT",
    },
}


class UpdateError(RuntimeError):
    """Raised when an upstream snapshot cannot be produced safely."""


def run(*args: str, cwd: Path | None = None) -> str:
    try:
        return subprocess.check_output(
            args, cwd=cwd, text=True, stderr=subprocess.STDOUT
        ).strip()
    except FileNotFoundError as exc:
        raise UpdateError(f"required command is unavailable: {args[0]}") from exc
    except subprocess.CalledProcessError as exc:
        raise UpdateError(f"command failed: {' '.join(args)}\n{exc.output}") from exc


def load_lock() -> dict:
    try:
        data = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise UpdateError(f"cannot read {LOCK_PATH.name}: {exc}") from exc
    if data.get("schema_version") != 1 or not isinstance(data.get("sources"), dict):
        raise UpdateError(f"unsupported or malformed {LOCK_PATH.name}")
    return data


def safe_relative(raw: str) -> Path:
    posix = PurePosixPath(raw)
    if posix.is_absolute() or not raw or ".." in posix.parts:
        raise UpdateError(f"unsafe tracked path: {raw!r}")
    return Path(*posix.parts)


def tracked_paths(clone: Path) -> list[Path]:
    output = subprocess.check_output(
        ["git", "-C", str(clone), "ls-files", "-z"]
    )
    return [safe_relative(item.decode("utf-8")) for item in output.split(b"\0") if item]


def snapshot_clone(clone: Path, destination: Path) -> int:
    destination.mkdir(parents=True, exist_ok=False)
    paths = tracked_paths(clone)
    for relative in paths:
        source = clone / relative
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if source.is_symlink():
            link_target = os.readlink(source)
            link_path = PurePosixPath(link_target.replace("\\", "/"))
            if link_path.is_absolute() or ".." in link_path.parts:
                raise UpdateError(f"unsafe symlink in upstream: {relative} -> {link_target}")
            try:
                target.symlink_to(link_target)
            except OSError:
                # Windows may require Developer Mode or elevated rights for symlinks.
                # Git represents a disabled symlink checkout as this same target text.
                target.write_text(link_target, encoding="utf-8")
        elif source.is_file():
            shutil.copy2(source, target)
        else:
            raise UpdateError(f"unsupported tracked entry: {relative}")
    return len(paths)


def tree_digest(root: Path) -> str:
    """Hash paths and bytes, normalizing symlinks for cross-platform checkouts."""
    digest = hashlib.sha256()
    entries = sorted(
        (path for path in root.rglob("*") if path.is_file() or path.is_symlink()),
        key=lambda path: path.relative_to(root).as_posix(),
    )
    for path in entries:
        relative = path.relative_to(root).as_posix().encode("utf-8")
        payload = os.readlink(path).encode("utf-8") if path.is_symlink() else path.read_bytes()
        digest.update(relative)
        digest.update(b"\0")
        digest.update(payload)
        digest.update(b"\0")
    return digest.hexdigest()


def clone_head(source_id: str, workspace: Path) -> tuple[Path, str]:
    source = SOURCES[source_id]
    clone = workspace / f"clone-{source_id}"
    run("git", "clone", "--quiet", "--depth", "1", source["url"], str(clone))
    commit = run("git", "rev-parse", "HEAD", cwd=clone)
    return clone, commit


def write_lock(data: dict) -> None:
    temporary = LOCK_PATH.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    os.replace(temporary, LOCK_PATH)


def apply_snapshots(selected: list[str], clones: dict[str, tuple[Path, str]], workspace: Path) -> dict:
    lock = load_lock()
    staged: dict[str, Path] = {}
    records: dict[str, dict] = {}
    for source_id in selected:
        clone, commit = clones[source_id]
        stage = workspace / f"snapshot-{source_id}"
        file_count = snapshot_clone(clone, stage)
        source = SOURCES[source_id]
        staged[source_id] = stage
        records[source_id] = {
            **source,
            "commit": commit,
            "file_count": file_count,
            "tree_sha256": tree_digest(stage),
        }

    backups: dict[str, Path] = {}
    installed: list[str] = []
    try:
        for source_id in selected:
            target = ROOT / SOURCES[source_id]["path"]
            backup = workspace / f"backup-{source_id}"
            if target.exists() or target.is_symlink():
                os.replace(target, backup)
                backups[source_id] = backup
            target.parent.mkdir(parents=True, exist_ok=True)
            os.replace(staged[source_id], target)
            installed.append(source_id)
        lock["audited_on"] = date.today().isoformat()
        for source_id, record in records.items():
            lock["sources"][source_id] = record
        write_lock(lock)
    except Exception:
        for source_id in reversed(installed):
            target = ROOT / SOURCES[source_id]["path"]
            if target.exists() or target.is_symlink():
                shutil.rmtree(target) if target.is_dir() and not target.is_symlink() else target.unlink()
            if source_id in backups:
                os.replace(backups[source_id], target)
        raise
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", action="append", choices=sorted(SOURCES), default=[])
    parser.add_argument(
        "--apply",
        action="store_true",
        help="replace selected snapshots and update the lockfile after fetching",
    )
    args = parser.parse_args()
    selected = args.source or list(SOURCES)
    lock = load_lock()

    try:
        # Keep staging on the repository filesystem so directory replacements are
        # atomic even when the operating-system temp directory is another volume.
        with tempfile.TemporaryDirectory(
            prefix=".marketing-agent-os-upstreams-", dir=ROOT
        ) as raw:
            workspace = Path(raw)
            clones = {source_id: clone_head(source_id, workspace) for source_id in selected}
            if args.apply:
                records = apply_snapshots(selected, clones, workspace)
                print(json.dumps({"updated": records}, indent=2, sort_keys=True))
                return 0

            status = {}
            updates = False
            for source_id, (_, latest) in clones.items():
                pinned = lock["sources"].get(source_id, {}).get("commit")
                available = pinned != latest
                updates = updates or available
                status[source_id] = {
                    "pinned": pinned,
                    "latest": latest,
                    "update_available": available,
                }
            print(json.dumps({"sources": status}, indent=2, sort_keys=True))
            return 3 if updates else 0
    except UpdateError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
