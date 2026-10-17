# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 17; no PARK.
Latest fully verified release: **0.2.1-draft**, `f31d58f`.
Incoming **0.2.2-draft**, `7e71765`, awaits release review and evaluator checks.

**Current phase-2 score: 1/2.** Verified dual canonical coverage is 44/57.
Full 57/57 coverage plus one full round without a new open item is required for
early PARK. One specification bug and three implementation bugs remain open.
The original supported-vector score 2/2 at `b1ae299` is historical and narrower.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package and release | `f31d58f`, 14 schemas, 52 clauses | Prior corrections verified; R7-031 release review pending |
| Package validator | 94 JSON files, 14 domain documents, 20 intended violation controls | 0.2.1 pass |
| Semantic inventory | 57 canonical vectors | Every vector executable |
| Dual-implementation coverage | Source `1f3180d`, package `f10c7ba`, package 0.2.1 | **44/57; 13 source-unsupported** |
| Source evaluator | Exact independent canonical reproduction | 44 pass / 0 fail / 13 unsupported semantic |
| Package evaluator | Exact independent canonical reproduction | 57 pass / 0 fail / 0 unsupported semantic |
| Supplemental inventory | 32 semantic cases, counted separately | Source 17/2/13; package 30/2/0 (pass/fail/unsupported) |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 24 fixed | R7-031 spec; R7-032/036/037 impl open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical and 1 supplemental vector | Both evaluators unsupported |

S07 now passes both implementations, as do the exact Cartesian-proof and
clean-alternative supplemental regressions. Source controls: 33 source, 5 adapter,
11 transaction, 4 proof and 5 harness (58 passing, unchanged controls reused).
Package controls: 4 checker and 12 product (16 passing). Immutable first failures
and all corrections remain linked from the ledger.

The remaining canonical source gaps at this pinned baseline are B01, B07, P05,
P06, P08, P12, S17, S20, S23, S24, S25, S26 and S27. Source import candidate
`1f35727` and package `7e71765` are queued for review; producer claims are not
silently counted as independent verification. Unsupported inputs never count as
passes. Synthetic erasure, restore, release or delivery does not qualify a real
protected deployment. Phase 2 follows convener event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; 13:00Z hard cap remains.
