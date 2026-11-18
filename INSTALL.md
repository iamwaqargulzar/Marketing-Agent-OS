# Marketing Agent OS installation

The package is self-contained. Instructions need no runtime. Each skill carries the helpers it uses: many need only Python 3, and some list optional packages such as `requests` or `playwright` in the skill's helper notes. Skills ask before installing anything.

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

With 243 skills, a selective install improves discovery on hosts with limited context budgets. Skills mention related skills by name; if one is not installed, the agent says so instead of failing.

The Python installer includes the shared `marketing-os` library with specialist selections. When selecting specialists through a third-party skill manager, select `marketing-os` too. Each source runtime can be extracted offline, including its original dependency manifests, helpers, tests, and agent definitions. See the [source library guide](skills/marketing-os/references/source-library.md). Use `--force` to upgrade an existing package-owned skill after reviewing local changes.

## Additional hosts

The installer also has native targets for Pi, Cursor, Gemini CLI, GitHub Copilot, Amp, Cline, Roo, Windsurf, OpenClaw, and Hermes. Run `python3 scripts/install.py --help` for the accepted `--agent` values. The `universal` target is preferred whenever a host reads `.agents/skills`.

Directory support and native-discovery confidence differ by host. Consult `docs/COMPATIBILITY.md`; an installer target means Marketing Agent OS can project files into that host's documented or conventional directory, not that every host version has been executed in CI.

## Verification

Run `python3 scripts/doctor.py` against the supplied release manifest before installation. Use `--dry-run` to preview targets.
