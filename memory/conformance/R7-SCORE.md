# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 20; no PARK.
Current verified release: **0.2.2-draft**, `7e71765`.
Retention-scope/future-input release 0.2.3 is pending.

**Current phase-2 score: 1/2.** Verified dual canonical coverage is **49/57**.
Full 57/57 coverage plus one full round without a new open item is required for
early PARK. Two specification bugs and seven implementation bugs remain open.
The original supported-vector score 2/2 at `b1ae299` is historical and narrower.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `7e71765`, 14 schemas, 52 clauses | R7-039 retention scope and R7-042 checker gaps open |
| Package validator | 94 JSON files, 14 domains, 23 intended violation controls; exact regeneration | Canonical pass; supplemental future-input false positive remains |
| Canonical semantic inventory | 57 vectors | Every vector executable |
| Dual coverage | Source `68152c5`, package runtime `53266dd`, package 0.2.2 | **49/57; 8 source-unsupported** |
| Source evaluator | Exact independent canonical report | 49 pass / 0 fail / 8 unsupported semantic |
| Package evaluator | Exact independent canonical report | 57 pass / 0 fail / 0 unsupported semantic |
| Supplemental execution | 43 semantic cases | Source 33/1/9; package 39/4/0 (pass/fail/unsupported) |
| Additional judge probes | Rule/check invalidation and remaining authority head | Source failures remain; package controls pass |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 27 fixed | R7-039/042 spec; R7-036/037/040/043/044/045/046 impl open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

P06 and P12 now pass both implementations. Package CAS R7-041 closes, while
source R7-040 remains open: it rejects a valid remaining-head withdrawal after
passing the original four fixtures. Source established controls total 77 with
unchanged groups reused; package controls total 19. These passing suites do not
cover all newly exposed failures. First reports, input hashes, case migrations,
setup failures and correction evidence remain explicitly preserved in the ledger.

Remaining canonical source gaps: B07, P05, P08, S20, S24, S25, S26 and S27.
Canonical agreement does not close the separate adversarial bugs. Unsupported
inputs never count as passes. Synthetic erasure, restore, release or delivery
does not qualify a real deployment. Phase 2 follows convener event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; 13:00Z hard cap remains.
Continue until the convener posts PARK.
