# rp417 — CH32H417 dev/test board supervised by an RP2350

Hardware project: a board where an RP2350 powers, resets, programs, stimulates and measures a
CH32H417 for automated limit testing (USB3, parallel ADC capture, internal ADCs, SD).

## Where things are

- `SPEC.md` — the living specification. Update it whenever a design decision is made or changed.
- `DECISIONS.md` — append-only log of **every** design decision (ID, date, decision, why,
  alternatives, who decided, SPEC section). Changes = new entry that supersedes the old one.
- `datasheets/` — PDFs and their markdown translations (`markitdown file.pdf > file.md`).
  Grep the `.md` files; quote the source file when citing a fact in SPEC.md.
- `userinputs/` — raw notes from the user. Treat claims there as **unverified** until checked
  against datasheets; record the verdict in SPEC.md.
- `projects/` — cloned CH32H417 reference repos (hardware/sdk/firmware/tools). List + rationale in
  `projects/README.md`; clones are gitignored, recreate with `projects/clone.sh`. Grep them for
  pinouts, USB3/UHSIF/DVP examples before designing a block.
- `.claude/TODO.md` — open actions and open questions.
- `.claude/DONE.md` — completed actions (move items from TODO, with date).
- `.claude/commits.md` — one entry per commit: date, short hash, what and why.

## Rules

- **Log every design decision in `DECISIONS.md`** the moment it is made (user's or Claude's call),
  and reflect it in SPEC.md in the same commit.

- Every commit gets an entry in `.claude/commits.md` (add it in the same commit; hash can be
  filled in by the following commit or left as "this commit").
- Never state a chip capability in SPEC.md without a datasheet reference or a "to verify" flag.
- Key gotchas (see SPEC.md §3): QFN128 package required for ISP; lot digit 5 must be ≠ 0;
  SWD pins PB8/PB9 are the USBHS pins; ISP entry is by power-cycle (no BOOT0 pin).
- **Session start hook** (`.claude/settings.json` → `.claude/hooks/pending-decisions.py`) lists every
  unchecked item under `## Open questions (user)` in `.claude/TODO.md` and every proposal row
  (`<tr><td>Pn-m</td>…`) in `docs/design/*.html` not yet tagged `<span class="tag d">Dxx</span>`.
  When it reports pending points, ask the user about them first. Keep those two formats so the hook
  keeps finding them: tick/remove answered questions, tag approved proposals with their Dxx.
