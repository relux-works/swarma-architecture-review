# R7 score

Owner: astra-27 (judge). Status: provisional, round 13; collective active.
Latest validated release: **0.2.1-draft**, package commit `f31d58f`.

**Current rubric score: 1/2.** Package corrections are verified. Two source
evaluator bugs remain: source-resolution accounting and source-state precedence.

| Requirement | Evidence | State |
| --- | --- | --- |
| Closed package and release | `f31d58f`, 14 schemas, 52 clauses | All classified package corrections verified |
| Package validator | 94 JSON files, 14 domain documents, 20 intended violation controls | Structural pass |
| Semantic inventory | 57 canonical vectors | Every vector executable; package evaluator 57 pass |
| Deployment inventory | 8 canonical vectors | Both evaluators explicitly unsupported |
| Source evaluator | `4e647ea`, package 0.2.1, exact independent reproduction | 43 pass / 0 fail / 14 unsupported semantic |
| Package evaluator | `f5fdd8b`, package 0.2.1, exact independent reproduction | 57 pass / 0 fail / 0 unsupported semantic |
| Ledger | [LEDGER.md](LEDGER.md): 8 rejected, 19 fixed, 0 open spec bugs, 2 open impl bugs | R7-028/029 |
| Owner questions | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md) | None established |

Both immutable original runs remain preserved and independently reproduced:
source [0.1.0-first](impl-astra-22/runs/0.1.0-first.md) and package
[FIRST-RUN](impl-astra-23/FIRST-RUN.md). Later first release failures and corrected
runs are preserved and independently checked as detailed in ledger rounds 10–13.
Source canonical reproduction has 44 passing source/adapter/transaction/harness
controls; package reproduction has 13 passing checker/product controls.

Current supplemental 0.2.1 inventory: 22 semantic cases. Package: 22 pass / zero
fail / zero unsupported; source: 13 pass / one fail / eight unsupported. The
source failure is R7-028; R7-029 has separate schema-valid targeted probes.
Both evaluators leave one supplemental deployment case unsupported. Counts stay
outside canonical totals, and unsupported inputs never count as passes.

Score 2 requires no open spec/implementation bug, every semantic vector
executable, both evaluators passing every semantic vector they support, and
all source ambiguities filed. No real protected-deployment qualification is
claimed from any synthetic erasure, release, restore or delivery trace.
