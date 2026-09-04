# Initial audit report

Audit date: 2026-08-11

## Input and source verification

The original combined ZIP was structurally readable but was not accepted as the release source. Work was rebuilt and checked against four independently cloned repositories pinned in `upstreams.lock.json`. The ZIP is excluded from version control and is not needed to build, validate, install, or update Marketing Agent OS.

The upstream snapshots contain 1,897 tracked entries and 218 `SKILL.md` files representing 216 unique declared skill names. All upstream names are covered by the normalized layer. Duplicate upstream names are resolved into one installable implementation rather than exposed as routing conflicts.

## Corrected issues

- Removed a complete duplicated plugin payload and made the repository root the plugin.
- Added seven upstream skills absent from the original combined inventory.
- Replaced 145 generic trigger descriptions with specific upstream-derived routing descriptions.
- Removed unsupported skill frontmatter and safely quoted all descriptions.
- Corrected stale source claims and pinned exact source commits.
- Replaced platform-specific Python assumptions with Linux/macOS and Windows wrappers.
- Hardened installation against path traversal, unknown names, partial replacement, and accidental overwrite.
- Hardened URL fetching against private-network access, unsafe redirects, credentials in URLs, and unbounded responses.
- Fixed JSON-LD escaping and strengthened deterministic report/input validation.
- Added integrity, reconciliation, cross-platform CI, installer, wrapper, and security tests.

## Verified state

- 236 normalized skills pass the local metadata validator.
- Portable package discovery reports all 236 skills through the Agent Skills CLI.
- Agent Skills CLI 1.5.22 projected a selected skill across all 76 registered agent definitions (55 unique directories).
- OpenCode 1.18.15 discovered the selected skill from both its native and universal project paths.
- Every pinned upstream snapshot matches its lock hash.
- Every declared upstream skill name is represented in the normalized layer.
- The package doctor passes before release once `SHA256SUMS.json` is regenerated.

Native execution has not been claimed for every listed harness. The installer paths are documented separately from host-version smoke-test status in `COMPATIBILITY.md`. Codex CLI 0.147.0 and OpenCode 1.18.15 were available during the audit; Claude Code, Pi, and Amp were not installed.
