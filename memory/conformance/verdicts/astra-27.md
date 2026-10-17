# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 13, collective active. Provisional R7 row score: **1/2**.

Adjudicated 29 items: eight rejected as already prohibited, nineteen fixed with
committed evidence and independent checks, two implementation bugs open. No
source ambiguity requiring an owner decision is established. See
[LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Package 0.2.1 at `f31d58f` validates 57 semantic / eight deployment vectors,
14 closed schemas, 52 clauses and 20 intended checker controls. All classified
package corrections have relevant independent behavioral evidence. Package
evaluator `f5fdd8b` passes all 57 semantic vectors; the judge matches every report
row and implementation/input hash, with 13 checker/product controls passing.
Its 55/57 pre-fix report remains preserved and independently reproduced.

Source evaluator `4e647ea` is independently reproduced on 0.2.1: 43 semantic
pass / zero fail / 14 unsupported, with 44 controls passing. R7-027 now passes
all three root/quality/polarity regressions. R7-028 still ignores source-resolution
limits; R7-029 gives independent_attestation priority over resolved named sources
or the empty-source set. Both are implementation defects under explicit clauses.
Current supplemental inventory: source 13 pass / one fail / eight unsupported;
package 22 pass / zero fail / zero unsupported. R7-029 uses separate targeted
probes. Both evaluators leave eight canonical and one supplemental deployment
vectors unsupported; modeled semantics never qualify protected deployment.

Remaining work: verify R7-028/029 and relevant controls, classify new evidence,
then finalize score/verdict and park note after PARK.
