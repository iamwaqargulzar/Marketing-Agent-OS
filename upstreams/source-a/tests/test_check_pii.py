import pathlib
import shutil
import subprocess
import tempfile
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
SCANNER = ROOT / "scripts" / "check-pii.py"
PRE_COMMIT = ROOT / ".githooks" / "pre-commit"


class StagedPiiScanTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repo = pathlib.Path(self.temp.name)
        self._git("init", "-q")

    def tearDown(self):
        self.temp.cleanup()

    def _git(self, *args):
        return subprocess.run(
            ["git", "-C", str(self.repo), *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

    def _scan(self):
        return subprocess.run(
            ["python3", str(SCANNER), "--staged"],
            cwd=self.repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )

    def _scan_tracked(self):
        return subprocess.run(
            ["python3", str(SCANNER), "--tracked"],
            cwd=self.repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )

    def test_scans_index_blob_not_clean_worktree_replacement(self):
        target = self.repo / "credentials.txt"
        target.write_text("token=" + "sk-" + "A" * 24 + "\n", encoding="utf-8")
        self._git("add", "--", target.name)
        target.write_text("no credential here\n", encoding="utf-8")

        result = self._scan()

        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("OpenAI-style key", result.stdout)
        self.assertIn("credentials.txt", result.stdout)

    def test_nul_delimited_staged_path_preserves_newline_filename(self):
        target = self.repo / "line\nbreak.md"
        target.write_text("key=" + "AKIA" + "1" * 16 + "\n", encoding="utf-8")
        self._git("add", "--", target.name)

        result = self._scan()

        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("AWS access key id", result.stdout)
        self.assertIn(r"line\nbreak.md", result.stdout)
        self.assertNotIn("line\nbreak.md", result.stdout)

    def test_clean_staged_blob_passes(self):
        target = self.repo / "clean.md"
        target.write_text("public documentation only\n", encoding="utf-8")
        self._git("add", "--", target.name)

        result = self._scan()

        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("scan clean", result.stdout)

    def test_extensionless_staged_text_is_scanned(self):
        target = self.repo / "credentials"
        target.write_text("token=" + "ghp_" + "C" * 24 + "\n", encoding="utf-8")
        self._git("add", "--", target.name)

        result = self._scan()

        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("GitHub token", result.stdout)

    def test_nul_and_utf16_without_bom_cannot_hide_secrets(self):
        secret = "sk-" + "N" * 24
        nul_target = self.repo / "nul.md"
        nul_target.write_bytes(b"binary\0token=" + secret.encode("ascii") + b"\n")
        utf16_target = self.repo / "utf16.md"
        utf16_target.write_bytes(("token=" + secret + "\n").encode("utf-16-le"))
        utf16_be_target = self.repo / "utf16-be.md"
        utf16_be_target.write_bytes(("token=" + secret + "\n").encode("utf-16-be"))
        self._git("add", "--", nul_target.name, utf16_target.name, utf16_be_target.name)

        result = self._scan()

        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("nul.md", result.stdout)
        self.assertIn("utf16.md", result.stdout)
        self.assertIn("utf16-be.md", result.stdout)
        self.assertNotIn(secret, result.stdout)
        self.assertIn("[redacted]", result.stdout)

    def test_pre_commit_hook_uses_staged_mode(self):
        scripts = self.repo / "scripts"
        scripts.mkdir()
        shutil.copy2(SCANNER, scripts / "check-pii.py")
        target = self.repo / "hook-check.txt"
        target.write_text("token=" + "sk-" + "B" * 24 + "\n", encoding="utf-8")
        self._git("add", "--", target.name)
        target.write_text("clean worktree replacement\n", encoding="utf-8")

        result = subprocess.run(
            ["bash", str(PRE_COMMIT)],
            cwd=self.repo,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )

        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("OpenAI-style key", result.stdout)

    def test_tracked_mode_includes_hidden_directories_and_redacts(self):
        hidden = self.repo / ".claude" / "credentials"
        hidden.parent.mkdir()
        secret = "ghp_" + "H" * 24
        hidden.write_text("token=" + secret + "\n", encoding="utf-8")
        self._git("add", "--", str(hidden.relative_to(self.repo)))

        result = self._scan_tracked()

        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn(".claude/credentials", result.stdout)
        self.assertNotIn(secret, result.stdout)

    def test_case_insensitive_bearer_and_url_schemes_are_scanned(self):
        target = self.repo / "mixed-case-credentials.txt"
        target.write_text(
            "authorization: " + "bEaReR " + "T" * 32 + "\n"
            + "HTTPS" + "://admin:s3cret@127.0.0.1/private\n",
            encoding="utf-8",
        )
        self._git("add", "--", target.name)

        result = self._scan()

        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn("Bearer token", result.stdout)
        self.assertIn("URL-embedded credentials", result.stdout)


if __name__ == "__main__":
    unittest.main()
