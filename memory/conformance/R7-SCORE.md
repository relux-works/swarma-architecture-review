# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 27; no PARK.
Current verified release: **0.2.4-draft**, `ef02647`.

**Current phase-2 score: 1/2.** Exact dual canonical passes: **50/57**.
Both authority-order corrections are independently verified. Retention-deadline
findings and seven source coverage gaps remain. Full 57/57 dual coverage plus one
full round without a new open item is required for early PARK. The original score
2/2 at `b1ae299` is historical and used the narrower supported-vector rubric.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `ef02647`, 14 schemas, 52 clauses | R7-054 exact expiry mapping open |
| Package validator | 94 JSON files, 14 domains, 33 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Every vector executable |
| Dual exact passes | Source `427fed5`, package `942bdee`, release 0.2.4 | **50/57; 7 source-unsupported** |
| Source evaluator | Exact independent full canonical report | 50 pass / 0 fail / 7 unsupported semantic |
| Package evaluator | Exact independent full canonical report | 57 pass / 0 fail / 0 unsupported semantic |
| Current supplemental corpus | 61 semantic vectors; 0.2.4 plus adjudicated expiry mapping | Source 48/5/8; package 56/5/0 |
| Strict succession | Three exact negatives, expanded B01 and native full-state controls | R7-047/048 fixed |
| Receipt-only ancestry | Exact read-only pair, transitive write and expanded B01 | R7-051 fixed |
| Retention deadline | Seven exact vectors plus isolated full-state probes | R7-052/053 implementation and R7-054 mapping open |
| Runtime/harness controls | Independent complete reruns | 106 source, 28 package pass |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 41 fixed | 2 implementation and 1 specification finding open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

All 62 current supplemental artifacts validate. The previous 54 semantic inputs
and exact outputs remain unchanged; the seven new expiry vectors add five failures
and two passes in each runtime. Isolated operation controls give three positive
passes and seven intended negative failures each. Original typed/native first
inputs are unchanged. Canonical runtime/release bytes and prior 106/28 controls
remain the round-26 baseline; they do not prove expiry handling.

Both evaluators' expired-retention first probes remain unresolved: new storage
and replay require current retention over outputs and known input closure.
The adjudicated not_authorized,false refusal precedes idempotency, preserves
complete state and the original receipt, and does not initiate erasure. The exact supplemental witnesses are now verified; the package clarification
and implementation corrections remain pending.

Remaining unsupported source vectors: B07, P08, S20, S24, S25, S26 and S27.
Unsupported never counts as pass; synthetic erasure, restore, release or delivery
does not qualify a real deployment. Phase 2 follows convener event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; the 13:00Z hard cap remains.
Continue until the convener posts PARK.
