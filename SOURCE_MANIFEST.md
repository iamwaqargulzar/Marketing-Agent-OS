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
| `aaron-marketing-skills` | `79c145da991dd00dad3c0b94b23a18ef27482456` |
| `claude-seo` | `23a2a811f874361d228fc2681acfc0ad66272736` |
| `geo-seo-claude` | `989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c` |
| `marketingskills` | `e85f3cbc2e4a79bf33b2a12e9bdd9087d414735b` |

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

See `docs/MAINTENANCE.md` for the update workflow, `docs/UPSTREAM_REVIEW-2026-10-22.md` for the latest review decisions, and `UPSTREAM_STATUS.json` for the inventory reconciliation.
