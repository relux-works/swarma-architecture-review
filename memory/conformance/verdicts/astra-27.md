# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 12, collective active. Provisional R7 row score: **1/2**.

Adjudicated 27 items: eight rejected as already prohibited, eighteen fixed with
committed evidence and independent checks, one implementation bug open. No
source ambiguity requiring an owner decision is established. See
[LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Package 0.2.1 at `f31d58f` validates 57 semantic / eight deployment vectors,
14 closed schemas, 52 clauses and 20 intended checker controls. All classified
package corrections now have relevant independent behavioral evidence. Package
evaluator `f5fdd8b` passes all 57 semantic vectors; the judge matches every report
row and implementation/input hash, with 13 checker/product controls passing.
Its 55/57 pre-fix report is preserved and independently reproduced.

Source evaluator `26d8cc6` is independently reproduced on 0.2.1: 43 semantic
pass / zero fail / 14 unsupported. History and identity fixes R7-025/026 pass
relevant controls. One supplemental budget bug remains: R7-027 combines existence
and opposite-quality counters, incorrectly losing a sufficient witness under a
tight budget. Source supplemental: 10 pass / 2 fail / 8 unsupported; package:
20 pass / zero fail / zero unsupported. The two source failures share one cause.
Both evaluators leave eight canonical and one supplemental deployment vectors
unsupported; modeled semantics never qualify protected deployment behavior.

Remaining work: verify R7-027 and its relevant reruns, classify
new evidence, then finalize the score/verdict and park note after PARK.
