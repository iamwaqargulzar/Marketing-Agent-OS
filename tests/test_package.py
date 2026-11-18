import hashlib
import http.server
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import threading
import unittest
from unittest.mock import patch
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
        self.assertEqual(names, sorted(names))
        self.assertEqual(
            catalog,
            json.loads(
                (ROOT / "skills/marketing-os/references/skill-index.json").read_text(
                    encoding="utf-8"
                )
            ),
        )

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

    def test_specialist_resources_survive_harness_installation(self):
        resources = {
            "cold-email": "outbound-operations.md",
            "prospecting": "enrichment-and-signals.md",
            "revops": "qualification-and-routing.md",
            "referrals": "reviews-and-affiliates.md",
            "launch": "release-and-site-qa.md",
            "lead-magnets": "content-library-skill.md",
            "marketing-loops": "channel-operators.md",
            "seo-audit": "local-and-query-diagnosis.md",
            "conversion-tracking": "verification.md",
            "link-building": "earned-link-plan.md",
            "seo-technical": "stack-exposure.md",
            "geo-technical": "continued.md",
            "seo-local": "skill-contract.md",
        }
        targets = {
            "codex": ".agents/skills",
            "claude-code": ".claude/skills",
            "opencode": ".opencode/skills",
            "pi": ".pi/skills",
            "amp": ".agents/skills",
            "cursor": ".cursor/skills",
        }
        for agent, destination in targets.items():
            with self.subTest(agent=agent), tempfile.TemporaryDirectory() as directory:
                args = ["--agent", agent, "--project", directory]
                for skill in resources:
                    args.extend(["--skill", skill])
                result = run_script("install.py", *args)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                for skill, reference in resources.items():
                    source = ROOT / "skills" / skill
                    installed = Path(directory) / destination / skill
                    self.assertEqual(
                        (installed / "SKILL.md").read_bytes(),
                        (source / "SKILL.md").read_bytes(),
                    )
                    self.assertTrue((installed / "references" / reference).is_file())
                    for resource in source.rglob("*"):
                        if resource.is_file():
                            self.assertEqual(
                                (installed / resource.relative_to(source)).read_bytes(),
                                resource.read_bytes(),
                            )

    def test_installed_skills_are_self_contained_and_licensed(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run_script(
                "install.py", "--project", directory,
                "--skill", "conversion-tracking", "--skill", "link-building",
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            for skill in ("conversion-tracking", "link-building"):
                installed = Path(directory) / ".agents/skills" / skill
                self.assertEqual(
                    (installed / "references/skill-contract.md").read_bytes(),
                    (ROOT / "references/skill-contract.md").read_bytes(),
                )
                self.assertTrue((installed / "LICENSE.txt").is_file())
                self.assertIn("Derived from", (installed / "NOTICE.md").read_text(encoding="utf-8"))
                self.assertFalse(list(installed.rglob("*.pyc")))
                self.assertFalse((installed / "evals").exists())
                self.assertFalse((Path(directory) / "upstreams").exists())

    def test_installed_library_preserves_every_source_entry(self):
        lock = json.loads((ROOT / "upstreams.lock.json").read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as directory:
            result = run_script("install.py", "--project", directory, "--skill", "geo-audit", "--skill", "seo-audit")
            self.assertEqual(result.returncode, 0, result.stderr)
            skills = Path(directory) / ".agents/skills"
            router = skills / "marketing-os"
            for source, record in lock["sources"].items():
                digest = hashlib.sha256()
                with tarfile.open(router / "assets" / f"{source}.tar.bz2", "r|bz2") as archive:
                    count = 0
                    for entry in archive:
                        mode = record["file_modes"].get(entry.name, "100644")
                        self.assertEqual(entry.issym(), mode == "120000", entry.name)
                        if entry.issym():
                            payload = entry.linkname.encode("utf-8")
                        else:
                            self.assertTrue(entry.isfile(), entry.name)
                            self.assertEqual(bool(entry.mode & 0o111), mode == "100755", entry.name)
                            payload = archive.extractfile(entry).read()
                        digest.update(entry.name.encode("utf-8") + b"\0" + payload + b"\0")
                        count += 1
                self.assertEqual(count, record["file_count"], source)
                self.assertEqual(digest.hexdigest(), record["tree_sha256"], source)
            result = subprocess.run([PYTHON, "scripts/validate_control_artifact.py", "--help"],
                                    cwd=router, capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            for agent in (ROOT / "agents").glob("*.md"):
                self.assertEqual((router / "references/agents" / agent.name).read_bytes(), agent.read_bytes())
                if agent.name.startswith("geo-"):
                    self.assertEqual((skills / "geo-audit/references/agents" / agent.name).read_bytes(), agent.read_bytes())
            licenses = (skills / "seo-audit/LICENSE.txt").read_bytes()
            for name in ("marketingskills-MIT.txt", "claude-seo-MIT.txt"):
                self.assertIn((ROOT / "THIRD_PARTY_LICENSES" / name).read_bytes(), licenses)

    def test_skills_keep_upstream_depth(self):
        """Guard against regressing to templated wrappers that drop the source workflow."""
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        full = [item["name"] for item in catalog["skills"] if not item["alias_of"]]
        self.assertGreaterEqual(len(full), 220)
        for name in full:
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
            self.assertNotIn("Use this skill for **", text, name)
            self.assertNotIn("## Domain Checklist", text, name)
            self.assertGreater(len(text), 1500, name)
        phrases = {
            "copywriting": "three-question gate",
            "content-writer": "Mode Selector",
            "seo-technical": "Technical",
            "geo-citability": "Citab",
        }
        for name, phrase in phrases.items():
            self.assertIn(phrase, (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8"), name)
        self.assertTrue((ROOT / "skills/seo-audit/references/full-site-audit-workflow.md").is_file())

    def test_build_is_reproducible(self):
        result = run_script("build_skills.py", "--check")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_router_points_at_real_skills(self):
        text = (ROOT / "skills/marketing-os/SKILL.md").read_text(encoding="utf-8")
        table = text[text.index("## Choosing between"):text.index("Routing does not authorize")]
        names = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
        for name in re.findall(r"`([a-z0-9-]+)`", table):
            self.assertIn(name, names)

    def test_legacy_names_delegate_to_real_skills(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        names = {item["name"] for item in catalog["skills"]}
        for item in catalog["skills"]:
            if item["alias_of"]:
                self.assertIn(item["alias_of"], names)
                self.assertIn(f"../{item['alias_of']}/SKILL.md",
                              (ROOT / "skills" / item["name"] / "SKILL.md").read_text(encoding="utf-8"))

    def test_bundled_helpers_load_and_exclude_denied_ones(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        from build_skills import DENY_HELPERS

        seen = {}
        for path in sorted((ROOT / "skills").rglob("scripts/**/*.py")):
            self.assertNotIn(path.name, DENY_HELPERS, path)
            if not path.name.startswith("_"):
                seen.setdefault(hashlib.sha256(path.read_bytes()).digest(), path)
        self.assertGreater(len(seen), 30)
        for path in seen.values():
            result = subprocess.run(
                [PYTHON, "-B", path.name, "--help"], cwd=path.parent,
                capture_output=True, text=True, timeout=60,
                env={**os.environ, "PYTHONUTF8": "1"}, encoding="utf-8", errors="replace",
            )
            self.assertEqual(result.returncode, 0, f"{path}: {result.stderr[-300:]}")

    def test_installer_rejects_unknown_and_traversal_names(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in ("does-not-exist", "../scripts"):
                result = run_script("install.py", "--project", directory, "--skill", name)
                self.assertEqual(result.returncode, 2)
                self.assertIn("Unknown skill", result.stderr)

    @unittest.skipUnless(os.name != "nt" and shutil.which("bash"), "Bash unavailable")
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
            path.write_bytes(
                (json.dumps(artifact, indent=2, sort_keys=True) + "\n").encode(
                    "utf-8"
                )
            )
            result = run_script("validate_control_artifact.py", path)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertTrue(json.loads(result.stdout)["valid"])

            artifact["authority"]["status"] = "pending"
            del artifact["authority"]["granted_at"]
            del artifact["authority"]["granted_by"]
            path.write_bytes(
                (json.dumps(artifact, indent=2, sort_keys=True) + "\n").encode(
                    "utf-8"
                )
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

    def test_fetch_page_detects_cloudflare_managed_robots(self):
        class Handler(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                self.send_header("Content-Type", "text/plain; charset=utf-8")
                self.end_headers()
                content = "User-agent: *\nAllow: /\n"
                if self.path != "/robots.txt?plain":
                    content = "# BeGiN Cloudflare Managed content\n" + content
                self.wfile.write(content.encode("utf-8"))

            def log_message(self, *_):
                pass

        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            for path, expected in (("/robots.txt", True), ("/robots.txt?plain", False), ("/", None)):
                with self.subTest(path=path):
                    result = run_script(
                        "fetch_page.py", f"http://127.0.0.1:{server.server_port}{path}",
                        "--allow-private", "--json",
                    )
                    self.assertEqual(result.returncode, 0, result.stderr)
                    output = json.loads(result.stdout)
                    if expected is None:
                        self.assertNotIn("cloudflare_managed", output)
                    else:
                        self.assertIs(output["cloudflare_managed"], expected)
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
        self.assertEqual(report["normalized_skill_count"], 243)
        self.assertTrue(
            all(source["snapshot_matches_lock"] for source in report["sources"].values())
        )
        self.assertTrue(
            all(
                source["missing_from_normalized_layer"] == []
                for source in report["sources"].values()
            )
        )

    def test_updater_restores_snapshot_when_staged_replace_fails(self):
        sys.path.insert(0, str(ROOT / "scripts"))
        import update_upstreams as updater

        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old = root / "upstreams/source-a"
            old.mkdir(parents=True)
            (old / "original").touch()
            stage = root / "snapshot-source-a"
            stage.mkdir()
            replace = os.replace

            def fail_install(source, target):
                if source == stage:
                    raise OSError("simulated filesystem failure")
                replace(source, target)

            with patch.object(updater, "ROOT", root), patch.object(updater, "file_modes", return_value={}), \
                    patch.object(updater, "snapshot_clone", return_value=0), patch.object(os, "replace", fail_install):
                with self.assertRaisesRegex(OSError, "simulated"):
                    updater.apply_snapshots(["source-a"], {"source-a": (root, "test")}, root)
            self.assertTrue((old / "original").is_file())

    def test_upstream_updater_help_is_offline(self):
        result = run_script("update_upstreams.py", "--help")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("--apply", result.stdout)


if __name__ == "__main__":
    unittest.main()
