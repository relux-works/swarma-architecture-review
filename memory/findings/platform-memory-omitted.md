# Finding: base never engages the platform's own memory design (platform book ch. 09/10)

- Lens: rubric and proof (wonder-04). Status: `proposed`.
- Duplicate candidate: wonder-02's C-25 / `f-platform-memory-chapters` (same defect, independently
  filed). Convener may keep either file; both seats confirm both.

## Problem

SKETCH Part 2 embeds agent memory into Swarma using only the Swarma book. The platform (apiary)
book already contains the platform's own memory thinking, which the base neither builds on nor
explicitly supersedes:

- `book/ru/09-pamyat.md`: four memory kinds; a memory skill with
  `memory add|search|expand|forget|review|approve` as the only write path; git files by default
  (SQLite/external behind the same commands); per-note provenance; a daily write budget; quarantine
  for facts from external sources until human review ("otherwise a planted instruction can
  persist"); an L0–L3 summary ladder where every summary line references what it retells; an
  immutable session-start snapshot; "this is not instructions" (memory overlay weight below any
  role module); "notes grant nothing" marked decided.
- `book/ru/10-sny.md`: "dreams" are a rehearsal sandbox (`--dream` tools, nothing reaches the real
  world), with a deterministic (non-model) log distiller and dream-memory held in quarantine until
  human review. This is not Letta-style consolidation, and reusing the word for consolidation
  collides with it.

Status of ch. 09/10 is mostly "proposed", so this is not a claim that working code exists. It is a
claim that a design asserting platform fit cannot silently ignore the platform's prior design for
the same component, including its write-path discipline and its quarantine rule, which is strictly
stronger than anything in the base for externally sourced facts.

## Evidence

- Platform book files above (read in full by wonder-04; line refs in `verdicts/wonder-04.md` §2 F-a).
- Base text: SKETCH Part 1 §6 (`MemoryAPI`, automatic capture adapters) and Part 2 passim (no
  reference to ch. 09/10, the memory skill, the ladder or quarantine).
- Independent corroboration: wonder-02 claim-check C-25 reaches the same verdict ("OMISSION,
  material") from the same files.

## Proposed change

1. Map the kernel API onto the ch. 09 verbs instead of replacing them:
   `add → propose/observe`, `search → recall`, `expand → explain`, `forget → erase`,
   `review/approve → review-queue operations by authorised identities`.
2. Adopt ch. 09 semantics where they are stronger: quarantine for external-source material,
   session-start snapshot immutability, summary-ladder lines as claims whose evidence is the level
   below.
3. Reserve the word "dreams" for the ch. 10 rehearsal meaning in all memory documents; name any
   consolidation pass differently and keep its output quarantined until review.

## Rubric rows affected

R2 (reuse — base capped at 1 until mapped), R8 (the ch. 09 shape is the cheapest first slice).

## Confirmed by

- wonder-02 (five 1), platform memory-omitted review
  (independently filed as C-25).
