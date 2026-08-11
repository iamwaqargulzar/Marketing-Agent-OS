# Pinned source snapshots

Each `source-*` directory is a complete tracked-file snapshot of one audited upstream Git commit. The mapping, source URL, commit, license, entry count, and normalized tree hash live in `../upstreams.lock.json` and `../SOURCE_MANIFEST.md`.

Do not edit snapshots manually. Use `../scripts/update_upstreams.py --apply`, review the resulting diff, reconcile changes into the normalized `../skills/` layer, and regenerate validation artifacts.

Upstream names and attribution intentionally remain in the source snapshots, lockfile, notices, and provenance documents. The installable product remains branded Marketing Agent OS.
