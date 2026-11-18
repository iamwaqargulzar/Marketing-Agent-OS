### Additional checks

- Before reading an account export or recommending pause/keep/scale, read `references/account-evidence.md`; reconcile report coverage, conversion definitions, lag, configuration changes, and brand/non-brand results.

### Affordability and causal validation

Use gross-margin payback, not revenue-only CAC/ARPU, to assess recovery: CAC / (monthly ARPU × gross-margin fraction) assumes steady profit and no churn. Prefer cumulative measured cohort gross profit per original acquired customer, with collection delay; year-end retention is not a monthly recovery path or a discount rate. Compare with runway and the user's target before proposing spend.

Treat optimized ad-delivery winners as screening evidence, not randomized landing-page evidence. Confirm a mirrored headline in a fresh page experiment with consistent incoming traffic and planned guardrails. Static-versus-video, broad-targeting, algorithm, and lift claims require account evidence; no creative format guarantees a gain.

For Google Ads API setup, verify OAuth-project API access and target-account permissions separately. Developer tokens were sunset in September 2026; new access is managed in the OAuth credentials' Google Cloud project. Do not request a retired token to satisfy an old local CLI. Reuse an approved connector and current first-party setup documentation; changing project, billing, credentials, or scopes requires explicit authorization.

### Operating review and tracking handoff

For account reviews, read [references/operating-review.md](operating-review.md). Check the user's paid-media targets and approved learnings, label missing data, and separate facts from hypotheses. Route pixel/CAPI/server-side setup and conversion-delivery faults to `conversion-tracking`; a recommended account change is not an executed change.

### Additional references

- `references/account-evidence.md`
- `references/operating-review.md`
