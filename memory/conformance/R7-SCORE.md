# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 19; no PARK.
Current release: **0.2.2-draft**, `7e71765`. Structure, regeneration and R7-031
receipt behavior independently verified. Retention-scope release 0.2.3 is pending.

**Current phase-2 score: 1/2.** Verified dual canonical coverage is **47/57**.
Full 57/57 coverage plus one full round without a new open item is required for
early PARK. Two specification bugs and five implementation bugs remain open.
The original supported-vector score 2/2 at `b1ae299` is historical and narrower.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package and release | `7e71765`, 14 schemas, 52 clauses | R7-031 closed; retention scope and future-fact checker gaps open |
| Package validator | 94 JSON files, 14 domain documents, 23 intended violation controls; exact regeneration | Canonical package pass; supplemental R7-042 false positive remains |
| Semantic inventory | 57 canonical vectors | Every vector executable |
| Dual implementation coverage | Source `e38c37c`, package runtime `a016781`, package 0.2.2 | **47/57; 10 source-unsupported** |
| Source evaluator | Exact independent canonical reproduction | 47 pass / 0 fail / 10 unsupported semantic |
| Package evaluator | Exact independent canonical reproduction | 57 pass / 0 fail / 0 unsupported semantic |
| Supplemental execution | 38 semantic fixtures, all closed shape; one known checker false positive | Source 24/3/11; package 35/3/0 (pass/fail/unsupported) |
| Additional judge invalidation probes | Three independently specified S17 neighbors | Source 1/2/0; package 3/0/0 |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 26 fixed | R7-039/042 spec; R7-036/037/040/041/043 impl open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

B01 and S17 now pass both implementations. Source controls: 33 source, 8 adapter,
11 transaction, 4 proof, 6 impact and 5 harness (67 passing). Package controls:
4 checker and 14 product (18 passing). These suites do not cover the newly found
rule/certificate invalidation failure R7-043. All first failures, exact regression
inputs, case migrations and closure evidence remain linked from the ledger.

Remaining canonical source gaps: B07, P05, P06, P08, P12, S20, S24, S25, S26 and
S27. Canonical agreement does not close the adversarial retention/CAS bugs or the
additional judge invalidation failure. Unsupported inputs never count as passes.
Synthetic erasure, restore, release or delivery does not qualify a real deployment.
Phase 2 follows convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`;
13:00Z hard cap remains. Continue until the convener posts PARK.
