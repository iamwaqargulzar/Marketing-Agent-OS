# TALE Benchmark — Narrative and Messaging Evaluation Standard

TALE governs the L1 narrative system through **Truth · Architecture · Landing · Evidence**. v18 reports three distinct reads: whether the narrative is defensible, whether the message system is coherent across surfaces, and whether effectiveness is actually observed. A coherent story cannot compensate for a false claim, and a truthful canon cannot be declared effective without outcome evidence.

The framework is advisory. Executable profiles, item policies, context, and vetoes live in [`framework-catalog.json`](framework-catalog.json); shared scoring semantics live in [`scoring-semantics.md`](scoring-semantics.md).

**Keyless by design:** Tier 1 uses the narrative canon, claims state, owned surfaces, interviews/win-loss evidence, and compliant public signals. Closed-platform or review-site data must be user-provided or labeled proxy.

## Units and Profiles

| Profile | Unit | Dimensions | Question |
|---|---|---|---|
| `truth` | One canon/positioning claim set for a market and audience | T 100% | Is the strategic narrative materially true and defensible? |
| `system` | One canon plus a declared flagship-surface set | A 50% · L 50% | Is the message system coherent and consistently landed? |
| `effectiveness` | One message experiment or locked observation panel/date | E 100% | What evidence shows the message was understood or changed behavior? |

There is no v18 overall composite. Preserve the three profile results and their dates. A later effectiveness read must link to the exact canon version tested.

## Stable Item Anchors

### Truth (`T1`–`T10`)

`T1` material differentiation integrity · `T2` positioning alternatives/value evidence · `T3` category-frame defensibility where used · `T4` beachhead/audience truth · `T5` claim provenance/needs-source handling · `T6` superlative basis · `T7` product-stage reality · `T8` aspiration/fact separation · `T9` interview/win-loss grounding · `T10` current canon version.

`T1` does not require an “onlyness” sentence. It asks whether the material differentiation actually asserted is false, contradictory, or unsubstantiated against named alternatives.

### Architecture (`A1`–`A10`)

`A1` canon existence and internal consistency · `A2` chosen message hierarchy/pillars where applicable · `A3` traceability from messages to positioning/proof · `A4` strategic change arc where appropriate · `A5` persona proof provenance · `A6` voice rules · `A7` naming/lexicon governance · `A8` fixed-length boilerplates only when operationally required · `A9` concreteness/empty-chair quality · `A10` append-only version/supersession history.

Three pillars, a Raskin-style change arc, and 25/50/100-word boilerplates are optional design patterns, not universal quality requirements. When a pattern is chosen, score its execution; otherwise use catalog-authorized `na` with reason.

### Landing (`L1`–`L10`)

`L1` no material flagship-surface contradiction · `L2` campaign/landing/offer match · `L3` channel derivation from canon · `L4` cascade ownership · `L5` governed localization · `L6` channel-voice inheritance · `L7` objection consistency · `L8` proof at claim location · `L9` enablement consistency · `L10` pre-ship drift check.

### Evidence (`E1`–`E10`)

`E1` no unsupported effectiveness/resonance assertion or mislabeled proxy · `E2` differentiating-claim substantiation · `E3` preregistered comprehension/behavior test · `E4` defined echo/recall method · `E5` locked comparison panel · `E6` answer-engine perception as proxy where used · `E7` proof assets · `E8` actual-vs-intended retro · `E9` win-loss/objection writeback · `E10` revision after failed test.

Per item: Pass = 10, Partial = 5, Fail = 0. Each profile requires 100% applicable evidence coverage. A test not yet run is Unknown, not Partial and not evidence of failure.

## Vetoes

| Qualified ID | Verified failure |
|---|---|
| `TALE-T1` | A material differentiation is false, internally contradictory, or unsubstantiated. Aspirational framing clearly labeled as future intent is not present-tense differentiation. |
| `TALE-A1` | The canon demonstrably contradicts itself. No canon/access is `unknown`; a governed draft can be assessed as a draft. |
| `TALE-L1` | A declared flagship surface materially contradicts the tested canon/approved claim wording, excluding governed localization. |
| `TALE-E1` | An effectiveness claim is asserted without evidence, or proxy evidence is presented as measured. Missing results alone are `unknown`. |

One verified veto caps the containing profile at 59; two or more produce `BLOCK` without a final score. Vetoes do not transfer numerically between profiles; linked prior failures remain visible in the audit record.

## Evidence Contract

| Need | Preferred evidence |
|---|---|
| Positioning truth | Interviews, win-loss, product truth, named alternatives, approved claims |
| Canon/system | Versioned narrative registry and claims projection |
| Landing | Rendered/live flagship surfaces with canon-version linkage |
| Effectiveness | Preregistered comprehension, recall, preference, behavior, or win-loss read |
| Public resonance | Locked query/panel signals with own/proxy provenance |
| History | Append-only canon events and `wayback.py` where public history is relevant |

Echo, share-of-voice, sentiment, and answer-engine descriptions are not interchangeable with comprehension or behavior. State the construct and denominator for every metric.

## Skill Ownership

- **Trace** — baseline/category/audience/positioning skills and claims state supply `T`.
- **Architect** — narrative, message-system, language, and story-bank skills produce the governed canon and `A` evidence.
- **Land** — cascade, pitch, enablement, and proof packaging supply `L` evidence to downstream channel builders.
- **Evaluate** — [`narrative-quality-auditor`](../narrative/evaluate/narrative-quality-auditor/SKILL.md) runs the selected profile; message tests, resonance monitoring, and drift monitoring supply `E` evidence without claiming causality beyond their design.

TALE remains advisory until each versioned profile passes the shared reliability and outcome-calibration protocol.
