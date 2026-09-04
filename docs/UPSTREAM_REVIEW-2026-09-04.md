# Upstream Review — 2026-09-04

This record explains how each upstream change was handled in Marketing Agent OS. Exact source files remain in `upstreams/`; only reviewed, portable behavior enters the normalized `skills/`, `references/`, `schema/`, and `scripts/` layers.

| Source | Previous commit | Reviewed commit | Normalized decision |
|---|---|---|---|
| source A | `388172e65e58f7487e22dcf436349b6003d64d0d` | `b08683918e2bab70502f3d65ab0ae2f32beff2c6` | Adopted the general lifecycle invariants as a vendor-neutral control-artifact contract, JSON schema, validator, router rule, and maintenance guidance. Preserved the source-specific runtime, generated projections, staff/bot profiles, and detailed discipline bindings only in the audited snapshot. |
| source B | `09d37bed0379dd4382e128b631312e0fe2e49750` | `a1480c7e590b16001bd9dc1627eacdcd44d580f9` | Reviewed Windows uninstall/manual installation, portability, rendered-page, JSON-LD, current Google guidance, and dependency changes. The extra HTML-cleaning dependency belongs to that source's bundled runtime and was not added to the independent standard-library installer. |
| source C | `03fd443a9b267d328ca9221f292c3b1455710066` | `9484cf0920da04448cf89ea7d710cffeddbbdcab` | Chart-asset refresh only; no normalized behavior change. |
| source D | `7868cb9251fad80a73d26e488a5ad5f6c4a9f335` | `5cd4a7eae3a9a7b5d2aceb0613f7d1f7c4b65968` | Added the new portable `events` skill and four focused event references. Existing-skill enrichment remains available in the audited snapshot; the normalized skills retain Marketing Agent OS evidence, consent, permission, and portability rules. |

## Resulting release surface

- Version: `1.2.0`
- Normalized skills: 236
- New skill: `events`
- New portable control format: `schema/control-artifact.json`
- New read-only validator: `scripts/validate_control_artifact.py`
- Source snapshots remain pinned by commit and platform-normalized tree hash in `upstreams.lock.json`.

## Validation record

The completed release must pass:

```text
python3 scripts/doctor.py
python3 -m unittest discover -s tests -v
npx --yes skills@1.5.22 add . --list --full-depth
```

The final manifest is regenerated only after all reviewed changes are complete. The release is publishable only if the doctor reports no errors or warnings, all tests pass, upstream reconciliation has no missing names, and independent discovery reports all 236 skills.
