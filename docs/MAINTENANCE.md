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

When an upstream adds orchestration or execution controls, preserve the useful invariant without importing a vendor-specific runtime blindly. Prefer the portable control-artifact contract for cross-skill or side-effecting workflows, and validate machine artifacts with:

```bash
python3 scripts/validate_control_artifact.py path/to/control-artifact.json
```

Treat routing changes as behavior changes: compare new trigger language with `catalog.json`, verify every declared upstream name remains covered, and add a focused regression test when a changed boundary could misroute common requests.

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

## 6. Publish and verify the release

A commit, push, or `VERSION` change does not publish a GitHub release. For an authorized public version update, push the reviewed commit and wait for its cross-platform validation workflow to pass. Publish the version in `VERSION` against that exact tested commit, with reviewed release notes covering every change since the last published release:

```bash
gh release create vX.Y.Z --repo iamwaqargulzar/Marketing-Agent-OS --target FULL_TESTED_COMMIT_SHA --title "Marketing Agent OS vX.Y.Z" --notes-file /path/to/release-notes.md --latest
```

Replace the version, commit, and notes path with verified values. Do not use `--draft` for a release intended to be public. GitHub automatically provides ZIP and tar.gz source archives for the release tag.

Verify publication separately from the command's success:

```bash
gh api repos/iamwaqargulzar/Marketing-Agent-OS/releases/latest --jq '{tag: .tag_name, draft: .draft, prerelease: .prerelease, published_at: .published_at, url: .html_url}'
gh api repos/iamwaqargulzar/Marketing-Agent-OS/git/ref/tags/vX.Y.Z --jq '.object'
git fetch origin tag vX.Y.Z
```

Confirm that the latest tag matches `VERSION`, the release is neither draft nor prerelease, and the tag resolves to the tested commit (dereference an annotated tag if needed). Report the live release URL to the user. If the version already has a release, inspect it before taking further action; never overwrite an existing release tag silently.

## Recovery

The updater is all-or-nothing for the selected sources during a run. If a later review rejects an applied update, restore the affected files through normal version-control history; do not edit a pinned snapshot by hand.
