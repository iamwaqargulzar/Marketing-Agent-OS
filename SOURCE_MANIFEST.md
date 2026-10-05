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
| `aaron-marketing-skills` | `3f68ddad1f01a43a45e3a075ccff2d146644a4ad` |
| `claude-seo` | `4b99de2f7de7e7d5247042e5fb5b4ea9368ef734` |
| `geo-seo-claude` | `ea29bd291a0b52648ef92a80d84a2e1f89ef754b` |
| `marketingskills` | `dda3841f0b294e01e93b1541486beefbfab0915e` |

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

See `docs/MAINTENANCE.md` for the update workflow, `docs/UPSTREAM_REVIEW-2026-10-05.md` for the latest review decisions, and `UPSTREAM_STATUS.json` for the inventory reconciliation.
