# R7 verdict — astra-27

Role: judge; sole writer of ledger, owner questions and score.
Status: round 34, phase 2 active; awaiting PARK. Current score: **2/2**.

Adjudicated 57 items: ten rejected as defects, forty-six independently fixed,
and one filed owner question (R7-055). No specification or implementation bug
remains open. See [LEDGER.md](../LEDGER.md), [R7-SCORE.md](../R7-SCORE.md)
and [OWNER-QUESTIONS.md](../OWNER-QUESTIONS.md).

Both independent readers pass **57/57 canonical and 63/63 supplemental semantic
vectors** on release 0.2.5 `6a04e8c`. Source runtime is `946cbd8`; package runtime
is `23b4d74`, unchanged by its latest supplemental report `348ea38`. Complete
committed rows, input/module hashes and actuals reproduce independently after
only declared fresh-handle normalization. All 64 supplemental artifacts validate.
Original failures and author fixture bytes remain preserved.

R7-057, the final open implementation bug, closes at `946cbd8`. Current erase
authority precedes changed-intent conflict; stored-ref metadata permission gates
only exact replay. Both unchanged purpose/audience regressions and six independent
native probes pass. Expanded controls retain read/use/metadata revocation,
fresh-key empty-ref purge, lost erase authority and immutable empty receipts.
All 128 source native/comparer controls pass; 31 package controls remain applicable
to its unchanged runtime. Earlier expiry and public-recovery closures remain valid.

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
