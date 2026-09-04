import hashlib
import http.server
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


def run_script(name, *args):
    return subprocess.run(
        [PYTHON, str(ROOT / "scripts" / name), *map(str, args)],
        capture_output=True,
        text=True,
    )


class PackageTests(unittest.TestCase):
    def test_catalog_matches_skills(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        names = [item["name"] for item in catalog["skills"]]
        folders = [path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")]
        self.assertEqual(set(names), set(folders))
        self.assertEqual(len(names), len(set(names)))
        self.assertEqual(catalog, json.loads((ROOT / "skills/marketing-os/references/skill-index.json").read_text()))

    def test_doctor(self):
        result = run_script("doctor.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(result.stdout)["errors"], [])

    def test_installer_dry_run_for_documented_agents(self):
        with tempfile.TemporaryDirectory() as directory:
            for agent in (
                "universal", "codex", "opencode", "claude-code", "pi", "cursor",
                "gemini", "copilot", "amp", "cline", "roo", "windsurf",
                "openclaw", "hermes", "all",
            ):
                result = run_script(
                    "install.py",
                    "--agent",
                    agent,
                    "--scope",
                    "project",
                    "--project",
                    directory,
                    "--skill",
                    "marketing-os",
                    "--dry-run",
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_installer_actual_and_force(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run_script(
                "install.py",
                "--agent",
                "pi",
                "--project",
                directory,
                "--skill",
                "marketing-os",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            target = Path(directory) / ".pi/skills/marketing-os"
            self.assertTrue((target / "SKILL.md").is_file())
            (target / "local-change.txt").write_text("replace me", encoding="utf-8")
            result = run_script(
                "install.py",
                "--agent",
                "pi",
                "--project",
                directory,
                "--skill",
                "marketing-os",
                "--force",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertFalse((target / "local-change.txt").exists())

    def test_installer_rejects_unknown_and_traversal_names(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in ("does-not-exist", "../scripts"):
                result = run_script("install.py", "--project", directory, "--skill", name)
                self.assertEqual(result.returncode, 2)
                self.assertIn("Unknown skill", result.stderr)

    @unittest.skipUnless(shutil.which("bash"), "Bash unavailable")
    def test_shell_wrapper(self):
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    "bash",
                    str(ROOT / "install.sh"),
                    "--agent",
                    "universal",
                    "--project",
                    directory,
                    "--skill",
                    "marketing-os",
                    "--dry-run",
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    @unittest.skipUnless(shutil.which("pwsh") or shutil.which("powershell"), "PowerShell unavailable")
    def test_powershell_wrapper(self):
        executable = shutil.which("pwsh") or shutil.which("powershell")
        with tempfile.TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    executable,
                    "-NoProfile",
                    "-File",
                    str(ROOT / "install.ps1"),
                    "-Agent",
                    "universal",
                    "-Project",
                    directory,
                    "-Skill",
                    "marketing-os",
                    "-DryRun",
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_schema_generator_escapes_values(self):
        result = run_script(
            "schema_generator.py",
            ROOT / "schema/organization.json",
            "--set",
            'name=Example "Quoted"',
            "--set",
            "url=https://example.com",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["name"], 'Example "Quoted"')

    def test_score_validation(self):
        result = run_script(
            "seo_health_score.py",
            "--technical",
            "90",
            "--content",
            "80",
            "--on-page",
            "85",
            "--schema",
            "70",
            "--performance",
            "75",
            "--ai-readiness",
            "80",
            "--images",
            "90",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["score"], 82.2)
        invalid = run_script(
            "seo_health_score.py",
            "--technical",
            "101",
            "--content",
            "80",
            "--on-page",
            "85",
            "--schema",
            "70",
            "--performance",
            "75",
            "--ai-readiness",
            "80",
            "--images",
            "90",
        )
        self.assertNotEqual(invalid.returncode, 0)

    def test_control_artifact_validation(self):
        artifact = {
            "action": {
                "payload_sha256": "a" * 64,
                "scope": "publish one approved repository release",
                "type": "publish",
            },
            "artifact_id": "release:1.2.0",
            "authority": {
                "granted_at": "2026-09-04T10:00:00Z",
                "granted_by": "repository owner",
                "required": True,
                "scope": "publish one approved repository release",
                "status": "granted",
            },
            "created_at": "2026-09-04T09:00:00Z",
            "idempotency_key": "release:1.2.0:publish",
            "inputs": [{"evidence_label": "measured", "ref": "test-report"}],
            "objective": "Publish the validated release",
            "owner": "release operator",
            "revision": 1,
            "schema_version": "1.0",
            "state": "approved",
            "updated_at": "2026-09-04T10:00:00Z",
        }
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "control.json"
            path.write_text(
                json.dumps(artifact, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            result = run_script("validate_control_artifact.py", path)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(json.loads(result.stdout)["valid"])

            artifact["authority"]["status"] = "pending"
            del artifact["authority"]["granted_at"]
            del artifact["authority"]["granted_by"]
            path.write_text(
                json.dumps(artifact, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            result = run_script("validate_control_artifact.py", path)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertFalse(json.loads(result.stdout)["valid"])

    def test_fetch_page_blocks_private_network_by_default(self):
        result = run_script("fetch_page.py", "http://127.0.0.1:9", "--json")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("blocked", result.stderr)

    def test_fetch_page_local_opt_in_and_size_limit(self):
        payload = b"<html><head><title>Test</title></head><body><h1>Hi</h1></body></html>"

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.end_headers()
                self.wfile.write(payload)

            def log_message(self, *_):
                pass

        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            url = f"http://127.0.0.1:{server.server_port}"
            result = run_script("fetch_page.py", url, "--allow-private", "--json")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(result.stdout)["h1_count"], 1)
            limited = run_script(
                "fetch_page.py",
                url,
                "--allow-private",
                "--max-bytes",
                "10",
            )
            self.assertNotEqual(limited.returncode, 0)
        finally:
            server.shutdown()
            server.server_close()

    def test_manifest_is_sorted_and_complete(self):
        manifest = json.loads((ROOT / "SHA256SUMS.json").read_text(encoding="utf-8"))
        self.assertEqual(list(manifest), sorted(manifest))
        self.assertTrue(all("\\" not in relative for relative in manifest))
        for relative, expected in manifest.items():
            path = ROOT / relative
            payload = os.readlink(path).encode("utf-8") if path.is_symlink() else path.read_bytes()
            actual = hashlib.sha256(payload).hexdigest()
            self.assertEqual(actual, expected, relative)

    def test_upstream_snapshots_reconcile(self):
        result = run_script("reconcile_upstreams.py")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(report["normalized_skill_count"], 236)
        self.assertTrue(
            all(source["snapshot_matches_lock"] for source in report["sources"].values())
        )
        self.assertTrue(
            all(
                source["missing_from_normalized_layer"] == []
                for source in report["sources"].values()
            )
        )

    def test_upstream_updater_help_is_offline(self):
        result = run_script("update_upstreams.py", "--help")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("--apply", result.stdout)


if __name__ == "__main__":
    unittest.main()
