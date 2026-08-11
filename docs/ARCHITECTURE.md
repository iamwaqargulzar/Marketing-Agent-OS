# Architecture

Marketing Agent OS separates source preservation from runtime distribution.

## Installable layer

`skills/` contains 235 uniquely named, portable Agent Skills. Every skill uses a constrained frontmatter contract, and `catalog.json` is the canonical discovery inventory. Shared references and deterministic helper scripts are maintained at the repository root and validated against copies embedded in skills.

`agents/`, `schema/`, `tools/`, `references/`, and `assets/` provide specialist prompts, structured-data templates, optional connector contracts, governance rules, and reusable context. The root `.claude-plugin/` files expose the same installable layer as a Claude Code plugin without duplicating the payload.

## Source layer

`upstreams/source-a` through `source-d` preserve all tracked entries from four exact Git commits. `upstreams.lock.json` authenticates each snapshot with the repository URL, commit, entry count, license, and a cross-platform tree hash. Symlink payloads are normalized in that hash so validation remains stable on Windows checkouts that materialize symlinks as ordinary files.

The updater replaces only source snapshots. It never modifies the normalized layer automatically; a human-readable diff must be reviewed and intentionally reconciled.

## Distribution layer

`scripts/install.py` projects selected skills into a target harness directory. `install.sh` and `install.ps1` provide Linux/macOS and Windows entry points. Installation is staged and replaced atomically, validates requested names against the catalog, and does not include `upstreams/`.

The universal target uses `.agents/skills`; native projections cover hosts with different discovery paths. Selective installation is preferred when a harness has a tight context or discovery budget.

## Integrity layer

- `scripts/doctor.py` validates skill metadata, catalogs, shared copies, JSON, upstream pins, and the release hash manifest.
- `scripts/reconcile_upstreams.py` proves that every declared upstream skill name is represented by the normalized layer.
- `SHA256SUMS.json` detects any unrecorded package change.
- `tests/test_package.py` exercises installers, wrappers, validators, security boundaries, helpers, and source reconciliation.
