# Control Artifacts

Use a control artifact when work crosses skills, spans multiple turns, or can produce a persistent or real-world side effect. It is an operational record, not business truth and not permission by itself.

## Required separations

Keep these facts distinct:

1. **Proposal:** what should happen and why.
2. **Approval:** who authorized the exact scope and payload.
3. **Execution:** what an authorized executor attempted.
4. **Receipt:** what the destination system actually returned.
5. **Measurement:** what happened afterward under a declared window and rule.

A quality-gate verdict such as `SHIP` means an artifact is eligible to proceed. It never proves approval, execution, publication, delivery, payment, or success.

## Binding rules

- Bind approvals and receipts to the exact action scope and payload hash. A changed payload needs a new revision and fresh approval.
- Use one stable artifact ID with monotonically increasing revisions. Never edit history to make an earlier state look approved or complete.
- Require an idempotency key for persistent writes and external actions so retries can be detected.
- Keep one writer for authoritative registries; other skills submit proposals or evidence.
- Record limits, timing, stop conditions, and recovery steps before execution where relevant.
- Mark a side effect complete only from a matching receipt. A plan, dry run, command, queued item, or visible URL is not a receipt for a different operation.
- Keep observations and interpretations separate. Measurement must name its source, evidence label, time window, and decision rule.
- Store opaque references instead of credentials or unnecessary personal data.

## Lifecycle

`proposed → approved → executing → complete`

Use `blocked` when a declared dependency, authority, or safety condition prevents progress. Approval is never inferred from elapsed time, a prior unrelated approval, or a gate verdict.

## Portable format

[`schema/control-artifact.json`](../schema/control-artifact.json) defines the interoperable JSON format. Validate an artifact without third-party dependencies:

```bash
python3 scripts/validate_control_artifact.py path/to/control-artifact.json
```

The validator is read-only and works with standard Python on Linux, macOS, and Windows.
