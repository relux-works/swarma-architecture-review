# astra-22 source evaluator verdict

Position: **R7 1/2 pending independent coverage review, remaining judge decisions
and the Phase-2 quiet-round/PARK condition**. No PARK has been received.

Current package: **0.2.5-draft**,
`6a04e8cfb1490569cd1de7468d2085dd4840cf51`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic (61, explicitly migrated by authors) | 61 | 0 | 0 |
| Supplemental deployment | 0 | 0 | 1 |

Evidence: `impl-astra-22/RESULTS.*`, `runs/phase2-erasure-first.*`,
`runs/phase2-erasure-cases-current.*`. The initial mixed-profile supplemental
41/20/0 is retained in `phase2-erasure-cases-first.*`; author24's explicit27303e4
profile migration alone resolves those20differences. No oracle is edited.

The evaluator was independently frozen from kernel/companion/design before
PACKAGE LANDED. Source baseline4d4ef45, every first disagreement and classified
correction remain retained. Current source core SHA-256:
`7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.
No foreign evaluator implementation was read.

New coverage maps admitted content/custody erasure closure, metadata-filtered
receipts, current authorized replay, generation and late-writer fencing, partial
and unreachable custody, initial-backup restore and current-witness reconciliation.
It preserves tombstone inventory and independent recipients. Load and availability
stimuli preserve logical non-interference; control only records observations.

Initial124controls pass: source33,adapter8,transaction14,proof4,impact9,boundary8,
retention8,release9,succession4,authority-projection4,deadline6,erasure8,
availability4,harness5. Exact native outputs and module hashes are in
`runs/erasure-controls-first.json`; chronology/claims/limits in `WORKLOG.md`.

Judge-closed source defects:011/012/013/015,025/026/027/028/029,030,032,036,040,043,
047,050,051,052. Deadline052 is closed at4a14a56; native firstc9e1faf and exact
old-source0.2.5 first49/1/7 remain unchanged. New native ASTRA24-12 cross-issuer
ancestry has no oracle pending adjudication; issuer-local source behavior stays
unchanged. Package053candidate23b4d74 and this coverage extension await judge.

Remaining unmapped non-canonical API paths: changes, audience proof-reference
disclosure and request_check. Proof families can grow exponentially. No protected
deployment, physical deletion, timing isolation, randomness qualification or crash
durability is claimed. Semantic delivery sends no external bytes; restore witness
and custody facts are trusted fixture inputs. Phase-1 historical2/2 was narrower
and is not Phase-2 completion.

New ASTRA22-08 native probe exposes an additional failing recovery control:
initial public_availability=degraded remains unavailable after authorized
set_availability available succeeds. Exact inputs/state/actuals and module hashes
are frozen in `runs/availability-recovery-first.json`; prior124controls pass,
this125thfails. It is outside both semantic vector denominators. No silent fix;
judge classification is requested before correction.
