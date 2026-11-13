#!/usr/bin/env python3
"""SessionStart hook: list unanswered decision points so Claude asks them first.

Sources:
  - .claude/TODO.md, section "## Open questions (user)": unchecked "- [ ]" items
  - docs/design/*.html, proposal tables: rows "<td>Pn-m</td>" not yet tagged as a decision (Dxx)
"""
import glob
import html
import json
import os
import re
import sys

root = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

questions = []
todo = os.path.join(root, ".claude", "TODO.md")
if os.path.exists(todo):
    in_section = False
    for line in open(todo, encoding="utf-8"):
        if line.startswith("## "):
            in_section = line.strip().lower().startswith("## open questions")
            continue
        if in_section and line.lstrip().startswith("- [ ]"):
            questions.append(line.strip()[6:].strip())

proposals = []
row_re = re.compile(r"<tr><td>(P\d+-\d+)(.*?)</td><td>(.*?)</td>", re.S)
for path in sorted(glob.glob(os.path.join(root, "docs", "design", "*.html"))):
    text = open(path, encoding="utf-8").read()
    for pid, tag, desc in row_re.findall(text):
        if 'tag d' in tag or 'tag w' in tag:  # approved (Dxx) or withdrawn
            continue
        desc = html.unescape(re.sub(r"<[^>]+>", "", desc)).strip()
        proposals.append(f"{pid}: {desc} ({os.path.relpath(path, root)})")

if not questions and not proposals:
    sys.exit(0)

lines = ["rp417 has unanswered decision points. Before other work, ask the user about them "
         "(one at a time or as a short list), then log each answer in DECISIONS.md + SPEC.md "
         "and update .claude/TODO.md / the proposal table."]
if questions:
    lines.append("Open questions (.claude/TODO.md):")
    lines += [f"  - {q}" for q in questions]
if proposals:
    lines.append("Pending proposals awaiting approval:")
    lines += [f"  - {p}" for p in proposals]

n = len(questions) + len(proposals)
print(json.dumps({
    "systemMessage": f"rp417: {n} unanswered decision point(s) — Claude will ask about them.",
    "hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": "\n".join(lines)},
}))
