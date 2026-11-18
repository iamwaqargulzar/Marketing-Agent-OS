# Enrichment and buying signals

Use when list building includes signal-based sourcing, account tiers, researched briefs, multiple providers, paid credits, or cache reuse.

## Qualify first

Record ICP fit and the source/date/freshness of each trigger: hiring, role changes, product activity, funding, or other permitted business evidence. A signal is a hypothesis about relevance, not proof of intent. Keep company/account matching separate from person matching. Do not scrape LinkedIn, buy unprovenanced contact dumps, or use sensitive traits.

Choose research depth from account value and the user's capacity, not a universal tier size. For a high-priority account, return sourced facts, likely problem as a labeled hypothesis, current tools when evidenced, a supportable angle, missing facts, and a next step. Unsupported personalization stays out of outreach.

## Budgeted waterfall

For each requested field define accepted identity/value, freshness, allowed providers, maximum cost, and stop condition. Reuse verified CRM fields first. Advance only while a field remains unresolved; a nonempty wrong-company result is not success. Preserve unknowns rather than expanding to personal addresses or unrelated data.

A reusable cache key includes account/workspace, provider, endpoint/version, normalized identity, requested fields, and meaningful options. Keep account boundaries and field provenance. Distinguish a fresh accepted hit, expired hit, true no-match, ambiguous identity, and operational error; authentication failure or a cache miss does not prove the entity does not exist.

Apply a separate expiry to negative results. Merge accepted fields without overwriting stronger verified values with nulls. Guard duplicate in-flight requests and late writes. Cache/contact persistence requires an approved location, access and retention policy; never store credentials in lookup keys or evidence logs.

## Verification and pilot

Verify contact deliverability separately and preserve catch-all/risky/invalid/unknown status. Set recheck timing from provider freshness and sending risk. Verification is not outreach authorization.

Pilot fresh/expired hits, no-match, ambiguous identity, provider error, and duplicate inputs. Report source/date, accepted fields, verification status, cost, rejected matches, unresolved reasons, and measured savings against an equivalent baseline. Hand accepted contacts to cold-email; live form routing belongs to revops.
