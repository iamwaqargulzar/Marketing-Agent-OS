# RAMP Benchmark — Product Launch Evaluation Standard

RAMP evaluates a launch through four lenses: **Readiness · Assets · Momentum · Proof**. These lenses occur at different times, so v18 reports three distinct reads rather than one temporally incoherent Launch Quality Score.

The framework is advisory. Executable profiles, item identity, context, and vetoes live in [`framework-catalog.json`](framework-catalog.json); shared scoring semantics live in [`scoring-semantics.md`](scoring-semantics.md).

**Keyless by design:** Tier 1 uses the launch plan, claims and launch registries, own analytics exports, and public/keyless launch telemetry. Platform APIs and commercial ASO tools are optional.

## Unit and Lifecycle Context

Score one launch at one declared `lifecycle_read`, market, launch type, and access model. The same launch may produce preflight, execution, and outcome results, but they remain separate records with separate dates. Never average them into a single score.

## Profiles

| Profile | Included evidence | Intended time | Decision supported |
|---|---|---|---|
| `preflight` | R 40% + A 40% + policy/embargo item M1 10% + instrumentation item P1 10% | Before release | Ready/fix/block before committing the moment |
| `execution` | M 100% | During/just after the launch window | Whether the plan was executed safely and coherently |
| `outcome` | P2–P10 100% | After the declared lag | What was observed and learned |

Outcome evidence is not backfilled into preflight. Preflight plans are not scored as realized outcomes.

## Stable Item Anchors

### Readiness (`R1`–`R10`)

`R1` stage truth against declared access/eligibility · `R2` positioning and alternatives · `R3` ICP/beachhead fit · `R4` tier/type and effort · `R5` timing/window · `R6` competitor launch evidence · `R7` early-access graduation where applicable · `R8` risk/rollback register · `R9` internal ownership/escalation · `R10` preregistered D0/W1/M1 targets.

### Assets (`A1`–`A10`)

`A1` claim/disclosure integrity · `A2` narrative/message architecture · `A3` proof-point completeness · `A4` press/facts asset manifest · `A5` channel-specific asset compliance · `A6` pricing/offer terms where applicable · `A7` sales/support enablement where applicable · `A8` announcement/landing/offer match · `A9` technical go-live verification · `A10` localization/regional readiness where applicable.

### Momentum (`M1`–`M10`)

`M1` platform/embargo integrity · `M2` channel mix and dependency risk · `M3` T-minus execution · `M4` authoritative date/commitment coordination · `M5` owned-channel sequence · `M6` media/partner activation · `M7` community response operation · `M8` live monitoring/alerts · `M9` go/rollback observation windows · `M10` launch-spacing/capacity guardrail.

### Proof (`P1`–`P10`)

`P1` preflight instrumentation verification · `P2` actuals vs preregistered targets · `P3` attribution reconciliation · `P4` spike-to-sustain retention · `P5` owned-capture rate · `P6` feedback loop closure · `P7` compliant social-proof pipeline · `P8` causal retro/uncertainty · `P9` registry learning/outcome writeback · `P10` T+1→T+30 momentum plan and next decision.

Per item: Pass = 10, Partial = 5, Fail = 0. Each profile requires 100% coverage of its applicable items. The common bands describe each profile only; v18 defines no cross-lifecycle composite.

## Vetoes

| Qualified ID | Verified failure |
|---|---|
| `RAMP-R1` | The announced lifecycle stage materially contradicts verifiable access or eligibility. A public pricing page is required only when the access model promises public paid availability. Missing registry/access evidence is `unknown`. |
| `RAMP-A1` | Launch copy contains a false/unsubstantiated material claim or missing required disclosure. |
| `RAMP-M1` | Verified vote/engagement manipulation, material embargo breach, or launch-blocking platform-policy violation. A genuine feedback request is not vote solicitation. |
| `RAMP-P1` | Required participating surfaces have demonstrably broken instrumentation. A genuinely unused surface is `na`; privacy-limited modeled data may be partial. |

Veto policy applies within the profile that contains the item: `R1/A1/M1/P1` at preflight and `M1` again as observed execution evidence in the execution profile. A preflight plan and its later execution are different dated runs. The outcome profile has no inherited numeric veto; prior verdicts remain linked records. One veto caps at 59; two or more produce `BLOCK` without a final score.

## Evidence Contract

| Need | Preferred evidence |
|---|---|
| Stage/access | Launch registry plus direct access/eligibility check |
| Positioning/assets | Narrative canon, claims ledger, launch manifest, rendered surfaces |
| Rules/commitments | Dated official platform rules, contracts, embargo record |
| Instrumentation | Verified events/UTMs and own-data destination checks |
| Outcomes | Own analytics/CRM/store truth set after declared lag |
| Public echo | `hn.py`, `producthunt.py`, `appstore.py`, `gdelt.py`, each provenance-labeled |

Public telemetry is supporting evidence, not a substitute for own conversion/outcome data. Platform folklore remains dated `estimated` guidance outside the rubric.

## Skill Ownership

- **Research** — positioning, launch tier/window, early-access, risk, and target definition supply `R`.
- **Assemble** — message/claim, asset, offer, enablement, and go-live work supply `A` and preflight `P1`.
- **Mobilize** — [`launch-readiness-auditor`](../launch/mobilize/launch-readiness-auditor/SKILL.md) runs preflight; launch-day/community/media operators later supply `M` execution evidence.
- **Prove** — `launch-monitor`, `launch-feedback-synthesizer`, `launch-retro-analyzer`, and `momentum-planner` supply outcome `P2–P10` evidence.

RAMP results remain advisory until each lifecycle profile passes the shared reliability and outcome-calibration protocol.
