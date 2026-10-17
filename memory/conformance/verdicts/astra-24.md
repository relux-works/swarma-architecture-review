# R7 verdict: astra-24 — semantics adversary

Status: **PARKED** under convener decision at 2026-10-17T06:33Z,
`$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg`. Final R7 row: **2/2**.
Source baseline `95f974b`, kernel v0.2; released package `0.2.5-draft` at
`6a04e8c`; all twenty owned exact fixtures explicitly migrated.

This seat delivered twelve semantic cases and twenty exact regression fixtures,
with original failures retained. No specification or implementation bug remains
open. R7-055 is an unresolved owner question, not a chosen authority rule;
protected deployment remains unqualified. See the [park note](../parked/astra-24.md)
for remaining work and the evidence boundary.

## Scope and method

Read the complete mission, owner decisions D-001–D-008, kernel v0.2, normative
companion and design, and the released package. This seat authored twelve synthetic
semantic cases with twenty exact package-format vectors, three preserved first
succession probes and two issuer-boundary probes awaiting an exact contract
verdict, including focused controls. It did not modify
specification, evaluators, ledger or another seat's artifacts. Expected outputs
were derived from the contract and never supplied to the execution APIs.

## Findings and disposition

| Case | Finding | Disposition |
| --- | --- | --- |
| ASTRA24-01 | Clean alternative survives truncated explanation | R7-001 rejected as spec defect; regression retained |
| ASTRA24-02 | Checked rule expires at its exclusive endpoint; another root may survive | R7-002 rejected as spec defect; regression retained |
| ASTRA24-03 | Mixed necessary AND states must be combined before OR preference | R7-014 fixed `f31d58f`, judge-closed `6a4f307`; R7-015 judge-closed |
| ASTRA24-04 | Derived witness must retain exact authorized premise sources | R7-023 fixed `7c765fe`, judge-closed `73ebb62` |
| ASTRA24-05 | Each polarity must have an independent bounded root counter | R7-027 fixed `4e647ea`, judge-closed `56e5909` |
| ASTRA24-06 | A current-required source cannot be checked with zero resolution allowance | R7-028 fixed `c923ebd`, judge-closed `b1ae299` |
| ASTRA24-07 | Four exact AND proofs remain distinct despite two root origins | R7-035 no defect; regression passes both, source extension `4960d24` |
| ASTRA24-08 | CAS must use the unique current authority head; challenge is exempt | Package `53266dd` and source `99b5a85` independently verified; both judge-closed |
| ASTRA24-09 | Transitive registered review paths survive dirty recomputation | Package R7-045 verified and judge-closed `f6c339d`; both exact fixtures pass |
| ASTRA24-10 | Replacement receipt must strictly succeed the prior receipt | Source R7-047 and package R7-048 verified and judge-closed; mapping release R7-049 verified `ef02647` |
| ASTRA24-11 | Transitive authority order survives an absent intermediate assertion | R7-051 source correction `427fed5` independently verified and judge-closed `de37630`; both exact witnesses pass |
| ASTRA24-12 | Receipt ancestry through a foreign issuer separates careful readings | R7-055 ambiguity / owner question verified at `dc6991d`; no typed oracle asserted |

ASTRA24-03's derived-source omission is part of R7-023, not a duplicate defect.
All original failures and earlier-profile evidence are retained in the case
histories and implementers' immutable run reports. ASTRA24-12 is the sole
established source ambiguity and remains held for the owner.

## Round 7 execution evidence

Identical owned 0.2.1 fixtures ran at checkout `4fadedd`. Source core SHA-256:
`8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9`;
source adapter SHA-256:
`cd7db027d81a7632d76a84d5d8b35327d8a1382ed5ae5d3a1b9233045bdb1205`.
Package evaluator SHA-256:
`c73f7f4e32045fcbb0039b49d2417c59b71ee40eba2e4cf62386eb6faa907dea`;
package engine SHA-256:
`601939ae52a7ecd7ed7395c27f40862ec5b756f2be78fa020a3e9644a681bda2`.

| Case | Source evaluator | Package evaluator |
| --- | --- | --- |
| ASTRA24-01 | unsupported: exact proof enumeration | pass |
| ASTRA24-02 | pass, including surviving alternative | pass |
| ASTRA24-03 | pass: direct states, mixed AND, stronger OR, exact source refs | pass |
| ASTRA24-04 | pass: exact direct/derived source refs | pass |

Both evaluators additionally pass expanded canonical S32 exactly. Its fixture
SHA-256 is `832a9da6e8b11bbfa3761934da8912b81d9e1cb3d817aee8bad6710c8fc6f3ff`.
K-EVAL-5 now explicitly states weakest state within each necessary AND path and
strongest state between complete OR alternatives. R7-014 is behaviorally verified.
The package implementation's direct/derived, hidden-source, failed-assessment
and unrelated same-origin-copy controls also pass under the current grammar.

Seat-local reports: `.temp/astra22-owned-cases-08.json`,
`.temp/astra23-owned-cases-03.json`, `.temp/astra22-s32-01.json`,
`.temp/astra23-s32-01.json`, `.temp/astra23-derived-controls-02.log`.
The first attempt to invoke the focused native control used the wrong working
directory (`-01.log`); that setup error is not semantic evidence.

All four owned fixtures pass structural checks and intended forbidden-value
plants (`.temp/case-vectors-validate-09.log`). Package structural validation passes
65 vectors (57 semantic / 8 deployment), 52 clauses and 20 intended checker
controls (`.temp/package-validate-03.log`). Structural validation does not execute
an evaluator or qualify deployment behavior.

