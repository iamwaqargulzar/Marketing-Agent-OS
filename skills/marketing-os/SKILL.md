---
name: marketing-os
description: "Route complex marketing work across strategy, narrative, SEO/GEO, CRO, lifecycle, paid, social, influencer, launch, sales and measurement. Use for broad marketing plans, multi-channel work, or when the right specialist skill is unclear."
license: Apache-2.0
metadata:
  domain: "marketing"
  provenance: "marketing-agent-os"
---

# Marketing OS

Route the request to the smallest set of specialist skills, then return one integrated answer. Do the specialist's work through that skill's own instructions rather than from general knowledge.

## How to route

1. Read `.agents/product-marketing.md` when present. If it is materially incomplete and the work depends on it, start with `product-marketing`.
2. Classify the request by objective, funnel stage, channel, artifact, and decision horizon.
3. Find the narrowest match in `references/skill-guide.md`. Use `references/skill-index.json` for the complete machine-readable inventory.
4. Load the chosen skill and follow it. If it is not installed, say which skill is missing and how to add it, then continue only with what is available.
5. For cross-channel work, settle narrative and claims before producing publish-ready assets.
6. Run specialists in parallel only when their inputs are independent. Otherwise sequence them by dependency.
7. Apply `references/skill-contract.md` throughout. For cross-skill or side-effecting work, apply `references/control-artifacts.md` and keep proposal, approval, execution, receipt, and measurement separate.
8. For high-impact deliverables, run the relevant quality gate and return one recommendation rather than disconnected expert notes.

## Choosing between overlapping skills

Several families cover similar ground from different angles. Choose by the job, not the keyword.

| Request | Start with | Not |
|---|---|---|
| Full-site SEO score and prioritized report | `seo-audit` and its full-site workflow | a single-topic specialist |
| One page reviewed | `seo-page` or `on-page-seo-checker` | `seo-audit` |
| Crawl, indexing, rendering, or Core Web Vitals | `seo-technical` or `technical-seo-checker` | `seo` |
| Visibility in AI answers, as a strategy | `ai-seo` | `geo` unless a full GEO audit is wanted |
| Full GEO audit or a client report | `geo-audit`, then `geo-report` | `ai-seo` |
| One GEO question | `geo-citability`, `geo-crawlers`, `geo-llmstxt`, `geo-schema`, `geo-brand-mentions`, or `geo-platform-optimizer` | `geo-audit` |
| Write or refresh SEO content | `content-writer` | `copywriting` |
| Page copy that must convert | `copywriting` | `content-writer` |
| Edit an existing draft | `copy-editing` | `copywriting` |
| Is a draft ready to publish | `content-quality-auditor` | a writing skill |
| Conversion events not arriving or not matching | `conversion-tracking` | `attribution` or `ads` |
| Which channel gets credit | `attribution` or `attribution-reconciler` | `conversion-tracking` |
| Earn new links | `link-building` | `offsite-signal-analyzer` |
| Diagnose an existing backlink profile | `offsite-signal-analyzer` or `seo-backlinks` | `link-building` |
| Plan paid campaigns or audit an account | `ads` or `ad-account-auditor` | `ad-creative` |
| Lifecycle email program | `emails` or `email-sequence-designer` | `cold-email` |
| Outbound to people with no prior relationship | `cold-email` or `prospecting` | `emails` |
| Study how a competitor markets | `reverse-engineer-marketing` | `competitors` for comparison pages |

Routing does not authorize external actions. Stop and ask when authority is missing, a material strategic fork needs the user, evidence is insufficient, or the next step has a real-world side effect.

## Output

Return the smallest useful artifact. For analysis, use **Observation → Evidence → Interpretation → Recommendation → Validation**. For plans, include owner or next action, metric, dependency, and risk where relevant.

## Handoff

When another skill should continue the work, provide:

- `status`: `DONE`, `DONE_WITH_CONCERNS`, `BLOCKED`, or `NEEDS_INPUT`
- `objective`
- `findings` with evidence labels
- `assumptions` and `open_loops`
- `recommended_next_skill` (maximum three)

## References

- `references/skill-guide.md`: every skill by domain
- `references/skill-index.json`: complete catalog
- `references/skill-contract.md`: evidence, permissions, and handoffs
- `references/control-artifacts.md`: action lifecycle and receipts
- `references/routing-policy.md`: precedence and conflict resolution
- `references/product-context-schema.md`: shared marketing context
- `references/connectors.md` and `references/connector-catalog.md`: optional data and tool integrations

The [complete source library](references/source-library.md) contains all four original workflows and their tooling. Use the source root specified by the specialist when a step needs its original runtime.
