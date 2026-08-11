#!/usr/bin/env python3
"""Compare pinned upstream skill inventories with the normalized skill layer."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from update_upstreams import LOCK_PATH, ROOT, SOURCES, tree_digest


NAME_LINE = re.compile(r"^name:\s*(.+?)\s*$", re.MULTILINE)


def declared_name(path: Path) -> str | None:
    match = NAME_LINE.search(path.read_text(encoding="utf-8", errors="replace"))
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value.strip() or None


def reconcile() -> tuple[dict, bool]:
    lock = json.loads(LOCK_PATH.read_text(encoding="utf-8"))
    normalized = {path.parent.name for path in (ROOT / "skills").glob("*/SKILL.md")}
    report: dict = {
        "schema_version": 1,
        "normalized_skill_count": len(normalized),
        "sources": {},
    }
    has_error = False
    for source_id, source in SOURCES.items():
        root = ROOT / source["path"]
        skill_files = sorted(root.rglob("SKILL.md")) if root.is_dir() else []
        names = [name for path in skill_files if (name := declared_name(path))]
        unique = set(names)
        missing = sorted(unique - normalized)
        record = lock.get("sources", {}).get(source_id, {})
        expected_hash = record.get("tree_sha256")
        actual_hash = tree_digest(root) if root.is_dir() else None
        snapshot_matches_lock = bool(expected_hash and expected_hash == actual_hash)
        if missing or not snapshot_matches_lock:
            has_error = True
        report["sources"][source_id] = {
            "commit": record.get("commit"),
            "snapshot_path": source["path"],
            "tracked_entries": record.get("file_count"),
            "skill_files": len(skill_files),
            "declared_names": len(names),
            "unique_skill_names": len(unique),
            "missing_from_normalized_layer": missing,
            "snapshot_matches_lock": snapshot_matches_lock,
        }
    return report, has_error


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="write UPSTREAM_STATUS.json")
    args = parser.parse_args()
    try:
        report, has_error = reconcile()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.write:
        destination = ROOT / "UPSTREAM_STATUS.json"
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_text(rendered, encoding="utf-8")
        os.replace(temporary, destination)
        print(destination)
    else:
        print(rendered, end="")
    return 1 if has_error else 0


if __name__ == "__main__":
    sys.exit(main())
