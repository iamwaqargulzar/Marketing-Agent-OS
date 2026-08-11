<div align="center">

# Social — ECHO

**An always-on organic-social presence — no posting, engagement, or DM automation, ever.**

English | [简体中文](README.zh.md)

</div>

> One discipline inside **[Aaron Marketing Skills](../README.md)** — 120 skills across seven disciplines on one contract. For the whole system, the four-layer map, and install steps, start at the [main README](../README.md).

Organic Social is an always-on **L2 · Channel** — the owned social presence that expresses the brand narrative in public, in real time. Sixteen skills run the **ECHO** loop — **E**xplore where to be and how to sound, **C**raft platform-native assets, **H**ost the community (replies, selling, crisis), then **O**bserve mentions, share of voice, and dark-social attribution. The channel roster is owned by [`channel-registry`](../protocol/channel-registry/SKILL.md); the gate is [`social-quality-auditor`](host/social-quality-auditor/SKILL.md). **The discipline ships no posting, engagement, or DM automation of any kind** — it plans, drafts, and measures; a human presses publish.

## The loop — Explore → Craft → Host → Observe

- **Explore** — earn your presence: channel mix and per-channel role, brand voice and persona, per-platform norms and red lines, and a non-promotional warm-up ramp.
- **Craft** — make platform-native assets: a capacity-governed editorial calendar, posts/threads/carousels, short-video scripts, and an advocacy program spec.
- **Host** — run the community: the asset/program quality gate, reply/mention triage, founder-led social selling, and a pre-drafted crisis ladder.
- **Observe** — read the signal: mentions and sentiment pulse, share of voice vs competitors, dark-social attribution, and a period-stable measurement loop back to memory.

## The 16 skills

Links open each `SKILL.md`. ⛩ marks the discipline's auditor-class quality gate. The **ECHO lever** column shows the primary dimension (**E**mbeddedness · **C**raft · **H**osting · **O**bservability).

| Phase | Skill | ECHO | What it does |
|-------|-------|:----:|--------------|
| **Explore** | [channel-portfolio-planner](explore/channel-portfolio-planner/SKILL.md) | E | Pick the platform mix and per-channel role/cadence from where the audience actually is (records channels to the registry). |
| **Explore** | [voice-dossier-builder](explore/voice-dossier-builder/SKILL.md) | E | Brand voice, tone, persona, and do/don't lexicon for a consistent, human-sounding presence. |
| **Explore** | [platform-norm-profiler](explore/platform-norm-profiler/SKILL.md) | E | Per-platform norms, formats, ranking signals, and red-line rules before you post there. |
| **Explore** | [participation-warmup-planner](explore/participation-warmup-planner/SKILL.md) | E | Non-promotional community warm-up plan — where to show up and add value before selling. |
| **Craft** | [social-calendar-builder](craft/social-calendar-builder/SKILL.md) | C | Editorial calendar — themes, series, cadence balanced to real capacity (no over-posting). |
| **Craft** | [social-creative-builder](craft/social-creative-builder/SKILL.md) | C | Platform-native posts (hook/body/CTA), message-matched and claims-ledger-aware. |
| **Craft** | [short-video-scripter](craft/short-video-scripter/SKILL.md) | C | Short-form video scripts — hook, beats, on-screen text, retention structure. |
| **Craft** | [advocacy-program-designer](craft/advocacy-program-designer/SKILL.md) | C | Employee/community advocacy program — opt-in, disclosure defaults, sharable asset kit. |
| **Host** | ⛩ [social-quality-auditor](host/social-quality-auditor/SKILL.md) | E·C·H·O | Auditor-class ECHO gate: scores one declared unit/profile, enforces applicable E1/C1/C2/H1/H2/O1 controls, emits SHIP/FIX/BLOCK. |
| **Host** | [engagement-inbox-manager](host/engagement-inbox-manager/SKILL.md) | H | Reply/comment/DM triage playbook — response tiers, escalation, genuine-engagement discipline (no manufactured/baited engagement). |
| **Host** | [social-selling-planner](host/social-selling-planner/SKILL.md) | H | Founder/team social-selling motion — relationship-first outreach, no automated DMs. |
| **Host** | [crisis-response-planner](host/crisis-response-planner/SKILL.md) | H | Pre-drafted crisis tiers, holding statements, escalation ladder, and pause-the-queue triggers. |
| **Observe** | [social-pulse-monitor](observe/social-pulse-monitor/SKILL.md) | O | Mentions/sentiment/topic pulse from keyless sources, spike-vs-sustain reads (proxy data labeled). |
| **Observe** | [share-of-voice-tracker](observe/share-of-voice-tracker/SKILL.md) | O | Share of voice vs named competitors over a period-stable denominator. |
| **Observe** | [dark-social-attributor](observe/dark-social-attributor/SKILL.md) | O | Attribute dark-social/unlinked traffic — UTM discipline, self-reported-attribution capture, referral parsing. |
| **Observe** | [social-measurement-loop](observe/social-measurement-loop/SKILL.md) | O | Read one shipped change back against a baseline over a window → Promote / Keep-testing / Rollback. |

