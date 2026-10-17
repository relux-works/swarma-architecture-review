# astra-22 source evaluator verdict

Status: **closure verified; quiet round and new convener PARK pending**.
Own R7 row score: **2/2**, matching signed judge `75c13d2`. D-009 is implemented by the existing issuer-local
source runtime `946cbd8`; no product code change was required this round.
The prior 06:33Z PARK is historical and does not close this reopened round.

Current package: **0.2.6-draft**, `77b951eb86d5ba9198921d058930884918a39942`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical 0.2.6 semantic | 66 | 0 | 0 |
| Canonical 0.2.6 deployment | 0 | 0 | 8 |
| Historical 0.2.5 supplemental semantic | 68 | 0 | 0 |
| Historical 0.2.5 supplemental deployment | 0 | 0 | 1 |

[First canonical report](../impl-astra-22/runs/0.2.6-first.md) is immutable at
`31d77d2`; all nine new vectors pass without alignment. The
[current canonical report](../impl-astra-22/runs/r7-059-canonical-corrected.md)
has identical vector rows. Only checkout metadata differs. The separate
[historical regression](../impl-astra-22/runs/d009-0.2.5-regression-first.md)
uses unchanged original fixtures and the complete live 0.2.5 package tree at
`6a04e8c`; provenance is in `0bf20dc`, independently verified by judge `5e93189`.
It is not counted as canonical 0.2.6 coverage.

All **134 controls freshly pass** on matching 0.2.6 grammar: source33, adapter8,
transaction14, proof4, impact9, boundary8, retention8, release9, succession4,
authority_projection4, deadline6, erasure12, availability5, D-0095 and harness5.
[Complete output](../impl-astra-22/runs/d009-0.2.6-controls-corrected.json)
records commands, counts and hashes. The pre-package D-009 freeze `abc8511`
also passed all134; judge `7d33ac1` independently reproduced its controls and
validated 282 constructed instances / 275 unique states. These include the
original pair, assertion-free middles, all256 four-event DAGs, foreign invariance,
protected issuer attribution, CAS consistency and atomic replace/correct pairs.
The global-order mutation control fails exactly as intended.

R7-059 is a judge-classified harness profile binding bug. The first complete
0.2.6 control run at `31d77d2` preserves133pass/1fail: one historical boundary
control expected0.2.5 labels from live0.2.6. The corrected control creates two
explicit scratch copies changing only two expected profile fields each; fixed
profile guards, recursive equality, original/copy hashes and a detected actor
mutation plant bound the migration. The
[audit](../impl-astra-22/runs/r7-059-profile-migration-audit.json)
preserves this evidence. Original cases and all first reports remain unchanged.
Only boundary_checks.py differs from `abc8511`; all22othermodules are identical.
Judge `75c13d2` independently closes R7-059 at `c7e86d5` and resolves
R7-055 by D-009 with both readers at66/66. The ledger has59items:48fixed,
10rejected and one resolved ambiguity; no open finding or owner question.
Closure event: `$b8foGPG6rv8TSQqyaHjhJUZkyLIBXmTKrWxuZv4cPSs`.

Source baseline `4d4ef45` was frozen from kernel, companion and design before
initial PACKAGE LANDED. D-009 controls were frozen from kernel v0.3 and
DECISIONS.md before 0.2.6 intake. No foreign evaluator implementation has been
read or executed. Core SHA-256 is
`7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.
Every first disagreement and classified correction remains retained in
[WORKLOG](../impl-astra-22/WORKLOG.md) and committed run artifacts.

Remaining unmapped non-canonical API paths are changes, audience proof-reference
disclosure and request_check. Proof families can grow exponentially. No protected
deployment, physical deletion, timing isolation, randomness qualification or
crash durability is claimed. Delivery sends no external bytes; custody and
outside-domain witness facts are trusted fixture inputs. Semantic controls do
not qualify deployment properties.

Historical grammar limitation: --package selects vectors/profile, while
transaction shape validation uses this checkout. Reproduce older grammars in
a matching isolated checkout. Every current0.2.6 report uses matching live
grammar; the historical0.2.5 regression was run before pulling0.2.6.
