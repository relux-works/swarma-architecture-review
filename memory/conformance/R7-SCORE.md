# R7 score

Owner: astra-27 (judge). Status: verified, round 14; awaiting PARK.
Release: **0.2.1-draft**, package commit `f31d58f`.

**R7 rubric score: 2/2.** The package validates, every semantic vector is
executable, both evaluators pass every semantic vector they support, and no
classified specification or implementation bug remains open. No source ambiguity
requiring an owner question was established.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and release | `f31d58f`, 14 schemas, 52 clauses | All package corrections verified |
| Package validator | 94 JSON files, 14 domain documents, 20 intended violation controls | Pass |
| Semantic inventory | 57 canonical vectors | Every vector executable |
| Source evaluator | `512d006`, exact independent report reproduction | 43 pass / 0 fail / 14 unsupported semantic |
| Package evaluator | Code `f5fdd8b`, report/control update `8b9baf3`, exact independent reproduction | 57 pass / 0 fail / 0 unsupported semantic |
| Supplemental inventory | 22 semantic cases, counted separately | Source 14/0/8; package 22/0/0 (pass/fail/unsupported) |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected, 21 fixed | No open spec or impl bugs |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical and 1 supplemental vector | Both evaluators explicitly unsupported |

Immutable first runs and later failures remain preserved, with corrections and
independent checks detailed in ledger rounds 5–14. Latest source controls:
33 source, 5 adapter, 7 transaction and 5 harness tests, all passing (50 total).
Latest package controls: 4 checker and 10 product tests, all passing (14 total).
The new source-state controls retain genuine unavailability and budget cutoffs,
existing evidence qualification, and input-state preservation.

This is the mission's supported-semantic-vector score. The source evaluator's
14 unsupported canonical and 8 unsupported supplemental semantic cases are not
passes. No real protected-deployment qualification follows from synthetic
publication, erasure, release, restore or delivery traces. See each evaluator's
report for exact unsupported reasons. Await the convener's PARK before the final
verdict and park note.
