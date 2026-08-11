#!/usr/bin/env bash
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if command -v python3 >/dev/null 2>&1; then
  exec python3 "$repo_dir/scripts/install.py" "$@"
fi

if command -v python >/dev/null 2>&1 && python -c 'import sys; raise SystemExit(sys.version_info < (3, 9))' 2>/dev/null; then
  exec python "$repo_dir/scripts/install.py" "$@"
fi

printf '%s\n' 'Marketing Agent OS requires Python 3.9+ for the local installer.' >&2
printf '%s\n' 'Alternative: install Node.js and run `npx skills add . --all` from this directory.' >&2
exit 1
