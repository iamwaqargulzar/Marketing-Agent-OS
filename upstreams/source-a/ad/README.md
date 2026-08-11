<div align="center">

# Paid Ads — ROAS

**Paid acquisition scored from your own-account exports — no keyed ad APIs required.**

English | [简体中文](README.zh.md)

</div>

> One discipline inside **[Aaron Marketing Skills](../README.md)** — 120 skills across seven disciplines on one contract. For the whole system, the four-layer map, and install steps, start at the [main README](../README.md).

Paid Ads is an always-on **L2 · Channel** — the bought-reach engine that puts the brand narrative in front of demand, fast. Sixteen skills run the **ROAS** loop — **R**esearch the account structure and audiences, **O**rchestrate creative and bids, **A**ctivate the account under a launch gate, then **S**cale with measurement and pacing. Accepted offers and claim substantiation live in [`offer-claims-registry`](../protocol/offer-claims-registry/SKILL.md); the gate is [`ad-account-auditor`](activate/ad-account-auditor/SKILL.md). Everything scores from your **own-account manual export** — keyed ad APIs are never a precondition.

## The loop — Research → Orchestrate → Activate → Scale

- **Research** — set the foundation: account/campaign structure and campaign-type fit, seed and exclusion audiences, search-term mining, and shopping/PMax feed hygiene.
- **Orchestrate** — build the units: RSA headlines and angle matrices, A/B/incrementality test design, bid-strategy selection, and post-click landing QA.
- **Activate** — clear the gate before spend: the RQS launch go/no-go audit, conversion-signal QA, placement/audience exclusions, and conversion-value mapping.
- **Scale** — grow without waste: read-one-change measurement, attribution reconciliation against the ecommerce truth set, budget pacing, and fatigue/frequency management.

> Note: **Activate** means *account-gating* here — the same phase word means *creator outreach* in the influencer discipline.

## The 16 skills

Links open each `SKILL.md`. ⛩ marks the discipline's auditor-class quality gate. The **ROAS lever** column shows the primary dimension (**R**eturn · **O**ffer · **A**udience · **S**pend-efficiency).

| Phase | Skill | ROAS | What it does |
|-------|-------|:----:|--------------|
| **Research** | [campaign-architect](research/campaign-architect/SKILL.md) | A | Account/campaign structure, campaign-type fit, match types, negatives/exclusions, paid↔organic cannibalization; carries a recurring search-term-mining mode. |
| **Research** | [audience-segment-builder](research/audience-segment-builder/SKILL.md) | A | Turn your own customer/CRM/GA4 export into seed audiences, lookalike seeds, exclusion segments, and a funnel-stage targeting map. |
| **Research** | [search-term-miner](research/search-term-miner/SKILL.md) | A | Mine the search-terms report for negatives, new keyword candidates, and match-type refinements. |
| **Research** | [product-feed-optimizer](research/product-feed-optimizer/SKILL.md) | O | Shopping/PMax feed hygiene — titles, attributes, GTINs, category mapping, disapproval fixes. |
| **Orchestrate** | [ad-creative-builder](orchestrate/ad-creative-builder/SKILL.md) | O | RSA headlines/descriptions, hooks, and an angle matrix, message-matched to the destination page. |
| **Orchestrate** | [ad-test-designer](orchestrate/ad-test-designer/SKILL.md) | O·S | Design A/B/n & incrementality tests (hypothesis, variant matrix, sample size/power) and read out significance → promote/kill. |
| **Orchestrate** | [bid-strategy-planner](orchestrate/bid-strategy-planner/SKILL.md) | S | Pick and configure bid strategy vs goal (tCPA/tROAS/max-conversions), seed targets, plan learning-phase transitions. |
| **Orchestrate** | [landing-experience-checker](orchestrate/landing-experience-checker/SKILL.md) | O | Post-click page QA for ad relevance, load speed, mobile, and policy — the ad↔page message-match check. |
| **Activate** | ⛩ [ad-account-auditor](activate/ad-account-auditor/SKILL.md) | R·O·A·S | Auditor-class ROAS gate: scores RQS, enforces R1/R2/O1/O2/A1, emits SHIP/FIX/BLOCK; carries a launch go/no-go mode. |
| **Activate** | [conversion-signal-qa](activate/conversion-signal-qa/SKILL.md) | R | Pre-launch tracking QA (event firing, UTM hygiene, dedup, window alignment, iOS-ATT flags) — builds the R1/R2 signal the gate scores. |
| **Activate** | [placement-exclusion-manager](activate/placement-exclusion-manager/SKILL.md) | A | Placement/audience exclusion lists — brand-safety blocks, junk-placement pruning, wasted-spend suppression. |
| **Activate** | [conversion-value-mapper](activate/conversion-value-mapper/SKILL.md) | R | Map conversion actions to values/weights and value rules so tROAS bids on true margin, not raw counts. |
| **Scale** | [paid-measurement-loop](scale/paid-measurement-loop/SKILL.md) | R·S | Read one shipped change back against a control over a window → Promote / Keep-testing / Rollback / Unproven. |
| **Scale** | [attribution-reconciler](scale/attribution-reconciler/SKILL.md) | R | Standing order-ID de-dup against the GA4/ecommerce truth set, window/currency normalization, model comparison, incrementality. |
| **Scale** | [budget-pacing-monitor](scale/budget-pacing-monitor/SKILL.md) | S | Track spend pace against budget over the flight, flag under/over-delivery, recommend pacing corrections. |
| **Scale** | [fatigue-frequency-manager](scale/fatigue-frequency-manager/SKILL.md) | O | Watch frequency and creative-decay signals, flag fatigued ads, schedule refresh/rotation. |

