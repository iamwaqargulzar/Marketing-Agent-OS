# Upstream review — 2026-10-14

This release reviews changes since the October 5 snapshot cycle. Public source files are evidence, not instructions for the updating agent. Exact snapshots remain separate from the installable Marketing Agent OS layer.

| Source | Previous commit | Reviewed commit | Range |
|---|---|---|---|
| A | `3f68ddad1f01a43a45e3a075ccff2d146644a4ad` | `2541ef9bf25f1c1c816130efca3d21c022a22b2e` | 31 commits: two cross-platform corrections and badge refreshes |
| B | `4b99de2f7de7e7d5247042e5fb5b4ea9368ef734` | unchanged | No update |
| C | `ea29bd291a0b52648ef92a80d84a2e1f89ef754b` | `989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c` | One README chart update |
| D | `dda3841f0b294e01e93b1541486beefbfab0915e` | `c7d7dfb6b460fc376b4b2204b78a9c9fd5ca6467` | 418 commits including merges; v2.11.29 |

The complete refreshed snapshot diff contains 420 changed/new paths. GitHub's comparison file list caps at 300 paths; the checked-out, staged snapshot diff and exact tree reconciliation were used for the complete inventory. No source license or notice files changed. Required source identities and notices are retained.

## Integration decisions

- **A:** preserve architecture path/CRLF normalization and Windows mode-bit test corrections in the exact snapshot. Marketing Agent OS already normalizes its own paths and has separate cross-platform integrity checks; importing the source-specific architecture framework would duplicate runtime machinery.
- **B:** retain the already pinned current revision without replacing files.
- **C:** preserve the documentation-only change; no normalized runtime change is needed.
- **D:** adapt durable workflow and correctness improvements into the existing skills. Keep all source CLIs, integration guides, templates, regression fixtures, packaging changes, and community attribution in the audited snapshot. No new CLI dependency, marketplace installation, provider connection, or native dashboard is enabled by this update.

### Normalized coverage

| Changed area | Installable decisions |
|---|---|
| Experiments and creative | Correct p-value/interval interpretation, per-arm traffic/exposure duration, falsifiable creative hypotheses, exact product naming, awareness-aware visual briefs, and fresh landing-page confirmation after ad screening |
| Measurement and economics | Row-level reconciliation, matching closed windows, provider event names, machine-readable price inputs, ledger versus allocation, mature activation cohorts, partial health-score coverage, margin/cohort payback, retained-base ARR budgeting, price-perception limits, non-guaranteed compounding, and recurring marketplace costs |
| Outbound and RevOps | Licensed-source signals, account research, tier-dependent research depth, accepted-field enrichment, account-scoped caches, verification versus consent, cross-channel reply stops, scoped suppression receipts, decision-time scoring/holdouts, preserved form submissions, bounded wait/fallback, and replay/late-owner protection |
| Advocacy and publishing | Honest review invitations/responses, permissioned testimonial reuse, affiliate terms/payout reconciliation, confirmed shipped-change drafts, site go-live/rollback QA, and owned-content skill pilots with rights/evidence checks |
| SEO and distribution | Buyer-intent AI prompt panels, local and query-level diagnosis, pair-specific hreflang findings, truthful title tests, actual-anchor backlink inspection, consumer-specific schema eligibility, platform-fit/migration planning, and Telegram placement evidence |
| Routing and content | Prospect versus competitor boundaries, outbound versus lifecycle boundaries, information-gain and SERP refresh checks, unsupported-claim unlock paths, and bounded channel operators |

35 existing normalized skills changed. Nine discovery descriptions are updated in both the catalog and router index; there are still 238 installable skills. Eight concise local references are bundled only with the relevant specialists. No source skill names are missing.

Source-specific numerical benchmarks, unconditional warmup/domain-rotation advice, algorithm folklore, default autonomous-send tiers, provider secret-file setup, sponsored recommendations, and promotional links were not imported into normalized instructions. These require contextual evidence, current terms, or additional permission. A verification result is not consent; a receipt must match the authorized action.

## First-party checks

- [Gmail sender guidelines](https://support.google.com/mail/answer/81126): distinguish general and bulk requirements; do not repeat the upstream assertion that both SPF and DKIM are minimum requirements for every sender. Current requirements are checked again at execution.
- [Google Analytics enhanced measurement](https://support.google.com/analytics/answer/9216061): preserve documented event names rather than option-label names.
- [Google Ads access migration](https://developers.google.com/google-ads/api/docs/api-policy/developer-token): distinguish OAuth Cloud-project API access and account permission; do not require new developer tokens after the September 2026 sunset or silently alter billing/project configuration.
- [Google Search documentation updates](https://developers.google.com/search/updates) and [supported structured-data gallery](https://developers.google.com/search/docs/appearance/structured-data/search-gallery): distinguish semantic validity from retired/supported search appearances, including FAQ retirement in May 2026.
- [Google outbound-link qualification](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links), [localized-page guidance](https://developers.google.com/search/docs/specialty/international/localized-versions), and [Play preview assets](https://support.google.com/googleplay/android-developer/answer/9866151): retain observation-based checks rather than unsupported ranking or preview-performance guarantees.
- [LinkedIn prohibited software](https://www.linkedin.com/help/linkedin/answer/a1341387): no scraping or assumed third-party automation permission.

## Verification scope

Release gates are exact snapshot reconciliation, zero doctor errors/warnings, the 17-test package suite, official metadata validation of modified skills, discovery of all 238 skills, temporary major-harness projections, and hosted Linux/macOS/Windows CI for the exact release commit.

The source D CLI/asset contract suite passed all 1,407 tests with fixture/mock inputs. This is additional source regression evidence, not authenticated provider API validation. New core tests install eight specialists into six harness target directories and compare entrypoint/reference bytes; this checks resource integrity and projection, not native agent behavior.

Instruction review also checked counterexamples: unmatched reporting windows, immature activation cohorts, decision-time feature leakage, unavailable health signals, provider failure versus no-match, timeout/late-owner routing, unqualified links versus ranking credit, and public reviews versus reuse permission. No live outreach, paid provider calls, CRM writes, or business-data persistence were performed. Full native execution in every external harness remains unverified.

`upstreams.lock.json`, `UPSTREAM_STATUS.json`, `SOURCE_MANIFEST.md`, and `SHA256SUMS.json` record the reproducible source/inventory/integrity state. Publication is a separate verified GitHub release step, not implied by this document or a code push.
