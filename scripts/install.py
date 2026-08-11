#!/usr/bin/env python3
"""Install Marketing Agent OS skills into supported agent skill directories."""

from __future__ import annotations

import argparse
import shutil
import sys
import uuid
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

# Paths are based on each host's documented Agent Skills discovery locations.
# Several hosts share .agents/skills, so aliases intentionally resolve there.
TARGETS = {
    "universal": (".agents/skills", "~/.agents/skills"),
    "codex": (".agents/skills", "~/.agents/skills"),
    "opencode": (".opencode/skills", "~/.config/opencode/skills"),
    "claude-code": (".claude/skills", "~/.claude/skills"),
    "pi": (".pi/skills", "~/.pi/agent/skills"),
    "cursor": (".cursor/skills", "~/.cursor/skills"),
    "gemini": (".gemini/skills", "~/.gemini/skills"),
    "copilot": (".github/skills", "~/.copilot/skills"),
    "amp": (".agents/skills", "~/.agents/skills"),
    "cline": (".cline/skills", "~/.cline/skills"),
    "roo": (".roo/skills", "~/.roo/skills"),
    "windsurf": (".windsurf/skills", "~/.codeium/windsurf/skills"),
    "openclaw": ("skills", "~/.openclaw/skills"),
    "hermes": (".agents/skills", "~/.hermes/skills"),
}

# A compact cross-host projection. OpenCode, Cursor, Gemini CLI, Copilot, Amp,
# and several other hosts already read the universal .agents location.
ALL_AGENTS = ("universal", "claude-code", "pi", "cline", "roo")


def available_skills() -> dict[str, Path]:
    return {
        path.parent.name: path.parent
        for path in SKILLS.glob("*/SKILL.md")
        if path.is_file()
    }


def destination(agent: str, scope: str, project: Path) -> Path:
    configured = TARGETS[agent][0 if scope == "project" else 1]
    if scope == "project":
        return (project / configured).absolute()
    return Path(configured).expanduser().absolute()


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def install_one(source: Path, target: Path, force: bool) -> str:
    if target.exists() or target.is_symlink():
        if not force:
            return "skipped (exists; use --force)"

    target.parent.mkdir(parents=True, exist_ok=True)
    staging = target.parent / f".{target.name}.tmp-{uuid.uuid4().hex}"
    backup = target.parent / f".{target.name}.backup-{uuid.uuid4().hex}"
    try:
        shutil.copytree(source, staging)
        if target.exists() or target.is_symlink():
            target.replace(backup)
        staging.replace(target)
        remove_path(backup)
    except Exception:
        remove_path(staging)
        if backup.exists() or backup.is_symlink():
            if target.exists() or target.is_symlink():
                remove_path(target)
            backup.replace(target)
        raise
    return "installed"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=[*TARGETS, "all"], default="universal")
    parser.add_argument("--scope", choices=["project", "user"], default="project")
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--skill", action="append", default=[])
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--list", action="store_true", help="list available skills and exit")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    inventory = available_skills()
    if args.list:
        print("\n".join(sorted(inventory)))
        return 0

    requested = args.skill or sorted(inventory)
    unknown = sorted(set(requested) - set(inventory))
    if unknown:
        print("Unknown skill(s): " + ", ".join(unknown), file=sys.stderr)
        return 2

    agents = ALL_AGENTS if args.agent == "all" else (args.agent,)
    destinations: list[tuple[str, Path]] = []
    seen: set[Path] = set()
    for agent in agents:
        target_root = destination(agent, args.scope, args.project)
        if target_root in seen:
            continue
        seen.add(target_root)
        destinations.append((agent, target_root))

    for agent, target_root in destinations:
        print(f"[{agent}] -> {target_root}")
        for name in requested:
            if args.dry_run:
                state = "would install"
                if (target_root / name).exists() and not args.force:
                    state = "would skip (exists; use --force)"
            else:
                state = install_one(inventory[name], target_root / name, args.force)
            print(f"  {name}: {state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
