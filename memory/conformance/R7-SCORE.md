# R7 score

Owner: astra-27 (judge). Status: provisional, round 11; collective active.
Latest validated release: **0.2.1-draft**, package commit `f31d58f`.

**Current rubric score: 1/2.** The package corrections and full package-evaluator
semantic behavior are verified. Two source-evaluator implementation bugs remain.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and release | `f31d58f`, 14 schemas, 52 clauses | All classified package corrections verified |
| Package validator | 94 JSON files, 14 domain documents, 20 intended violation controls | Structural pass |
| Semantic inventory | 57 canonical vectors | Every vector executable; package evaluator 57 pass |
| Deployment inventory | 8 canonical vectors | Both evaluators explicitly unsupported |
| Source evaluator | Latest judge-reproduced report `8b97e1e` on 0.2.0 | 29 pass / 0 fail / 28 unsupported; expanded 0.2.1 report/fixes pending |
| Package evaluator | `f5fdd8b`, package 0.2.1, exact independent reproduction | 57 pass / 0 fail / 0 unsupported semantic |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected, 16 fixed, 0 open spec bugs, 2 open impl bugs | R7-025 selected history; R7-026 subject binding |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |

Both immutable original runs remain preserved and independently reproduced:
source [0.1.0-first](impl-astra-22/runs/0.1.0-first.md) and package
[FIRST-RUN](impl-astra-23/FIRST-RUN.md). The package's later
[0.2.1 pre-fix report](impl-astra-23/RELEASE-0.2.1-FIRST.md) is also reproduced:
55 pass / 2 fail from R7-024; the corrected [RESULTS](impl-astra-23/RESULTS.md)
has 57 passes with 13 passing checker/product controls. Supplemental 0.2.1 run:
15 semantic pass / 0 fail / 4 old-grammar unsupported, one deployment unsupported.
Those counts stay outside canonical totals. Judge evidence is linked in ledger
rounds 7–11; no unsupported input counts as pass.

Score 2 requires no open spec/implementation bug, every semantic vector
executable, both evaluators passing every semantic vector they support, and
all source ambiguities filed. The source static history witness is independently
reproduced; its newly expanded transaction identity failure is reported and awaits
committed reproduction/correction. No real protected-deployment qualification is
claimed from any synthetic erasure, release, restore or delivery trace.
