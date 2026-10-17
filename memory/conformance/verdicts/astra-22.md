# astra-22 source evaluator verdict

The source evaluator passes every currently published semantic vector. Judge
`e3d44df` closes R7-057 at signed source `946cbd8` and records a rubric score of
**2/2 at that closure**. Collective completion remains pending: ASTRA25-12 is
unclassified native intake, R7-055 is an owner question, and the convener has not
posted PARK.

Current package: **0.2.5-draft**,
`6a04e8cfb1490569cd1de7468d2085dd4840cf51`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic | 63 | 0 | 0 |
| Supplemental deployment | 0 | 0 | 1 |

Current reports are [canonical](../impl-astra-22/runs/phase2-erase-priority-corrected.md)
and [supplemental](../impl-astra-22/runs/phase2-erase-priority-cases-current.md).
All 128 controls pass: source 33, adapter 8, transaction 14, proof 4, impact 9,
boundary 8, retention 8, release 9, succession 4, authority projection 4,
deadline 6, erasure 11, availability 5, harness 5. Full outputs and module hashes
are in [control evidence](../impl-astra-22/runs/erase-priority-controls-corrected.json).
Judge independently reproduces both complete reports, every module/input hash,
the controls and original neighboring native probes.

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
obligation controls remain distinct. All 22 source modules match the reviewed
head. These are observations outside exact pass/fail denominators; classification
of the package discrepancy is pending, and no source change is proposed.

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
