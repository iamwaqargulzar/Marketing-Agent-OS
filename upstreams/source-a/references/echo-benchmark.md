# ECHO Benchmark — Organic Social Evaluation Standard

ECHO evaluates organic social through **Embeddedness · Craft · Hosting · Observability**. v18 separates an individual asset's Craft gate from a channel portfolio's operating maturity. It does not let a polished post compensate for manufactured engagement, weak governance, or unobservable reporting.

The framework is advisory. Executable profiles, item policies, context, and vetoes live in [`framework-catalog.json`](framework-catalog.json); shared scoring semantics live in [`scoring-semantics.md`](scoring-semantics.md).

**Keyless by design:** Tier 1 uses registry state, own platform/analytics exports, and compliant public surfaces. Closed-platform data enters as user-provided exports or explicitly labeled proxies. Platform folklore belongs in dated norm cards as `estimated`, never as a universal rubric threshold.

## Units and Profiles

| Profile | Unit | Dimensions | Purpose |
|---|---|---|---|
| `asset-gate` | One post/asset package for named channels and market | E1 10% · C1–C10 60% · H1/H2 20% · O1 10% | Pre-publish channel truth, content, anti-manipulation/UGC rights, and metric-integrity gate |
| `program-maturity-community` | One channel portfolio/window | E 37.5% · H 37.5% · O 25% | Community-led operating maturity |
| `program-maturity-b2c` | One channel portfolio/window | E 20% · H 40% · O 40% | Feed-led brand operating maturity |
| `program-maturity-founder` | One channel portfolio/window | E 28.5% · H 21.5% · O 50% | Founder-led operating maturity |

The asset gate contains only controls observable on the publish package and its governing records. An observed asset with no performance rate or metric claim passes O1 because there is no denominator assertion to misrepresent; missing access to the asset remains Unknown. Do not combine the asset gate and program maturity into one score. Report outcomes such as qualified reach, retention, pipeline, or community health as measured metrics with controls; they receive no rubric score until outcome calibration exists.

## Stable Item Anchors

### Embeddedness (`E1`–`E10`)

`E1` channel truth/registry state · `E2` participation before promotion · `E3` give/ask evidence · `E4` current rule digest · `E5` governed profile/bio/link state · `E6` owned-space lifecycle where applicable · `E7` channel-capability fit · `E8` handle security/governance · `E9` pinned/bio-link freshness · `E10` cross-community rule-conflict check.

### Craft (`C1`–`C10`)

`C1` claim integrity where claims exist · `C2` material-connection/synthetic-media disclosure where applicable · `C3` platform-native adaptation · `C4` hook/payload/spec fit · `C5` accessibility · `C6` voice/canon adherence · `C7` declared editorial mix · `C8` freshness on reused assets · `C9` link/placement policy · `C10` format-specific execution evidence.

### Hosting (`H1`–`H10`)

`H1` no manufactured/baited engagement · `H2` UGC permission where republishing occurs · `H3` response SLA · `H4` crisis/pause protocol · `H5` cadence/capacity fit · `H6` voluntary advocacy · `H7` warm-touch selling discipline · `H8` escalation ownership · `H9` moderation rules/log · `H10` advocate-roster hygiene.

### Observability (`O1`–`O10`)

`O1` stable named denominators and provenance · `O2` declared dark-social method · `O3` locked comparison panel · `O4` robust per-post rollups and organic/paid separation · `O5` vanity/EMV exclusion from decision scores · `O6` attribution instrumentation · `O7` listening baseline · `O8` query architecture · `O9` employee-excluded community health · `O10` learning writeback.

Per item: Pass = 10, Partial = 5, Fail = 0. Every profile requires 100% coverage of applicable items. `C1`, `C2`, and `H2` may be `na` only under their catalog conditions and with a reason.

Typed context is profile-bound: `asset-gate` uses `assessment_mode: asset` and `program_archetype: not-applicable`; program profiles use `assessment_mode: program` and the exact `community`, `b2c`, or `founder` archetype. A mismatched profile/context pair is invalid rather than a weighting choice.

## Vetoes

| Qualified ID | Verified failure |
|---|---|
| `ECHO-E1` | Activity materially contradicts the governed channel record. No record/access is `unknown`, not a veto. |
| `ECHO-C1` | An asset makes a false/unapproved material product or offer claim. Opinion with no such claim is `na`. |
| `ECHO-C2` | Required material-connection or realistic-synthetic-media disclosure is missing. |
| `ECHO-H1` | Verified bought/coordinated/bot engagement or prohibited engagement bait. Genuine feedback requests and independent disclosed advocates are not failures. |
| `ECHO-H2` | Third-party UGC is republished without applicable permission. A native attributed share is not automatically republishing. |
| `ECHO-O1` | A reported rate hides/switches its denominator or presents proxy data as measured. |

One verified veto caps the containing profile at 59; two or more produce `BLOCK` without a final score. A previous asset verdict is linked to, not averaged into, the program-maturity profile.

## Evidence Contract

| Need | Preferred evidence |
|---|---|
| Channel/governance | Projected channel registry, dated rules, account-control records |
| Asset truth | Narrative canon, claims state, rendered asset, platform requirements |
| Permission/advocacy | Append-only permission/consent events and current projections |
| Own performance | User-exported native analytics plus GA4/GSC truth set |
| Public participation | `discourse.py`, `hn.py`, `bluesky.py`, `fediverse.py`, public RSS |
| Public echo | `gdelt.py`, `tavily.py`, and adjacent sources labeled `proxy` |

No compliant keyless read surface is assumed for X, Instagram, TikTok, LinkedIn, or Xiaohongshu. Missing private exports produce Unknown, not fabricated measurement.

## Skill Ownership

- **Explore** — channel portfolio, voice dossier, norm profile, warmup, and channel registry supply `E`.
- **Craft** — calendar/creative/video/advocacy skills produce assets; [`social-quality-auditor`](../social/host/social-quality-auditor/SKILL.md) applies `asset-gate` before publication.
- **Host** — inbox, selling, crisis, moderation, permission, and advocacy operations supply `H`.
- **Observe** — pulse, share-of-voice, dark-social, and measurement-loop skills supply `O` and separately report outcomes.

ECHO remains advisory until each versioned profile passes the shared reliability and outcome-calibration protocol.
