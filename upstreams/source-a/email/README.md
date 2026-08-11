<div align="center">

# Email — SEND

**Owned-audience email that authenticates, lands in the inbox, and converts.**

English | [简体中文](README.zh.md)

</div>

> One discipline inside **[Aaron Marketing Skills](../README.md)** — 120 skills across seven disciplines on one contract. For the whole system, the four-layer map, and install steps, start at the [main README](../README.md).

Email is an always-on **L2 · Channel** — the owned-audience engine that carries the brand narrative straight to the inbox. Sixteen skills run the **SEND** loop — **S**et up auth, lists, and hygiene, **E**ngage with message-matched creative, **N**urture across the lifecycle, then **D**eliver under a pre-send quality gate. Per-subject consent and suppression are owned by [`consent-registry`](../protocol/consent-registry/SKILL.md) (the email truth SSOT); the gate is [`email-quality-auditor`](deliver/email-quality-auditor/SKILL.md).

## The loop — Setup → Engage → Nurture → Deliver

- **Setup** — earn the right to send: SPF/DKIM/DMARC/BIMI auth pre-flight, behavioral + lifecycle segments and suppression, compliant list-growth capture, and ongoing hygiene.
- **Engage** — write what gets opened and clicked: subject/preheader/body/CTA matched to the landing page, subject-line ideation, HTML render QA, and dynamic personalization.
- **Nurture** — build the lifecycle: welcome/cart/post-purchase/win-back flows with frequency governance, newsletter monetization economics, preference-center design, and reactivation.
- **Deliver** — ship safely: the EQS pre-send go/no-go gate, A/B and send-time experiment design, inbox-placement monitoring, and compliant cold outbound.

## The 16 skills

Links open each `SKILL.md`. ⛩ marks the discipline's auditor-class quality gate. The **SEND lever** column shows the primary dimension (**S**ender-integrity · **E**ngagement · **N**urture · **D**irect-response).

| Phase | Skill | SEND | What it does |
|-------|-------|:----:|--------------|
| **Setup** | [deliverability-qa](setup/deliverability-qa/SKILL.md) | S | Pre-flight SPF/DKIM/DMARC/BIMI auth, reputation, inbox-placement, spam-content, and list hygiene (the S1 check). |
| **Setup** | [list-segment-builder](setup/list-segment-builder/SKILL.md) | E | Behavioral + lifecycle-stage segments and suppression rules from your own list/CRM/GA4 export. |
| **Setup** | [list-growth-designer](setup/list-growth-designer/SKILL.md) | S·N | List-growth strategy — acquisition channels, lead-magnet concepts, a compliant opt-in capture-flow spec, and referral-loop mechanics. |
| **Setup** | [list-hygiene-monitor](setup/list-hygiene-monitor/SKILL.md) | S | Ongoing list health — bounce/complaint pruning, sunset policies, re-permission, inactive-segment suppression. |
| **Engage** | [email-creative-builder](engage/email-creative-builder/SKILL.md) | E·D | Subject/preheader/body/CTA, message-matched to the landing page, claims-ledger-aware. |
| **Engage** | [subject-line-lab](engage/subject-line-lab/SKILL.md) | E | Subject/preheader ideation and scoring — length, spam-trigger, curiosity/clarity balance, variant sets for testing. |
| **Engage** | [email-render-builder](engage/email-render-builder/SKILL.md) | E | HTML email build/QA — client compatibility, dark-mode, accessibility, plain-text alt, render-test checklist. |
| **Engage** | [dynamic-content-personalizer](engage/dynamic-content-personalizer/SKILL.md) | E | Merge-tag/liquid personalization blocks, conditional content rules, and fallback-value safety. |
| **Nurture** | [email-sequence-designer](nurture/email-sequence-designer/SKILL.md) | N | Lifecycle/automation flows (welcome, cart, post-purchase, win-back) + frequency governance. |
| **Nurture** | [newsletter-monetization-planner](nurture/newsletter-monetization-planner/SKILL.md) | D | Paid-sub, sponsorship inventory + rate card, and referral growth-loop economics. |
| **Nurture** | [preference-frequency-manager](nurture/preference-frequency-manager/SKILL.md) | N | Preference-center design and send-frequency governance to cut fatigue and unsubscribes. |
| **Nurture** | [reactivation-specialist](nurture/reactivation-specialist/SKILL.md) | N | Win-back / re-engagement flows for dormant subscribers with sunset-or-recover decision rules. |
| **Deliver** | ⛩ [email-quality-auditor](deliver/email-quality-auditor/SKILL.md) | S·E·N·D | Auditor-class SEND gate: scores EQS, enforces S1/S2/N1/D1, emits SHIP/FIX/BLOCK; carries a pre-send go/no-go mode. |
| **Deliver** | [send-experiment-designer](deliver/send-experiment-designer/SKILL.md) | E | A/B / send-time / hold-out design with sample-size + significance read (promote/kill). |
| **Deliver** | [inbox-placement-monitor](deliver/inbox-placement-monitor/SKILL.md) | S | Ongoing inbox-vs-spam placement tracking via seed lists and provider signals, with reputation-drift alerts. |
| **Deliver** | [cold-outbound-sequencer](deliver/cold-outbound-sequencer/SKILL.md) | D | Compliant B2B cold-outbound cadences — deliverability-safe ramp, personalization tokens, reply-handling steps. |

