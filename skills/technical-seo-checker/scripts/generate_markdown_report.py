#!/usr/bin/env python3
"""Turn normalized finding JSON into a Marketing Agent OS Markdown report."""

import argparse
import json
from pathlib import Path


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("json_file")
parser.add_argument("--output")
args = parser.parse_args()
data = json.loads(Path(args.json_file).read_text(encoding="utf-8"))
if isinstance(data, dict):
    summary = data.get("summary", "")
    findings = data.get("findings", [])
elif isinstance(data, list):
    summary = ""
    findings = data
else:
    raise SystemExit("Input must be a JSON object or list")
if not isinstance(findings, list) or not all(isinstance(item, dict) for item in findings):
    raise SystemExit("findings must be a list of objects")

lines = ["# Marketing Agent OS Audit Report", "", str(summary), "", "## Findings", ""]
for index, finding in enumerate(findings, 1):
    lines.extend(
        [
            f"### {index}. {finding.get('title', 'Finding')}",
            "",
            f"- Severity: {finding.get('severity', 'unspecified')}",
            f"- Evidence: {finding.get('evidence', 'not provided')}",
            f"- Recommendation: {finding.get('recommendation', 'not provided')}",
            f"- Validation: {finding.get('validation', 'not provided')}",
            "",
        ]
    )
text = "\n".join(lines)
if args.output:
    Path(args.output).write_text(text, encoding="utf-8")
else:
    print(text)
