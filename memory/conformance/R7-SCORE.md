# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 15; no PARK.
Release: **0.2.1-draft**, package commit `f31d58f`.

**Current phase-2 score: 1/2.** Full dual-implementation coverage is incomplete:
43 of 57 canonical semantic vectors pass both evaluators. The convener's phase-2
gate requires 57/57 and one full round without a new open item before early PARK.

The original mission's supported-vector rubric was verified at **2/2** in
`b1ae299`. That historical result remains valid on its stated narrower basis;
it is not the full dual-coverage claim now required. No classified bug is open.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and release | `f31d58f`, 14 schemas, 52 clauses | All package corrections verified |
| Package validator | 94 JSON files, 14 domain documents, 20 intended violation controls | Pass |
| Semantic inventory | 57 canonical vectors | Every vector executable |
| Dual-implementation coverage | Source `512d006` and package runtime `f5fdd8b` | **43/57; 14 still source-unsupported** |
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

The fourteen canonical gaps are B01, B07, P05, P06, P08, P12, S07, S17, S20,
S23, S24, S25, S26 and S27. The source evaluator's 14 unsupported canonical and
8 unsupported supplemental semantic cases are not passes. No real protected-deployment qualification follows from synthetic
publication, erasure, release, restore or delivery traces. See each evaluator's
report for exact unsupported reasons. Phase 2 was announced in rounds event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; the 13:00Z hard cap remains.
The judge continues intake and verification until the convener posts PARK.
