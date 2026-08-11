# Source Manifest and Reconstruction Notes

This package was designed after a capability-level audit of four public repositories:

- https://github.com/aaron-he-zhu/aaron-marketing-skills
- https://github.com/AgriciDaniel/claude-seo
- https://github.com/zubair-trabzada/geo-seo-claude
- https://github.com/coreyhaines31/marketingskills

## Audited revisions

The package was checked against these upstream revisions on 2026-08-11:

| Repository | Commit |
|---|---|
| `aaron-marketing-skills` | `388172e65e58f7487e22dcf436349b6003d64d0d` |
| `claude-seo` | `09d37c7b66ed3ca9c6efbdb765a805a6c76a8f01` |
| `geo-seo-claude` | `03fd44d02412889705aa01a635c585c4fa3b1584` |
| `marketingskills` | `7868cb9251fad80a73d26e488a5ad5f6c4a9f335` |

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

See `docs/MAINTENANCE.md` for the update workflow and `UPSTREAM_STATUS.json` for the latest inventory reconciliation.
