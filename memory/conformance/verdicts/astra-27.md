# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 36, phase 2 active; no PARK. Current score: **1/2**.

Adjudicated 58 items: ten rejected as defects, forty-six independently fixed,
one open package implementation bug (R7-058), and one filed owner question
(R7-055). The new native finding supersedes the round-34 score 2/2. See [LEDGER.md](../LEDGER.md), [R7-SCORE.md](../R7-SCORE.md)
and [OWNER-QUESTIONS.md](../OWNER-QUESTIONS.md).

Both independent readers pass **57/57 canonical semantic vectors** on release
0.2.5 `6a04e8c`. Source `946cbd8` passes **68/68 supplemental**; package `23b4d74`
passes **65/68**, with three exact R7-058 failures. All 69 supplemental artifacts
validate. Every older report row, input/module hash and normalized actual remains
unchanged; original failures and author fixture bytes are preserved.

R7-057 closes at `946cbd8`. Current erase
authority precedes changed-intent conflict; stored-ref metadata permission gates
only exact replay. Both unchanged purpose/audience regressions and six independent
native probes pass. Expanded controls retain read/use/metadata revocation,
fresh-key empty-ref purge, lost erase authority and immutable empty receipts.
All 128 source native/comparer controls pass; 31 package controls remain applicable
to its unchanged runtime. Earlier expiry and public-recovery closures remain valid.

R7-058 is the newly confirmed restore bug. Original native `644c793` supplies a
current complete external obligation A missing from the old snapshot's local
erasure inventory. The package claims reconciliation but leaves both controlled
sinks present and A readable; an unreachable affected sink also falsely succeeds
and opens the global fence. Judge independently reproduces every field of all
four validated traces, including correct source behavior, known/empty-obligation
controls, atomic false-witness refusals and restore-fenced queries. All seventeen
snapshot hashes verify. Current witnessed obligations must actually enter the
reconciliation closure; package correction is authorized under existing sources.
Five exact fixtures `1cefcf9` enter the supplemental denominator: original four
native inputs are preserved and an independent-content neighbor protects B.
New/current, unreachable and independent-B cases fail only in the package reader;
known/empty controls pass. Two intended checker plants are detected. Closure
still requires complete protected state, atomicity and late-writer verification.

The package has no open specification finding. Its 14 schemas, 52 clauses and
94 JSON artifacts were independently regenerated exactly, with 34 intended
checker violations detected. Full source adaptation and later corrections do not
constitute another package-blind run.

R7-055 remains unresolved: an H1 canonical edge may adopt H2's ordering claim or
merely cite a foreign causal reference. The native pair at `4424598` validates;
source gives ambiguous d1/d3, package current d3, and the same-H1 control agrees.
Both readings, exact input and recommendation are recorded in OWNER-QUESTIONS
and `q-authority-issuer`. The convener holds the question for Ivan. No attributed
owner decision, guessed oracle, new invalid-state rule or authority edit exists.
The pair stays outside executable denominators; filing it satisfies the rubric,
without claiming the architectural choice is resolved.

Eight canonical plus one supplemental deployment case remain unsupported.
Synthetic success does not qualify real custody, authorization or restore
boundaries. Continue until the convener posts PARK, then finalize this verdict
and the park note.
