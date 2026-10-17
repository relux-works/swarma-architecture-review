# astra-21 park note

Status: **HISTORICAL PARK — reopened for D-009 / R7-055 at 2026-10-17T18:44:45Z**.
The delivery below remains the 0.2.5 record. This seat is active for 0.2.6 and
will replace this note only after the new convener PARK.

Prior PARK by convener `ivmbp_swarma-memory_orch` at
**2026-10-17T06:33Z**, event
`$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg` in `rounds`.
Seat: package editor, sole writer of `memory/spec/`.

## Delivered and verified

Package **0.2.5-draft** is signed release `6a04e8c`. Fresh PARK readback at
`1f92e91` confirms its entire package tree remains
`d79144db66a5e1328d3cc25fc573ad3c93959d02`, identical to the release. Validation
passes: 94 JSON artifacts, 14 closed schemas, 14 domains, one reusable fixture,
52 normative clauses and 34 intended checker-violation controls. Exact release
validation and deterministic-generation evidence remain applicable unchanged;
the convener also checked validation before PARK.

All 14 editor-owned specification bugs are judge-closed across releases
`cde5754`, `f31d58f`, `7e71765`, `23290b3`, `ef02647` and `6a04e8c`.
[Release history](../../spec/RELEASES.md) records each semantic delta and retained
regression witness. No source design or other seat's implementation was edited.

| Evidence | Final pin/result |
| --- | --- |
| R7 score | **2/2**, judge closure `9d2cdd4`, quiet readback `73408ec` |
| Source evaluator | Runtime `946cbd8`, expanded report/test `b8189ba`; 57/57 canonical + 68/68 supplemental semantics |
| Package evaluator | Runtime `104fbe8`; 57/57 canonical + 68/68 supplemental semantics |
| Source controls | 129 pass coverage: 12 focused erasure groups plus 117 unchanged prior controls |
| Package controls | 34 pass: 30 product tests plus four comparer controls |
| Ledger | 58 items: 47 fixed, 10 rejected, one filed owner question; no open spec/implementation bug |
| Deployment | Eight canonical plus one supplemental unsupported; no qualification claim |

The [final verdict](../verdicts/astra-21.md) retains this seat's exact audit scopes,
commands, first failures, full-state comparisons and evidence paths. Latest
independent correction reviews are `2ae3ebc` (R7-057) and `21221cb` (R7-058);
quiet editor round is `4e171e1`. Both corrections are now judge-closed. All
assigned reviews and directed requests are answered; no unclassified editor
finding, pending package edit or unpublished implementation remains.

## Open thread: R7-055

[OWNER-QUESTIONS.md](../OWNER-QUESTIONS.md) preserves the undecided meaning of a
canonical predecessor path through a different deciding issuer. Ivan must choose
issuer-local ancestry or explicit global canonical endorsement, or specify a
separate integrity rule. The conservative issuer-local recommendation is not a
source-proven requirement. No option has been implemented as a new oracle.

Original separating input `4424598` has SHA-256
`8224829a810a97c79fef81cb18f0d650b59ffc84a3262bdef09b1ea900c521b3`.
Same-issuer paths agree; the mixed intermediate produces ambiguous d1/d3 in the
source reader and current d3 in the package reader. Both readings and complete
native firsts remain preserved outside executable pass/fail denominators.
The convener holds the question for Ivan. Any later attributed decision requires
an explicit follow-up package release and corresponding conformance work; PARK
itself makes no authority decision and does not resolve this thread.

## Evidence continuity and limits

Task continuity is `.temp/tasks.md`. This seat's untracked scratch evidence is
under `.temp/astra-21/`, especially `park-readback-01.json`, `validate-20.log`,
`regeneration-06.log`, `deadline-025-verification.md`,
`erase-priority-verification.md`, `restore-obligation-verification.md` and their
linked reports, complete native snapshots, hashes and negative controls. The
frozen old-runtime restore check reproduces seven intended failures with no setup
error; the same new controls pass on the corrected runtime. Originals remain
immutable. These artifacts are local evidence, not claimed committed files.

Deployment erasure, outside-domain witness verification, identity, transport,
isolation and timing remain unqualified. No physical device, service, network
sink or user data was changed by the synthetic semantic evaluators. The held
owner question and deployment limits are the remaining open threads at PARK.
