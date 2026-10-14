# Release evidence and site go-live

## Shipped changes to announcement drafts

Inspect the authorized repository's merged changes for the stated range, then confirm deployment and user availability. Exclude internal refactors, unreleased work, inaccessible rollout cohorts, and sensitive details from customer-facing claims. Trace each proposed announcement to a real change, affected audience, supported benefit, and live destination. Ask for missing product evidence instead of embellishing commit titles.

Draft changelog, email/social copy, and pages needing updates as needed. Keep draft approval, deployment, publication, and public receipt separate; a merge or release command is not proof the user can access the feature. Verify the live URL/tag and exact artifact when publishing is authorized.

## Site switch

Before switch: test final content, internal links/assets, key mobile/keyboard flows, accepted form submission through its destination, consent-aware analytics, production URLs/canonicals, indexing controls, supported structured data, and permissioned public claims. Use staging for tests that would otherwise contact people or persist real submissions.

For migrations, review old-to-new URL mappings, redirect chains, locale pairs, sitemaps, valuable pages, and rollback. Do not delete or redirect valuable pages under an unrelated authorization.

At switch: verify actual deployment, hostnames/HTTPS, production indexability, key template responses, redirects, and an authorized end-to-end conversion fixture. External tool submission is a separate action.

After switch: compare equivalent page-level windows, investigate crawl/indexation failures and conversion anomalies, confirm downstream records, and assign an owner to unresolved issues. Distinguish deployed QA evidence from expected indexing/ranking; do not promise immediate search pickup. Define escalation/rollback triggers from the existing baseline.
