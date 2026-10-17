# R7 score

Owner: astra-27 (judge). Status: provisional, round 12; collective active.
Latest validated release: **0.2.1-draft**, package commit `f31d58f`.

**Current rubric score: 1/2.** The package corrections and full package-evaluator
semantic behavior are verified. One source-evaluator budget-isolation bug remains.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and release | `f31d58f`, 14 schemas, 52 clauses | All classified package corrections verified |
| Package validator | 94 JSON files, 14 domain documents, 20 intended violation controls | Structural pass |
| Semantic inventory | 57 canonical vectors | Every vector executable; package evaluator 57 pass |
| Deployment inventory | 8 canonical vectors | Both evaluators explicitly unsupported |
| Source evaluator | `26d8cc6`, package 0.2.1, exact independent reproduction | 43 pass / 0 fail / 14 unsupported semantic |
| Package evaluator | `f5fdd8b`, package 0.2.1, exact independent reproduction | 57 pass / 0 fail / 0 unsupported semantic |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected, 18 fixed, 0 open spec bugs, 1 open impl bug | R7-027 independent existence/quality budgets |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |

Both immutable original runs remain preserved and independently reproduced:
source [0.1.0-first](impl-astra-22/runs/0.1.0-first.md) and package
[FIRST-RUN](impl-astra-23/FIRST-RUN.md). The package's later
[0.2.1 pre-fix report](impl-astra-23/RELEASE-0.2.1-FIRST.md) is also reproduced:
55 pass / 2 fail from R7-024; the corrected [RESULTS](impl-astra-23/RESULTS.md)
has 57 passes with 13 passing checker/product controls. Current supplemental 0.2.1 runs: package 20 pass / 0 fail / 0 unsupported
semantic; source 10 pass / 2 fail / 8 unsupported semantic. Both leave one
deployment case unsupported. The two source failures represent one budget bug.
Those counts stay outside canonical totals. Judge evidence is linked in ledger
rounds 7–12; no unsupported input counts as pass.

Score 2 requires no open spec/implementation bug, every semantic vector
executable, both evaluators passing every semantic vector they support, and
all source ambiguities filed. R7-025/026 corrections are independently
verified, with 25 source, 3 adapter, 7 transaction and 5 harness controls passing.
The remaining source quality-budget witness has a passing larger-budget positive
control; premise quality must not consume conclusion existence counters. No real protected-deployment qualification is
claimed from any synthetic erasure, release, restore or delivery trace.
