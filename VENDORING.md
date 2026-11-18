# Upstream snapshots

The four complete source snapshots are already committed under `upstreams/` and pinned by `upstreams.lock.json`. The build also ships all four trees in the installed router as deterministic archives. Git modes in the lock preserve executable files and symlinks across build platforms.

Check current default branches without changing local files:

```bash
python3 scripts/update_upstreams.py
```

After reviewing upstream releases, commits, diffs, and license changes, refresh selected snapshots explicitly:

```bash
python3 scripts/update_upstreams.py --source source-a --apply
python3 scripts/build_skills.py
python3 scripts/reconcile_upstreams.py --write
```

`scripts/vendor_upstreams.py` remains as a compatibility alias for the updater. New automation should use `scripts/update_upstreams.py`.

Never flatten `upstreams/` into `skills/`: overlapping names would create conflicting discovery surfaces. See `docs/MAINTENANCE.md` for the complete review and validation sequence.
