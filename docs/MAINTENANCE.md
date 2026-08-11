# Upstream maintenance

This workflow keeps Marketing Agent OS current without silently replacing local behavior.

## 1. Check

```bash
python3 scripts/update_upstreams.py
```

The default mode is read-only. It shallow-clones each current default branch into a temporary directory, compares HEAD with `upstreams.lock.json`, prints JSON, and exits `3` when an update is available. Network or Git failures exit `2`.

## 2. Review before applying

Inspect the upstream commit range on GitHub. Review at least:

- new, removed, or renamed skills and agents;
- changed trigger descriptions, workflows, scripts, and connector assumptions;
- security-sensitive network, shell, filesystem, publishing, or credential behavior;
- new dependencies and operating-system assumptions;
- license, notice, and attribution changes.

Do not copy an upstream directory over `skills/`. Resolve overlapping names into one governed Marketing Agent OS implementation.

## 3. Refresh the pinned snapshot

Update one source at a time so its diff remains reviewable:

```bash
python3 scripts/update_upstreams.py --source source-a --apply
```

`--apply` clones and stages tracked files, validates paths and symlinks, atomically replaces the selected snapshot, and updates its lock record. If replacement fails, the previous snapshot is restored.

## 4. Reconcile the normalized layer

```bash
python3 scripts/reconcile_upstreams.py --write
```

The command fails if a snapshot no longer matches its lock or any declared upstream skill name is absent from `skills/`. For every source diff, either update an existing normalized skill, add a portable skill, or record why the change does not affect the installable surface.

Synchronize `catalog.json` and `skills/marketing-os/references/skill-index.json` after adding or changing skills. Keep source-specific identities out of product-facing files except provenance and legally required material.

## 5. Validate and record

```bash
python3 scripts/build_manifest.py
python3 scripts/doctor.py
python3 -m unittest discover -s tests -v
npx --yes skills@1.5.22 add . --list --full-depth
```

Confirm the portable discovery count, smoke-test affected harness targets, update the pinned CLI version deliberately when its compatibility registry changes, update `CHANGELOG.md`, and commit the upstream snapshot, lockfile, normalized changes, status report, licenses/notices, and regenerated hash manifest together.

Some pinned sources contain their own `.gitignore` files. When a reviewed source update adds an intentionally tracked file that matches one of those nested rules, stage the preserved snapshot explicitly with `git add -f upstreams/` so the Git commit remains complete.

## Recovery

The updater is all-or-nothing for the selected sources during a run. If a later review rejects an applied update, restore the affected files through normal version-control history; do not edit a pinned snapshot by hand.
