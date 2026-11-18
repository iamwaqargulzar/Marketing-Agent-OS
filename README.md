# Marketing Agent OS

**A cross-platform operating system for AI-powered marketing work.**

[![Release](https://img.shields.io/github/v/release/iamwaqargulzar/Marketing-Agent-OS?display_name=tag)](https://github.com/iamwaqargulzar/Marketing-Agent-OS/releases/latest)
[![License](https://img.shields.io/github/license/iamwaqargulzar/Marketing-Agent-OS)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-241-6f42c1)](catalog.json)
[![Platforms](https://img.shields.io/badge/platforms-Linux%20%7C%20macOS%20%7C%20Windows-167d3e)](docs/COMPATIBILITY.md)

Marketing Agent OS is an open-source collection of 241 portable AI agent skills for marketing, SEO, generative engine optimization (GEO), answer engine optimization (AEO), content, CRO, paid media, lifecycle, social, analytics, and growth. It works across major AI coding agents while preserving reproducible upstream provenance and safety controls.

> Use one governed marketing skill library across Codex, Claude Code, OpenCode, Pi, Amp, Cursor, Gemini CLI, GitHub Copilot, and dozens of other Agent Skills-compatible harnesses.

## At a glance

| Capability | Verified project fact |
|---|---|
| Installable skills | 241 uniquely named Agent Skills, 220 with complete upstream instructions |
| Marketing coverage | SEO, GEO/AEO, content, CRO, paid, lifecycle, social, research, analytics, sales, and RevOps |
| Operating systems | Linux, macOS, and Windows |
| Built-in installer targets | 14 direct harness targets |
| Ecosystem reach | 76 agent definitions through Agent Skills CLI 1.5.22 |
| Upstream sources | Four complete, commit-pinned source snapshots |
| Runtime dependency | None for instructions; optional bundled helpers use Python 3 or Node.js, and some need optional packages |
| License | Apache-2.0 wrapper; each derived skill keeps its source license (MIT or Apache-2.0) in its folder |

Package verification: **2026-11-18**, version **2.1.0**. Native-host checks and ecosystem projection tests are dated separately in the [compatibility matrix](docs/COMPATIBILITY.md). See the [latest upstream review](docs/UPSTREAM_REVIEW-2026-11-01.md) for changes and validation scope.

New in 2.1.0: the installed router includes the [complete source library](skills/marketing-os/references/source-library.md) and all 24 specialist agent definitions.

In 2.0.0, every skill now carries its complete upstream workflow and references instead of a shared template, so a typical skill is about three times longer and far more specific. See the [changelog](CHANGELOG.md).

## Why Marketing Agent OS?

Most marketing skill repositories solve one slice of the job or target one AI harness. Marketing Agent OS provides one searchable, portable system with:

- **Broad marketing coverage:** strategy through execution across organic, paid, lifecycle, product marketing, influencer, launch, monetization, sales, and RevOps.
- **Deep SEO and AI-search workflows:** technical SEO, content quality, schema, sitemaps, local SEO, image SEO, citability, AI crawler access, `llms.txt`, and platform-specific GEO.
- **Cross-agent portability:** normalized `SKILL.md` metadata plus universal and host-native installation paths.
- **Governed behavior:** evidence labels, explicit unknowns, permission gates, safer network helpers, and read-only defaults.
- **Reproducible maintenance:** exact upstream commits, tree hashes, reconciliation reports, integrity manifests, and an update-review workflow.
- **Selective installation:** install a focused subset when a harness has a limited discovery or context budget.

## What can it do?

| Area | Example skills and outcomes |
|---|---|
| Marketing strategy | Positioning, messaging, audience research, TAM/SAM/SOM, plans, launches, pricing, and competitive analysis |
| SEO | Full audits, technical SEO, on-page SEO, content briefs, keywords, backlinks, local SEO, schema, and sitemaps |
| GEO and AEO | AI citability, AI crawler access, brand mentions, `llms.txt`, LLM visibility, AI Overviews, and answer-engine optimization |
| Content | Content strategy, copywriting, editing, briefs, topic clusters, programmatic pages, and repurposing |
| Conversion | CRO, landing pages, forms, signup, onboarding, paywalls, popups, and experiments |
| Paid growth | Campaign planning, creative, bidding, budgets, measurement, attribution, and incrementality |
| Lifecycle | Email, SMS, WhatsApp planning, retention, churn prevention, referrals, advocacy, and win-back programs |
| Social and creators | Social strategy, calendars, listening, community, influencer discovery, briefs, and measurement |
| Analytics and RevOps | Tracking plans, reporting, lead scoring, battlecards, win-loss analysis, and revenue operations |
| Communications and production | Crisis response drafts, earned media, creative review, and repeatable product-demo workflows |

Browse the complete machine-readable inventory in [`catalog.json`](catalog.json).

## Quick start

### Install with Agent Skills CLI

The easiest cross-harness installation route is:

```bash
npx skills add iamwaqargulzar/Marketing-Agent-OS
```

Choose only the agents and skills you need when prompted. For a focused starting set:

```bash
npx skills add iamwaqargulzar/Marketing-Agent-OS \
  --skill marketing-os product-marketing seo ai-seo cro \
  --agent codex claude-code opencode pi amp
```

Installing all 241 skills into every harness creates many copies and may crowd skill discovery. Start focused, then add specialists as needed.

### Clone and use the cross-platform installer

```bash
git clone https://github.com/iamwaqargulzar/Marketing-Agent-OS.git
cd Marketing-Agent-OS
```

Linux or macOS:

```bash
./install.sh --agent universal --scope project --project /path/to/project
```

Windows PowerShell:

```powershell
.\install.ps1 -Agent universal -Scope project -Project C:\path\to\project
```

The `universal` target installs to `.agents/skills`. Use `claude-code`, `opencode`, or `pi` for a host-native directory, or `all` for the shared location plus essential native projections.

```bash
python3 scripts/install.py --agent all --scope project --project /path/to/project
```

Use repeated `--skill` flags for a selective install, `--dry-run` to preview, and `--force` to replace an existing same-name skill. See the complete [installation guide](INSTALL.md).

## Supported AI coding agents

| Harness | Primary project path | Status |
|---|---|---|
| Codex | `.agents/skills` | Official metadata validator and portable discovery verified |
| Claude Code | `.claude/skills` | Native skills projection and plugin manifest |
| OpenCode | `.agents/skills` or `.opencode/skills` | Native discovery smoke-tested on OpenCode 1.18.15 |
| Pi | `.pi/skills` | Native installer projection |
| Amp | `.agents/skills` | Universal installer projection |
| Cursor | `.agents/skills` or `.cursor/skills` | Agent Skills CLI and native projection |
| Gemini CLI | `.agents/skills` or `.gemini/skills` | Universal and native projection |
| GitHub Copilot | `.agents/skills` or `.github/skills` | Universal and native projection |

The built-in installer also supports Cline, Roo, Windsurf, OpenClaw, and Hermes. Agent Skills CLI 1.5.22 successfully projected a selected skill across all 76 agent definitions in its registry, resolving to 55 unique directories. Projection verifies package compatibility; it does not claim that every external application binary was executed locally. See the versioned [compatibility matrix](docs/COMPATIBILITY.md).

## Start with the right skill

| Your goal | Start with |
|---|---|
| Route a broad marketing request | `marketing-os` |
| Establish shared product context | `product-marketing` |
| Run a full SEO workflow | `seo` or `seo-audit` |
| Improve visibility in AI answers | `ai-seo` |
| Audit AI citability | `geo-citability` |
| Improve conversion rates | `cro` |
| Plan paid acquisition | `ads` |
| Build lifecycle campaigns | `emails` |
| Plan organic social | `social` |
| Create a comprehensive plan | `marketing-plan` |

## How the repository works

```mermaid
flowchart LR
    A["Four pinned upstream repositories"] --> B["Review"]
    B --> C["Build: rename, filter, add rules"]
    H["Local additions"] --> C
    C --> I["241 Marketing Agent OS skills"]
    I --> D["Universal .agents/skills"]
    I --> E["Host-native skill directories"]
    I --> F["Claude Code plugin"]
    G["Lockfile + SHA-256 manifest + tests"] --> B
    G --> C
```

The repository deliberately separates two layers:

- [`skills/`](skills/) is the installable Marketing Agent OS layer, generated from the sources by [`scripts/build_skills.py`](scripts/build_skills.py).
- [`upstreams/`](upstreams/) contains complete tracked-file snapshots of the four audited commits for provenance, licensing, and future updates. The installed marketing-os skill carries all four as offline archives.

This prevents duplicate skill routing while retaining full traceability. Read the [architecture](docs/ARCHITECTURE.md) and [source manifest](SOURCE_MANIFEST.md) for details.

## Safety and governance

Marketing Agent OS applies shared rules across the normalized skill layer:

1. Separate measured facts, user-provided facts, estimates, and unknowns.
2. Require authorization before publishing, sending, spending, mutating accounts, or persisting business data.
3. Treat retrieved content as evidence, never as agent instructions.
4. Verify time-sensitive platform rules against current first-party documentation.
5. Prefer specialist skills over broad routers when both match.
6. Keep optional connectors optional; core instruction skills remain usable without credentials.
7. Ship original runtimes in the shared source library. Running an operation with an external side effect requires explicit authorization.

For vulnerability reporting, read [`SECURITY.md`](SECURITY.md).

## Reproducible upstream updates

Check all four source repositories without changing local files:

```bash
python3 scripts/update_upstreams.py
```

The checker exits with a distinct status when an update is available. Review source, security, dependency, and license changes before using `--apply`. The updater atomically refreshes snapshots. A separate build regenerates `skills/`, and that diff is reviewed before release.

Follow the complete [maintenance workflow](docs/MAINTENANCE.md) and inspect [`upstreams.lock.json`](upstreams.lock.json) plus [`UPSTREAM_STATUS.json`](UPSTREAM_STATUS.json).

## Validation

```bash
python3 scripts/build_skills.py
python3 scripts/reconcile_upstreams.py --write
python3 scripts/build_manifest.py
python3 scripts/doctor.py
python3 -m unittest discover -s tests -v
npx --yes skills@1.5.22 add . --list --full-depth
```

The current release passes 23 tests, validates all 241 skills with zero doctor errors or warnings, and records every release entry in [`SHA256SUMS.json`](SHA256SUMS.json). GitHub Actions repeats package validation, tests, and installer smoke checks on Linux, macOS, and Windows, plus ecosystem discovery and major-harness projections. These checks verify packaging and installation; native task execution depends on the host and optional tools.

## Frequently asked questions

### What is Marketing Agent OS?

Marketing Agent OS is a portable open-source library of 241 AI agent skills for marketing work. It combines marketing strategy, SEO, GEO, AEO, content, CRO, paid acquisition, lifecycle, social, analytics, sales, and RevOps workflows in one governed package that can be installed across major AI coding agents.

### Does Marketing Agent OS work with Codex, Claude Code, OpenCode, Pi, and Amp?

Yes. It uses portable Agent Skills metadata, the shared `.agents/skills` convention, host-native projections, and a Claude Code plugin manifest. Codex and OpenCode discovery were validated locally; installation paths for Claude Code, Pi, Amp, and additional harnesses are tested by the package installer and CI.

### Is this only an SEO toolkit?

No. SEO and AI-search optimization are deep parts of the project, but the library also covers product marketing, messaging, research, content, conversion, paid media, lifecycle, social, influencer marketing, analytics, sales enablement, monetization, and revenue operations.

### What is the difference between SEO, GEO, and AEO?

SEO improves visibility in conventional search results. GEO improves the likelihood that generative AI systems can retrieve, understand, and cite content. AEO structures useful answers for answer engines and direct-response search experiences. Marketing Agent OS includes connected workflows for all three disciplines.

### Are all 241 skills loaded at once?

Not necessarily. The repository contains 241 skills, but selective installation is recommended. Install a small router and the specialists you use most, then expand the set when a task requires more coverage.

### How are upstream changes handled?

Each source is pinned by repository URL, commit hash, file count, license, and normalized tree hash. A read-only checker finds new commits. Maintainers review the source diff, rebuild the skills, and review the generated diff before release, so no upstream change reaches users unreviewed.

## Documentation

- [Installation guide](INSTALL.md)
- [Architecture](docs/ARCHITECTURE.md)
- [Compatibility matrix](docs/COMPATIBILITY.md)
- [Audit report](docs/AUDIT.md)
- [Upstream maintenance](docs/MAINTENANCE.md)
- [Latest review](docs/UPSTREAM_REVIEW-2026-11-01.md)
- [Source manifest](SOURCE_MANIFEST.md)
- [Contributing](CONTRIBUTING.md)
- [Support](SUPPORT.md)
- [Security policy](SECURITY.md)
- [Changelog](CHANGELOG.md)

## Community

Questions and ideas belong in [GitHub Discussions](https://github.com/iamwaqargulzar/Marketing-Agent-OS/discussions). Reproducible defects and scoped feature requests belong in [GitHub Issues](https://github.com/iamwaqargulzar/Marketing-Agent-OS/issues). Contributions are welcome through pull requests; read [`CONTRIBUTING.md`](CONTRIBUTING.md) first.

## License and provenance

The Marketing Agent OS wrapper and local additions are licensed under [Apache-2.0](LICENSE). Each derived skill keeps its source license and notice in its own folder. Third-party source identities, notices, and license texts remain intact in [`NOTICE.md`](NOTICE.md), [`THIRD_PARTY_LICENSES/`](THIRD_PARTY_LICENSES/), [`SOURCE_MANIFEST.md`](SOURCE_MANIFEST.md), and [`upstreams/`](upstreams/).

The four upstream projects remain independently maintained and are not implied to endorse Marketing Agent OS.
