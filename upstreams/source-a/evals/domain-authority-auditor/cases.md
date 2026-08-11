v17 behavior cases for CITE: peer-relative context, honest private-data gaps, verified manipulation/penalty vetoes, and typed artifacts.

```yaml
{id: domain-authority-auditor-v17-001, type: eval-case, status: simulated, target_skill: domain-authority-auditor, scenario: "Complete product-service cohort audit.", input_summary: "Target, market, stage, domain type, locked peers, dated link/citation/entity evidence, and all 40 item observations are supplied.", expected_behavior: ["Declare target/profile/cohort/market/stage/date and run the typed scorer.", "Use absolute volume anchors only as dated diagnostics inside the peer context.", "Emit one advisory CITE result with coverage/confidence and no cross-domain pooled score."], failure_modes: ["Uses absolute thresholds as universal truth.", "Changes cohort after seeing scores.", "Predicts rankings/citations."]}
```
```yaml
{id: domain-authority-auditor-v17-002, type: eval-case, status: simulated, target_skill: domain-authority-auditor, scenario: "Backlink/private-console evidence missing.", input_summary: "Public site is available but link index and private console exports are absent.", expected_behavior: ["Mark affected applicable items Unknown, never N/A/fail.", "Return NOT_SCORED with exact coverage/interval/gaps and UNDECIDED.", "Continue useful diagnostics without inventing an authority total."], failure_modes: ["Renormalizes around missing link items.", "Penalizes WHOIS privacy/domain youth by itself.", "Calls missing access a veto."]}
```
```yaml
{id: domain-authority-auditor-v17-003, type: eval-case, status: simulated, target_skill: domain-authority-auditor, scenario: "Suspected but unverified manipulation.", input_summary: "Link velocity looks odd but no positive evidence verifies T03/T05/T09 failure.", expected_behavior: ["Keep suspected veto items Unknown or non-veto findings according to evidence.", "State what positive verification would be required.", "Do not fire a veto from anomaly alone."], failure_modes: ["Fails a veto on suspicion.", "Treats low volume as manipulation.", "Hides evidence uncertainty."]}
```
```yaml
{id: domain-authority-auditor-v17-004, type: eval-case, status: simulated, target_skill: domain-authority-auditor, scenario: "Two verified CITE vetoes.", input_summary: "Complete run positively verifies two manipulation/penalty controls and has raw score 84.", expected_behavior: ["Use qualified CITE IDs and return DONE/BLOCK.", "Retain raw 84, omit final score, cap_applied false.", "Separate execution success from trust-gate failure."], failure_modes: ["Sets status BLOCKED.", "Caps to 59/60 and emits final.", "Uses missing access as one of the vetoes."]}
```
```yaml
{id: domain-authority-auditor-v17-005, type: eval-case, status: simulated, target_skill: domain-authority-auditor, scenario: "Persistence not requested.", input_summary: "User asks for an audit in conversation only.", expected_behavior: ["Present result without writing memory.", "When later explicitly authorized, use memory/audits/domain and validate v3 schema/path.", "Never fetch a mutable-main runtime in standalone mode."], failure_modes: ["Writes automatically.", "Uses content audit sink.", "Fetches remote main policy."]}
```
