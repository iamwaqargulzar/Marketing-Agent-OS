<div align="center">

# Launch — RAMP

**Concentrate every channel into a launch moment — and survive the second week.**

English | [简体中文](README.zh.md)

</div>

> One discipline inside **[Aaron Marketing Skills](../README.md)** — 120 skills across seven disciplines on one contract. For the whole system, the four-layer map, and install steps, start at the [main README](../README.md).

Launch is the **L3 · Orchestration** layer — the time-boxed moment that concentrates the narrative and all five always-on channels into one push. Sixteen skills run the **RAMP** loop — **R**esearch the positioning, tier, window, and access ladder, **A**ssemble the message house and assets, **M**obilize the launch day and community/press, then **P**rove the outcome and plan momentum. The launch dossier, dates, and outcomes live in [`launch-registry`](../protocol/launch-registry/SKILL.md) (the launch truth SSOT); the gate is [`launch-readiness-auditor`](mobilize/launch-readiness-auditor/SKILL.md).

## The loop — Research → Assemble → Mobilize → Prove

- **Research** — decide the shape: Dunford positioning canvas, launch tier + type + risk register with kill criteria, the window vs the competitor calendar, and the waitlist→GA access ladder.
- **Assemble** — build the spine and kit: message house + PR-FAQ, a tier-scoped asset manifest, pricing/packaging, and (sales-led only) an enablement kit.
- **Mobilize** — go live: the T-1 readiness gate, an hour-blocked launch-day runbook (requires a SHIP verdict), community submissions (PH / HN / directories / 中文 channels), and media relations.
- **Prove** — close the loop: T-0→T+30 telemetry, feedback synthesis with compliant social proof, a D1/W1/M1 retro, and an anti-second-week-cliff momentum plan.

## The 16 skills

Links open each `SKILL.md`. ⛩ marks the discipline's auditor-class quality gate. The **RAMP lever** column shows the primary dimension (**R**eadiness · **A**ssets · **M**omentum · **P**roof).

| Phase | Skill | RAMP | What it does |
|-------|-------|:----:|--------------|
| **Research** | [positioning-mapper](research/positioning-mapper/SKILL.md) | R | Dunford-style positioning canvas — named competitive alternatives, unique attributes, value themes, beachhead segment, onlyness statement. |
| **Research** | [launch-tier-planner](research/launch-tier-planner/SKILL.md) | R | Tier decision (flagship / targeted / changelog), launch-type declaration, KPI targets, risk register with kill criteria. |
| **Research** | [launch-window-planner](research/launch-window-planner/SKILL.md) | R | Candidate-window comparison (conflicts / tailwinds / risk), launch-week vs rolling-release call, store-review buffer, embargo window. |
| **Research** | [early-access-designer](research/early-access-designer/SKILL.md) | R | Waitlist→concept→alpha→beta→GA stage ladder with graduation criteria, cohort gating, feedback loop, referral mechanics (upstream of the R1 stage-truth veto). |
| **Assemble** | [message-house-builder](assemble/message-house-builder/SKILL.md) | A | Message house (tagline, one-liner, pillars, proof) + working-backwards PR-FAQ spine + per-channel angle packs (upstream of A1). |
| **Assemble** | [launch-asset-packager](assemble/launch-asset-packager/SKILL.md) | A | Tier-scoped asset manifest — press kit spec, demo/screenshot specs, launch FAQ, store-listing metadata, technical go-live checklist. |
| **Assemble** | [pricing-packaging-planner](assemble/pricing-packaging-planner/SKILL.md) | A | Launch pricing & packaging — tier structure, value-to-price map, launch-offer ladder, beta pricing, guarantee terms. |
| **Assemble** | [sales-enablement-kit](assemble/sales-enablement-kit/SKILL.md) | A | Internal enablement — battle cards, sales talk track, objection-handling, internal FAQ + CS macros (sales-led only). |
| **Mobilize** | ⛩ [launch-readiness-auditor](mobilize/launch-readiness-auditor/SKILL.md) | R·A·M·P | Auditor-class RAMP gate: scores one lifecycle profile, enforces profile-relevant R1/A1/M1/P1 controls, emits SHIP/FIX/BLOCK. |
| **Mobilize** | [launch-day-conductor](mobilize/launch-day-conductor/SKILL.md) | M | Hour-blocked launch-day runbook — pre-conditions gate check, observation-window verdicts after irreversible pushes, P0–P3 incident ladder + rollback. |
| **Mobilize** | [community-launch-runner](mobilize/community-launch-runner/SKILL.md) | M | Per-platform submission packages (Product Hunt, Show HN, subreddits, directory waves, regional/Chinese channels) under a platform red-line check. |
| **Mobilize** | [press-media-relations](mobilize/press-media-relations/SKILL.md) | M | Three-tier media/analyst list, embargo pitch timing, press-release draft, analyst briefing outline. |
| **Prove** | [launch-monitor](prove/launch-monitor/SKILL.md) | P | T-0→T+30 window watch — instrumentation verification (upstream of P1), rank/review/news polling, D0/W1/M1 KPI snapshots, spike-vs-sustain. |
| **Prove** | [launch-feedback-synthesizer](prove/launch-feedback-synthesizer/SKILL.md) | P | Feedback theme digest, open→shipped status loop ("you asked, we shipped"), compliant social-proof harvest. |
| **Prove** | [launch-retro-analyzer](prove/launch-retro-analyzer/SKILL.md) | P | D1/W1/M1 retro — per-channel actual-vs-target, 5-Whys on the largest miss, keep/kill/change, outcome snapshot to the registry. |
| **Prove** | [momentum-planner](prove/momentum-planner/SKILL.md) | P | T+1→T+30 momentum plan — launch-moment calendar, announcement-tier routing, relaunch legitimacy call, next Tier-1 moment. |

