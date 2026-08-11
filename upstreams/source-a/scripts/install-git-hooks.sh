#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
chmod +x .githooks/pre-commit
git config core.hooksPath .githooks
printf 'Configured core.hooksPath=.githooks for %s\n' "$ROOT"
