---
name: seo-matomo
description: "Analyze Matomo analytics for SEO and marketing decisions using an authorized connector, Reporting API, or user export. Use for organic traffic, landing pages, referrers, devices, countries, goals, events, or GA4-to-Matomo reporting comparisons. Not for Search Console query/index data or changing Matomo configuration."
license: Apache-2.0
metadata:
  version: "1.0.0"
  domain: "analytics"
  provenance: "marketing-agent-os"
---

# Matomo Analytics

Use Matomo as a first-party analytics evidence source. Work from an authorized connector, a read-only Reporting API session, or an export supplied by the user; the skill does not require a particular host integration.

## Establish the Measurement Contract

Confirm:

- instance/site identifier and whether the data is live or exported;
- date range, comparison period, timezone, and site currency;
- segment definition, especially what counts as organic traffic;
- visit, action, conversion, goal, and revenue definitions;
- consent, anonymization, retention, and sampling/configuration constraints.

Do not silently map Matomo metrics to similarly named GA4 metrics. State any definition differences before comparing them.

## Evidence Modes

1. Prefer an already-authorized Matomo connector when available.
2. Otherwise use a read-only Reporting API configuration already present in the environment.
3. Otherwise analyze a user-provided CSV/JSON export and label it `user-provided`.
4. If none is available, provide the exact report/export requirements; do not request that credentials be pasted into chat or committed to the repository.

Keep API tokens out of commands, logs, output, and source control. Do not disable network/SSRF protections for a private instance; use the host's explicit local-target or trusted-connector mechanism.

## Analysis

Choose only the views needed for the question:

- organic visits and trend by period;
- landing-page entrances, engagement, exits, goals, and revenue;
- search engines, referrer types, campaigns, and source detail;
- device, country, language, and other justified segments;
- events and goals tied to the stated business outcome;
- change versus a comparable baseline with annotation of releases or tracking changes.

Treat unavailable or anonymized search keywords as unavailable, not zero. Matomo traffic data does not replace Search Console impressions, queries, indexing, or crawl evidence.

## Quality Checks

- Validate date/timezone and segment consistency before comparing periods.
- Separate tracking/configuration changes from marketing performance changes.
- Check for bot/internal traffic handling, consent effects, duplicate tracking, missing goals, and material unknown/referrer shares.
- Label direct API results **measured**, export facts **user-provided**, derived ratios **calculated**, and inferred causes **estimated** or **proxy**.
- Avoid personal-level reporting unless the user has a legitimate, authorized need and the minimum necessary data.

## Permission Boundary

Read-only analysis within the user's requested Matomo scope is allowed. Obtain explicit authorization before changing tracking, goals, segments, dashboards, users, tokens, consent settings, retention, or any persistent configuration.

## Output

Return the data source and retrieval/export time, scope, definitions, findings, confidence, tracking caveats, recommended decision, and validation step. Use tables for comparable periods or segments and keep Matomo data distinct from Search Console, advertising-platform, or third-party estimates.

## Shared References

- [skill-contract.md](references/skill-contract.md) — evidence, permission, and handoff rules
- [routing-policy.md](references/routing-policy.md) — specialist routing and conflicts
- [product-context-schema.md](references/product-context-schema.md) — shared business context
- [connectors.md](references/connectors.md) — optional integrations

## Related Skills

- `analytics` — tracking plans, metric definitions, and general reporting
- `attribution` — cross-channel contribution and incrementality
- `seo-google` — Search Console, CrUX, and Google search evidence
- `technical-seo-checker` — crawl, index, rendering, and performance diagnosis
