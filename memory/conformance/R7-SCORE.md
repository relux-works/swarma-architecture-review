# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 24; no PARK.
Current verified release: **0.2.3-draft**, `23290b3`.

**Current phase-2 score: 1/2.** Exact dual canonical passes: **50/57**.
Source declassification and digest framing are verified. Authority-succession
writes still fail both implementations; source projection also loses ordering
through receipt-only intermediate events. Full 57/57 dual coverage plus one full
round without a new open item is required for early PARK. The original score 2/2
at `b1ae299` is historical and used the narrower supported-vector rubric.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `23290b3`, 14 schemas, 52 clauses | R7-049 successor-refusal mapping remains open |
| Package validator | 94 JSON files, 14 domains, 32 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Every vector executable |
| Dual exact passes | Source `8a42945`, package `4af0360`, package 0.2.3 | **50/57; 7 source-unsupported** |
| Source evaluator | Exact independent full canonical report | 50 pass / 0 fail / 7 unsupported semantic |
| Package evaluator | Independently verified full canonical report | 57 pass / 0 fail / 0 unsupported semantic |
| Expanded supplemental corpus | 52 semantic vectors, 0.2.3 plus adjudicated succession mapping | Source 40/4/8; package 49/3/0 |
| Receipt-only ancestry | Validated fresh read-only snapshots | Source transitive case fails; direct control and package pair pass |
| Digest correction | Original framed/raw ASCII/non-ASCII probes | All four now pass both runtimes |
| Runtime/harness controls | Source `8a42945`; package `4af0360` | All 98 source controls rerun; 26 package controls previously verified |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 37 fixed | R7-047/048/051 impl and R7-049 spec open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

R7-050 closes on exact P05/ASTRA25-02, raw-digest negative, full-state refusal and
owner/pin/revocation controls. First failures remain immutable. R7-051 isolates
source projection independently of replacement admission: a valid receipt chain
must retain its transitive order when an intermediate event has no assertion.
All 53 supplemental artifacts validate. The three forbidden succession writes
remain R7-047/048; their exact code has been adjudicated, while its package release
is still R7-049. These distinctions prevent canonical green results from hiding
remaining adversarial failures.

Remaining unsupported source vectors: B07, P08, S20, S24, S25, S26 and S27.
Exact pins, input hashes, first failures and excluded setup errors remain in the
ledger. Unsupported inputs never count as passes. Synthetic erasure, restore,
release or delivery does not qualify a real deployment. Phase 2 follows convener
event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; the 13:00Z hard cap
remains. Continue until the convener posts PARK.
