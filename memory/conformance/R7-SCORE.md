# R7 score

Owner: astra-27 (judge). Status: phase 2 active, round 21; no PARK.
Current verified release: **0.2.3-draft**, `23290b3`.

**Current phase-2 score: 1/2.** Current exact dual canonical passes: **47/57**.
Source implements 49 vectors; the new P11/P13 retention cases fail both runtimes.
Full 57/57 dual coverage plus one full round without a new open item is required
for early PARK. Three implementation bugs remain open; no specification bug or
owner question is open. The original score 2/2 at `b1ae299` is historical and
used the narrower supported-vector rubric.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `23290b3`, 14 schemas, 52 clauses | R7-039 retention scope and R7-042 checker gaps fixed |
| Package validator | 94 JSON files, 14 domains, 32 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Every vector executable |
| Current dual exact passes | Source `99b5a85`, package runtime at `5416283`, package 0.2.3 | **47/57; 2 failures shared, 8 source-unsupported** |
| Source evaluator | Independent full 0.2.3 run | 47 pass / 2 fail / 8 unsupported semantic |
| Package evaluator | Independent full 0.2.3 run | 55 pass / 2 fail / 0 unsupported semantic |
| Previous-release correction checks | Exact 0.2.2, source `99b5a85`, package `f6c339d` | Source 49/0/8; package 57/0/0; dual 49/57 |
| Frozen supplemental corpus | 44 semantic cases at `3f06da5`, package 0.2.2 | Source 34/1/9; package 42/2/0 |
| Judge invalidation probes | Three original exact inputs | Both pass after source correction |
| Ledger | [LEDGER.md](LEDGER.md): 10 rejected, 33 fixed | R7-036/037 retention and R7-046 delivery actor remain open |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

Round 21 closes source CAS R7-040 and rule/certificate invalidation R7-043,
package exact-import coverage R7-044 and transitive review R7-045, plus both
specification gaps. Source established controls total 81 with unchanged groups
reused explicitly; package 22 controls were rerun on frozen 0.2.2. These results
do not claim that the new retention requirements are implemented. Isolated
positive P11/P13 traces verify the new oracles without bypassing the full red runs.
Incoming actor correction `3ce8ee3`, current supplemental migrations and the
transitive-unknown retention pair are queued for independent review.

Remaining canonical source gaps: B07, P05, P08, S20, S24, S25, S26 and S27.
First failures, exact pins, input hashes and setup errors remain preserved in the
ledger. Unsupported inputs never count as passes. Synthetic erasure, restore,
release or delivery does not qualify a real deployment. Phase 2 follows convener
event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc`; the 13:00Z hard cap
remains. Continue until the convener posts PARK.
