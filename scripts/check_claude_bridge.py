"""Verify that CLAUDE.md is only the bridge to AGENTS.md.

Claude Code reads CLAUDE.md and resolves the `@AGENTS.md` import; Codex and other
agents read AGENTS.md directly and do not resolve imports. The content therefore
has to live in AGENTS.md, and CLAUDE.md may hold nothing but that import and an
HTML comment explaining the arrangement. Without this check, the habit of editing
CLAUDE.md forks the two files silently.
"""

from __future__ import annotations

import sys
from pathlib import Path

BRIDGE = Path("CLAUDE.md")
IMPORT_LINE = "@AGENTS.md"


def offending_lines(text: str) -> list[tuple[int, str]]:
    """Return the lines that are neither the import, an HTML comment, nor blank."""
    offenders: list[tuple[int, str]] = []
    in_comment = False

    for number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()

        if in_comment:
            in_comment = "-->" not in line
            continue

        if not line or line == IMPORT_LINE:
            continue

        if line.startswith("<!--"):
            # A single-line comment opens and closes on the same line.
            in_comment = "-->" not in line
            continue

        offenders.append((number, raw))

    return offenders


def main() -> int:
    if not BRIDGE.exists():
        return 0

    offenders = offending_lines(BRIDGE.read_text(encoding="utf-8"))
    if not offenders:
        return 0

    print(f"{BRIDGE} must hold only the `{IMPORT_LINE}` import and an HTML comment.")
    print("Move this content to AGENTS.md, which every agent reads directly:")
    for number, raw in offenders:
        print(f"  {BRIDGE}:{number}: {raw}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
