<div align="center">

# Narrative — TALE

**The brand story every channel inherits — traced, architected, landed, and evaluated.**

English | [简体中文](README.zh.md)

</div>

> One discipline inside **[Aaron Marketing Skills](../README.md)** — 120 skills across seven disciplines on one contract. For the whole system, the four-layer map, and install steps, start at the [main README](../README.md).

Narrative is the **L1 · Strategy** layer: one brand voice that the five always-on channels (SEO/GEO, social, email, paid, influencer) inherit and that Launch concentrates into a moment. Sixteen skills run the **TALE** loop end to end — **T**race the story as it actually lives today, **A**rchitect the canon, **L**and it into every channel and pitch, then **E**valuate whether it is true, coherent, and resonating. The canon itself is owned by [`narrative-registry`](../protocol/narrative-registry/SKILL.md) (the brand-canon SSOT); the gate is [`narrative-quality-auditor`](evaluate/narrative-quality-auditor/SKILL.md).

## The loop — Trace → Architect → Land → Evaluate

- **Trace** — capture the honest starting point: the story as it lives across owned surfaces today, the category's dominant narratives and named alternatives, what the audience already believes, and every positioning claim traced back to substantiation.
- **Architect** — design the canon: the core strategic narrative, the message system (tagline / pillars / proof), the voice-and-lexicon rules, and a reusable bank of proof stories.
- **Land** — move the canon into the world without dilution: cascade it per channel, shape it into pitch form, and package proof points into channel-ready, claims-ledger-aware assets.
- **Evaluate** — check that it holds: the TALE gate runs truth / system / effectiveness profiles separately, message tests read resonance, and two monitors watch for landing and for drift off the approved canon.

## The 16 skills

Links open each `SKILL.md`. ⛩ marks the discipline's auditor-class quality gate. The **TALE lever** column shows which dimension each skill primarily serves (**T**ruth · **A**rchitecture · **L**anding · **E**vidence).

| Phase | Skill | TALE | What it does |
|-------|-------|:----:|--------------|
| **Trace** | [narrative-baseline-mapper](trace/narrative-baseline-mapper/SKILL.md) | T | Capture the current, actual brand story as it lives across owned surfaces — the honest starting point before any redesign. |
| **Trace** | [category-narrative-mapper](trace/category-narrative-mapper/SKILL.md) | T | Map the category's dominant narratives and named alternatives so the brand can claim a defensible, differentiated position. |
| **Trace** | [audience-belief-mapper](trace/audience-belief-mapper/SKILL.md) | T | Surface what the target audience already believes, doubts, and cares about — the beliefs the narrative must move. |
| **Trace** | [positioning-truth-tracer](trace/positioning-truth-tracer/SKILL.md) | T | Trace every positioning claim back to substantiation, retiring anything unsupported (upstream of the T1 truth veto). |
| **Architect** | [strategic-narrative-designer](architect/strategic-narrative-designer/SKILL.md) | A | Design the core strategic narrative — the change-in-the-world story arc, stakes, and resolution the brand leads with. |
| **Architect** | [message-system-architect](architect/message-system-architect/SKILL.md) | A | Architect the message system — tagline, pillars, proof points, and per-audience angles as one coherent structure. |
| **Architect** | [brand-language-codifier](architect/brand-language-codifier/SKILL.md) | A | Codify voice, tone, lexicon, and do/don't language so every channel sounds like one brand. |
| **Architect** | [story-bank-builder](architect/story-bank-builder/SKILL.md) | A | Build a reusable bank of proof stories, customer narratives, and analogies channels can draw from. |
| **Land** | [narrative-cascade-planner](land/narrative-cascade-planner/SKILL.md) | L | Plan how the narrative cascades into each channel and moment without dilution or drift. |
| **Land** | [pitch-narrative-builder](land/pitch-narrative-builder/SKILL.md) | L | Shape the narrative into pitch form — deck spine, demo story, and investor/press framing. |
| **Land** | [narrative-enablement-kit](land/narrative-enablement-kit/SKILL.md) | L | Enablement kit that lets every team tell the story consistently — talk track, FAQ, and message map. |
| **Land** | [proof-point-packager](land/proof-point-packager/SKILL.md) | L | Package proof points into channel-ready, claims-ledger-aware assets. |
| **Evaluate** | ⛩ [narrative-quality-auditor](evaluate/narrative-quality-auditor/SKILL.md) | T·A·L·E | Auditor-class TALE gate: scores one typed profile, enforces T1/A1/L1/E1 when applicable, and emits SHIP/FIX/BLOCK; full mode preserves three linked results. |
| **Evaluate** | [message-test-designer](evaluate/message-test-designer/SKILL.md) | E | Design message tests — variant matrix, audience cells, and resonance read for the strategic narrative. |
| **Evaluate** | [narrative-resonance-monitor](evaluate/narrative-resonance-monitor/SKILL.md) | E | Track how the narrative is landing across channels from keyless sources (proxy data labeled). |
| **Evaluate** | [narrative-drift-monitor](evaluate/narrative-drift-monitor/SKILL.md) | E | Watch for narrative drift — where channels have wandered off the approved canon — and flag corrections. |

