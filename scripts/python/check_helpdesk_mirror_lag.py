#!/usr/bin/env python3
"""
Detect .md/.json status mismatches across the helpdesk directory.

A ticket is "mirror-lagged" when its companion .md narrative still says
OPEN/INVESTIGATING/BLOCKED while the authoritative .json says RESOLVED
(or vice versa). The 2026-05-07 sweep found two such cases — this
script generalises that detection so future sweeps catch the whole class.

Usage:
    python check_helpdesk_mirror_lag.py [HELPDESK_DIR]

If HELPDESK_DIR is omitted, defaults to .lumina/docs/helpdesk/ relative
to the operator tree root. Exit code is the number of mismatches found
(0 = clean).

Author: 2026-05-07 mirror-sync sweep
Tags: #HELPDESK #SYNC #DETECTOR
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# Status values that mean "still open" — anything else in .md is treated
# as effectively closed for comparison purposes.
OPEN_PATTERNS = re.compile(
    r"\b(OPEN|INVESTIGATING|BLOCKED|CONFIRMED BUG|PENDING|IN[_\s-]PROGRESS|BACKLOG|TODO|WIP|FOLLOW[_\s-]UP|PENDING[_\s-]SENTIENT)\b",
    re.IGNORECASE,
)
CLOSED_PATTERNS = re.compile(
    r"\b(RESOLVED|CLOSED|COMPLETE(D)?|CANCELLED|WORKAROUND IN PLACE|FIXED|DONE)\b",
    re.IGNORECASE,
)


def md_status_token(md_path: Path) -> str:
    """
    Extract the bolded status keyword from the first 'Status' line.

    Markdown ticket headers look like:
        **Status**: ✅ **RESOLVED** (closed 2026-01-16)

    We want just `RESOLVED` — not the whole line — because the trailing
    parenthetical can include words like 'closed' that would otherwise
    fool the open/closed classifier.
    """
    try:
        text = md_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "?"
    for line in text.splitlines():
        if re.match(r"^\s*\*\*Status\*\*\s*:?", line, re.IGNORECASE):
            # Drop the leading "**Status**:" portion before scanning the
            # rest of the line for the bolded status keyword.
            after_label = re.sub(
                r"^\s*\*\*Status\*\*\s*:?\s*", "", line, count=1, flags=re.IGNORECASE
            )
            keyword_match = re.search(r"\*\*([A-Za-z][A-Za-z _\-]+)\*\*", after_label)
            if keyword_match:
                return keyword_match.group(1).strip()
            # No bolded keyword — fall back to the whole line.
            return line.strip()
    return "?"


def classify(token: str) -> str:
    """Bucket a status token into 'open', 'closed', or 'unknown'."""
    if CLOSED_PATTERNS.search(token):
        return "closed"
    if OPEN_PATTERNS.search(token):
        return "open"
    return "unknown"


def find_pairs(helpdesk_dir: Path) -> list[tuple[Path, Path | None]]:
    """Return (md, json_or_None) pairs for every .md ticket in the dir."""
    pairs: list[tuple[Path, Path | None]] = []
    for md in sorted(helpdesk_dir.glob("*.md")):
        if md.name.startswith("00-") or md.name.upper() in {
            "README.MD",
            "INDEX.MD",
        }:
            continue
        json_path = md.with_suffix(".json")
        pairs.append((md, json_path if json_path.is_file() else None))
    return pairs


def main(argv: list[str]) -> int:
    if len(argv) > 1:
        helpdesk_dir = Path(argv[1])
    else:
        # Walk up to find an operator-tree root that has .lumina/docs/helpdesk
        cwd = Path.cwd()
        for candidate in [cwd, *cwd.parents]:
            probe = candidate / ".lumina" / "docs" / "helpdesk"
            if probe.is_dir():
                helpdesk_dir = probe
                break
            probe2 = candidate / "docs" / "helpdesk"
            if probe2.is_dir():
                helpdesk_dir = probe2
                break
        else:
            print("ERROR: could not auto-locate helpdesk dir; pass it explicitly")
            return 2

    if not helpdesk_dir.is_dir():
        print(f"ERROR: {helpdesk_dir} is not a directory")
        return 2

    print(f"Scanning {helpdesk_dir} for .md/.json status mismatches...\n")

    pairs = find_pairs(helpdesk_dir)
    mismatches: list[tuple[Path, str, str]] = []
    md_only: list[Path] = []

    for md, json_path in pairs:
        if json_path is None:
            md_only.append(md)
            continue
        try:
            data = json.loads(json_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"WARN: cannot parse {json_path.name}: {e}")
            continue
        json_status = str(data.get("status", "?"))
        md_status = md_status_token(md)
        json_class = classify(json_status)
        md_class = classify(md_status)

        if json_class == "closed" and md_class == "open":
            mismatches.append((md, json_status, md_status))
        elif json_class == "open" and md_class == "closed":
            mismatches.append((md, json_status, md_status))

    if mismatches:
        print(f"FOUND {len(mismatches)} MIRROR-LAG MISMATCH(ES):")
        for md, jstatus, mstatus in mismatches:
            print(f"  - {md.name}")
            print(f"      json: {jstatus}")
            print(f"      md:   {mstatus}")
        print()
        print("Action: update the .md to match the authoritative .json,")
        print("then append an entry to docs/helpdesk/00-MIRROR-SYNC-LOG.md")
    else:
        print("No mismatches — public-mirror narrative aligned with JSON ground truth.")

    if md_only:
        print(f"\n{len(md_only)} .md ticket(s) without companion .json (informational only):")
        for md in md_only[:10]:
            print(f"  - {md.name}")
        if len(md_only) > 10:
            print(f"  ... and {len(md_only) - 10} more")

    return len(mismatches)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