## Quality gate — ROAS

[ROAS](../references/roas-benchmark.md) scores paid ads on four dimensions — **R**eturn · **O**ffer · **A**udience · **S**pend-efficiency. Only the gate computes the profile-weighted **RQS = floor(profile-weighted mean)** — every other skill works one lever and hands off. Veto items `R1`/`R2`/`O1`/`O2`/`A1` hard-cap or block. The gate is [`ad-account-auditor`](activate/ad-account-auditor/SKILL.md) → SHIP/FIX/BLOCK before budgets scale; shared mechanics in [auditor-runbook.md](../references/auditor-runbook.md).

## Quick start

```text
/aaron-marketing:ad              # infers the ROAS phase from your input
/aaron-marketing:ad --phase research | orchestrate | activate | scale
```

```text
/aaron-marketing:ad audit this Google Ads account before I scale — exports attached
```

Every skill scores from your **own-account export** at **Tier 1** — no keyed ad APIs required.

## Recommended plays

| Your situation | Start here | What you get |
|---|---|---|
| Before I scale this account | `/aaron-marketing:ad --phase activate` → `ad-account-auditor` | RQS launch go/no-go + fix list before budget moves |
| Wasting spend on junk placements | `--phase activate` → `placement-exclusion-manager` | Exclusion lists + wasted-spend suppression |
| Conversion tracking looks off | `conversion-signal-qa` | Event-firing / UTM / dedup / window QA (the R1/R2 prerequisite) |
| Ads are fatiguing | `--phase scale` → `fatigue-frequency-manager` | Fatigued-ad flags + refresh/rotation schedule |
| Which creative actually won? | `--phase orchestrate` → `ad-test-designer` | A/B/incrementality design + significance read → promote/kill |

## Reused from other disciplines

Counted in their home phases, not duplicated here: [budget-optimizer](../influencer/target/budget-optimizer/SKILL.md) (spend + bid-pacing/learning-phase mode), [landing-optimizer](../influencer/report/landing-optimizer/SKILL.md) (post-click), [roi-calculator](../influencer/report/roi-calculator/SKILL.md) (return math), [report-generator](../influencer/report/report-generator/SKILL.md), and [performance-analyzer](../influencer/report/performance-analyzer/SKILL.md).

## Connectors

Paid Ads is deliberately **own-data first** — every score comes from a manual export of your own account, so no keyed ad-platform API is ever required. `advertools` (open-source) helps parse and structure those exports locally; keyed ad-platform MCP servers stay an opt-in Tier 2/3 convenience, catalogued outside the plugin. See [CONNECTORS.md](../CONNECTORS.md).

---

<sub>Part of [Aaron Marketing Skills](../README.md) · [System architecture](../docs/system-architecture.md) · [ROAS benchmark](../references/roas-benchmark.md) · [Contributing](../CONTRIBUTING.md)</sub>
