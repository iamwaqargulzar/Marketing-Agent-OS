#!/usr/bin/env python3
"""Build the deterministic SHA-256 release manifest."""

import hashlib
import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "SHA256SUMS.json"


def included(path: Path) -> bool:
    return (
        path.is_file()
        and path != OUTPUT
        and not (path.parent == ROOT and path.suffix.lower() == ".zip")
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and not any(part.startswith(".marketing-agent-os-upstreams-") for part in path.parts)
        and path.suffix != ".pyc"
    )


manifest = {
    str(path.relative_to(ROOT)): hashlib.sha256(
        os.readlink(path).encode("utf-8") if path.is_symlink() else path.read_bytes()
    ).hexdigest()
    for path in sorted(ROOT.rglob("*"))
    if included(path)
}
OUTPUT.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"{len(manifest)} files")