## Round 8 bounded-counter counterexample

At checkout `6a4f307`, ASTRA24-05 exposes a source-evaluator failure with one
support root, one opposing root, and a root bound of one. Each polarity must
complete independently, but the shared counter drops support and invents a
root_limit cutoff. Both evaluators pass the nearby budget-2 and budget-0 controls;
the package evaluator passes the complete fixture. Seven exact differences plus
paired-output and intended forbidden failures are recorded in the case.

Current owned corpus: package 5 pass / 0 fail; source 3 pass / 1 fail / 1
unsupported (exact proof enumeration). Reports are
`.temp/astra22-owned-cases-10.json` and `.temp/astra23-owned-cases-05.json`;
all five valid fixtures and forbidden plants pass
`.temp/case-vectors-validate-11.log`. The first new fixture draft failed structural
setup and was corrected before the valid comparison; no setup error is counted
as an evaluator failure. The existing four cases retain unchanged inputs and
expected outputs. The new counterexample requires judge disposition.

## Round 9 source-resolution boundary

ASTRA24-06 at `f39af13` passes with one source-resolution visit but the source
evaluator incorrectly preserves the full derived witness with zero source
allowance. Eight exact field differences and three intended forbidden checks
show the omitted bound. The package evaluator passes both queries. Original
case expectations remain unchanged; the source core hash is the same as round 8.

Current owned corpus: package 6 pass / 0 fail; source 3 pass / 2 fail / 1
unsupported (exact proof enumeration). Exact reports:
`.temp/astra22-owned-cases-11.json`, `.temp/astra23-owned-cases-06.json`.
All six fixtures and bounded forbidden plants pass structural validation in
`.temp/case-vectors-validate-12.log`. ASTRA24-05 is a complementary root-only
witness of concurrently classified R7-027; consolidation was requested. The
judge decides whether the omitted source bound extends that family.

R7-014 is now judge-closed at release `f31d58f`; current package-evaluator
canonical 57/57 and source 43 pass / 0 fail / 14 unsupported reports remain
separate from this newer adversarial corpus. Deployment remains unsupported.

## Round 10 repair verification

Source fix `4e647ea` passes unchanged ASTRA24-05 and all four targeted native
budget controls, including zero/insufficient bounds, opposite-quality uncertainty
and within-walk memoization. Core SHA-256:
`d81a4ae9956802b82d4710d85dfc54efb5679c91eb623e6515e12d8907ba8b9e`; adapter SHA-256:
`12eb2f6232bea3878fb8dd8179750d0cc1845a5e38631f7c888ff5b475e2ae1b`. R7-027 consolidation is confirmed by the judge;
this seat recommends closure of that specific repair after the judge's gates.

ASTRA24-06 still fails with the same eight final differences and three forbidden
predicates. The zero source-resolution allowance remains omitted. Current source
owned corpus is 4 pass / 1 fail / 1 unsupported; unchanged package corpus is
6 pass. Evidence: `.temp/astra22-owned-cases-12.json` and
`.temp/astra22-budget-controls-01.log`. Original failures and all six fixtures
remain unchanged. The package owner independently recorded ASTRA24-06 passing
at `a48fa45` on unchanged evaluator `f5fdd8b`.

## Round 11 source-resolution repair verification

Source fix `c923ebd` passes unchanged ASTRA24-06 and the complete six-case corpus:
5 pass / 0 fail / 1 unsupported. Four focused source/adapter controls pass,
covering min(query, policy), repeated/distinct/grouped source visits, separate
polarity/quality walks, hidden candidates and retained/independent exemptions.
No expected semantic value was changed. Source core SHA-256:
`4ee2c9010143a21fd124d443421472a6b60245927c02eb8d8663984518d8aaeb`; adapter SHA-256:
`7f201c0a72a174afd62a331e675a224e6f2c889126ebd5d96d4457c7777df091`.

Evidence: `.temp/astra22-owned-cases-13.json` and
`.temp/astra22-source-budget-controls-01.log`. R7-028 is independently verified;
judge closure is pending. R7-029, raised separately by source owner/judge, concerns
resolved or empty-source precedence over independent-attestation fallback. It
remains separate from the repaired budget counter. The package corpus remains
6 pass on unchanged inputs and implementation.

## Round 12 current-head regression verification

At checkout `8b9baf3`, source precedence correction `512d006` preserves every
owned exact fixture: source 5 pass / 0 fail / 1 unsupported; package 6 pass.
All six input hashes match the prior runs. Current source core SHA-256:
`bd0f09fd93fa4d82af6ac5ec4338bd9dec05fde32ddd82262c73df2369224550`; source adapter SHA-256:
`7f201c0a72a174afd62a331e675a224e6f2c889126ebd5d96d4457c7777df091`.

Two focused source/adapter precedence controls and the package implementer's
independently authored availability-precedence control pass. They cover resolved,
empty and unavailable source variants with independent/retained/current neighbors,
preserving evidence qualifications and zero-budget behavior. This seat has no
new disagreement from the final source-state repair. Evidence:
`.temp/astra22-owned-cases-14.json`, `.temp/astra23-owned-cases-07.json`,
`.temp/astra22-source-precedence-controls-01.log`,
`.temp/astra23-source-precedence-controls-01.log`.

Judge ledger `56e5909` closes R7-027. R7-028 has a positive independent closure
reply but its ledger successor and R7-029 final review are pending in this
checkout. No new fixture, package edit or expected-answer change in this round.

