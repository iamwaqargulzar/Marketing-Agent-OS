#!/usr/bin/env python3
"""Behavior tests for the host-project memory Git-ignore preflight."""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


def load_module():
    path = ROOT / "scripts" / "check-memory-private.py"
    spec = importlib.util.spec_from_file_location("check_memory_private", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class MemoryPrivacyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.module = load_module()

    def git(self, root, *arguments):
        return subprocess.run(
            ["git", "-C", str(root), *arguments],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )

    def test_non_git_project_allows_local_memory(self):
        with tempfile.TemporaryDirectory() as directory:
            self.module.require_private_memory_path(directory, "memory/hot-cache.md")

    def test_non_memory_write_does_not_require_memory_ignore(self):
        with tempfile.TemporaryDirectory() as directory:
            self.git(directory, "init", "--quiet")
            self.module.require_private_memory_path(directory, "README.md")

    def test_unignored_memory_is_rejected_before_creation(self):
        with tempfile.TemporaryDirectory() as directory:
            self.git(directory, "init", "--quiet")
            target = Path(directory) / "memory" / "events" / "consent.ndjson"
            with self.assertRaisesRegex(self.module.PrivacyError, "not Git-ignored"):
                self.module.require_private_memory_path(directory, target)
            self.assertFalse(target.exists())

    def test_ignored_memory_is_allowed(self):
        with tempfile.TemporaryDirectory() as directory:
            self.git(directory, "init", "--quiet")
            (Path(directory) / ".gitignore").write_text("memory/**\n", encoding="utf-8")
            self.module.require_private_memory_path(directory, "memory/audits/content/report.md")

    def test_force_tracked_memory_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            (root / ".gitignore").write_text("memory/**\n", encoding="utf-8")
            target = root / "memory" / "hot-cache.md"
            target.parent.mkdir()
            target.write_text("sensitive\n", encoding="utf-8")
            self.git(root, "add", "-f", "memory/hot-cache.md")
            with self.assertRaisesRegex(self.module.PrivacyError, "tracked or is not ignored"):
                self.module.require_private_memory_path(root, target)

    def test_outside_root_target_is_out_of_jurisdiction(self):
        with tempfile.TemporaryDirectory() as directory:
            # A destination outside the project root is not this plugin's
            # namespace: the preflight must not police it.
            self.module.require_private_memory_path(directory, "../elsewhere/private.md")
            self.module.require_private_memory_path(directory, "/tmp/aaron-preflight-probe.md")

    def test_outside_root_alias_into_memory_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "memory").mkdir()
            with tempfile.TemporaryDirectory() as elsewhere:
                alias = Path(elsewhere) / "alias"
                try:
                    alias.symlink_to(root / "memory", target_is_directory=True)
                except (OSError, NotImplementedError) as exc:
                    self.skipTest("symlinks unavailable: %s" % exc)
                with self.assertRaisesRegex(self.module.PrivacyError, "symlink or alias"):
                    self.module.require_private_memory_path(root, alias / "hot-cache.md")

    def test_symlinked_memory_parent_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "actual-memory").mkdir()
            try:
                (root / "memory").symlink_to(root / "actual-memory", target_is_directory=True)
            except (OSError, NotImplementedError) as exc:
                self.skipTest("symlinks unavailable: %s" % exc)
            with self.assertRaisesRegex(self.module.PrivacyError, "cannot traverse a symlink"):
                self.module.require_private_memory_path(root, "memory/private.md")

    def test_existing_hard_link_target_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "memory").mkdir()
            outside = root / "outside.txt"
            outside.write_text("do not overwrite\n", encoding="utf-8")
            target = root / "memory" / "hot-cache.md"
            try:
                os.link(outside, target)
            except (OSError, NotImplementedError) as exc:
                self.skipTest("hard links unavailable: %s" % exc)
            with self.assertRaisesRegex(self.module.PrivacyError, "hard-linked"):
                self.module.require_private_memory_path(root, target)
            self.assertEqual(outside.read_text(encoding="utf-8"), "do not overwrite\n")

    def test_opaque_namespace_rejects_any_force_tracked_memory(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            (root / ".gitignore").write_text("memory/**\n", encoding="utf-8")
            target = root / "memory" / "events" / "secret.ndjson"
            target.parent.mkdir(parents=True)
            target.write_text("secret\n", encoding="utf-8")
            self.git(root, "add", "-f", "memory/events/secret.ndjson")
            with self.assertRaisesRegex(self.module.PrivacyError, "index tracks operational"):
                self.module.require_private_memory_namespace(root)

    def test_hook_input_finds_mcp_destination_and_bash_variable(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            mcp = {
                "tool_name": "mcp__filesystem__write_file",
                "tool_input": {"destination": "memory/events/secret.ndjson", "content": "x"},
            }
            with self.assertRaisesRegex(self.module.PrivacyError, "opaque shell/MCP"):
                self.module.preflight_hook_input(root, mcp)
            bash = {
                "tool_name": "Bash",
                "tool_input": {"command": 'd=memory; printf x > "$d/hot-cache.md"'},
            }
            with self.assertRaisesRegex(self.module.PrivacyError, "opaque shell/MCP"):
                self.module.preflight_hook_input(root, bash)

    def test_hook_input_blocks_memory_namespace_paths_only(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            denied = [
                "cat memory/hot-cache.md > /tmp/x",
                "tee %s/memory/audit.md" % root,
                "rm -rf ./memory/",
            ]
            for command in denied:
                payload = {"tool_name": "Bash", "tool_input": {"command": command}}
                with self.assertRaisesRegex(self.module.PrivacyError, "opaque shell/MCP"):
                    self.module.preflight_hook_input(root, payload)
            allowed = [
                "grep -rn memory README.md",
                "git log --grep=memory",
                "echo the in-memory cache design",
                "python3 -c 'print(\"memory\")'",
                "sysctl hw.memsize && vm_stat",
            ]
            for command in allowed:
                payload = {"tool_name": "Bash", "tool_input": {"command": command}}
                self.module.preflight_hook_input(root, payload)

    def test_hook_input_allows_writes_outside_the_project_root(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            for tool in ("Write", "Edit"):
                payload = {
                    "tool_name": tool,
                    "tool_input": {"file_path": "/tmp/aaron-scratch/report.md", "content": "x"},
                }
                self.module.preflight_hook_input(root, payload)
            mcp = {
                "tool_name": "mcp__filesystem__write_file",
                "tool_input": {"destination": "/tmp/aaron-scratch/out.json", "content": "x"},
            }
            self.module.preflight_hook_input(root, mcp)

    def test_case_variant_and_symlink_alias_to_memory_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            (root / ".gitignore").write_text("memory/**\n", encoding="utf-8")
            with self.assertRaisesRegex(self.module.PrivacyError, "canonical lowercase"):
                self.module.require_private_memory_path(root, "Memory/hot-cache.md")
            (root / "memory").mkdir()
            try:
                (root / "alias").symlink_to(root / "memory", target_is_directory=True)
            except (OSError, NotImplementedError) as exc:
                self.skipTest("symlinks unavailable: %s" % exc)
            with self.assertRaisesRegex(self.module.PrivacyError, "symlink or alias"):
                self.module.require_private_memory_path(root, "alias/hot-cache.md")

    def test_namespace_allows_static_templates_but_audits_operational_files(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            (root / ".gitignore").write_text(
                "memory/**\n!memory/\n!memory/README.md\n!memory/templates/\n"
                "!memory/templates/**\n",
                encoding="utf-8",
            )
            template = root / "memory" / "templates" / "hot-cache.md"
            template.parent.mkdir(parents=True)
            template.write_text("template\n", encoding="utf-8")
            (root / "memory" / "README.md").write_text("docs\n", encoding="utf-8")
            self.git(root, "add", ".gitignore", "memory/README.md", str(template.relative_to(root)))
            runtime = root / "memory" / "events" / "consent.ndjson"
            runtime.parent.mkdir()
            runtime.write_text("{}\n", encoding="utf-8")
            self.module.require_private_memory_namespace(root)

            (root / ".gitignore").write_text("", encoding="utf-8")
            with self.assertRaisesRegex(self.module.PrivacyError, "not Git-ignored"):
                self.module.audit_private_memory_namespace(root)

    def test_post_state_audit_catches_alias_write_not_visible_in_command_text(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            (root / "memory").mkdir()
            try:
                (root / "alias").symlink_to(root / "memory", target_is_directory=True)
            except (OSError, NotImplementedError) as exc:
                self.skipTest("symlinks unavailable: %s" % exc)
            (root / "alias" / "hot-cache.md").write_text("private\n", encoding="utf-8")
            with self.assertRaisesRegex(self.module.PrivacyError, "not Git-ignored"):
                self.module.audit_private_memory_namespace(root)

    def test_post_state_audit_catches_tracked_operational_blob_after_file_deletion(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            (root / ".gitignore").write_text("memory/**\n", encoding="utf-8")
            target = root / "memory" / "events" / "secret.ndjson"
            target.parent.mkdir(parents=True)
            target.write_text("private\n", encoding="utf-8")
            self.git(root, "add", "-f", str(target.relative_to(root)))
            target.unlink()
            with self.assertRaisesRegex(self.module.PrivacyError, "index tracks operational"):
                self.module.audit_private_memory_namespace(root)

    def test_hook_input_ignores_memory_word_in_direct_write_content(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.git(root, "init", "--quiet")
            payload = {
                "tool_name": "Write",
                "tool_input": {"file_path": "README.md", "content": "Document memory behavior."},
            }
            self.module.preflight_hook_input(root, payload)

    def test_deep_hook_json_is_rejected_without_recursion_failure(self):
        with tempfile.TemporaryDirectory() as directory:
            nested = {}
            cursor = nested
            for _ in range(self.module.MAX_JSON_DEPTH + 2):
                cursor["nested"] = {}
                cursor = cursor["nested"]
            payload = {
                "tool_name": "Write",
                "tool_input": {"file_path": "README.md", "metadata": nested},
            }
            with self.assertRaisesRegex(self.module.PrivacyError, "traversal limits"):
                self.module.preflight_hook_input(directory, payload)

    def test_parser_deep_hook_json_fails_cleanly_without_traceback(self):
        with tempfile.TemporaryDirectory() as directory:
            nested = "[" * 400_000 + "]" * 400_000
            payload = (
                '{"tool_name":"Write","tool_input":{"file_path":"README.md",'
                '"metadata":' + nested + "}}"
            )
            result = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "scripts/check-memory-private.py"),
                    "--root", directory, "--hook-input",
                ],
                input=payload,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )
        self.assertEqual(result.returncode, 1)
        self.assertIn("hook input must be UTF-8 JSON", result.stderr)
        self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
