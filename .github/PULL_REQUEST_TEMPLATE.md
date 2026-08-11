## Summary

Describe the problem and the result of this change.

## Scope

- [ ] Normalized skill or shared reference
- [ ] Installer or compatibility target
- [ ] Helper script or security boundary
- [ ] Upstream snapshot reconciliation
- [ ] Documentation or repository metadata

## Validation

- [ ] `python3 scripts/reconcile_upstreams.py --write`
- [ ] `python3 scripts/build_manifest.py`
- [ ] `python3 scripts/doctor.py`
- [ ] `python3 -m unittest discover -s tests -v`
- [ ] `npx --yes skills@1.5.22 add . --list --full-depth`

## Safety and provenance

- [ ] I did not include credentials, customer data, generated caches, or local harness installations.
- [ ] I retained required third-party licenses, notices, source identities, and attribution.
- [ ] I did not edit `upstreams/source-*` manually.
- [ ] New or changed external side effects remain behind explicit authorization.

## Notes for reviewers

List tradeoffs, compatibility limits, source commits, screenshots, or follow-up work.