## Quality gate — TALE

[TALE](../references/tale-benchmark.md) scores brand narrative on four dimensions — **T**ruth · **A**rchitecture · **L**anding · **E**vidence. It is deliberately **not** rolled into one composite: [`narrative-quality-auditor`](evaluate/narrative-quality-auditor/SKILL.md) runs the **truth**, **system**, and **effectiveness** profiles separately, and a full review links the three results without averaging them. Veto items `T1`/`A1`/`L1`/`E1` (framework-qualified — the IDs collide textually with other frameworks) hard-cap or block a profile regardless of the rest. Gate mechanics are shared across all eight auditors in [auditor-runbook.md](../references/auditor-runbook.md).

## Quick start

```text
/aaron-marketing:narrative              # infers the right TALE phase from your input
/aaron-marketing:narrative --phase trace | architect | land | evaluate
```

```text
/aaron-marketing:narrative we keep sounding like everyone else in our category — fix our story
```

Every skill runs at **Tier 1** with data you paste; no API keys required.

## Recommended plays

| Your situation | Start here | What you get |
|---|---|---|
| "We sound like everyone else in our category" | `/aaron-marketing:narrative --phase trace` | A category-narrative map + the honest baseline of your current story |
| Leadership rewrote the pitch and channels are drifting | `--phase evaluate` → `narrative-drift-monitor` | Where each channel wandered off-canon, with corrections |
| You need one message system before a raise or launch | `--phase architect` → `message-system-architect` | Tagline, pillars, proof points, per-audience angles as one structure |
| A claim in the deck might not be substantiated | `positioning-truth-tracer` | Every claim traced to evidence; unsupported ones retired (T1 veto) |
| Prepping an investor/press narrative | `--phase land` → `pitch-narrative-builder` | Deck spine, demo story, investor/press framing |

## Reused from other disciplines

Counted in their home phases, not duplicated here: [positioning-mapper](../launch/research/positioning-mapper/SKILL.md) (Dunford canvas — logically the front of Trace, physically in `launch/`), [message-house-builder](../launch/assemble/message-house-builder/SKILL.md) (message spine), [audience-mapper](../influencer/scout/audience-mapper/SKILL.md) (persona/belief), and [share-of-voice-tracker](../social/observe/share-of-voice-tracker/SKILL.md) (resonance denominator).

## Connectors

**No new connector.** Narrative's resonance and drift monitors reuse the existing keyless recipes — [`bluesky.py`](../scripts/connectors/bluesky.py), [`gdelt.py`](../scripts/connectors/gdelt.py), [`tavily.py`](../scripts/connectors/tavily.py), and the Wayback CDX recipe. All proxy data is labeled as such. See [CONNECTORS.md](../CONNECTORS.md).

---

<sub>Part of [Aaron Marketing Skills](../README.md) · [System architecture](../docs/system-architecture.md) · [TALE benchmark](../references/tale-benchmark.md) · [Contributing](../CONTRIBUTING.md)</sub>