## Quality gate — ECHO

[ECHO](../references/echo-benchmark.md) scores organic social on four dimensions — **E**mbeddedness · **C**raft · **H**osting · **O**bservability (40 stable IDs). Each run selects **either** the asset gate **or** one program-maturity profile — asset and operating constructs are never combined. Veto items `E1`/`C1`/`C2`/`H1`/`H2`/`O1` (framework-qualified — the `O1`/`O2` IDs collide textually with ROAS) hard-cap or block. The gate is [`social-quality-auditor`](host/social-quality-auditor/SKILL.md) → SHIP/FIX/BLOCK; shared mechanics in [auditor-runbook.md](../references/auditor-runbook.md).

## Quick start

```text
/aaron-marketing:social              # infers the ECHO phase from your input
/aaron-marketing:social --phase explore | craft | host | observe
```

```text
/aaron-marketing:social boost this   # routes to content-amplifier (repurposing)
```

Every skill runs at **Tier 1** with data you paste; no API keys required.

## Recommended plays

| Your situation | Start here | What you get |
|---|---|---|
| Starting a channel from zero | `/aaron-marketing:social --phase explore` | Channel mix, voice dossier, per-platform norms, warm-up ramp |
| Need a month of posts without over-posting | `--phase craft` → `social-calendar-builder` | Capacity-governed editorial calendar + platform-native drafts |
| A post is blowing up (good or bad) | `--phase host` → `crisis-response-planner` / `engagement-inbox-manager` | Holding statements + escalation ladder, or reply-triage tiers |
| How's our share of voice vs competitors? | `--phase observe` → `share-of-voice-tracker` | SOV on a period-stable denominator |
| Turn one asset into a week of content | `content-amplifier` ("boost this") | Repurposed variants across formats |

## Reused from other disciplines

Counted in their home phases, not duplicated here: [trend-spotter](../influencer/scout/trend-spotter/SKILL.md) (cultural timing), [audience-mapper](../influencer/scout/audience-mapper/SKILL.md) (persona), [content-amplifier](../influencer/activate/content-amplifier/SKILL.md) ("boost this" repurposing), [outreach-manager](../influencer/activate/outreach-manager/SKILL.md), [competitor-tracker](../influencer/target/competitor-tracker/SKILL.md), [community-launch-runner](../launch/mobilize/community-launch-runner/SKILL.md) (launch-day posts), plus `landing-optimizer`, `performance-analyzer`, `roi-calculator`, `report-generator`, `page-play-builder`, and the [offer-claims-registry](../protocol/offer-claims-registry/SKILL.md) / [creator-registry](../protocol/creator-registry/SKILL.md) / [memory-management](../protocol/memory-management/SKILL.md) protocol skills.

## Connectors

Keyless social reads only — **no posting/engagement/DM automation**: [`bluesky.py`](../scripts/connectors/bluesky.py) (Bluesky/AT-Proto public reads), [`fediverse.py`](../scripts/connectors/fediverse.py) (Mastodon + Lemmy trends/timelines), [`discourse.py`](../scripts/connectors/discourse.py) (public Discourse-forum health), [`youtube.py --rss`](../scripts/connectors/youtube.py) (keyless channel feed), and [`gdelt.py`](../scripts/connectors/gdelt.py) (news mentions). Reddit degrades to its `.rss` recipe; `threads.py` stays recipe-only. Full list: [CONNECTORS.md](../CONNECTORS.md).

---

<sub>Part of [Aaron Marketing Skills](../README.md) · [System architecture](../docs/system-architecture.md) · [ECHO benchmark](../references/echo-benchmark.md) · [Contributing](../CONTRIBUTING.md)</sub>
