# Contributing

Marketing Agent OS has a normalized runtime layer and immutable upstream snapshots. Keep those responsibilities separate.

For a normalized skill change:

1. Use a unique lowercase hyphenated directory under `skills/` with a `SKILL.md` whose frontmatter name matches the directory.
2. Write a specific trigger description and keep the skill portable; optional tools must degrade gracefully.
3. Preserve evidence labels, permission gates, and current-source verification rules from `references/skill-contract.md`.
4. Update `catalog.json` and its exact copy at `skills/marketing-os/references/skill-index.json`.
5. Update `CHANGELOG.md` and `VERSION` when the release contract changes.

For an upstream update, follow `docs/MAINTENANCE.md`. Never edit `upstreams/source-*` manually or copy those trees directly into `skills/`.

Before submitting a change:

```bash
python3 scripts/reconcile_upstreams.py --write
python3 scripts/build_manifest.py
python3 scripts/doctor.py
python3 -m unittest discover -s tests -v
npx --yes skills@1.5.22 add . --list --full-depth
```

Retain all third-party license, notice, provenance, and attribution material. Product-facing additions should use the Marketing Agent OS name.
