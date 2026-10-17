# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 16, phase 2 active. Current phase-2 score: **1/2**.
Historical original supported-vector score: **2/2** at `b1ae299`.

Adjudicated 35 items: nine rejected as already explicit regression properties,
twenty-one fixed with committed evidence, one open specification bug and four
open implementation bugs. No source ambiguity requiring an owner decision is
established. See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Package 0.2.1 at `f31d58f` validates 57 semantic / eight deployment vectors,
14 closed schemas, 52 clauses and 20 intended checker controls. All classified
package corrections have independent behavioral evidence. Package evaluator
code `f5fdd8b`, with reports and controls at `8b9baf3`, passes all 57 canonical
semantic vectors at its accepted phase-1 baseline. The new 28-case supplemental
inventory has 25 passes and three failures (R7-031/033/034). Four checker and ten product controls
pass; all report rows, hashes and normalized actuals match judge reproduction.

Source evaluator `512d006` passes 43 canonical semantic vectors, with zero
failures and 14 unsupported; the new supplemental inventory has 14 pass / one fail / thirteen
unsupported (R7-032). A separate valid snapshot probe exposes R7-030 idempotency
reconstruction. Exact-proof candidate 4960d24 awaits independent verification. All 50 source/adapter/transaction/harness controls pass. The final
corrections independently verified are root/quality isolation (R7-027), source
resolution limits (R7-028) and source-state precedence (R7-029). Original failing
runs and witnesses remain preserved; no vector was changed to hide these errors.

Full dual canonical semantic coverage is **43/57**. Phase 2 requires the source
evaluator to execute the remaining fourteen canonical vectors and one full round
without a new open item before early PARK. Source-derived initial implementation
and later package intake remain distinct; expanded coverage is not described as
a second package-blind run.

Both evaluators leave eight canonical and one supplemental deployment vector
unsupported. The source evaluator's unsupported semantic coverage is explicit;
this score does not claim a full source implementation or protected deployment
qualification. Remaining work: audit expanded source coverage and new focused
cases, classify and verify every disagreement, then finalize only after PARK.
