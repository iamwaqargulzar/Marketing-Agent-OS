#!/usr/bin/env python3
"""PII / secret scanner — Python 3 stdlib only.

Ported (the detection half only) from common pre-commit secret scanners; the
vendor-attribution / CTA-block half is deliberately NOT included. Fails closed
on high-confidence secrets and non-allowlisted emails so credentials can't be
committed into this public skill library.

Scans repo files (a filesystem walk minus SKIP_DIRS); NUL-bearing and UTF-16
content is decoded through bounded text views rather than skipped. Phone/IPv4
detection is intentionally omitted — a content/SEO repo is full of numbers and they
produce false positives. Allowlists are token/anchored, never whole-line, so a real
secret on a line that also contains a placeholder word is still caught.

Usage:
  python3 scripts/check-pii.py                 # scan the repo (CI gate; exit 1 on finding)
  python3 scripts/check-pii.py path [path ...] # scan specific paths
  python3 scripts/check-pii.py --staged        # scan blobs in the Git index
  python3 scripts/check-pii.py --tracked       # scan every tracked blob in the Git index
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {".git", "reference-oss", "node_modules", "__pycache__", ".agents", ".claude"}

# High-confidence secret patterns (name, regex).
PATTERNS = [
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9]{20,}\b")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}\b")),
    ("GitHub fine-grained PAT", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b")),
    ("AWS access key id", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z_\-]{30,}\b")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Bearer token", re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{24,}\b", re.I)),
    ("Private key block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----")),
    ("URL-embedded credentials", re.compile(
        r"\b[a-z][a-z0-9+.\-]*://[^/\s:@]+:[^/\s:@]+@", re.I)),
    ("US SSN", re.compile(r"\b\d{3}-\d{2}-\d{4}\b")),
]

EMAIL = re.compile(r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b")
# Email allowlist is ANCHORED, not substring: a full placeholder local-part OR an allowlisted domain.
# (A substring test would leak a real address whose local-part merely ENDS in user/name/test/you.)
EMAIL_LOCAL_ALLOW = {"user", "name", "test", "you", "noreply", "example", "email"}
EMAIL_DOMAIN_ALLOW = ("example.com", "example.org", "example.net", "anthropic.com",
                      "your-domain.com", "yourdomain.com", "zhuhe.io")  # zhuhe.io = project public contact
# Exact-address allowlist — the strongest anchor: the WHOLE address must match.
# For fixture placeholders whose domains can't be domain-allowed (gmail.com /
# outlook.com carry real mail — a domain allow would exempt real addresses) and
# for third parties' own published public contacts.
EMAIL_FULL_ALLOW = {
    # connector test/docstring fixtures (tests/, scripts/connectors/resend.py,
    # email/deliver/inbox-placement-monitor/) — provider domains are the point
    # of seed-list examples, so they can't be rewritten to example.com
    "me@x.dev", "a@y.com", "me@my.dom", "r@my.dom", "me@my.domain",
    "s1@gmail.com", "s2@outlook.com", "seed1@gmail.com", "seed2@outlook.com",
    # published public contact of agentskills.me (docs/registry-submissions.md)
    "hi@evergreenai.cn",
    # Product Hunt's own published API-terms contact (their ToS requires naming
    # it for business-use requests — quoted in producthunt.py + CONNECTORS.md)
    "hello@producthunt.com",
    # Existing public commit-identity aliases intentionally recorded in .mailmap.
    "139607425+aaron-he-zhu@users.noreply.github.com",
    "aaron@aarons-macbook-air.local", "smzdm@aaronmbp.local",
    "zhuhe1983@gmail.com",
}
# Placeholder fragments that exonerate a matched SECRET-LIKE TOKEN — applied to the matched token ONLY,
# never the whole line (whole-line skipping would let a real key on a "placeholder"/"example" line slip).
TOKEN_PLACEHOLDER = ("xxxx", "redacted", "placeholder", "example", "akiaiosfodnn7example", "your-token")


def _email_allowed(email):
    lowered = email.lower()
    if lowered in EMAIL_FULL_ALLOW:
        return True
    local, _, domain = lowered.partition("@")
    return local in EMAIL_LOCAL_ALLOW or domain in EMAIL_DOMAIN_ALLOW


def _token_allowed(tok):
    t = tok.lower()
    return any(frag in t for frag in TOKEN_PLACEHOLDER)


def scan_text(text):
    findings = []
    for n, line in enumerate(text.splitlines(), 1):
        for name, pat in PATTERNS:
            for m in pat.finditer(line):
                if _token_allowed(m.group(0)):
                    continue
                findings.append((n, name, "[redacted]"))
        for m in EMAIL.finditer(line):
            if not _email_allowed(m.group(0)):
                findings.append((n, "email address", "[redacted]"))
    return findings


def scan_bytes(data):
    """Scan UTF-8/binary bytes plus plausible UTF-16 views without fail-open skips."""
    encodings = ["utf-8"]
    if data.startswith((b"\xff\xfe", b"\xfe\xff")):
        encodings.insert(0, "utf-16")
    elif b"\0" in data:
        encodings.extend(("utf-16-le", "utf-16-be"))
    findings = set()
    for encoding in encodings:
        findings.update(scan_text(data.decode(encoding, "replace")))
    return sorted(findings)


def scan_file(path):
    try:
        data = open(path, "rb").read()
    except OSError as e:
        return [(0, "unreadable file", str(e))]
    return scan_bytes(data)


def iter_targets(paths):
    for p in paths:
        if os.path.isfile(p):
            yield p
            continue
        for dirpath, dirnames, filenames in os.walk(p):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                yield os.path.join(dirpath, fn)


def _git(root, *args):
    return subprocess.run(
        ["git", "-C", root, *args], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, check=False,
    )


def _display_path(path):
    """Escape control characters so one finding always occupies one line."""
    return path.encode("unicode_escape", "backslashreplace").decode("ascii")


def _index_blobs(root, listing_arguments):
    """Yield ``(path, bytes)`` selected from the index with NUL-delimited names.

    Reading ``:<path>`` with ``git cat-file`` ensures an unstaged worktree edit
    cannot hide a secret already staged. NUL framing preserves spaces, tabs,
    and newlines in valid Git paths without line-oriented splitting.
    """
    listing = _git(root, *listing_arguments)
    if listing.returncode:
        raise RuntimeError(
            "cannot list staged paths: %s"
            % listing.stderr.decode("utf-8", "replace").strip()
        )
    for raw_path in listing.stdout.split(b"\0"):
        if not raw_path:
            continue
        path = os.fsdecode(raw_path)
        blob = _git(root, "cat-file", "blob", ":" + path)
        if blob.returncode:
            raise RuntimeError(
                "cannot read staged blob %s: %s"
                % (_display_path(path), blob.stderr.decode("utf-8", "replace").strip())
            )
        yield path, blob.stdout


def staged_blobs(root):
    return _index_blobs(
        root,
        ("diff", "--cached", "--no-renames", "--name-only", "--diff-filter=ACMR", "-z"),
    )


def tracked_blobs(root):
    """Yield every tracked index blob, including dot-directories and symlinks."""
    return _index_blobs(root, ("ls-files", "-z"))


def _print_findings(records, root):
    total = 0
    for path, findings in records:
        for n, name, snippet in findings:
            total += 1
            display = _display_path(os.path.relpath(path, root))
            print("FAIL  %s:%d  %s  ::  [redacted]" % (display, n, name))
    if total:
        print("\nPII/SECRET SCAN FAILED — %d finding(s). Redact or add to the allowlist if a false positive." % total)
        return 1
    print("PII/secret scan clean.")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group()
    source.add_argument("--staged", action="store_true",
                        help="Scan added/changed blobs from the Git index.")
    source.add_argument("--tracked", action="store_true",
                        help="Scan every tracked blob from the Git index.")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args(argv)
    if (args.staged or args.tracked) and args.paths:
        parser.error("--staged/--tracked do not accept filesystem paths")
    if args.staged or args.tracked:
        top = _git(os.getcwd(), "rev-parse", "--show-toplevel")
        if top.returncode:
            print("PII/SECRET SCAN FAILED — not inside a Git worktree", file=sys.stderr)
            return 1
        root = os.fsdecode(top.stdout.rstrip(b"\r\n"))
        try:
            selected_blobs = staged_blobs(root) if args.staged else tracked_blobs(root)
            records = (
                (os.path.join(root, path), scan_bytes(data))
                for path, data in selected_blobs
            )
            return _print_findings(records, root)
        except RuntimeError as exc:
            print("PII/SECRET SCAN FAILED — %s" % exc, file=sys.stderr)
            return 1
    paths = args.paths or [ROOT]
    records = ((path, scan_file(path)) for path in iter_targets(paths))
    return _print_findings(records, ROOT)


if __name__ == "__main__":
    sys.exit(main())