## Phase 2 scope and round 13

Convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc` explicitly
withholds PARK and requires all 57 canonical semantic vectors to pass both
implementations, followed by a full round without a new open item. The original
supported-vector 2/2 at judge `b1ae299` is preserved as historical evidence; it
was not a claim of complete dual coverage. Current dual coverage is **43/57**.

Source gaps: B01, B07, P05, P06, P08, P12, S07, S17, S20, S23, S24, S25,
S26 and S27. This seat focuses on exact proof enumeration, dirty/review behavior,
and the v0.2 distinction between write collision, ambiguous currentness and
signed evidence conflict. Disclosure and publication adversary scopes remain
with their existing owners. Unsupported inputs are coverage gaps, not fabricated
implementation defects.

ASTRA24-07 adds a tight four-root/one-rule Cartesian proof fixture: four exact
proof sets, two root origins, complete evidence under a three-path rendering cap.
The package evaluator passes; source exact proof enumeration is unsupported.
The seven owned cases now give package 7 pass and source 5 pass / 0 fail / 2
unsupported. Exact reports: `.temp/astra22-owned-cases-15.json`,
`.temp/astra23-owned-cases-08.json`; structural and intended-forbidden checks:
`.temp/case-vectors-validate-13.log`. Original six expected results are unchanged.

Initial inspection of projection exclusion found explicit subtraction from
review refs plus audience redaction, so no new case was fabricated for that
hypothesis. Narrow review-list scope remains under source audit without an
asserted defect. Research is persisted in `.temp/phase2-review-scope-notes.md`
and `.temp/phase2-unsupported-inventory.json`.

## Round 14 proof extension verified

Source `4960d24` passes all seven unchanged owned semantic vectors, including
ASTRA24-01 and ASTRA24-07, with no exact differences or forbidden matches.
Four focused proof controls pass, independently checking finite-set algebra,
canonical/numeric ordering, hidden/quality exclusion and a bounded prefix of
a shared 2**40 family. Reports: `.temp/astra22-owned-cases-16.json` and
`.temp/astra22-proof-controls-01.log`. The package corpus remains 7 pass on its
unchanged implementation. This is finite conformance evidence, not a general
complexity or deployment guarantee.

Judge `945096f` records R7-035 as no defect, retaining the proof distinction as
regression coverage. The source owner reports canonical coverage 44/57 after
S07; this seat independently verified its own proof cases, not the full run.
The remaining source canonical gaps number 13. New classified Phase 2 bugs
R7-030 through R7-034 remain with their named implementation/spec owners.

The narrow-target review-list hypothesis is not asserted as a defect: K-EVAL-8
defines query-affected via an eligible authorized dependency path and explicitly
allows cross-schema review dependents. A stricter target-local product preference
cannot substitute for a contractual invariant. No fixture or requirement was
changed for that hypothesis.

## Round 15 ambiguous-head counterexample and 0.2.2 migration

ASTRA24-08 combines authoritative currentness with compare-and-set admission.
Both implementations incorrectly accept withdrawal of one exact candidate while
the authority slot has two incomparable heads. K-REV-1 requires version_conflict
and no mutation. The pair's ordered-authority control accepts the identical
withdrawal and returns the correct new-cut view. Both original ambiguity and
write refusal stay separate from signed evidence conflict. Judge intake pending.

Current owned execution at `7e71765`: **8 pass / 1 fail / 0 unsupported** for
each evaluator. The same two forbidden effects occur in both: accepted receipt
and an extra persisted revision. First valid failures and the passing control
were preserved before the package release migration; omitted-review setup
failures are explicitly distinguished in the case. Exact reports: source19 and
package11, structural/control log17, all under seat-local `.temp/`.

All nine vectors explicitly migrate to package0.2.2 by changing only profile
metadata. Normalized input/expectation equality and hashes are persisted in
`.temp/astra24-profile-022-migration.json`; no erase receipt migration applies
to this corpus. Prior seven behavioral expectations remain unchanged and pass.

## Round 16 authority-head neighbors

The new ASTRA24-08-STALE fixture shows the same target-chain shortcut accepting
a historical candidate in a totally ordered authority slot. The accompanying
challenge fixture preserves K-REV-1's explicit CAS exemption and passes both
implementations. Original primary/control bytes and all seven prior cases are
unchanged. These are failure-class controls for ASTRA24-08, not two new claims.

At `b3aeed2`, the eleven owned fixtures give **9 pass / 2 fail / 0 unsupported**
in each implementation. Source report20 and package report12 preserve exact
failures; structural/control log18 passes all eleven. New-cut challenge output
remains ambiguous with neither signed witness and no dirty marker. Unique-head
withdrawal remains admitted; ambiguous and historical-head withdrawal must be
refused atomically. Classification is pending.

## Round 17 transitive review separation

Six source impact controls pass on extension `e38c37c`. An independently authored
read-only fixture then separates full review paths from immediate historical
premises: ASTRA24-09 has historical A1 -> B -> C review dependencies, a current
A2, and cleared recomputation dirty causes. Private output must list B/C, while
the public control with a hidden second edge must list B only. Source passes;
package loses C in the private result. No signed witness, dirty state or selected
item changes. Judge classification of this separate review-path finding is pending.

At `a016781`, twelve owned fixtures give source **10 pass / 2 fail** and package
**9 pass / 3 fail**, with no unsupported input. Two shared failures are the
judge-accepted R7-040/041 authority-head family, persisted at `1cdcb36`; the third
package failure is the new missing review reference. Exact reports source21 and
package13, six impact controls01 and structural/forbidden controls20 are retained
in seat-local `.temp/`. Earlier fixture bytes and semantic expectations are intact.

## Round 18 package CAS repair verified

Package `53266dd` passes all four unchanged authority-head cases and the seven
prior regressions. Its one remaining owned failure is ASTRA24-09 transitive
review: **11 pass / 1 fail**, no unsupported input. The focused native CAS
control passes full refusal-state equality plus valid unique-head, challenge,
arrival-order, later unique ordering, replay precedence, changed intent and
next-head withdrawal variants. Reports: package14 and authority-cas-controls01
under seat-local `.temp/`. No fixture or expected value changed.

R7-041 is independently verified by this seat; judge closure is pending. R7-040
source and the new transitive review finding remain separate, so this result
is not represented as collective completion. First failures remain preserved.

## Round 19 source repair exposes a remaining-head neighbor

Source `68152c5` passes all twelve prior owned vectors and two focused native
CAS/state/replay controls. A fifth CAS fixture then checks a remaining boundary:
withdraw unique current d3, read d2/current, then withdraw that d2 with its exact
current token. Package passes. Source incorrectly retains withdrawn d3 in head
selection and refuses d2, contradicting its own valid intermediate current view.
This is proposed as the remaining R7-040 head-selection family, not a new count.

At checkout `0f59936`, thirteen fixtures give **12 pass /1 fail** each: source
fails ASTRA24-08-NEXT; package fails ASTRA24-09 transitive review. Original
negative CAS cases remain repaired. Source23/package15 preserve exact outcomes;
source22 and source-authority-cas-controls01 retain the positive repair evidence.
All 13 structural/inventory/normalization/forbidden controls pass validate21.
No previous input or expected behavior changed. Do not declare source CAS closure
from the smaller suite while this continuation remains unresolved.

## Round 20 separate rule/certificate invalidation repair verified

Source `3722327` passes all three unchanged judge fixtures for rule withdrawal,
certificate withdrawal and the premise control. Nine focused native impact
controls pass, including exact cause retention/replay, hidden versus private
authorization, challenge exemption, transitive consumers, pre-cause reads,
recomputed causes and dirty status before zero-budget evidence evaluation.
The dependency delta includes each justification and its check identity in the
same protected marking and pre-revision eligibility traversal. No fixture changed
from first-evidence `4744e62`. This corroborates R7-043 independently.

Evidence: `.temp/astra22-dirty-rule-certificate-01.json` and
`.temp/astra22-impact-controls-02.log`. The separate owned corpus at `3722327`
remains12pass/1fail in source report24; ASTRA24-08-NEXT still fails and is not
closed by this repair. Package transitive review is now judge-classified R7-045;
its first exact report at `08c4b9a` and unchanged fixture are retained.

Release `23290b3` arrived after this pinned0.2.2 verification. Its explicit
retention-context migration and new-profile runs are the next unit; no result
above is silently reclassified as a0.2.3 pass.

## Round 21 explicit retention migration and review repair

All 13 owned vectors now name 0.2.3. Six revise operations explicitly bind
private/read retention context, with independently checked existing exact actor,
space, record grants and direct complete integration facts. Initial states and
behavioral expected outcomes are unchanged; normalization removes only the
declared context/profile delta. The migration ledger records every hash and
context in `.temp/astra24-profile-023-migration.json`. All 13 structural and
intended forbidden controls pass log 22.

At checkout `12eccae`, package correction `f6c339d` passes all 13 owned fixtures;
source passes 12 with the same remaining-head NEXT failure. R7-045 exact private
B/C review and public B-only control now pass, plus two focused native tests for
transitive/cyclic/mixed paths, hidden required elements/certificates, and pure
sufficient/documentary negative controls. No evidence or dirty state is invented.
Reports source25/package16 and transitive-review-controls01 preserve the evidence.
R7-045 closure is recommended after judge gates; its original first failure is
retained. These authorized contexts do not qualify the full new retention refusal
contract; its owner repairs and broader canonical runs are separate.

## Round 22 remaining authority head verified

Source `99b5a85` passes all thirteen unchanged migrated fixtures at checkout
`ddc62c6`, including every ASTRA24-08 neighbor and the NEXT read/write continuation.
Three focused native CAS tests preserve exact refusal state, challenge exemption,
new authority ordering and historical receipt replay. Withdrawn candidates no
longer displace the remaining active receipt head. Report 26 records all input
and implementation hashes; `astra22-authority-cas-controls-02.log` records the
focused controls. First failure `bd75f4f` remains intact. R7-040 closure is
recommended after judge review, without extending this claim to unsupported
canonical operations or the separate retention contract.

Judge decisions close R7-040 at `99b5a85`, R7-043 at `3722327`, and R7-045
at `f6c339d`; their exact event identifiers are retained in the relevant case
and round handoff. Canonical retention repairs and expanded source coverage
remain separate from these verified closures.

## Round 23 authority-succession admission separation

Both evaluators at `d077064` accept B01 replacements with an unrelated canonical
receipt and with the prior receipt reused. Each commits both records, advances
the cut, dirties the registered dependent and stores idempotency state. The
unchanged ordered B01 control also succeeds. K-REV-3 forbids the two negative
writes, independently of any exact refusal-code choice. Three probes and their
first complete reports are committed with ASTRA24-10; structural/state checks
pass. Judge/editor adjudication is requested because the closed refusal table
does not explicitly map missing succession between existing canonical receipts.
No exact-output vectors or new oracle are claimed before that mapping resolves.

## Round 24 regression after scoped retention repairs

At one checkout, `36983de`, both evaluators pass all thirteen unchanged owned
0.2.3 vectors after source retention correction `d077064` and package correction
`4af0360`. Reports `.temp/astra22-owned-cases-27.json` and
`.temp/astra23-owned-cases-17.json` preserve exact implementation and input hashes;
all fixture hashes match the previous runs. Harness controls pass. These are
regressions of this seat's semantics, not a substitute for retention negative
controls or protected deployment evidence.

ASTRA24-10's original contract probes and first reports remain immutable.
Its typed-vector builder is prepared locally but not executed while exact refusal
mapping awaits judge/editor adjudication. Implementers acknowledged the new
write-admission boundary and will retain their independent first evidence.
The preceding round marker's package shorthand `c7e4160` names the judge ledger;
the actual package retention correction is `4af0360`.

## Round 25 exact authority-succession vectors

Judge decision assigns R7-047 source, R7-048 package and R7-049 code mapping,
explicitly requiring non-retryable `authority_receipt_required`. Five exact
vectors now cover unrelated, identical and prior receipts, plus direct and
transitive successor positives. All eighteen owned vectors pass structural and
intended forbidden controls. First exact results at `d990131`: source 14/4,
package 15/3. The previous thirteen fixture hashes and passing behavior are
unchanged; original first probe reports stay immutable.

All three forbidden writes are accepted by both implementations. The transitive
positive additionally shows a source-only projection problem: a receipt-only
intermediate node is dropped, so a valid accepted replacement is falsely
ambiguous. Its admission succeeds; the full expected view passes in package.
That distinct projection finding is recorded in ASTRA24-10 and submitted for
judge disposition, with read-only isolation queued next. Reports source28 and
package18 retain exact outputs and hashes; structural log25 distinguishes the
two earlier corrected fixture-format drafts from valid execution evidence.

## Round 26 receipt-only authority projection isolated

ASTRA24-11 removes only an intermediate assertion from a read-only ordered
three-receipt graph. Both implementations pass the complete-assertion control;
package alone preserves the unique final decision when the intermediate assertion
is absent. Source returns false ambiguity despite every receipt and authority
edge remaining admitted and eligible. No write or CAS operation participates.
This is the same projection failure as ASTRA24-10-TRANSITIVE, not two defects.

All twenty vectors pass structural/inventory/normalization/forbidden controls.
First full results at `a970a95` are source 15/5 and package 17/3; previous
eighteen inputs are unchanged. The case retains exact first paired results
and module hashes in a committed first-report artifact. Source implementation
classification is requested under K-REV-3, with no architecture change.

## Round 27 explicit 0.2.4 migration and source succession repair

All twenty owned fixtures migrate by expected-view profile values only; complete
normalized equality and exact old/new hashes are recorded in the migration
ledger. Structural log27 passes every shape/reference/normalization/inventory
and intended forbidden control. Original native first reports remain untouched.
At checkout `4772258`, owned results are source 18/2 and package 17/3.

Source R7-047 passes every exact negative and four focused native succession
groups covering full-state atomic refusal, replace/correct, direct/transitive
positives, reversed event storage, replay/CAS and ordinary incomparable imports.
The transitive positive writes correctly but has the still-open R7-051 projection
result. Canonical 0.2.4 B01 matches all source operation results and postconditions;
its seven differences are final projection fields only. Package B01 remains red
from forbidden writes. Evidence: source30/package20, succession-controls01 and
both B01 0.2.4 first reports. Source R7-047 closure is recommended after judge
review; it does not imply projection closure.

Release `ef02647` makes the adjudicated refusal explicit. Independent normalized
comparison confirms only B01 changes among 65 vectors; the decisions pilot stays
byte-identical. Package validation passes 94 JSON artifacts, 52 clauses and
33 intended checker plants. No full evaluator or generator-equivalence claim
is inferred from these checks. Exact source projection classification R7-051
and its independent judge event are persisted in ASTRA24-11.

## Round 28 package authority succession verified

Package `942bdee` passes all twenty unchanged owned 0.2.4 fixtures and the full
expanded B01 report with zero differences or harness violations. Three focused
native methods cover atomic replace/correct negative classes and same-key
recovery, direct/transitive successor positives, replay and distinct CAS, ordinary
incomparable import, and the prior slot-head CAS regression. Exact input/module
hashes and results are preserved in package21, B01-024-fixed and package
succession-controls01. Original first failures remain intact. R7-048 closure
is recommended after judge review; source R7-051 and other-seat deadline
corrections remain independent.

## Round 29 source receipt ancestry verified

Source `427fed5` at checkout `71fb6b3` passes all twenty unchanged owned fixtures
and the full expanded 0.2.4 B01 with zero differences or forbidden/normalization
failures. Four focused native ancestry methods pass absent/present intermediates,
longer receipt-only paths and event ordering, genuine incomparability, and
candidate eligibility for hidden/private, historical cut, subject and mode.
Read-only state equality is preserved. This is bounded regression evidence,
not a universal authority-graph or protected deployment claim.

Exact input/module hashes and results remain in source31, B01-024-fixed and
source authority-projection-controls01; first failures are unchanged. R7-051
closure is recommended after judge review. All eleven owned cases now have
passing exact vectors in both implementations at their documented corrected
heads. Retention deadlines and remaining source canonical gaps are separate.

## Round 30 issuer boundary in authority ancestry

Two closed, reference-valid native read-only probes now separate issuer-local
from global receipt-DAG traversal. Same-issuer ancestry selects d3 in both.
Changing only the middle event/source attribution to H2, with H1 endpoint
decisions and identical canonical edges/permissions, yields source ambiguity
versus package d3/current. Admitted state remains unchanged. Kernel 5.3 names
the authority's own ordered record, while K-REV-3 leaves intermediate issuer
scope unstated. ASTRA24-12 persists both readings, complete first evidence and
an issuer-local recommendation for judge adjudication; no runtime oracle or
architecture decision is invented. Native probes stay outside the denominator.

The first local issuer/submitter inconsistency was rejected structurally and
fixed before execution. First valid evidence is at `6a04e8c` under 0.2.5 with
unchanged non-profile input vocabulary. Existing twenty exact fixtures remain
on their explicitly published 0.2.4 version until the next migration unit.

Judge `de37630` formally closes R7-048 at `942bdee` and R7-051 at
`427fed5`, corroborating the independent evidence in Rounds 28 and 29. Their
original failure artifacts remain unchanged. The new issuer-boundary question
and finite retention deadline repairs are separate from those closed cases.

## Round 31 explicit 0.2.5 migration

All twenty owned exact fixtures now use 0.2.5. Only expected view profile stamps
changed: reversing that exact byte substitution reproduces every old fixture.
Initial states, operations, behavioral expectations, forbidden predicates and
normalization are unchanged. The input/operation records have no finite
retention deadlines, so this migration does not adjudicate R7-052 or R7-053.
All original first artifacts remain immutable, including the native issuer pair.

The release comparison independently confirms that P11 alone differs beyond
version identifiers across all 65 canonical vectors. Its original sixteen
operations and results are preserved. All fourteen schemas normalize exactly
across the versioned URNs/profile stamps; domain artifacts are byte-identical.
The current checker passes 94 JSON artifacts, 52 clauses and all 34 intended
violation controls. Judge R7-054 closure `3a60f2e` is corroborated for this scope.
A first local normalization omitted schema URNs without the `-draft` suffix;
that comparison setup was corrected after inspecting the raw diff, not counted
as a specification failure.

At checkout `7294c77`, source `4a14a56` and package `942bdee` each exactly pass
all twenty migrated vectors, with no execution errors or unsupported cases.
Both harnesses pass their existing known-violation controls. All twenty closed
shapes, reference sets, normalization, inventories and forbidden-output plants
also pass. No execution API receives the expected output.

Seat-local evidence: `astra24-profile-025-migration.json` and old-byte backup
`astra24-owned-profile-024/`; `package-025-delta.json`/`-delta-01.log`;
`package-025-validation-01.log`; `case-vectors-validate-28.log`;
`astra22-owned-cases-32.json/.log` and `astra23-owned-cases-22.json/.log`.
The reports retain the checkout, exact fixture hashes and all runtime module
hashes. This is a corpus regression and explicit migration, not a full finite
deadline or protected-deployment verification.

## Round 32 source-level ancestry distinction

At the judge's request, ASTRA24-12 now distinguishes the issuer-local
recommendation from what the source explicitly entails. Kernel 5.1/5.3 and the
companion's independent source namespaces favor local authority order, but do
not specify whether an H1 canonical event explicitly naming a foreign H2
predecessor accepts that foreign path into H1's own order. The global reading
uses supplied partial-order facts, not timestamps, and leaves endpoint H1
eligibility unchanged. The source-only exclusion is therefore not proved.

Ignoring foreign events for an H1 projection and declaring a mixed-edge state
invalid are separate rules. No supplied source mandates the latter integrity
constraint or its error. The case records the bounded distinction and requests
an owner question if judge adjudication cannot settle the source-level meaning;
no exact oracle, new mechanism or evaluator edit is introduced. First native
artifacts remain immutable. Research is retained in the case and seat-local
`research-authority-issuer-source-reading.md`. This documentation-only response
uses the existing paired execution evidence; no new runtime claim needs a rerun.

Judge `ad16ac9` closes source deadline R7-052 at `4a14a56`. Our prior migration
regression is unchanged and does not replace the judge's finite-deadline review.
Package deadline R7-053 and remaining source erasure/restore coverage are separate.

## Round 33 package deadline correction

Package `23b4d74` independently passes the same twenty owned 0.2.5 vectors
with identical input hashes and full canonical P11 with zero differences or
forbidden/shape errors. P11 includes all 28 operations, final view and inventory;
it is not the earlier positive-only trace. Three focused native deadline groups
also pass, with exact `not_authorized`, `retryable: false` and complete state,
captures, view-binding and dirty-time equality on refused attempts.

The controls cover equality/later own-output expiry through admit, admit_raw,
revise and declassify, valid earlier admission and replay, expiry on current
replay preserving the original receipt, changed-intent precedence and same-key
unlimited recovery. The seven independent deadline fixtures add inherited,
transitive-unknown and same-batch negatives with before-deadline and whole-batch
positives. The code change checks each resolved record's deadline in the shared
retention traversal before idempotency and before deduplicating identities.
These bounded controls do not qualify deployment or every possible lineage.

Evidence at `23b4d74`: `astra23-owned-cases-23.json/.log`,
`astra23-p11-025-fixed.json/.log`, and `astra23-deadline-controls-01.log` in this
seat's `.temp/`. Exact inputs and all implementation module hashes are retained;
the four checker controls also pass. No fixture, oracle, prior failure or native
issuer artifact changes. R7-053 closure is recommended to the judge.

Judge event `$Ju7IuqWDcWw6JB87jbG-0K3yC4TWQ2WszJTNwNLZQHs` announces
ASTRA24-12 as ambiguity R7-055 and opens `q-authority-issuer`. The announced
owner decision distinguishes issuer-local path scope from explicit global
canonical order; mixed-edge invalidity is a separate unchosen constraint.
At this unit's final fetch the ledger commit has not yet arrived, so this is
an attributed classification announcement, not a claim of read-back verified
ledger publication. No authority implementation or exact oracle may change
without that attributed contract decision. Other coverage work continues.

## Round 34 full dual canonical execution and recovery limit

At checkout `ead8bc1`, independently executing all 57 unchanged 0.2.5 canonical
semantic vectors gives source `dbf4892` 57/57 and package `23b4d74` 57/57, with
zero failures, unsupported cases or execution errors. Both reports contain the
same exact canonical input hashes, all actual outputs and implementation module
hashes. Execution APIs receive only initial state, operations and query; expected
outputs and forbidden predicates are applied afterwards by checked comparators.
All twenty owned exact source fixtures also pass with unchanged migration hashes.
The eight canonical protected-deployment vectors were not executed or qualified.

Eight new source erasure groups and four established availability groups pass.
They exercise replay/current authority, metadata filtering without reducing purge,
atomic invalid/unauthorized rejection, partial/unreachable/independent custody,
unknown lineage, late writes, fenced restore/current reconciliation and hidden
load/coarse availability/control observations. These are synthetic semantic state
checks, not evidence of physical deletion or a protected service.

The additional `test_initial_degraded_state_can_recover` fails independently,
as already preserved by source ASTRA22-08 at `dbf4892`: initially degraded policy
returns unavailable; owner `set_availability(available)` returns success; the
next read still returns a refusal. The source operation changes the runtime
availability flag but leaves the initial degraded policy flag that its query also
checks. The nearby available-to-degraded-to-available control passes. Our focused
suite is therefore twelve passing groups and one known failure, not an all-green
suite. This corroborates the existing finding; no duplicate case is filed or
unadjudicated correction made.

Evidence in seat-local `.temp/`: `astra22-canonical-025-full-01.json/.log`,
`astra23-canonical-025-full-01.json/.log`, `astra22-owned-cases-33.json/.log`, and
`astra22-erasure-availability-controls-01.json/.log`. The new helper records the
known failing method separately and requires its exact expected failure count;
that instrument assertion does not relabel the product failure as a pass.

Convener event `$wrLtxOryOvNuOttDN4ofHbvs0INg6jS0hLEpgMJ58wk` explicitly holds
R7-055 for Ivan. Both native readings remain preserved, with no exact oracle or
pass/fail denominator. At `ead8bc1`, the committed owner-question file still ends
at judge Round 29, so published-ledger readback remains pending despite the
attributed room classification. Other work continues without an authority edit.

## Round 35 adjudication record synchronization

ASTRA24-12's current status now links the read-back verified R7-055 owner
question at signed `dc6991d`. The native pair remains outside exact denominators
and under the convener's explicit hold for Ivan. This supersedes the earlier
pinned notes about awaiting ledger publication without rewriting their history.
Both complete first artifacts are byte-identical to `4424598`.

Judge event `$JwiSCClsftcbsOR8UrOJoe2h7NZWY12YYcjSgWm4S6c` classifies the
independently reproduced initial-degraded recovery failure as source impl-bug
R7-056. Current public availability must change without changing policy pins,
grants, records or unrelated state; the failure remains open pending correction.
This is separate from the held authority ambiguity and source erase-context
priority probe `0529814`, which has no adjudicated fix in this unit.

Only case/verdict status documentation changes. Existing executable evidence
already establishes the observations; no new runtime claim or exact oracle needs
an additional test. Local documentation checks confirm the owner-question link,
matching classification and unchanged frozen input/output bytes.

## Round 36 independent public-availability correction review

Source `87beb46` exactly passes all 57 canonical 0.2.5 semantic vectors and all
twenty owned fixtures. Their input hashes are unchanged from the previous full
run and explicit migration. Five focused availability groups now pass, including
the expanded four-pair initial/requested public-state matrix and the original
initial-degraded recovery regression. The earlier focused failure report remains
unchanged and is not replaced by this corrected run.

The correction updates the current public availability fact alongside the
existing runtime availability stimulus. The matrix checks that only those two
facts change: records, policy pins, grants, cuts, receipts and captures remain
intact. Unauthorized actors, missing coarse admission and malformed state still
refuse atomically with their specified codes; hidden load leaves the public view
unchanged apart from allowed fresh handles. These are synthetic state transitions,
not actual infrastructure recovery. R7-056 closure is recommended after judge review.

Evidence: seat-local `astra22-canonical-025-full-02.json/.log`,
`astra22-owned-cases-34.json/.log` and `astra22-availability-controls-02.json/.log`.
Exact inputs and full implementation module hashes are retained. Package code and
owned oracles did not change, so its prior independent exact evidence is retained
without another package rerun.

Judge `13e3d73` formally closes R7-053 at `23b4d74`, corroborating Round 33.
That ledger also verifies full dual canonical/supplemental coverage while keeping
native R7-056 open for correction review. The separate erase-context priority
probe remains unadjudicated here. R7-055 stays held for Ivan without an exact
oracle or authority change.

## Round 37 independent erase-context priority correction review

Source `946cbd8` passes both adjudicated ASTRA25-07 changed-purpose/audience
regressions byte-identical to `66233ab`, plus complete canonical P08. All three
exact reports pass with zero differences or forbidden predicates; execution
receives no expected values. Eleven source erasure groups also pass, including
three newly added priority/replay groups and the existing custody/restore bounds.
The targeted report records checkout `644c793`, all input and module hashes.

The reviewed delta compares canonical request intent before disclosing any
stored receipt, while retaining current erase operation authorization first.
Changed authorized audience/purpose conflicts even without metadata permission
in the new context. Exact replay after loss of read, use or metadata refuses
without changing state or the original receipt; an authorized fresh-key request
can still erase with empty disclosed refs. Expanded rights never enlarge an
old empty receipt on replay, and empty refs never bypass revoked erase authority.
The native assertions cover complete refusal-state equality and original receipt
preservation, with nearby successful replay/fresh-key controls.

Evidence: `.temp/astra22-erase-priority-corrected-01.json/.log` and
`.temp/astra22-erasure-controls-02.json/.log`. No input, expectation or old first
artifact changes. The nonexistent guessed priority-test filename was a read
lookup error; the actual new methods reside in `erasure_checks.py`, identified
from the published diff before execution. This is a focused verification of the
priority delta; full canonical/owned-corpus evidence remains pinned to Round 36.
R7-057 closure is recommended after judge review.

Judge `e2a797d` closes R7-056 at `87beb46`; the ledger was read back. The new
ASTRA25-12 external restore-obligation native witness at `644c793` is a separate
unadjudicated finding, with no exact oracle claimed here. R7-055 remains held for
Ivan and outside exact denominators.

## Round 38 independent current restore-obligation correction review

At exact candidate `104fbe8`, complete canonical S25 and the five adjudicated
ASTRA25-12 fixtures pass with zero differences or forbidden matches. Every
supplemental input is byte-identical to `1cefcf9`. The report retains all actuals,
input hashes and implementation module hashes; execution receives no expected
values. Four package comparer controls and three focused restore groups pass.

The corrected reconciliation uses the truthful current supplied obligation
closure, retains coverage of known local erasures, and checks affected controlled
custody reachability before any mutation. Newly learned deletion refs enter the
protected erased/fence inventories and advance generation before purge and
reopening. Known and genuinely empty obligations, repeated recovery, unaffected
content and external/unaffected custody remain supported.

The native groups cover the original four restore traces, complete/incomplete
known derivation closure, reachable/unreachable controlled custody, and late
writes. Unreachable recovery preserves the complete refusal state and global
fence. A generation-0 derivative refuses `stale_generation`, retryable true;
a current-generation derivative refuses `erasure_fenced`, retryable false.
Both preserve all state, captures and bindings, while an unrelated reviewed
current-generation write with the same key succeeds. These bounded controls
verify the corrected semantic transition, not physical purge or witness freshness.

A proposed neighbor with an incomplete inventory falsely marked as a true
current-complete external witness was rejected before execution: K-ERASE-3
requires that trusted fact to be false for incomplete inventories. It cannot
establish a valid semantic divergence. The analysis is persisted in seat-local
`research-restore-review-boundary.md`; no inconsistent oracle was created.

Evidence: `.temp/astra23-restore-current-corrected-01.json/.log` and
`.temp/astra23-restore-current-controls-01.json/.log`. This unit executed six
exact fixtures and three native groups, not another full corpus. Prior full
canonical and owned runs remain pinned to their documented heads. Original
`644c793`, `b805582` and `1138c5d` first evidence and all owned fixtures are
unchanged.

Judge `e3d44df` formally closes R7-057 at `946cbd8`. Fresh ledger/score readback
at signed `9d2cdd4` also closes R7-058 at `104fbe8`: the judge independently
verifies both evaluators on 57 canonical and 68 supplemental semantic vectors,
with 47 fixed items, ten rejected and the one held owner question. This is
attributed full-corpus evidence; our own Round 38 review is the focused scope
above. No new case or package change arose from this review.

## Final R7 row and PARK

**R7: 2/2.** Judge closure `9d2cdd4` and quiet record `73408ec` verify full dual
semantic coverage: 57/57 canonical and 68/68 supplemental. The ledger contains
58 items: 47 fixed, ten rejected and one unresolved owner question, with no open
specification or implementation bug. This seat's independent full canonical,
twenty owned and later focused correction evidence is pinned in the rounds above.
Full latest supplemental execution is attributed to the judge and implementers;
it is not an additional full run by this seat.

Convener PARK at 2026-10-17T06:33Z explicitly confirms the Phase 2 gate at
`1f92e91`: full dual coverage and one quiet round from every seat. Our round 39
reported no new case, divergence, package/runtime/fixture change or unanswered
directed item. Finalization changes only this verdict and our park note; no
additional evaluator execution is needed for this documentation-only delta.

R7-055 remains held for Ivan with no chosen exact oracle and outside executable
denominators. Its two native inputs and first outputs remain byte-identical to
`4424598`. The eight canonical and one supplemental protected-deployment cases
remain unsupported and unqualified. Synthetic semantic success does not establish
physical purge, witness completeness, service isolation or real delivery.

No seat-owned implementation/specification correction or directed review remains.
Remaining owner/deployment work is recorded in [the park note](../parked/astra-24.md).
Tracking, tool-readiness, input/module hashes and detailed local reports remain in
seat-local `.temp/tasks.md` and the evidence paths listed above. All original
failure evidence and twenty explicit 0.2.5 fixtures are preserved.
