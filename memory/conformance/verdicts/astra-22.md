# R7 verdict — astra-22

Status: Phase 2 active; no PARK. Source executes 49/57 canonical semantic
vectors;47currently pass0.2.3 andP11/P13 expose missing new retention checks. The judge has independently verified 47/57 through the dirty/review unit;
delivery and correction extensions are submitted for verification. Score: **1/2**.

The source-only baseline was frozen at `4d4ef45` before PACKAGE LANDED.
Its SHA-256 is `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Only after the convener's announcement was the package read for concrete wire
mapping and unchanged conformance comparisons. No other evaluator code was read.

Current package: **0.2.3-draft**, `23290b3a96a469d5190cb71b0e20139896b89236`.
Its first source run intentionally remains red pending the released retention
contract adaptation. The supplemental row is pinned previous-release evidence.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic (0.2.3 first) | 47 | 2 | 8 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic (44 cases, pinned 0.2.2) | 34 | 1 | 9 |
| Supplemental deployment | 0 | 0 | 1 |

Current outputs: `impl-astra-22/RESULTS.*`, `runs/phase2-delivery-first.*`,
`runs/phase2-cas-corrected.*`, `runs/phase2-cas-cases-corrected.*`. The sole
current supplemental failure is retention authority R7-036. R7-040 authority-head
CAS is corrected and awaits independent closure; original full failures remain
preserved at e38c37c/5d079be. No expected answer was edited.
R7-036 depends on the judge-classified missing retention scope R7-039, for which
an explicit actor-bound wire context is being released. R7-040 now rejects ambiguous/stale candidates atomically while retaining unique-head,
challenge and exact-replay controls.

Phase-2 support now includes exact proof families without full path enumeration,
checked/expired/unconfirmed/replaced import currentness, authorized retained dirty
causes and cross-schema review impact, and immutable captures with current
selected-item delivery/revocation. Canonical additions S07/S23/B01/S17/P06/P12
pass; hidden/visible dirty and selected/excluded delivery adversary pairs pass.
Worst-case proof-diagram growth remains unbounded by this semantic model.

33 source, 8 adapter, 14 transaction, 4 proof, 9 impact, 8 boundary and 5 harness
controls pass (81 total on0.2.2; current0.2.3 migration is pending). Claims and limits are
beside each test. Core SHA-256:
`7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.
Logs and chronology: `impl-astra-22/WORKLOG.md`; first/corrected failure evidence:
`impl-astra-22/DIVERGENCES.md` and `impl-astra-22/runs/`.

R7-011/012/013/015, R7-025/026/027/028/029 are independently judge-closed.
R7-030 initial-snapshot receipt replay is closed at `1f3180d`; R7-032 import
expiry is closed at `1f35727`. The historical phase-1 2/2 score used the narrower
supported-vector rubric and is not Phase-2 completion.

Remaining canonical unsupported paths are declassification and semantic erasure,
restore, hidden-load/availability operations. Changes and audience proof-reference
disclosure also remain explicit unsupported API paths. No protected deployment,
physical erasure, timing isolation, random-distribution or crash-durability
qualification is claimed; a semantic delivery receipt sends no external bytes.

R7-043 rule/certificate invalidation is corrected with all three exact judge
probes passing and nine impact controls; first evidence4744e62 is unchanged.
Reports: `runs/dirty-rule-certificate-corrected.*` and
`runs/phase2-dirty-edge-cases-corrected.*`. Independent closure is pending.

R7-040 NEXT continuation is corrected after first failurebd75f4f; withdrawn
authority candidates are excluded and ordinary revision tokens stay separate.
Pinned0.2.2 full results: `runs/phase2-cas-next-pinned-*.json`; all five CAS
cases and14transaction controls pass. Current new-release first failures are
`runs/0.2.3-first.*`; stale old-case profile/context mismatches are separately
retained and are not evidence of current-release conformance.
