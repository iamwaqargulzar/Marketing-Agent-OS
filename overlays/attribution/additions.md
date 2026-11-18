### Additional checks

- Separate conceptual attribution models from models currently supported by the user's platform. Verify settings, scope, conversion actions, lookback windows, and attribution/reporting dates before comparing credits. Do not recommend a retired model as an available GA4 or Google Ads setting.
- Treat data-driven or multi-touch credit as a model estimate; low-volume allocation and missing identity/consent data limit interpretation. Triangulate with first-party sales, customer-reported sources, experiments, and business economics; document conflicts instead of silently overriding the model.
- For booking or cross-domain journeys, verify which campaign parameters and identifiers actually reach the destination and CRM. Do not assume a link's UTM tags persist through every widget or integration.

### Ledger and booking boundaries

Keep the deduplicated conversion/revenue ledger separate from modeled channel allocation. Direct and branded-search traffic may reflect repeat buyers, genuine direct visits, offline influence, or lost referrers; investigate before claiming either broken tracking or successful top-of-funnel influence.

For third-party booking attribution, distinguish click, confirmed booking, cancellation, and held meeting. Use documented provider events and stable IDs, consent-safe identity matching, and replay-safe receipts; reconcile unknown matches without inventing attribution. A successful tracking request is not proof of delivery or a completed business outcome.

### Conversion delivery handoff

Use `conversion-tracking` to diagnose or implement delivery of confirmed conversions to analytics/ad destinations, including pixels, server-side events, and offline outcome uploads. Keep credit allocation here and CRM stage definitions in `revops`; a delivery discrepancy does not by itself establish attribution bias or an implementation cause.
