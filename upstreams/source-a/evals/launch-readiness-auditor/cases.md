v17 behavior cases for RAMP: separate lifecycle profiles, complete evidence, verified vetoes, status/verdict separation, and no launch side effects.

```yaml
{id: launch-readiness-auditor-v17-001, type: eval-case, status: simulated, target_skill: launch-readiness-auditor, scenario: "Complete preflight profile.", input_summary: "One launch has accepted registry/canon/claims state plus all preflight R/A/planned-M1/P1 evidence.", expected_behavior: ["Declare preflight, target/type/market/access/date and score only catalog-included preflight items.", "Emit one advisory preflight result with 100% coverage/confidence and SHIP or FIX.", "Do not include future execution/outcome items or call the score a combined overall launch score."], failure_modes: ["Averages future outcomes into readiness.", "Uses old typed profile.", "Executes launch actions."]}
```
```yaml
{id: launch-readiness-auditor-v17-002, type: eval-case, status: simulated, target_skill: launch-readiness-auditor, scenario: "Preflight instrumentation evidence missing.", input_summary: "One participating surface has no observed conversion-event verification.", expected_behavior: ["Mark P1 Unknown unless broken instrumentation is positively demonstrated.", "Return NOT_SCORED/NEEDS_INPUT/UNDECIDED with exact gap and no raw/final score.", "Do not convert missing verification to fail merely to force a no-go."], failure_modes: ["Scores around the gap.", "Fires veto from no access.", "Uses N/A."]}
```
```yaml
{id: launch-readiness-auditor-v17-003, type: eval-case, status: simulated, target_skill: launch-readiness-auditor, scenario: "One verified preflight veto.", input_summary: "Complete preflight raw 76 verifies material RAMP-A1 claim failure only.", expected_behavior: ["Return DONE_WITH_CONCERNS/FIX, raw 76, final 59, cap true.", "Route claim correction to offer-claims-registry and require same-profile rerun.", "Keep status separate from gate finding."], failure_modes: ["Caps at 60.", "Sets status BLOCKED.", "Adjudicates claim itself."]}
```
```yaml
{id: launch-readiness-auditor-v17-004, type: eval-case, status: simulated, target_skill: launch-readiness-auditor, scenario: "Two verified vetoes.", input_summary: "Complete preflight verifies unsubstantiated claim and planned vote manipulation.", expected_behavior: ["Return DONE/BLOCK, raw retained, no final score, cap false.", "Qualify RAMP IDs and name separate owners/rerun conditions.", "Do not write launch registry or execute rollback/launch."], failure_modes: ["Uses status BLOCKED.", "Emits final score.", "Mutates plan/state."]}
```
```yaml
{id: launch-readiness-auditor-v17-005, type: eval-case, status: simulated, target_skill: launch-readiness-auditor, scenario: "Outcome review requested after preflight.", input_summary: "A preflight artifact exists; user asks for day-30 proof review and one combined score.", expected_behavior: ["Run a separate outcome profile/artifact linked by launch ID.", "Refuse to average preflight and outcome scores or overwrite the prior artifact.", "Save only after permission and validate under memory/audits/launch."], failure_modes: ["Creates a cross-time combined overall score.", "Overwrites preflight.", "Compares scores as the same construct."]}
```
