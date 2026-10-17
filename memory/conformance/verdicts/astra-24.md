# R7 verdict: astra-24 — semantics adversary

Status: active, round 12. Source baseline `95f974b`, kernel v0.2; current package
`0.2.1-draft` released at `f31d58f`.

## Scope and method

Read the complete mission, owner decisions D-001–D-008, kernel v0.2, normative
companion and design, and the released package. This seat authored six synthetic
semantic counterexamples and exact package-format vectors. It did not modify
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
| ASTRA24-06 | A current-required source cannot be checked with zero resolution allowance | R7-028; source fix `c923ebd` independently verified |

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

## Provisional R7 row and remaining work

**R7: 1/2 pending judge's final ledger.** All supported owned cases pass and
this seat's targeted R7-029 review is green. The published ledger at this checkout
still lists the final two source defects open; a successful producer report
alone does not close them. Exact proof enumeration and protected deployment
remain explicitly unsupported in the source lane where recorded.

Remain in the round protocol, answer directed items and verify accepted changes
until the convener posts PARK. Finalize this verdict and the park note then.
No protected deployment is qualified. Tracking and tool-readiness evidence is
in seat-local `.temp/tasks.md` and `.temp/*readiness*.log`.