## Quality gate — SEND

[SEND](../references/send-benchmark.md) scores email on four dimensions — **S**ender-integrity · **E**ngagement · **N**urture · **D**irect-response. Only the gate computes **EQS = floor(profile-weighted mean)** from the declared **promotional**, **retention**, **cold-outbound**, or **newsletter** profile — every other skill works one lever and hands off. Veto items `S1`/`S2`/`N1`/`D1` hard-cap or block. The gate is [`email-quality-auditor`](deliver/email-quality-auditor/SKILL.md) → SHIP/FIX/BLOCK; shared mechanics in [auditor-runbook.md](../references/auditor-runbook.md).

## Quick start

```text
/aaron-marketing:email              # infers the SEND phase from your input
/aaron-marketing:email --phase setup | engage | nurture | deliver
```

```text
/aaron-marketing:email design a 5-email post-purchase flow for our DTC skincare list
```

Every skill runs at **Tier 1** with data you paste; connectors only automate retrieval or an explicitly approved send.

## Recommended plays

| Your situation | Start here | What you get |
|---|---|---|
| Emails are landing in spam | `/aaron-marketing:email --phase setup` → `deliverability-qa` | SPF/DKIM/DMARC/BIMI auth read + placement/hygiene fixes (S1) |
| Need a welcome / cart / win-back flow | `--phase nurture` → `email-sequence-designer` | Lifecycle flow + frequency governance |
| About to send to the whole list | `--phase deliver` → `email-quality-auditor` | EQS pre-send go/no-go + fix list before send |
| Open rates are sliding | `--phase engage` → `subject-line-lab` | Scored subject/preheader variants for testing |
| Launching a B2B cold sequence | `cold-outbound-sequencer` | Compliant, deliverability-safe cadence + reply handling |

## Reused from other disciplines

Counted in their home phases, not duplicated here: [audience-mapper](../influencer/scout/audience-mapper/SKILL.md) (persona / lifecycle stage), [landing-optimizer](../influencer/report/landing-optimizer/SKILL.md) (post-click), [roi-calculator](../influencer/report/roi-calculator/SKILL.md) (revenue-per-send), [report-generator](../influencer/report/report-generator/SKILL.md), [performance-analyzer](../influencer/report/performance-analyzer/SKILL.md), and the [offer-claims-registry](../protocol/offer-claims-registry/SKILL.md) (D1 claim compliance).

## Connectors

[`doh.py`](../scripts/connectors/doh.py) pulls a sending domain's SPF/DMARC/BIMI/MX records and probes common DKIM selectors — the keyless, any-ESP **S1 record evidence** (facts only, no verdicts). [`resend.py`](../scripts/connectors/resend.py) automates the one ESP with a free-tier key: domain-auth status, per-recipient seed-test sends, suppression sync, and broadcasts — **mutating subcommands dry-run by default, `--live` to execute**. Keyed ESP suites (Klaviyo, Mailchimp, HubSpot, Customer.io, Braze) stay external. Full list: [CONNECTORS.md](../CONNECTORS.md).

---

<sub>Part of [Aaron Marketing Skills](../README.md) · [System architecture](../docs/system-architecture.md) · [SEND benchmark](../references/send-benchmark.md) · [Contributing](../CONTRIBUTING.md)</sub>
