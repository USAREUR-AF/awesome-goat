#!/usr/bin/env python3
"""Check README.md: required sections, entry format, no duplicate links.

usage: python3 tools/check.py [--links]
  --links  also request every link and fail on one that does not load
Standard library only.
"""
import re
import sys
import urllib.request
from pathlib import Path

SECTIONS = [
    "Open-source projects",
    "Commercial and proprietary products",
    "Feeds and integrations",
    "Deployments and case studies",
    "Research, talks and writing",
]
ENTRY = re.compile(r"^- \[([^\]]+)\]\((https://[^)\s]+)\) - (.+?) Uses goat for: (.+?)\. By: (.+?)\.$")
EMPTY = "*No entries yet. [Add yours](#add-your-work).*"


def main() -> int:
    text = (Path(__file__).resolve().parent.parent / "README.md").read_text(encoding="utf-8")
    problems, links, entries = [], [], 0
    parts = re.split(r"^## (.+)$", text, flags=re.M)
    body = {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}
    for name in SECTIONS:
        if name not in body:
            problems.append(f"section missing: {name}")
            continue
        lines = [ln for ln in body[name].splitlines() if ln.startswith("- ") or ln.strip() == EMPTY]
        items = [ln for ln in lines if ln.startswith("- ")]
        if items and EMPTY in body[name]:
            problems.append(f"{name}: has entries and still says 'No entries yet'")
        if not items and EMPTY not in body[name]:
            problems.append(f"{name}: no entries and no 'No entries yet' line")
        for ln in items:
            m = ENTRY.match(ln)
            if not m:
                problems.append(f"{name}: entry does not match the form in CONTRIBUTING.md: {ln[:80]}")
                continue
            entries += 1
            if "github.com/USAREUR-AF/" in m.group(2):
                problems.append(f"{name}: goat's own repositories are not listed here: {m.group(1)}")
            if m.group(2) in links:
                problems.append(f"{name}: duplicate link: {m.group(2)}")
            links.append(m.group(2))
    if "--links" in sys.argv:
        for url in sorted(set(re.findall(r"\((https://[^)\s]+)\)", text))):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "awesome-goat-link-check"})
                with urllib.request.urlopen(req, timeout=20) as r:
                    if r.status >= 400:
                        problems.append(f"link returned {r.status}: {url}")
            except Exception as e:  # noqa: BLE001
                problems.append(f"link did not load: {url} ({type(e).__name__})")
    for p in problems:
        print("FAIL", p)
    if problems:
        return 1
    print(f"ok: {len(SECTIONS)} sections, {entries} entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
