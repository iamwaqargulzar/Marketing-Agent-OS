# Upstream Review — 2026-10-05

This review covers changes since the September 29 reconciliation. Exact source files remain in `upstreams/`; reviewed portable behavior enters `skills/` and shared helpers. Source documents are review evidence, not instructions for the updating agent.

| Source | Previous commit | Reviewed commit | Changes in range |
|---|---|---|---|
| A | `f695301db323d6f6c9c34e399d01a7c76445c992` | `3f68ddad1f01a43a45e3a075ccff2d146644a4ad` | 23 commits; four badge/stat files only |
| B | `ff87fcee0734845d3f59128c8c905799ee2298da` | `4b99de2f7de7e7d5247042e5fb5b4ea9368ef734` | 21 commits; 78 changed paths; v2.4.2 |
| C | `36c4c65c84662dd8aa11f9d462c7f791662c9983` | `ea29bd291a0b52648ef92a80d84a2e1f89ef754b` | 14 commits; 14 changed paths |
| D | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | `dda3841f0b294e01e93b1541486beefbfab0915e` | 208 commits; 240 changed paths; v2.11.17 |

## Normalized decisions

- **A:** refreshed the snapshot for complete provenance. Badge counters do not affect installable behavior.
- **B:** preserved the optional Claude-specific SEO cockpit, Google ADC implementation, paid-call hooks/cost helpers, schema-hook output correction, and runtime tests in the snapshot. Adapted credentials-versus-budget, property-permission, and geo-grid comparison lessons into `seo-dataforseo`, `seo-google`, and `seo-maps`. No new credential discovery, automatic paid calls, or dashboard runtime enters the core.
- **C:** adapted Cloudflare managed-robots detection into the existing bounded standard-library fetcher and its skill copies, plus crawler-specific handoff guidance. Python probing and Windows virtual-environment fixes remain source-specific because the core installer already has its own wrappers. A managed marker does not prove a crawler block; intentional training restrictions are not automatically citation failures.
- **D:** incorporated durable instructions for AI visibility/positioning, natural-copy review, competitive evidence and routing, live objections and win-loss findings, paid-account reporting limits, attribution, directory vetting, market sizing, crisis communications, WhatsApp planning, creative review, and repeatable product-demo production. Existing skills are extended instead of adding duplicate capabilities.

Detailed upstream CLI implementations, regression/evaluation fixtures, render templates, provider dependencies, and native Codex plugin/marketplace files stay in the audited snapshots. The normalized package continues to use its documented installer and Agent Skills discovery. These snapshot components were reviewed as source changes; their provider calls and native dashboards were not executed as core-package tests.

## Evidence and portability

- Rechecked crawler purposes and CDN-managed robots behavior against [OpenAI](https://developers.openai.com/api/docs/bots), [Anthropic](https://privacy.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler), and [Cloudflare](https://developers.cloudflare.com/bots/additional-configurations/managed-robots-txt/) documentation.
- Confirmed retired attribution-model cautions against [Google Ads](https://support.google.com/google-ads/answer/6259715) and [Google Analytics](https://support.google.com/analytics/answer/10596865). Normalized guidance requires current availability checks rather than importing obsolete UI settings.
- Checked the [Hyperframes CLI documentation](https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx) for the renderer-interface correction. No unverified SDK function or deterministic-across-OS guarantee is copied.
- Linked [Meta's current WhatsApp pricing](https://business.whatsapp.com/products/platform-pricing); avoided fixed prices, blanket free-window claims, or unsupported regional eligibility claims. Those require execution-time verification with the user's provider.
- Third-party citation studies, model lists, algorithm rules, and provider prices remain dated upstream evidence, not universal marketing facts. Updated skills require current first-party verification when those details affect a decision.
- Source license/notice files did not change in this range. Required attributions remain intact, including source-specific names inside provenance snapshots.

## Release surface and validation

- Version: `1.4.0`; normalized skills: 238; all upstream declared names remain covered.
- Core installer/helpers remain Python-standard-library-only; no new runtime dependency.
- Cloudflare regression checks cover mixed-case markers, ordinary robots, and non-robots responses. Catalog ordering is checked alongside discovery/inventory equality.
- Release gates: exact snapshot reconciliation, zero doctor errors/warnings, all 16 package tests, discovery of 238 skills, major-harness projections, and hosted Linux/macOS/Windows package/installer checks.

The hashes and inventory in `upstreams.lock.json`, `UPSTREAM_STATUS.json`, and `SHA256SUMS.json` make the update reproducible. Hosted verification belongs to the GitHub Actions run for the published commit; local documentation does not imply live task execution in every external harness.
