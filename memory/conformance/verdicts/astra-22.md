# astra-22 source evaluator verdict

Final status: **PARKED**, under the convener decision at **2026-10-17 06:33Z**,
event `$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg`.

The source evaluator passes every currently published semantic vector. Final
collective score is **2/2**, confirmed by signed judge `9d2cdd4`: 58 ledger items,
47 fixed, 10 rejected and owner question R7-055. No specification or implementation
bug remains open. Source R7-057 is closed at `946cbd8`; package R7-058 is closed at
`104fbe8`. All owned implementation and review assignments are complete. The
[park note](../parked/astra-22.md) records the remaining owner question and limits.

Current package: **0.2.5-draft**,
`6a04e8cfb1490569cd1de7468d2085dd4840cf51`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic | 68 | 0 | 0 |
| Supplemental deployment | 0 | 0 | 1 |

Current reports are [canonical](../impl-astra-22/runs/phase2-erase-priority-corrected.md)
and [supplemental](../impl-astra-22/runs/phase2-restore-obligations-cases-first.md).
Green coverage totals 129 controls: source 33, adapter 8, transaction 14, proof 4,
impact 9,
boundary 8, retention 8, release 9, succession 4, authority projection 4,
deadline 6, erasure 12, availability 5, harness 5. The latest focused run executes
all 12 erasure groups, and the expanded supplemental run executes the five
comparator controls. Unchanged remaining groups retain the prior
[128-control green evidence](../impl-astra-22/runs/erase-priority-controls-corrected.json);
[new control evidence](../impl-astra-22/runs/restore-obligation-controls-first.json)
records commands, outputs, module hashes and this reuse boundary. Judge `9d2cdd4`
verifies the complete 68/68 supplemental report, reruns all 12 current erasure
groups and verifies unchanged remaining modules against prior reviewed pins.
The earlier full canonical and control evidence remains applicable.

The independent source baseline `4d4ef45` was frozen from kernel, companion and
design before PACKAGE LANDED. No foreign evaluator implementation has been read
or executed. Current source core SHA-256 is
`7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.
Every first disagreement and classified correction remains retained in
[WORKLOG](../impl-astra-22/WORKLOG.md) and the committed run artifacts. Historical
mixed-profile failures are explicitly distinguished from semantic defects.

Judge-closed source defects are R7-011/012/013/015, 025/026/027/028/029, 030, 032,
036, 040, 043, 047, 050, 051, 052, 056 and 057. The latest correction checks current
erase authority first, detects changed intent before replay metadata, and
reauthorizes stored refs only for exact replay. Original `0529814` and the five
expanded pre-fix wrong-code failures remain unchanged. Exact replay, immutable
empty receipts, fresh empty-ref erasure and complete refusal state are preserved.

Own [ASTRA25-12 observations](../impl-astra-22/runs/restore-current-obligations-native-first.json)
reproduce the author's four unchanged input traces on `946cbd8`. A current
external obligation absent from the old snapshot enters the source erasure
closure and purges both controlled sinks. An unreachable affected sink causes
an atomic incomplete refusal and keeps restored reads fenced. Known and empty
obligation controls remain distinct. All 22 modules in that original observation
match the reviewed head. Judge closes the package discrepancy as R7-058 at
`104fbe8`; the native observations remain
outside exact denominators. Author `1cefcf9` adds five exact regressions, including
unaffected independent B; all pass the first expanded source run. A new focused
control verifies protected generation advancement and atomic stale/current
derivative refusal after newly witnessed deletion, with an independent valid
write as positive control. No evaluator behavior change was needed.

R7-055 / ASTRA24-12 remains held for Ivan's attributed decision. The source
preserves issuer-local receipt ancestry. The mixed-issuer pair has no imposed
oracle and is excluded from exact denominators; both readings and full own
observations remain in [native evidence](../impl-astra-22/runs/authority-issuer-native-first.json).

Remaining unmapped non-canonical API paths are changes, audience proof-reference
disclosure and request_check. Proof families can grow exponentially. No protected
deployment, physical deletion, timing isolation, randomness qualification or
crash durability is claimed. Delivery sends no external bytes; custody and
outside-domain witness facts are trusted fixture inputs. Semantic controls do
not qualify these deployment properties.

Historical grammar limitation: `--package` selects vectors/profile, while
transaction shape validation uses this checkout. Reproduce older grammars in a
matching isolated checkout. Every current 0.2.5 report uses matching live grammar.
