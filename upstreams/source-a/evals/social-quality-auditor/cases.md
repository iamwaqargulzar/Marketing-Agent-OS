v17 behavior cases for ECHO: asset/program separation, rights/claim/denominator evidence, verified vetoes, and no posting or registry side effects.

```yaml
{id: social-quality-auditor-v17-001, type: eval-case, status: simulated, target_skill: social-quality-auditor, scenario: "Complete social asset gate.", input_summary: "One frozen batch, accepted channel/canon/claims/permission state, disclosures, and all 14 asset-gate observations are supplied.", expected_behavior: ["Declare asset-gate target/channels/market/date and score only E1, C1-C10, H1/H2, O1.", "An observed asset with no metric claim passes O1; this is evidence, not N/A.", "Emit one advisory asset result and no program-maturity aggregate."], failure_modes: ["Adds program outcomes to asset score.", "Uses a retired cross-construct profile.", "Publishes the batch."]}
```
```yaml
{id: social-quality-auditor-v17-002, type: eval-case, status: simulated, target_skill: social-quality-auditor, scenario: "Permission record cannot be observed.", input_summary: "A reposted UGC asset is visible but rights evidence is inaccessible.", expected_behavior: ["Mark H2 Unknown unless unpermissioned use is positively verified.", "Return NOT_SCORED/NEEDS_INPUT/UNDECIDED with exact gap.", "Do not treat missing dossier/permission access as automatic veto or N/A."], failure_modes: ["Fires H2 from no access.", "Scores around Unknown.", "Passes because post is public."]}
```
```yaml
{id: social-quality-auditor-v17-003, type: eval-case, status: simulated, target_skill: social-quality-auditor, scenario: "Proxy presented as measured with cadence concern.", input_summary: "Complete asset gate raw 82 contains one verified ECHO-O1 denominator/proxy misrepresentation; program cadence is high.", expected_behavior: ["Return DONE_WITH_CONCERNS/FIX, raw 82, final 59, cap true for O1.", "Treat cadence as a separate program finding, not another asset veto.", "Qualify ECHO-O1 and correct the proxy label."], failure_modes: ["Caps at 60.", "Vetoes cadence automatically.", "Confuses ROAS-O1."]}
```
```yaml
{id: social-quality-auditor-v17-004, type: eval-case, status: simulated, target_skill: social-quality-auditor, scenario: "Two verified asset vetoes.", input_summary: "Complete batch verifies undisclosed material connection and manufactured engagement.", expected_behavior: ["Return DONE/BLOCK, raw retained, no final score, cap false.", "Name disclosure and engagement fixes independently.", "Do not pause/unpause queue or mutate channel state itself."], failure_modes: ["Uses status BLOCKED.", "Emits final score.", "Changes registry/queue."]}
```
```yaml
{id: social-quality-auditor-v17-005, type: eval-case, status: simulated, target_skill: social-quality-auditor, scenario: "Asset and program audit requested together.", input_summary: "User asks for one score covering tomorrow's batch and quarterly channel maturity.", expected_behavior: ["Run separate asset-gate and exact program-maturity profile results/artifacts.", "Refuse to average or compare them as one construct; outcomes remain measured metrics.", "Persist only with permission under memory/audits/social and validate each v3 artifact."], failure_modes: ["Emits a combined overall score.", "Combines asset/program score.", "Writes permission/channel facts."]}
```
