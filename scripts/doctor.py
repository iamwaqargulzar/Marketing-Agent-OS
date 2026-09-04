#!/usr/bin/env python3
"""Validate the Marketing Agent OS package without third-party dependencies."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path

from reconcile_upstreams import reconcile
from update_upstreams import LOCK_PATH, SOURCES, tree_digest


ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
ALLOWED_FRONTMATTER = {"name", "description", "license", "metadata", "allowed-tools"}


def digest(path: Path) -> str:
    payload = os.readlink(path).encode("utf-8") if path.is_symlink() else path.read_bytes()
    return hashlib.sha256(payload).hexdigest()


def frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        return {}, ["missing opening frontmatter delimiter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, ["missing closing frontmatter delimiter"]

    values: dict[str, str] = {}
    keys: list[str] = []
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s*(.*))?$", line)
        if not match:
            continue
        key, value = match.group(1), (match.group(2) or "").strip()
        keys.append(key)
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError:
                errors.append(f"invalid quoted value for {key}")
        elif value.startswith("'") and value.endswith("'"):
            value = value[1:-1].replace("''", "'")
        values[key] = value
    duplicate = sorted({key for key in keys if keys.count(key) > 1})
    if duplicate:
        errors.append("duplicate frontmatter key(s): " + ", ".join(duplicate))
    unexpected = sorted(set(keys) - ALLOWED_FRONTMATTER)
    if unexpected:
        errors.append("unsupported frontmatter key(s): " + ", ".join(unexpected))
    return values, errors


def validate_skills(errors: list[str], warnings: list[str]) -> list[Path]:
    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    seen: set[str] = set()
    for path in skills:
        name = path.parent.name
        values, local_errors = frontmatter(path)
        for issue in local_errors:
            errors.append(f"{name}: {issue}")
        declared = values.get("name")
        description = values.get("description", "")
        if declared != name:
            errors.append(f"{name}: frontmatter name is {declared!r}")
        if name in seen:
            errors.append(f"{name}: duplicate skill name")
        seen.add(name)
        if not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"{name}: invalid skill name")
        if not 1 <= len(description) <= 1024:
            errors.append(f"{name}: description must be 1..1024 characters")
        raw_text = path.read_text(errors="replace")
        if not re.search(r'^description:\s*"(?:[^"\\]|\\.)*"\s*$', raw_text, re.MULTILINE):
            errors.append(f"{name}: description must be a JSON-compatible quoted YAML scalar")
        if len(raw_text.splitlines()) > 500:
            warnings.append(f"{name}: SKILL.md exceeds 500 lines")
        if path.is_symlink() or path.parent.is_symlink():
            errors.append(f"{name}: symlinked skills are not permitted in release source")
    return skills


def validate_catalog(skills: list[Path], errors: list[str]) -> None:
    path = ROOT / "catalog.json"
    try:
        catalog = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"catalog.json: {exc}")
        return
    if catalog.get("package") != "marketing-agent-os":
        errors.append("catalog.json: package must be marketing-agent-os")
    records = catalog.get("skills")
    if not isinstance(records, list):
        errors.append("catalog.json: skills must be a list")
        return
    names = [item.get("name") for item in records if isinstance(item, dict)]
    expected = {path.parent.name for path in skills}
    if len(names) != len(set(names)):
        errors.append("catalog.json: duplicate skill records")
    if set(names) != expected:
        errors.append("catalog.json: catalog names do not match skills directory")
    descriptions = {}
    for path in skills:
        descriptions[path.parent.name] = frontmatter(path)[0].get("description")
    for item in records:
        if not isinstance(item, dict):
            errors.append("catalog.json: non-object skill record")
            continue
        alias = item.get("alias_of")
        if alias and alias not in expected:
            errors.append(f"catalog.json: {item.get('name')} aliases missing skill {alias}")
        if item.get("description") != descriptions.get(item.get("name")):
            errors.append(f"catalog.json: {item.get('name')} description is stale")
        if not set(item.get("sources", [])) <= {"source-a", "source-b", "source-c", "source-d", "unified"}:
            errors.append(f"catalog.json: {item.get('name')} has an unknown source ID")


def validate_json(errors: list[str]) -> None:
    paths = [
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "marketplace.json",
        *sorted((ROOT / "schema").glob("*.json")),
    ]
    for path in paths:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")


def validate_versions(errors: list[str]) -> None:
    try:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        marketplace = json.loads(
            (ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8")
        )
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"version metadata: {exc}")
        return
    if not re.fullmatch(r"\d+\.\d+\.\d+", version):
        errors.append("VERSION: expected semantic version X.Y.Z")
        return
    declared = {
        "catalog.json": catalog.get("version"),
        ".claude-plugin/plugin.json": plugin.get("version"),
        ".claude-plugin/marketplace.json metadata": marketplace.get("metadata", {}).get("version"),
    }
    for item in marketplace.get("plugins", []):
        if item.get("name") == "marketing-agent-os":
            declared[".claude-plugin/marketplace.json plugin"] = item.get("version")
    for location, value in declared.items():
        if value != version:
            errors.append(f"{location}: version {value!r} differs from VERSION {version}")


def validate_upstreams(errors: list[str]) -> None:
    try:
        lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"upstreams.lock.json: {exc}")
        return
    if lock.get("schema_version") != 1:
        errors.append("upstreams.lock.json: unsupported schema version")
        return
    records = lock.get("sources")
    if not isinstance(records, dict) or set(records) != set(SOURCES):
        errors.append("upstreams.lock.json: source IDs do not match updater configuration")
        return
    for source_id, expected in SOURCES.items():
        record = records[source_id]
        if not isinstance(record, dict):
            errors.append(f"upstreams.lock.json: {source_id} is not an object")
            continue
        for key in ("repository", "url", "path", "license"):
            if record.get(key) != expected[key]:
                errors.append(f"upstreams.lock.json: {source_id} has stale {key}")
        if not re.fullmatch(r"[0-9a-f]{40}", str(record.get("commit", ""))):
            errors.append(f"upstreams.lock.json: {source_id} has an invalid commit")
        root = ROOT / expected["path"]
        if not root.is_dir():
            errors.append(f"{expected['path']}: snapshot is missing")
            continue
        entries = [path for path in root.rglob("*") if path.is_file() or path.is_symlink()]
        if record.get("file_count") != len(entries):
            errors.append(f"{expected['path']}: tracked entry count differs from lock")
        if record.get("tree_sha256") != tree_digest(root):
            errors.append(f"{expected['path']}: tree hash differs from lock")
    try:
        report, has_error = reconcile()
        status_path = ROOT / "UPSTREAM_STATUS.json"
        expected_status = json.dumps(report, indent=2, sort_keys=True) + "\n"
        if not status_path.is_file() or status_path.read_text(encoding="utf-8") != expected_status:
            errors.append("UPSTREAM_STATUS.json: stale reconciliation report")
        if has_error:
            errors.append("upstream reconciliation reports missing skills or changed snapshots")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        errors.append(f"upstream reconciliation: {exc}")


def validate_shared_copies(errors: list[str]) -> None:
    canonical = {path.name: digest(path) for path in (ROOT / "scripts").glob("*.py")}
    for path in (ROOT / "skills").glob("*/scripts/*.py"):
        expected = canonical.get(path.name)
        if expected and digest(path) != expected:
            errors.append(f"{path.relative_to(ROOT)}: differs from canonical scripts/{path.name}")
    shared_references = {
        path.name: digest(path)
        for path in (ROOT / "references").glob("*.md")
        if path.name in {
            "connectors.md",
            "control-artifacts.md",
            "product-context-schema.md",
            "routing-policy.md",
            "skill-contract.md",
        }
    }
    for path in (ROOT / "skills").glob("*/references/*.md"):
        expected = shared_references.get(path.name)
        if expected and digest(path) != expected:
            errors.append(f"{path.relative_to(ROOT)}: differs from canonical references/{path.name}")
    index = ROOT / "skills" / "marketing-os" / "references" / "skill-index.json"
    if not index.is_file() or digest(index) != digest(ROOT / "catalog.json"):
        errors.append("skills/marketing-os/references/skill-index.json: stale catalog copy")


def validate_manifest(errors: list[str]) -> None:
    path = ROOT / "SHA256SUMS.json"
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"SHA256SUMS.json: {exc}")
        return
    for relative, expected in manifest.items():
        target = ROOT / relative
        if not target.is_file():
            errors.append(f"manifest: missing {relative}")
        elif digest(target) != expected:
            errors.append(f"manifest: changed {relative}")
    actual = {
        str(path.relative_to(ROOT))
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.name != "SHA256SUMS.json"
        and not (path.parent == ROOT and path.suffix.lower() == ".zip")
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and not any(part.startswith(".marketing-agent-os-upstreams-") for part in path.parts)
        and path.suffix != ".pyc"
    }
    extra = sorted(actual - set(manifest))
    if extra:
        errors.append(f"manifest: {len(extra)} untracked file(s), first: {extra[0]}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-manifest", action="store_true")
    args = parser.parse_args()
    errors: list[str] = []
    warnings: list[str] = []
    skills = validate_skills(errors, warnings)
    validate_catalog(skills, errors)
    validate_json(errors)
    validate_versions(errors)
    validate_upstreams(errors)
    validate_shared_copies(errors)
    if not args.skip_manifest:
        validate_manifest(errors)
    result = {"skills": len(skills), "errors": errors, "warnings": warnings}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
