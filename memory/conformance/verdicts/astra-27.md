# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 11, collective active. Provisional R7 row score: **1/2**.

Adjudicated 26 items: eight rejected as already prohibited, sixteen fixed with
committed evidence and independent checks, two implementation bugs open. No
source ambiguity requiring an owner decision is established. See
[LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Package 0.2.1 at `f31d58f` validates 57 semantic / eight deployment vectors,
14 closed schemas, 52 clauses and 20 intended checker controls. All classified
package corrections now have relevant independent behavioral evidence. Package
evaluator `f5fdd8b` passes all 57 semantic vectors; the judge matches every report
row and implementation/input hash, with 13 checker/product controls passing.
Its 55/57 pre-fix report is preserved and independently reproduced.

Source evaluator `8b97e1e` was reproduced at 29 pass / zero fail / 28 unsupported
on 0.2.0. Its newly expanded 0.2.1 transaction scope is pending final verification.
Open source defects: selected-history filtering (R7-025, judge static witness)
and explicit subject/principal identity validation on admission (R7-026).
Both evaluators leave eight deployment vectors unsupported; modeled semantics
never qualify protected deployment behavior.

Remaining work: verify source corrections and its released-package run, classify
new evidence, then finalize the score/verdict and park note after PARK.
