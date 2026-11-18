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
| `aaron-marketing-skills` | `0d4f52b376da850d5b3a8825548f39aff09d0a5b` |
| `claude-seo` | `468ed5b0d9e3249394783710e54abb02837e326b` |
| `geo-seo-claude` | `989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c` |
| `marketingskills` | `73573e94a06a39965978b3fa1f9c1eace8cebc7c` |

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

See `docs/MAINTENANCE.md` for the update workflow, `docs/UPSTREAM_REVIEW-2026-11-18.md` for the latest review decisions, and `UPSTREAM_STATUS.json` for the inventory reconciliation.
