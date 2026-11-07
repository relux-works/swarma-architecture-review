# Finding: the base ignores the platform book's own memory design (ch. 09 «Память», ch. 10 «Сны»)

- **Lens:** rubric and proof (wonder-02); mechanical claim check C-25.
- **Status:** proposed
- **Confirmed-by:** wonder-01 (platform memory-chapters review); independently relied on by astra-01 ([memory data-channel finding](memory-data-channel.md)) and astra-04 (platform memory-chapters review).

## Problem

The base sketch's Part 2 grounds its Swarma embedding entirely in the Swarma book
(`wiki/book/swarma/ru`) and never mentions the platform (apiary) book's memory chapters,
`wiki/book/ru/09-pamyat.md` and `wiki/book/ru/10-sny.md`. Those chapters already contain a
memory design for this platform. A sketch claiming platform fit therefore proposes parallel
machinery without acknowledging the incumbent design, and re-derives weaker versions of
several of its mechanisms.

## Evidence

`ru/09-pamyat.md` proposes (status marks as in source):

- Four memory kinds (process/board, personal, persona, procedural/skills), `09:3-8`.
- A memory skill as the only write path: `memory add|search|expand|forget|review|approve`
  with `--json`; git-files store by default (SQLite/external service interchangeable);
  per-note provenance (who/when/from where); a daily write budget; **quarantine for facts
  from external sources until human review**, explicitly because otherwise a planted
  instruction can persist (`09:12-20`).
- A summary ladder (journal → session digests → day → week/month; fact cards), every
  summary line referencing what it retells; expand descends one level (`09:22-34`).
- An immutable per-session memory snapshot (`09:35`); "this is not instructions": memory
  overlay weight below every role module (`09:37`).
- "Notes grant nothing: authority lives only in confirmed process configuration and
  confirmed operator files" — marked ⟦решено⟧ (`09:41`).

`ru/10-sny.md` adds a night consolidation cycle: replay, rehearsal, ladder write-back,
insights to quarantined dream-memory; a **deterministic log distiller** (not a model) that
keeps journal references and strips secret-shaped material; insights become proposals via
normal approval, rejected insights remembered to prevent resurfacing (`10:24-31`); the
`dreams` right, windows and budgets (`10:35-43`).

Against this, the base Part 1 (§6) specifies four automatic capture adapters
(conversation/tool/runtime/external) feeding `observe`, with no quarantine, no write
budget, no ladder, and its own append-only log as recommended source of truth (§12);
Part 2 corrects scale and boundaries but still never references ch. 09/10. (Nuance, per
wonder-01's confirmation: most ch. 09 items are ⟦предложено⟧, so superseding them is
legitimate — silently ignoring them is not.)

## Proposed change

The winning RFC must include an absorb/supersede table for ch. 09/10, item by item
(skill write-path, store default, provenance, budget, quarantine, ladder, snapshot,
distiller, dreams cycle, rejection memory). Default: absorb. Any superseded item needs a
reason stronger than "the sketch does it differently".

## Rubric rows affected

R2 (base capped at 1: parallel memory machinery beside an existing design), R4 (no
quarantine/admission discipline for external or extracted material), R8 (the ch. 09 slice —
skill + git + ladder — is smaller than the base's P0 and useful sooner).
