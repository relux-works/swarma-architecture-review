# R7 verdict: astra-24 — semantics adversary

Status: Phase 2 active, round 17; no PARK. Source baseline `95f974b`, kernel v0.2; current package
`0.2.2-draft` released at `7e71765`.

## Scope and method

Read the complete mission, owner decisions D-001–D-008, kernel v0.2, normative
companion and design, and the released package. This seat authored nine synthetic
semantic cases with twelve exact package-format vectors, including focused controls. It did not modify
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
| ASTRA24-08 | CAS must use the unique current authority head; challenge is exempt | R7-040 source/R7-041 package impl-bugs; corrected-head verification pending |
| ASTRA24-09 | Transitive registered review paths survive dirty recomputation | Source passes; package omits the second dependent; judge pending |

ASTRA24-03's derived-source omission is part of R7-023, not a duplicate defect.
All original failures and earlier-profile evidence are retained in the case
histories and implementers' immutable run reports. No source ambiguity has been
established by these cases.

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

## Provisional R7 row and remaining work

**Phase 2 R7: 1/2.** Authority-head implementation repairs and the new package
review-path finding remain pending, alongside the collective's other repairs and
full dual-coverage gate. Source dirty/review canonical support is reported as
47/57 by its owner; this seat independently checked the six targeted controls and
its exact review-path fixture, not every canonical row. Protected deployment
remains unsupported and unqualified.

Remain in the round protocol, answer directed items and verify accepted changes
until the convener posts PARK. Finalize this verdict and the park note then.
Tracking and tool-readiness evidence is in seat-local `.temp/tasks.md` and
`.temp/*readiness*.log`.
