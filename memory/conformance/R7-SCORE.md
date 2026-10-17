# R7 score

Owner: astra-27 (judge). Current status: **ACTIVE — bounded D-009 round**.

**Current R7 score: 1/2.** D-009 is mapped and verified in 0.2.6 `77b951e`.
Judge first runs give source **66 pass / 0 fail / 0 unsupported** semantic and
unchanged package runtime **64 pass / 2 fail / 0 unsupported**. S34/S39 require
package alignment; first evidence `1be6026` is immutable. Both readers leave
8 deployment vectors unsupported. R7-055 closes only after both are green.

The 103 JSON artifacts regenerate exactly; 38 intended checker violations are
detected. All nine new D-009 expectations match the independently reviewed
issuer-local relation. The unchanged historical source regression remains
68/68 semantic on frozen 0.2.5, with one deployment case unsupported. This is
separate from the 0.2.6 denominator. No owner decision remains outstanding.
See [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) and the ledger's reopened rounds.

### Historical verified baseline — first PARK, 2026-10-17 06:33Z

Verified release: **0.2.5-draft**, `6a04e8c`. The following score and held-question
statements describe that prior PARK; D-009 supersedes the owner hold.

**Final R7 score: 2/2.** Both evaluators exactly pass **57/57 canonical** and
**68/68 supplemental semantic vectors**. No specification or implementation bug
remains open. R7-055 is a filed, unresolved owner question; its native pair has no
chosen oracle and stays outside executable denominators.

| Requirement | Pinned evidence | State |
| --- | --- | --- |
| Closed package | `6a04e8c`, 14 schemas, 52 clauses | All established specification findings fixed |
| Package validator | 94 JSON files, 14 domains, 34 intended violation controls | Pass; exact regeneration |
| Canonical semantic inventory | 57 vectors | Both readers execute and exactly pass all 57 |
| Source evaluator | Runtime `946cbd8`; expanded report/test `b8189ba` | 57 canonical + 68 supplemental pass |
| Package evaluator | `104fbe8`; independent full run and committed-report comparison | 57 canonical + 68 supplemental pass |
| Supplemental grammar | 69 explicitly versioned artifacts, including one deployment case | All validate at 0.2.5 |
| Source controls | 12 erasure groups rerun; 117 unchanged controls retain prior evidence | 129 pass coverage |
| Package controls | Full 30 product plus four comparer controls | 34 pass |
| Ledger | [LEDGER.md](LEDGER.md): 47 fixed, 10 rejected, one owner question | No open spec-bug or impl-bug |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | R7-055: cross-issuer predecessor-path scope |
| Deployment inventory | 8 canonical plus 1 supplemental | Both unsupported; no deployment qualification |

R7-058 closes at `104fbe8`: current witnessed obligations enter the full erasure
closure before recovery reopens. Unreachable affected custody refuses atomically;
new obligations update protected fences, erased refs and generation. The original
four recovery traces, three late-writer probes and five unchanged exact fixtures
pass. Known/empty/repeated recovery, unrelated content and valid independent writes
remain supported. Seven intended new-test failures reproduce on the old engine;
all first failures and original inputs remain immutable.

R7-055 asks whether an H1 canonical predecessor edge endorses transitive H2
ordering. Both source readings and the exact separating input remain recorded.
The convener holds it for Ivan; no implementation is marked wrong on that boundary
and no authority option has been applied. Filing this ambiguity satisfies the
rubric's owner-question requirement; it does not resolve the architecture choice.

Convener PARK event `$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg` confirms
full dual coverage and a quiet round from every seat. Final runtime, package and
fixture hashes remain at the reviewed pins. See the [judge park note](parked/astra-27.md).
Synthetic erasure, restore, release or delivery never qualifies a real deployment.
