# Upstream Review — 2026-09-29

This record explains how the September 29 upstream changes were handled. Exact source files remain in `upstreams/`; only reviewed, portable behavior enters the normalized package.

| Source | Previous commit | Reviewed commit | Normalized decision |
|---|---|---|---|
| source A | `b08683918e2bab70502f3d65ab0ae2f32beff2c6` | `f695301db323d6f6c9c34e399d01a7c76445c992` | Preserved the skill dashboard, fixtures, and runtime-control refinements in the audited snapshot. No core dashboard was added because it depends on source-specific memory, envelope, roster, and control-artifact layouts. |
| source B | `a1480c7e590b16001bd9dc1627eacdcd44d580f9` | `ff87fcee0734845d3f59128c8c905799ee2298da` | Added portable `seo-agentic` and `seo-matomo` skills. Reviewed current search facts, hostile-input handling, installer security, URL safety, rendering, schema, analytics, and dependencies. Source-specific scripts, credential installers, and third-party dependencies remain isolated in the snapshot. |
| source C | `9484cf0920da04448cf89ea7d710cffeddbbdcab` | `36c4c65c84662dd8aa11f9d462c7f791662c9983` | Preserved installer, fetcher, dependency, report-template, and chart changes in the audited snapshot. The normalized installer and report tools remain independently maintained. |
| source D | `5cd4a7eae3a9a7b5d2aceb0613f7d1f7c4b65968` | `5b2c0007766c6a1cf1d53fd8fc73e979e0821022` | Added portable format-volatility and repeated-run measurement guidance to `ai-seo`; omitted names and dated platform statistics from the normalized instructions. |

## Resulting release surface

- Version: `1.3.0`
- Normalized skills: 238
- New skills: `seo-agentic`, `seo-matomo`
- Updated skill: `ai-seo`
- Core installer remains Python-standard-library-only.
- Source snapshots remain pinned by commit and platform-normalized tree hash in `upstreams.lock.json`.

## Release gate

The release is publishable only when:

- every snapshot matches its lock and every declared upstream skill name is represented;
- `scripts/doctor.py` reports no errors or warnings;
- all package tests pass;
- Agent Skills CLI independently discovers all 238 skills; and
- hosted Linux, macOS, Windows, and harness-projection jobs pass.
