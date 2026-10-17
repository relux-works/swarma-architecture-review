# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 30; no PARK.
Current verified release: **0.2.5-draft**, `6a04e8c`.

**Current phase-2 score: 1/2.** Exact dual canonical passes: **49/57**.
Source expiry handling is fixed; the package runtime still fails P11. Seven
source coverage gaps remain. Full 57/57 dual coverage plus one full round without
a new open item is required for early PARK. The original 2/2 at `b1ae299` is
historical and used the narrower supported rubric.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `6a04e8c`, 14 schemas, 52 clauses | All established specification findings fixed |
| Package validator | 94 JSON files, 14 domains, 34 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Every vector executable |
| Dual exact passes | Source `4a14a56`, package `942bdee`, release 0.2.5 | **49/57; package P11 fails, 7 source-unsupported** |
| Source evaluator | Exact independent full corrected release run | 50 pass / 0 fail / 7 unsupported semantic |
| Package evaluator | Independent full first release run | 56 pass / 1 fail / 0 unsupported semantic |
| Source supplemental corpus | 41 semantic cases at 0.2.5; 20 pending author migration | 33/0/8 current; 20/20 exact at original 0.2.4 |
| Package supplemental baseline | 61 semantic vectors at 0.2.4 plus adjudicated expiry mapping | 56/5/0; current correction pending |
| Source retention deadline | Seven exact vectors and ten independent operation checks | R7-052 fixed; exact atomic refusal/replay |
| Runtime/harness controls | Source full 0.2.5 rerun; package prior 0.2.4 baseline | 112 source pass; 28 package previously pass |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 43 fixed | R7-053 implementation open; R7-055 owner-question |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | R7-055: cross-issuer predecessor-path scope |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

Source deadline controls cover admit/raw/revise/declassify and every output,
original live/expired receipt replay, transitive known closure through unknown
lineage, both batch orders, null/unrelated bounds and authorization precedence.
Full refusal state and the original receipt are preserved; no purge is inferred.
Original failing inputs and results remain immutable.

All 62 supplemental artifacts validate in their explicit profiles. The twenty
seat-24 cases differ only in expected profile stamps when run as 0.2.5, and pass
exactly when explicitly executed as 0.2.4. A unified current supplemental total
awaits author migration; no implicit conversion or semantic failure is claimed.

R7-055 is a source ambiguity about whether an H1 canonical predecessor edge
endorses transitive H2 ordering. The validated native pair separates the readers;
the same-H1 control agrees. It stays outside vector denominators pending an
attributed owner decision. No evaluator is marked wrong on that boundary.

Remaining unsupported source vectors: B07, P08, S20, S24, S25, S26 and S27.
Unsupported never counts as pass; synthetic erasure, restore, release or delivery
does not qualify a real deployment. Phase 2 follows convener event
`$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; the 13:00Z hard cap remains.
Continue until the convener posts PARK.
