# Marketing Agent OS installation

The package is self-contained. Instruction-only use has no runtime dependency. Optional helper scripts use Python 3's standard library except PDF rendering (`reportlab`).

## Operating systems

- Linux and macOS: `./install.sh --agent universal --scope project --project /path/to/project`
- Windows PowerShell: `.\install.ps1 -Agent universal -Scope project -Project C:\path\to\project`
- Python 3 fallback on any OS: `python3 scripts/install.py ...` (Windows may use `py -3 scripts/install.py ...`)

## Codex

Project: `python3 scripts/install.py --agent codex --scope project --project /path/to/repo`

User: `python3 scripts/install.py --agent codex --scope user`

The installer targets `.agents/skills/` for project installs and `~/.agents/skills/` for user installs.

## Claude Code

Project: `python3 scripts/install.py --agent claude-code --scope project --project /path/to/repo`

User: `python3 scripts/install.py --agent claude-code --scope user`

Or add this repository as a local Claude plugin marketplace and install `marketing-agent-os@marketing-agent-os`.

## OpenCode

Project: `python3 scripts/install.py --agent opencode --scope project --project /path/to/repo`

User: `python3 scripts/install.py --agent opencode --scope user`

OpenCode can also read universal `.agents/skills/`, so a Codex/universal install can be shared.

## Selective installs

Use repeated `--skill` flags, for example:

`python3 scripts/install.py --agent codex --skill marketing-os --skill seo --skill ai-seo --skill cro`

Because this package deliberately exposes hundreds of source-compatible skill names, a selective install can improve skill discovery/context budgets on hosts with large skill registries. The complete archive remains the source of truth.

## Additional hosts

The installer also has native targets for Pi, Cursor, Gemini CLI, GitHub Copilot, Amp, Cline, Roo, Windsurf, OpenClaw, and Hermes. Run `python3 scripts/install.py --help` for the accepted `--agent` values. The `universal` target is preferred whenever a host reads `.agents/skills`.

Directory support and native-discovery confidence differ by host. Consult `docs/COMPATIBILITY.md`; an installer target means Marketing Agent OS can project files into that host's documented or conventional directory, not that every host version has been executed in CI.

## Verification

Run `python3 scripts/build_manifest.py`, then `python3 scripts/doctor.py` before installation. Use `--dry-run` to preview targets.
