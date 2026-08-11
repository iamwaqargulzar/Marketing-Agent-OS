#!/usr/bin/env python3
"""Fill string placeholders in a JSON-LD template without guessing facts."""

import argparse
import json
import re
from pathlib import Path


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("template")
parser.add_argument("--set", action="append", default=[], metavar="KEY=VALUE")
parser.add_argument("--output")
args = parser.parse_args()
raw = Path(args.template).read_text(encoding="utf-8")
values: dict[str, str] = {}
for item in args.set:
    if "=" not in item:
        parser.error("--set requires KEY=VALUE")
    key, value = item.split("=", 1)
    if not key:
        parser.error("--set key cannot be empty")
    values[key] = value

placeholders = set(re.findall(r"\{\{([^}]+)\}\}", raw))
missing = sorted(placeholders - set(values))
unknown = sorted(set(values) - placeholders)
if missing:
    raise SystemExit("Missing explicit values: " + ", ".join(missing))
if unknown:
    raise SystemExit("Unknown template values: " + ", ".join(unknown))
for key, value in values.items():
    escaped = json.dumps(value, ensure_ascii=False)[1:-1]
    raw = raw.replace("{{" + key + "}}", escaped)
result = json.dumps(json.loads(raw), indent=2, ensure_ascii=False) + "\n"
if args.output:
    Path(args.output).write_text(result, encoding="utf-8")
else:
    print(result, end="")
