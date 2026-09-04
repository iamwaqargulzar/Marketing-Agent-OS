# Source Manifest and Reconstruction Notes

This package was designed after a capability-level audit of four public repositories:

- https://github.com/aaron-he-zhu/aaron-marketing-skills
- https://github.com/AgriciDaniel/claude-seo
- https://github.com/zubair-trabzada/geo-seo-claude
- https://github.com/coreyhaines31/marketingskills

## Audited revisions

The package was checked against these upstream revisions. The snapshot date reflects the latest completed reconciliation cycle.

| Repository | Commit |
|---|---|
| `aaron-marketing-skills` | `b08683918e2bab70502f3d65ab0ae2f32beff2c6` |
| `claude-seo` | `a1480c7e590b16001bd9dc1627eacdcd44d580f9` |
| `geo-seo-claude` | `9484cf0920da04448cf89ea7d710cffeddbbdcab` |
| `marketingskills` | `5cd4a7eae3a9a7b5d2aceb0613f7d1f7c4b65968` |

## Scope and structure

This repository ships both a clean normalized compatibility layer and complete snapshots of the four audited upstream commits:

- `skills/`, `agents/`, `scripts/`, and related root resources are the installable Marketing Agent OS layer.
- `upstreams/source-a` through `upstreams/source-d` are unchanged tracked-file snapshots used for auditing, attribution, and future reconciliation.

The updater never merges upstream files directly into `skills/`. This separation prevents duplicate skill discovery, preserves local governance improvements, and makes source changes reviewable. `upstreams.lock.json` records the exact commit, repository, entry count, license, and platform-normalized tree hash for every snapshot.

| Catalog ID | Repository |
|---|---|
| `source-a` | `aaron-marketing-skills` |
| `source-b` | `claude-seo` |
| `source-c` | `geo-seo-claude` |
| `source-d` | `marketingskills` |

See `docs/MAINTENANCE.md` for the update workflow, `docs/UPSTREAM_REVIEW-2026-09-04.md` for the latest review decisions, and `UPSTREAM_STATUS.json` for the inventory reconciliation.
