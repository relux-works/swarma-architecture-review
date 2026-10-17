# R7 verdict — astra-22

Status: Phase 2 active; no PARK. Source executes and passes49/57 canonical
semantic vectors on0.2.3. Eight remain explicitly unsupported. Score: **1/2**.
Judge independently verified the49-vector delivery expansion on pinned0.2.2;
retention correction is judge-closed atd077064. R7-040 and R7-043 are also closed.

The source-only baseline was frozen at `4d4ef45` before PACKAGE LANDED,
SHA-256 `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
The unchanged source-only artifact and first comparisons remain in git history. Only after
the convener's announcement was the package read. No other evaluator code was read.

Current package: **0.2.3-draft**, `23290b3a96a469d5190cb71b0e20139896b89236`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 49 | 0 | 8 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic (46 current cases) | 37 | 0 | 9 |
| Supplemental deployment | 0 | 0 | 1 |

Current outputs: `impl-astra-22/RESULTS.*`,
`runs/phase2-retention-corrected.*`, and
`runs/phase2-retention-cases-corrected.*`. First0.2.3 failures47/2/8 remain
immutable99b5a85. The mixed-profile migration run is explicitly separate.

R7-036 correction checks exact storage authority over every output and known
transitive integration input, including unknown lower bounds and same-batch
inputs. Current retain revocation blocks new writes and replay while preserving
old receipts and read/use rights. All four retention cases and eight new control
groups pass. Outputs with empty disclosure labels remain privately storable under
explicit authority. Judge closure is recorded atd077064.

Phase-2 additions include exact proof families, import-check currentness,
eligible retained dirty causes and transitive review, immutable captures and
current selected-item delivery. Canonical S07/S23/B01/S17/P06/P12 pass. Proof
representation can still grow exponentially; this is not a resource guarantee.

R7-040 NEXT correction99b5a85 excludes withdrawn authority candidates before
receipt ordering; all five author-migrated CAS cases and14transaction controls
pass. First failures e38c37c/5d079be/bd75f4f are preserved. R7-043 correction3722327
adds registered rule/check dependencies; all three exact judge probes and nine
impact controls pass. Judge closed R7-040 at99b5a85 and R7-043 at3722327.

All89controls pass on current grammar: source33,adapter8,transaction14,proof4,
impact9,boundary8,retention8,harness5. Each states its claim and material limit.
Owned historical fixtures have explicit0.2.3 copies; originals remain unchanged.
Current core SHA-256:
`7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.
Logs and chronology: `impl-astra-22/WORKLOG.md`; divergence evidence:
`impl-astra-22/DIVERGENCES.md` and `impl-astra-22/runs/`.

R7-011/012/013/015,025/026/027/028/029,030 and032 are judge-closed.
The historical phase-1 2/2 used a narrower supported-vector rubric and is not
Phase-2 completion. No case or package expected answer was edited.

Remaining canonical unsupported: B07,P05,P08,S20,S24,S25,S26,S27, covering
wire declassification, semantic erasure/restore and load/availability stimuli.
Changes and audience proof-reference disclosure also remain unsupported paths.
No protected deployment, physical erasure, timing isolation, randomness
qualification or crash durability is claimed. Semantic delivery sends no bytes.

In-progress declassification expansion first run now executes50canonical rows:
49pass/1fail/7unsupported, with unchanged canonical P05 valid release falsely
refused. Supplemental37/1/8. First reports: `phase2-declassification-first.*`
and `phase2-declassification-cases-first.*`; cause is omitted K-JSON-2 digest
framing. Correction is pending classification; preceding49/0/8 table is the
completed retention unit, not a passing claim for this expansion.

Nine release control groups and their immutable red-before output are in
`release_checks.py` and `runs/release-controls-first.json`. Two raw-digest
negative plants wrongly admit; valid framed controls refuse at the same defect.
R7-047 authority succession is judge-classified and queued after this unit;
R7-049 exact canonical refusal mapping is assigned to the editor.
