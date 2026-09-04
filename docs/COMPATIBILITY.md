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

For hosts not represented by the built-in Python installer, use the Agent Skills CLI after this repository is published:

```bash
npx skills add <owner>/marketing-agent-os
```

On 2026-09-04, `skills` CLI 1.5.22 discovered all 236 skills and installed the `marketing-os` smoke-test skill across all 76 agent definitions in its registry, resolving to 55 unique project directories. This included shared/universal locations plus host-native projections for AiderDesk, Amp, Claude Code, Codex-compatible hosts, Continue, Cursor-compatible hosts, Devin, Goose, Kilo Code, Kiro, OpenHands, Pi, Qwen, Roo, Trae, Windsurf, and others. This verifies package discovery and file projection, not the runtime behavior of every external application.

OpenCode 1.18.15 was executed locally and discovered `marketing-os` from both `.opencode/skills` and `.agents/skills`. Codex CLI 0.147.0 was present; its skill metadata was validated with the official validator and the portable discovery test. Claude Code, Pi, and Amp executables were not present in the audit environment, so no native-execution claim is made for those binaries.

Official discovery references used for the primary targets:

- Codex Agent Skills: https://learn.chatgpt.com/docs/build-skills
- Claude Code skills and plugins: https://code.claude.com/docs/en/skills and https://code.claude.com/docs/en/plugins
- OpenCode skills: https://opencode.ai/docs/skills/
- Pi skills: https://pi.dev/docs/latest/skills

Compatibility changes over time. Treat the table as a versioned implementation matrix, verify current first-party documentation during releases, and run a native smoke test before claiming a new host/version as fully verified.
