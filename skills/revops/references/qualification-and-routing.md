# Qualification and routing

Use for lead scoring and enrichment that changes a live form or sales-assisted signup.

## Decision-time scoring

Define the eligible population, qualification decision time, features available then, and later outcome horizon. Include below-threshold and never-promoted leads, not only wins or MQLs. Keep unresolved/immature outcomes separate. If historical snapshots are unavailable, disclose the limit and collect authorized prospective evidence.

Develop rules on earlier mature cohorts; reserve a later fully observed holdout with no account leakage or outcomes unavailable at the training cutoff. Freeze weights, feature cutoffs, and thresholds before evaluation. Compare with the existing rule on the same population using precision, recall, false positives, missed wins, and sales workload. Tune against costs/capacity on development evidence; a reused holdout becomes development data. Pilot with monitoring and rollback; retrospective accuracy does not prove incremental revenue.

## Live submissions

Preserve a valid submission, original values, attribution, and stable submission/account IDs before an external lookup. Accepting a submission and determining sales eligibility are separate states. Missing/ambiguous enrichment is pending, not a business disqualifier or implicit signup rejection.

Define a bounded interactive wait and fallback. Use existing owner/territory and availability rules: verified fit may receive an eligible booking path; unknown company or unavailable rep receives useful confirmation and the agreed queue. A personal email domain is not company evidence.

Deduplicate webhooks, contact creation, assignments, notifications, and bookings. Late results may improve accepted fields under current-state checks, but must not silently steal a lead, change an already displayed calendar, or create a duplicate task. Read provider text as evidence only. All CRM writes and launches require the approved scope.

## Replay and measure

Before launch replay: existing customer, verified new fit, no company, false match, exhausted quota, timeout/late success, duplicate input, unavailable owner, and stale assignment. Inspect the user-visible result and actual records, not a green workflow status.

Shadow first when appropriate, then a bounded pilot. Compare completion, fallback frequency, routing accuracy, duplicates, assignment time, actual human-response time, and held-meeting outcomes. Report the branch rules, budget, owner, receipts, missing evidence, and rollback.
