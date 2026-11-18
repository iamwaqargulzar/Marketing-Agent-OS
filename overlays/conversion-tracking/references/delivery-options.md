# Conversion delivery options

Choose from the user's actual platform, signal source, consent requirements, field access, existing senders, budget, and maintenance capacity. Explain the nearest viable alternative; do not make a paid tool the default cost of completing an audit.

| Option | Appropriate evidence | Limitation to verify |
|---|---|---|
| Existing native integration | Documented business event and destination receipt | Event coverage, consent behavior, duplicate sources, refunds, and current settings |
| Browser tag or GTM | Documented confirmed-success event accessible in the page | Blockers, consent, refresh/replay, cross-origin fields, and execution errors |
| Provider webhook/backend send | Authoritative business record and supported destination API | Authentication, allowed fields, consent, stable IDs, retries, processing status, and operations ownership |
| Server-side tagging | Explicit upstream success event and a supported server container path | Hosting cost, maintenance, data governance, and deduplication with browser/native senders |
| Managed connector/service | Verified coverage for this source, event, destination, and identifiers | Price, retention, access scope, security, lock-in, and evidence of receipt |

Do not promise a fixed percentage of recovered conversions. Different systems may legitimately differ because of definitions, counting rules, time zones, consent, attribution windows, processing lag, refunds, or source coverage. Diagnose those differences before changing tags or buying software.

Check current documentation before generating a payload: [GA4 event collection](https://developers.google.com/analytics/devguides/collection/ga4/events), [Google enhanced conversions](https://support.google.com/google-ads/answer/9888656), [Meta Conversions API](https://developers.facebook.com/docs/marketing-api/conversions-api/), and the selected provider's consent/deduplication documentation. Supported endpoints and import products can change; never reuse a retired API recipe from memory.
