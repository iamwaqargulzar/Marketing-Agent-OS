# Connector Integration Playbook

The end-to-end pipeline for connecting an external service to this library.
Distilled from the four v12.2–v12.5 connector waves (Resend, Firecrawl,
Tavily, DoH/Pageviews/GDELT); following it turns "integrate service X" from
exploratory work into checklist work. The only judgment calls left are the
three marked ⚖️ — everything else is mechanical and guarded by CI.

## Phase 0 — Qualify (⚖️ three decisions before any code)

**1. Category.** Which `~~category` placeholder does the service serve
([CONNECTORS.md](../CONNECTORS.md) §Tool Categories)? If none fits, adding a
category is a separate, deliberate change — do not invent one casually.

**2. Tier: connector vs recipe.** Write a bundled stdlib connector **only**
when the integration needs:

- **composition** — one logical task = many calls (e.g. `doh.py auth` ≈ 15+
  DNS lookups), or
- **normalization** — response quirks a recipe can't express (GDELT's
  plain-text throttle notice on HTTP 200, Wikimedia date windows, Resend's
  dry-run gating).

A single-URL GET with a clean JSON answer (crt.sh, W3C Nu, oEmbed, HN
Algolia) stays a **recipe row** in CONNECTORS.md plus one sentence in the
relevant skill — no code, no tests, no maintenance surface.

**3. Safety class.** Read-only public fetch · delegated fetch · external-state
mutation — see the class table in [SECURITY.md](../SECURITY.md) §Connector
network behavior. The class fixes the gates you must build in Phase 2.
When a service can both read and mutate, the mutating subcommands take the
mutation gates; classification is per-subcommand, not per-vendor.

## Phase 1 — Verify before building

- Read the **primary vendor docs** — prefer machine-readable forms
  (`llms.txt`, Mintlify `.md`-suffix pages) over blog posts. Blog claims
  (e.g. "keyless") must be confirmed against the API reference or a live call.
- **Live-test the golden path** with a minimal real request before writing
  the connector. Every wave this caught something the docs did not say:
  audiences→segments deprecation (Resend), SPF `redirect=` semantics
  (gmail), GDELT's two throttle shapes.
- Record `endpoints verified against <docs> <YYYY-MM>` in the connector
  docstring and the changelog entry. Freshness claims must be dated.

## Phase 2 — Implement (house style)

Match `openpagerank.py` / the newest wave's connectors:

- [ ] Python 3 **stdlib only**; all HTTP through `_http.py` (extend it
      backward-compatibly rather than bypassing it — cf. the `method=` param).
- [ ] Module docstring = the contract: what/why, endpoints + auth, safety
      notes, caveats, full CLI synopsis.
- [ ] **Pure request-builders** (`build_url` / `build_spec` / parse fns)
      separated from network calls — they are what the offline tests cover.
- [ ] JSON to stdout; clear one-line error to stderr; exit codes:
      `0` ok/dry-run · `1` bad input · `2` HTTP/network error ·
      `3` auth/credits/rate-limit (with a where-to-get-a-key hint) ·
      `4` robots-disallowed.
- [ ] Keys read from env at call time (`--key` override), never persisted;
      keyless-capable services must degrade gracefully without one.
- [ ] Safety-class gates (SECURITY.md table): mutation ⇒ dry-run default +
      `--live` + idempotency-or-no-retry; delegated fetch ⇒ egress notice +
      local robots pre-flight + `--own-site`.
- [ ] Connectors report **facts, not verdicts** — presence, parsed tags, raw
      series. Pass/fail/veto judgments belong to the skills' rubrics.
      (Record-level structural facts — e.g. "two SPF records" — are facts.)

## Phase 3 — Test

- [ ] Offline spec tests in `tests/test_connectors_local.py` for every pure
      builder: request shapes, flag logic, boundary caps, and (for delegated
      fetchers) a monkeypatched robots-disallow case. **No network in CI.**
- [ ] Add one shape-asserting call to
      [`scripts/connectors/smoke-live.sh`](../scripts/connectors/smoke-live.sh)
      (manual, pre-release): keyed connectors behind an env-var conditional,
      rate-limit answers as SKIP.

## Phase 4 — Wire skills (⚖️ differentiation rule)

Wire a skill **only where the connector adds capability that skill lacks** —
never everywhere it could technically be used (Tavily went into 4 skills,
not Firecrawl's 8, because only 4 gained something distinct). For each skill:

- [ ] One paragraph in **Data Sources**, house pattern:
      `**<Bold capability name> (keyless/…)**:` +
      `python3 "${CLAUDE_PLUGIN_ROOT}/scripts/connectors/<helper>.py" …` +
      what it Measures + the labeling rule (Measured / Estimated / proxy) +
      the caveat the connector cannot cover + a
      `[scripts/connectors/README.md]` link.
- [ ] Bump the skill's `version` AND `metadata.version` to the new bundle
      version (untouched skills keep their last-changed version — mixed
      versions are the convention).
- [ ] Keep the "deliberately NOT wired" list: name each plausible-but-skipped
      skill and why (AUP conflict, format incompatibility, duplication) in
      the changelog — negative decisions are documentation too.

## Phase 5 — Document (six touchpoints)

- [ ] `CONNECTORS.md`: bundled-helpers table row · keyless/public table row ·
      affected category rows (free-path + agent-default) · env-var table (if
      keyed) · MCP section (if the vendor ships one; add the endpoint to
      `docs/mcp-catalog.json` — remote HTTP entries only).
- [ ] `scripts/connectors/README.md`: helpers table row + safety-contract
      paragraph when the class introduces new behavior.
- [ ] `SECURITY.md`: add the connector to its class row; new class ⇒ new
      clause.

## Phase 6 — Track

The 10-surface list in [CONTRIBUTING.md §6](../CONTRIBUTING.md) + a `VERSIONS.md`
changelog entry (what shipped · skills wired · safety gates · verified-date ·
deliberately-not-done list). `scripts/check-versions.sh` fails CI on any
drift, so run it locally after this phase.

## Phase 7 — Regress (all must pass)

```bash
python3 tests/test_connectors_local.py
python3 -m py_compile scripts/connectors/*.py
bash scripts/check-stdlib-only.sh
bash scripts/check-versions.sh
cmp marketplace.json .claude-plugin/marketplace.json
for d in narrative/*/*/ seo-geo/*/*/ social/*/*/ email/*/*/ ad/*/*/ influencer/*/*/ launch/*/*/ protocol/*/; do
  bash scripts/validate-skill.sh "${d%/}" || exit 1
done
bash scripts/connectors/smoke-live.sh   # manual, live — before release
```

## Phase 8 — Record

One decision-log entry per wave (project memory or PR description): the
conventions this wave set or extended, vendor API gotchas, the
deliberately-not-wired list, and the **evaluated-and-rejected** services
with reasons — so the next integration starts from precedent instead of
re-litigating.
