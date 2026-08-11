---
name: geo-update
description: "Update an installed Marketing Agent OS GEO skill set safely. Use when users ask to check for GEO workflow updates, compare an installation with its configured source, or refresh GEO skills without overwriting custom work silently."
license: Apache-2.0
metadata:
  version: "1.0.0"
  domain: "seo-geo"
  provenance: "marketing-agent-os"
---

# GEO Update

Update installed GEO workflows only after identifying the installation source and obtaining permission for persistent changes.

## Workflow

1. Locate the installed skills and determine whether they came from a Git checkout, plugin installation, or copied skill folders.
2. Resolve the configured Marketing Agent OS source. Do not guess a repository or switch to an unrelated upstream project.
3. Fetch candidate files into a temporary directory and run that candidate's validation suite before comparing it with the installation.
4. Report added, changed, unchanged, and locally modified files. Treat local modifications as user-owned.
5. Ask for explicit authorization before replacing installed files or installing dependencies.
6. Apply updates through the same installer and scope originally used. Never edit host settings files as part of a skill refresh.
7. Validate the installed result and report the exact version or commit when available.

## Safety rules

- Never delete locally modified files automatically.
- Never run dependency installers without approval.
- Never update from a mutable or unverified source when a pinned release is available.
- If provenance cannot be established, stop with manual comparison instructions.

## Output

Return source identity, installed identity, validation status, diff summary, preserved customizations, actions taken, and restart requirements.
