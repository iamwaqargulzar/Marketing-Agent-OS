# Scoring Semantics and Calibration Protocol

This document defines the shared semantics for all eight advisory frameworks. It is the human-readable companion to [`framework-catalog.json`](framework-catalog.json), [`framework-catalog.schema.json`](framework-catalog.schema.json), [`audit-run.schema.json`](audit-run.schema.json), and [`scripts/rubric-score.py`](../scripts/rubric-score.py). If prose and executable policy disagree, the versioned catalog and scorer are authoritative and the prose must be corrected.

## 1. Claim Boundary

Framework scores are **advisory quality-control summaries**, not validated predictions of ranking, revenue, retention, reach, or any other business outcome. A score may support prioritization and a publish/go-live gate only for the declared framework, profile, target, and observation date. It must not be compared across frameworks or profiles.

A framework becomes outcome-calibrated only after the study in [§8](#8-calibration-and-reliability) is completed for a named population, version, and outcome. Until then every result carries `advisory: true` and `external_validity: advisory-until-outcome-calibrated`.

## 2. Unit and Context

Every run declares:

- `framework` and `profile`: the versioned rubric and one valid weighting/applicability profile.
- `target`: one auditable artifact, domain, program, portfolio, scope, or system.
- `observed_at`: the date on which the evidence set is frozen.
- `context`: every framework-required comparison and operating assumption.
- `items`: item states with evidence for every observed state.

Changing the target, profile, material context, observation date, or catalog version creates a different run. Trend reports preserve each run; they do not overwrite history or compare unlike units.

## 3. Item States

| State | Meaning | Points | Evidence |
|---|---|---:|---|
| `pass` | The declared criterion is satisfied. | 10 | Required |
| `partial` | The criterion is materially but incompletely satisfied. | 5 | Required |
| `fail` | The criterion is not satisfied. | 0 | Required |
| `unknown` | The item applies, but sufficient evidence was not observed. | None | Gap reason |
| `na` | The item genuinely does not apply under a catalog-declared conditional policy. | Excluded | Reason required |

An omitted item is `unknown`, never `partial` or `fail`. `N/A` is not a convenience for missing data and is rejected for unconditional items. A failed veto is still a `fail`; veto policy is applied after item scoring.

## 4. Evidence and Confidence

Every observed item cites a source, source date, evidence type, and confidence. Evidence dated after `observed_at` is invalid.

| Type | Use |
|---|---|
| `measured` | Direct observation from the target or a first-party system of record. |
| `user-provided` | A supplied record that the run could not independently verify. |
| `calculated` | A reproducible transformation of cited inputs. |
| `estimated` | A stated assumption or model-based estimate. |
| `proxy` | An adjacent signal standing in for the desired observation. |

`high`, `medium`, and `low` confidence describe the reliability of that evidence for the item, not the auditor's enthusiasm. The scorer reports aggregate `score_confidence`; it never upgrades a weak source because many weak observations agree.

## 5. Coverage and Scoring

All applicable items require an observed `pass`, `partial`, or `fail` before a comparable total is emitted. The v18 threshold is therefore **100% applicable evidence coverage**. Incomplete runs remain useful: they return dimension coverage, a best/worst score interval, explicit gaps, `score_state: NOT_SCORED`, and normally `verdict: UNDECIDED`.

For a complete run:

1. Item points are averaged exactly within each included dimension and scaled to 0–100. A fractional dimension value is not floored before weighting.
2. Profile dimension weights are applied with exact decimal arithmetic.
3. The weighted overall result is floor-rounded once, at the final documented rollup boundary. Score-interval bounds follow the same rule; a displayed dimension value never feeds a rounded value back into the calculation.
4. Named composite scores — such as ROAS RQS, SEND EQS, and STAR SQS — run only after every required dimension is independently complete and comparable. Each is a profile-weighted arithmetic mean of its dimensions under the same floor-once rule above; only the final documented composite value is floored.

The common descriptive bands are Excellent 90–100, Good 75–89, Medium 60–74, Low 40–59, and Poor 0–39. Bands are labels, not empirical outcome probabilities.

## 6. Veto, Status, and Verdict

`status` reports execution state; `verdict` reports the gate decision. They are orthogonal.

| Condition | Status | Verdict | Final score |
|---|---|---|---|
| Complete, no veto, score >=75, no failed items | `DONE` | `SHIP` | Raw score |
| Complete, remediation needed | `DONE_WITH_CONCERNS` | `FIX` | Raw score |
| Exactly one failed veto | `DONE_WITH_CONCERNS` | `FIX` | `min(raw, 59)` |
| Two or more failed vetoes | `DONE` | `BLOCK` | Not emitted |
| Two or more verified vetoes, with other applicable gaps | `DONE` | `BLOCK` | Not emitted (`NOT_SCORED`) |

A `SHIP` whose `score_confidence` is `low` additionally carries a `confidence_caveat` string in the run output: the evidence mix is weak, the handoff summary's first line must lead with the caveat, and the verdict is treated as provisional until stronger evidence lands. The caveat is run-output and handoff text only — it is not an artifact-schema field.
| Applicable evidence missing | `NEEDS_INPUT` | `UNDECIDED` | Not emitted |

A completed blocked audit is not `BLOCKED` status. A veto is triggered only by verified failure, not by absent access or missing data. Unknown veto evidence keeps the run undecided unless two other verified vetoes independently determine `BLOCK`; remaining gaps still keep that result `NOT_SCORED`.

## 7. Reproducible Execution

Prepare a JSON run conforming to `references/audit-run.schema.json`, then execute:

```bash
AARON_SKILLS_ROOT="${CLAUDE_PLUGIN_ROOT:-$(git rev-parse --show-toplevel 2>/dev/null || true)}"
if [ -z "$AARON_SKILLS_ROOT" ] \
  || [ ! -f "$AARON_SKILLS_ROOT/scripts/rubric-score.py" ] \
  || [ ! -f "$AARON_SKILLS_ROOT/references/framework-catalog.json" ]; then
  printf '%s\n' 'Aaron scoring runtime unavailable; return NOT_SCORED without a verdict or persistent artifact.' >&2
  exit 1
fi
python3 "$AARON_SKILLS_ROOT/scripts/rubric-score.py" check-catalog
python3 "$AARON_SKILLS_ROOT/scripts/rubric-score.py" score path/to/audit-run.json
```

For STAR, score each creator partnership separately — the creator, their deliverable, and the attributed outcome — under its own goal, `assessment_time`, `observed_at`, and catalog version. A budget-weighted mean of the per-partnership SQS may summarize a multi-creator campaign but never replaces the per-partnership diagnosis. Forecast and actual reads never mix.

Human-readable audit artifacts follow [`audit-artifact.schema.json`](audit-artifact.schema.json) and [`auditor-runbook.md`](auditor-runbook.md). Every durable artifact preserves the scorer's `catalog_version` and complete typed `context`; scalar summaries are not substitutes. Preserve the typed input and scorer output beside the narrative artifact when the host supports files.

If a standalone installation does not contain the scorer and catalog checked above, fail closed: report `NOT_SCORED`, do not hand-calculate a total or verdict, and do not persist an audit artifact.

## 8. Calibration and Reliability

Do not announce predictive validity from an arbitrary audit count. Register a study before inspecting outcomes:

1. **Population and unit**: name the target population, inclusion/exclusion rules, framework profile, catalog version, market, and observation window.
2. **Outcome**: define one independently measured outcome, its lag, attribution rule, minimum detectable effect, and missing-data treatment.
3. **Sample plan**: justify sample size from the intended precision or power; record selection and survivorship risks.
4. **Rater reliability**: have at least two blinded raters independently score a representative subset. Report weighted kappa for ordinal item states and ICC for total scores, with confidence intervals and adjudication rules.
5. **Criterion validity**: test association and calibration against the preregistered outcome on held-out data. Report uncertainty, effect size, baseline comparison, and subgroup stability; do not select thresholds on the evaluation set.
6. **Version lock**: results validate only the named catalog/profile/version. Material rubric changes require revalidation.
7. **Decision record**: store protocol, data lineage, exclusions, code, results, limitations, and the approved scope of claims.

Until both reliability and criterion-validity evidence meet the preregistered bar, keep the framework advisory. A failed or inconclusive calibration study is a result to report, not a reason to tune the rubric silently.

## 9. Change Control

Any scoring-policy change requires synchronized updates to the catalog, schemas if needed, scorer tests, affected benchmark prose, auditor skills, golden math, and version records. Never change item identity, weights, vetoes, or applicability in prose alone.
