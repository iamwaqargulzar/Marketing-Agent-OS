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
| `aaron-marketing-skills` | `903d6479165fe11fc32e73e0e3c8c0179ed0c55a` |
| `claude-seo` | `6be93f45064ffbadced572b5d5c95f55fd263af0` |
| `geo-seo-claude` | `989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c` |
| `marketingskills` | `88c79f6528a9347420e57ceb1fff9a60de651768` |

## Scope and structure

This repository ships both a clean normalized compatibility layer and complete snapshots of the four audited upstream commits:

- `skills/` and `agents/` are generated from the snapshots and `overlays/`. They and the related root resources form the installable Marketing Agent OS layer.
- `upstreams/source-a` through `upstreams/source-d` are unchanged tracked-file snapshots used for auditing, attribution, and future reconciliation.

`scripts/build_skills.py` generates `skills/` from these snapshots plus `overlays/`, and the updater never changes `skills/` itself. This separation prevents duplicate skill discovery, preserves local additions, and makes source changes reviewable. `upstreams.lock.json` records the exact commit, repository, entry count, license, and platform-normalized tree hash for every snapshot.

| Catalog ID | Repository |
|---|---|
| `source-a` | `aaron-marketing-skills` |
| `source-b` | `claude-seo` |
| `source-c` | `geo-seo-claude` |
| `source-d` | `marketingskills` |

See `docs/MAINTENANCE.md` for the update workflow, `docs/UPSTREAM_REVIEW-2026-11-01.md` for the latest review decisions, and `UPSTREAM_STATUS.json` for the inventory reconciliation.
