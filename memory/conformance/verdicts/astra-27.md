# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 14, awaiting PARK. Verified R7 row score: **2/2**.

Adjudicated 29 items: eight rejected as already prohibited and twenty-one fixed
with committed evidence and independent checks. No open specification or
implementation bugs remain; no source ambiguity requiring an owner decision was
established. See [LEDGER.md](../LEDGER.md) and [R7-SCORE.md](../R7-SCORE.md).

Package 0.2.1 at `f31d58f` validates 57 semantic / eight deployment vectors,
14 closed schemas, 52 clauses and 20 intended checker controls. All classified
package corrections have independent behavioral evidence. Package evaluator
code `f5fdd8b`, with reports and controls at `8b9baf3`, passes all 57 canonical
and 22 supplemental semantic vectors. Four checker and ten product controls
pass; all report rows, hashes and normalized actuals match judge reproduction.

Source evaluator `512d006` passes 43 canonical semantic vectors, with zero
failures and 14 unsupported; supplemental: 14 pass / zero fail / eight
unsupported. All 50 source/adapter/transaction/harness controls pass. The final
corrections independently verified are root/quality isolation (R7-027), source
resolution limits (R7-028) and source-state precedence (R7-029). Original failing
runs and witnesses remain preserved; no vector was changed to hide these errors.

Both evaluators leave eight canonical and one supplemental deployment vector
unsupported. The source evaluator's unsupported semantic coverage is explicit;
this score does not claim a full source implementation or protected deployment
qualification. Remaining protocol work: monitor new evidence and finalize the
verdict and park note after the convener posts PARK.