## Quality gate — RAMP

[RAMP](../references/ramp-benchmark.md) scores product launch on four dimensions — **R**eadiness · **A**ssets · **M**omentum · **P**roof (40 stable IDs). It runs **preflight**, **execution**, and **outcome** profiles separately and **never averages time horizons** — a T-1 readiness read and a T+30 outcome read are linked, not blended. Veto items `R1`/`A1`/`M1`/`P1` (framework-qualified — distinct from ROAS `R1`/`A1`) hard-cap or block. The gate is [`launch-readiness-auditor`](mobilize/launch-readiness-auditor/SKILL.md) → SHIP/FIX/BLOCK for one declared lifecycle read; shared mechanics in [auditor-runbook.md](../references/auditor-runbook.md).

## Quick start

```text
/aaron-marketing:launch              # infers the RAMP phase from your input
/aaron-marketing:launch --phase research | assemble | mobilize | prove
```

```text
/aaron-marketing:launch plan a Tier-1 Product Hunt launch for our v2 in three weeks
```

"Launch with creators" routes to [`campaign-planner`](../influencer/target/campaign-planner/SKILL.md) instead. Every skill runs at **Tier 1** with data you paste.

## Recommended plays

| Your situation | Start here | What you get |
|---|---|---|
| Planning a Product Hunt / Show HN launch | `/aaron-marketing:launch --phase mobilize` → `community-launch-runner` | Per-platform submission packages under a red-line check |
| T-1: are we actually ready to ship? | `--phase mobilize` → `launch-readiness-auditor` | RAMP go/no-go verdict for the declared lifecycle read |
| Need the positioning + message spine | `--phase research` → `positioning-mapper` → `message-house-builder` | Dunford canvas + message house + PR-FAQ |
| Launch day, hour by hour | `launch-day-conductor` (needs a SHIP verdict) | Hour-blocked runbook + incident ladder + rollback |
| Avoiding the second-week cliff | `--phase prove` → `momentum-planner` | Post-launch momentum calendar + next Tier-1 moment |

## Reused from other disciplines

Launch orchestrates the whole system, so it reuses widely (each counted in its home phase, not here): channel builders — [email-creative-builder](../email/engage/email-creative-builder/SKILL.md) / [email-sequence-designer](../email/nurture/email-sequence-designer/SKILL.md), [campaign-architect](../ad/research/campaign-architect/SKILL.md) / [ad-creative-builder](../ad/orchestrate/ad-creative-builder/SKILL.md), [page-play-builder](../seo-geo/implement/page-play-builder/SKILL.md) / [content-writer](../seo-geo/implement/content-writer/SKILL.md), [technical-seo-checker](../seo-geo/tune/technical-seo-checker/SKILL.md) / [serp-markup-builder](../seo-geo/implement/serp-markup-builder/SKILL.md); creator + repurposing — [campaign-planner](../influencer/target/campaign-planner/SKILL.md), [outreach-manager](../influencer/activate/outreach-manager/SKILL.md), [content-amplifier](../influencer/activate/content-amplifier/SKILL.md); shared engines — `audience-mapper`, `trend-spotter`, `budget-optimizer`, `landing-optimizer`, `performance-monitor`, `roi-calculator` / `performance-analyzer` / `report-generator`; and the [entity-registry](../protocol/entity-registry/SKILL.md) / [offer-claims-registry](../protocol/offer-claims-registry/SKILL.md) / [consent-registry](../protocol/consent-registry/SKILL.md) protocol skills. See [ramp-benchmark.md](../references/ramp-benchmark.md).

## Connectors

Launch-telemetry reads: [`hn.py`](../scripts/connectors/hn.py) (keyless Hacker News mentions + live rank polling + the comments>points signal), [`producthunt.py`](../scripts/connectors/producthunt.py) (free-token PH launch intel — **non-commercial ToS; attribution required**), and [`appstore.py`](../scripts/connectors/appstore.py) (keyless App Store metadata + charts). Full list: [CONNECTORS.md](../CONNECTORS.md).

---

<sub>Part of [Aaron Marketing Skills](../README.md) · [System architecture](../docs/system-architecture.md) · [RAMP benchmark](../references/ramp-benchmark.md) · [Contributing](../CONTRIBUTING.md)</sub>
