# Rebuild and upstream review: 2026-11-01

This review compared all four current upstream repositories against the installed package, then rebuilt the installed layer. Source documents were treated as evidence, not as instructions.

| Source | Previous commit | Reviewed commit | Version |
|---|---|---|---|
| A | `79c145da` | `903d6479` | 20.2.0 |
| B | `23a2a811` | `6be93f45` | 2.5.0 |
| C | `989cae01` | unchanged | n/a |
| D | `e85f3cbc` | `88c79f65` | 2.14.0 |

## What the audit found

Version 1.6.0 passed all of its own checks, but those checks measured packaging, not content.

| Finding | Measured in 1.6.0 |
|---|---|
| Skills built from one shared template | 228 of 240 |
| Text unique to a typical skill | about 1.2 KB, against a typical upstream `SKILL.md` of about 12.9 KB |
| Skills under half the size of their upstream package | 94 |
| Skills with full upstream instructions reduced to redirects | 38 |
| Agents | 23 stubs of about 300 bytes, against about 150 KB upstream |
| License files inside skill folders | none, although single-skill installs copy MIT and Apache material |
| `license` field | Apache-2.0 on every skill, including MIT-derived ones |

## Decision

The installed layer was rebuilt. Snapshots, the installer, integrity tooling, and local additions were kept. See [ARCHITECTURE.md](ARCHITECTURE.md) for how the build works.

Local additions from 1.2.0 to 1.6.0 moved unchanged to `overlays/` for 56 skills. Some now overlap the upstream text they summarized. They were kept because they carry deliberate safety adaptations, such as not treating a missing header as proof a site is safe.

## Excluded from installs

These stay in `upstreams/`. Affected skills name them in their helper notes and tell the agent to use a connected tool or user data, or to report the step as unknown.

- **Sends or changes accounts:** `indexpush`, `resend`, `indexnow_submit`, `indexing_notify`, `bing_webmaster`
- **Credential setup:** `google_auth`, `matomo_auth`, `backlinks_auth`, `setup_mcp`, and helpers importing them, including `gsc_query`, `ga4_report`, `pagespeed_check`, and `crux_history`
- **Paid calls:** `dataforseo_merchant`, `keywordseverywhere_api`, `moz_api`, `nlp_analyze`
- **Source runtimes:** `registry-events`, `profile-resolver`, run and context tooling, dashboards, plugin marketplaces, and evals

## Known limits

- **Registry skills:** without `registry-events`, they return changes as proposals, or append to `memory/events/` when authorized. They do not get the upstream's projection tooling.
- **Google and paid-data steps:** these need a connected tool or supplied exports in the installed package.
- **Helpers:** tests confirm each one loads and prints help. Network behavior against live services was not exercised, and helpers were reviewed by static scan rather than line by line.
- **Vendor mentions:** tools from upstream's sponsor list still appear where they sit in neutral comparisons, with sponsor markers removed.
- **Attribution:** author names remain only in license files, notices, required CC BY or MIT credit, and book citations.
- **Dependabot alerts:** alerts on `upstreams/source-c/requirements.txt` concern a never-installed snapshot. Excluding the path from `dependabot.yml` may not clear existing alerts.
- **Native execution:** Codex loaded and used a skill. OpenCode listed skills only, and Claude Code was not run. See [COMPATIBILITY.md](COMPATIBILITY.md).
