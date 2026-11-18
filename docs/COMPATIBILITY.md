# Compatibility

Marketing Agent OS uses the open Agent Skills directory convention and provides native projections for hosts that use another location. The Python installer is standard-library-only and is wrapped for Linux/macOS (`install.sh`) and Windows PowerShell (`install.ps1`).

| Target | Project destination | User destination | Support level |
|---|---|---|---|
| universal | `.agents/skills` | `~/.agents/skills` | Primary portable target |
| Codex | `.agents/skills` | `~/.agents/skills` | Primary; official discovery location |
| OpenCode | `.opencode/skills` | `~/.config/opencode/skills` | Native projection; universal location also supported |
| Claude Code | `.claude/skills` | `~/.claude/skills` | Native skills projection and root plugin manifest |
| Pi | `.pi/skills` | `~/.pi/agent/skills` | Native projection |
| Amp | `.agents/skills` | `~/.agents/skills` | Universal projection |
| Cursor | `.cursor/skills` | `~/.cursor/skills` | Installer projection; smoke-test in the intended host version |
| Gemini CLI | `.gemini/skills` | `~/.gemini/skills` | Installer projection; smoke-test in the intended host version |
| GitHub Copilot | `.github/skills` | `~/.copilot/skills` | Installer projection; smoke-test in the intended host version |
| Cline / Roo / Windsurf | Host-specific `.*/skills` | Host-specific `~/.*/skills` | Installer projection; host-version verification recommended |
| OpenClaw / Hermes | Host-specific directories | Host-specific user directories | Compatibility projection; host-version verification required |

`--agent all` installs one shared copy plus the Claude Code, Pi, Cline, and Roo native projections. It deliberately deduplicates destinations.

## Ecosystem bridge

For hosts not represented by the built-in Python installer, use the Agent Skills CLI:

```bash
npx skills add iamwaqargulzar/Marketing-Agent-OS
```

On 2026-11-01, `skills` CLI 1.5.22 discovered all 241 skills and installed three skills with their resources for Codex, Claude Code, OpenCode, Pi, Amp, and Cursor. On 2026-08-11, the same CLI installed the `marketing-os` smoke-test skill across all 76 agent definitions in its registry, resolving to 55 unique project directories. This included shared/universal locations plus host-native projections for AiderDesk, Amp, Claude Code, Codex-compatible hosts, Continue, Cursor-compatible hosts, Devin, Goose, Kilo Code, Kiro, OpenHands, Pi, Qwen, Roo, Trae, Windsurf, and others. This verifies package discovery and file projection, not the runtime behavior of every external application.

Version 2.0.0 keeps the same portable installer. Skills now carry their own helpers, some of which need optional Python packages or Node.js. As of 2.1.0 all four complete source trees also ship as offline archives inside the router.

The package suite also installs thirteen specialist skills into temporary Codex, Claude Code, OpenCode, Pi, Amp, and Cursor projects and verifies all installed resource bytes. Hosted CI runs this check on Linux, macOS, and Windows. These checks prove file projection, not native agent execution or successful provider operations.

On 2026-11-01, Codex CLI 0.163.0 ran in a clean project with the universal install, loaded `copywriting`, and quoted workflow text from its `SKILL.md`. OpenCode 1.19.4 listed the installed skills through `opencode debug skill`, but no prompt was run because its configured model was unavailable. A Claude Code run could not complete because the local CLI session had expired, so its projection is verified by installation tests only.

Earlier: OpenCode 1.18.15 was executed locally and discovered `marketing-os` from both `.opencode/skills` and `.agents/skills`. Codex CLI 0.147.0 was present; its skill metadata was validated with the official validator and the portable discovery test. Claude Code, Pi, and Amp executables were not present in the audit environment, so no native-execution claim is made for those binaries.

Official discovery references used for the primary targets:

- Codex Agent Skills: https://learn.chatgpt.com/docs/build-skills
- Claude Code skills and plugins: https://code.claude.com/docs/en/skills and https://code.claude.com/docs/en/plugins
- OpenCode skills: https://opencode.ai/docs/skills/
- Pi skills: https://pi.dev/docs/latest/skills

Compatibility changes over time. Treat the table as a versioned implementation matrix, verify current first-party documentation during releases, and run a native smoke test before claiming a new host/version as fully verified.
