# R7 verdict: astra-24 — semantics adversary

Status: active, round 8. Source baseline `95f974b`, kernel v0.2; current package
`0.2.1-draft` released at `f31d58f`.

## Scope and method

Read the complete mission, owner decisions D-001–D-008, kernel v0.2, normative
companion and design, and the released package. This seat authored five synthetic
semantic counterexamples and exact package-format vectors. It did not modify
specification, evaluators, ledger or another seat's artifacts. Expected outputs
were derived from the contract and never supplied to the execution APIs.

## Findings and disposition

| Case | Finding | Disposition |
| --- | --- | --- |
| ASTRA24-01 | Clean alternative survives truncated explanation | R7-001 rejected as spec defect; regression retained |
| ASTRA24-02 | Checked rule expires at its exclusive endpoint; another root may survive | R7-002 rejected as spec defect; regression retained |
| ASTRA24-03 | Mixed necessary AND states must be combined before OR preference | R7-014 release verified; judge closure pending. R7-015 source fix judge-closed |
| ASTRA24-04 | Derived witness must retain exact authorized premise sources | R7-023 fixed `7c765fe`, judge-closed `73ebb62` |
| ASTRA24-05 | Each polarity must have an independent bounded root counter | Observed source failure; judge classification pending |

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

## Provisional R7 row and remaining work

**R7: 1/2.** The package exists and validates; ASTRA24-05 now demonstrates a supported source-evaluator disagreement,
and collective release verification and open ledger work remain. Judge round 10
reported five candidate spec fixes pending behavioral evidence; R7-024 was then
classified as a package-implementation historical-selection bug. This seat's
local green regressions do not establish the collective score-2 gates.

Remain in the round protocol, answer directed items and verify accepted changes
until the convener posts PARK. Finalize this verdict and the park note then.
No protected deployment is qualified. Tracking and tool-readiness evidence is
in seat-local `.temp/tasks.md` and `.temp/*readiness*.log`.
