# R7 verdict — astra-22

Status: Phase 2 active; no PARK. Source executes and passes50/57 canonical
semantic vectors on0.2.4. Seven remain unsupported. Score: **1/2**.
Judge verified50/57 through declassification8a42945 on0.2.3; strict succession047
and receipt projection051 corrections are submitted for current-release review.

The source-only baseline was frozen at `4d4ef45` before PACKAGE LANDED,
SHA-256 `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
The unchanged baseline and first comparisons remain in git history. The package
was read only after the convener's announcement. No other evaluator code was read.

Current package: **0.2.4-draft**, `ef0264702d3ff937bd34410ea80660b196b6f1b0`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 50 | 0 | 7 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic (54 current cases) | 46 | 0 | 8 |
| Supplemental deployment | 0 | 0 | 1 |

Current outputs: `impl-astra-22/RESULTS.*`,
`runs/phase2-authority-projection-corrected.*`, and
`runs/phase2-authority-projection-cases-corrected.*`. No oracle was edited.

R7-047 correction4772258 requires strict canonical receipt ancestry for
replace/correct; three forbidden orders refuse atomically, while direct/transitive
successors, ordinary incomparable imports and exact replay remain allowed.
R7-051 correction traverses receipt DAGs before mapping exact assertion sequences;
receipt-only intermediates preserve order, eligible candidates stay scoped, and
incomparable branches remain ambiguous. Current B01 and all external succession
and read-only ancestry cases pass. First0.2.4 and native failuresd5f07be, earlier
64ef86e/4772258 reports and all original adversary inputs remain preserved.

Phase-2 implemented additions include exact proof families, import-check
currentness, retained eligible dirty causes/transitive review, immutable captures,
current selected-item delivery, explicit storage context/current replay authority,
and joint-owner declassification with exact framed body pins and live revocation.
Proof families can grow exponentially; no deployment resource guarantee follows.
R7-050/P05 is judge-closed at8a42945. Original framed/raw failures remain36983de
and e1ba8db; retention first0.2.3 failures remain99b5a85.

All106controls pass on current grammar: source33,adapter8,transaction14,proof4,
impact9,boundary8,retention8,release9,succession4,authority-projection4,harness5.
Each states its claim and limits; test setup/profile maintenance is explicit in
WORKLOG. Current source core SHA-256:
`7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.
Chronology/logs: `impl-astra-22/WORKLOG.md`; evidence:
`impl-astra-22/DIVERGENCES.md` and `impl-astra-22/runs/`.

Judge-closed source defects:011/012/013/015,025/026/027/028/029,030,032,036,040,043,050.
Corrections047/051 await review. Deadline intake/replay native probes are queued
pending judge/editor mapping. Phase-1's historical2/2 was a narrower rubric and
is not Phase-2 completion.

Remaining canonical unsupported: B07,P08,S20,S24,S25,S26,S27, covering semantic
erasure/restore and load/availability stimuli. Changes and audience proof-reference
disclosure also remain unsupported API paths. No protected deployment, physical
erasure, timing isolation, randomness qualification or crash durability is claimed.
Semantic delivery sends no external bytes.
