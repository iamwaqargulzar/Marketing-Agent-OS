# Contributing

Marketing Agent OS has immutable upstream snapshots and a generated skill layer. `skills/`, `agents/`, and `catalog.json` are build output, so changes made there directly fail validation.

To change a skill:

1. Add local guidance in `overlays/<skill>/additions.md`, with any new files in `overlays/<skill>/references/`.
2. For a skill that has no upstream source, write the whole skill in `overlays/<skill>/SKILL.md`.
3. Change renaming, helper policy, or promotion filters in `scripts/build_skills.py`.
4. Keep skills portable; optional tools must degrade gracefully. Preserve evidence labels, permission gates, and current-source verification rules from `references/skill-contract.md`.
5. Run `python3 scripts/build_skills.py`, and update `CHANGELOG.md` and `VERSION` when the release contract changes.

For an upstream update, follow `docs/MAINTENANCE.md`. Never edit `upstreams/source-*` manually.

Before submitting a change:

```bash
python3 scripts/build_skills.py
python3 scripts/reconcile_upstreams.py --write
python3 scripts/build_manifest.py
python3 scripts/doctor.py
python3 -m unittest discover -s tests -v
npx --yes skills@1.5.22 add . --list --full-depth
```

Retain all third-party license, notice, provenance, and attribution material. Product-facing additions should use the Marketing Agent OS name.
