# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 28; no PARK.
Current verified release: **0.2.5-draft**, `6a04e8c`.

**Current phase-2 score: 1/2.** Exact dual canonical passes: **49/57**.
The expiry mapping is verified; expanded P11 now exposes the existing deadline
failure in both runtimes. Seven source coverage gaps remain. Full 57/57 dual
coverage plus one full round without a new open item is required for early PARK.
The original 2/2 at `b1ae299` is historical and used the narrower supported rubric.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `6a04e8c`, 14 schemas, 52 clauses | R7-054 verified |
| Package validator | 94 JSON files, 14 domains, 34 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Every vector executable |
| Dual exact passes | Source `427fed5`, package `942bdee`, release 0.2.5 | **49/57; P11 fails both, 7 source-unsupported** |
| Source evaluator | Independent full first release run | 49 pass / 1 fail / 7 unsupported semantic |
| Package evaluator | Independent full first release run | 56 pass / 1 fail / 0 unsupported semantic |
| Pinned supplemental corpus | 61 semantic vectors; 0.2.4 plus adjudicated expiry mapping | Source 48/5/8; package 56/5/0 |
| Authority-order corrections | Original negatives, B01, receipt-only ancestry controls | R7-047/048/049/051 fixed |
| Retention deadline | Expanded P11, seven independent vectors, full-state probes | R7-052/053 implementation open |
| Prior runtime/harness baseline | Verified on 0.2.4; does not prove expiry | 106 source, 28 package pass |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 42 fixed | 2 implementation findings open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

Only P11 changes beyond release identifiers. Its first 16 operations/results,
all other 64 vectors and the reusable pilot remain unchanged. Eight isolated
package negative probes preserve five forbidden writes, two expired successful
replays and one wrong conflict priority. A separate 20-operation positive trace
matches all prescribed remaining outputs and final state; expired operations
are excluded from that control and never counted as passing.

The 62 supplemental artifacts were independently validated under their explicit
0.2.4 profile. Migration to 0.2.5 remains author-owned. Native and typed first
inputs stay immutable. Runtime fixes must cover every admission API, including
revise/declassify, current replay, transitive known inputs and full refusal state.

Remaining unsupported source vectors: B07, P08, S20, S24, S25, S26 and S27.
Unsupported never counts as pass; synthetic erasure, restore, release or delivery
does not qualify a real deployment. Phase 2 follows convener event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; the 13:00Z hard cap remains.
Continue until the convener posts PARK.
