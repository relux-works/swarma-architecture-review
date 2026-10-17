# R7 verdict — astra-22

Status: Phase 2 active; no PARK. Source executes and passes50/57 canonical
semantic vectors on0.2.3. Seven remain explicitly unsupported. Score: **1/2**.
Judge has independently verified49/57 through retentiond077064; declassification
coverage and R7-050 correction are submitted next. R7-047 succession is queued.

The source-only baseline was frozen at `4d4ef45` before PACKAGE LANDED,
SHA-256 `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
The unchanged baseline and first comparisons remain in git history. Only after
the convener's announcement was the package read. No other evaluator code was read.

Current package: **0.2.3-draft**, `23290b3a96a469d5190cb71b0e20139896b89236`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 50 | 0 | 7 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic (46 current cases) | 38 | 0 | 8 |
| Supplemental deployment | 0 | 0 | 1 |

Current outputs: `impl-astra-22/RESULTS.*`,
`runs/phase2-declassification-corrected.*`, and
`runs/phase2-declassification-cases-corrected.*`. No oracle was edited.

Declassification atomically admits owner assessments and their pinned output,
checks every lifted input owner and exact current release pins, and requires
independent admit/declassify/retain authority. New queries and prepared delivery
recheck live decisions. Revocation preserves old captures and semantic history.
R7-050 corrected K-JSON-2 digest framing; immutable first36983de and native
counterexamplese1ba8db preserve both false refusal and raw-hash acceptance.
P05 and ASTRA25-02 now pass. Nine release groups include Unicode bytes, owner
intersection, transitive constraints, pins, deadlines, scope and revoked replay.

R7-036 retention is judge-closed atd077064, including exact per-record storage
scope, complete/unknown transitive inputs, same-batch inputs and current receipt
authorization. Original0.2.3 first failures remain99b5a85. R7-040 authority CAS
is closed at99b5a85 and R7-043 dirty rule/check causes at3722327. Original failures
remain in the divergence history. New R7-047 concerns strict successor authority
receipts, distinct from CAS head selection; exact mapping R7-049 is editor-owned.

Phase-2 additions include exact proof families, import-check currentness,
eligible retained dirty causes/transitive review, immutable captures and current
selected-item delivery. Proof representation may grow exponentially; no resource
or deployment guarantee follows from this semantic model.

All98controls pass: source33,adapter8,transaction14,proof4,impact9,boundary8,
retention8,release9,harness5. Affected47existing controls reran with the new mapping.
Each test states its claim and limits. Current core SHA-256:
`7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.
Chronology/logs: `impl-astra-22/WORKLOG.md`; divergence evidence:
`impl-astra-22/DIVERGENCES.md` and `impl-astra-22/runs/`.

Judge-closed source defects:011/012/013/015,025/026/027/028/029,030,032,036,040,043.
The historical phase-1 2/2 used a narrower supported-vector rubric and is not
Phase-2 completion. Correction050 awaits independent closure;047 remains open.

Remaining canonical unsupported: B07,P08,S20,S24,S25,S26,S27, covering semantic
erasure/restore and load/availability stimuli. Changes and audience proof-reference
disclosure also remain unsupported API paths. No protected deployment, physical
erasure, timing isolation, randomness qualification or crash durability is claimed.
Semantic delivery sends no external bytes.
