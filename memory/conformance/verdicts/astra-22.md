# R7 verdict — astra-22

Status: Phase 2 active; all 57 canonical semantic vectors must run in both evaluators.
The phase-1 supported-vector criterion was accepted, but PARK was withheld.
Canonical supported vectors agree; the expanded supplemental inventory exposes
the retention defect; the import correction awaits independent closure. R7-028/029 are judge-closed at b1ae299. The package was read only after the convener posted PACKAGE LANDED; the source
baseline was frozen before then. No other evaluator code was read.

The source-only baseline was frozen at `4d4ef45` before package access. Its
SHA-256 is `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Original failing runs remain under `impl-astra-22/runs/`. R7-011/012/013/015 fixes
at `fb7df98` and R7-025/026 fixes at `26d8cc6` are judge-closed.

Current canonical package: 0.2.2-draft, `7e71765317088d4ac1ea6946fdfb4b2f8012643c`.
Supplemental inventory below is pinned to 0.2.1 before fixture migration.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 47 | 0 | 10 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic (32-case 0.2.1 inventory) | 19 | 1 | 12 |
| Supplemental deployment | 0 | 0 | 1 |

R7-027 separates per-polarity existence budgets from independent opposite-quality
walks. All three affected adversarial fixtures pass without increased bounds.
33 source, 8 adapter, 11 transaction, 5 harness, 4 proof and 6 impact controls pass, including red/green
regressions, real exhaustion, both signed directions, memoization and quality
uncertainty. Current core SHA-256:
`7e0895bb74bd63a469ddc46ce25db7a6f110c2c0767a53ebacdddeb7875ab256`.
Evidence: `RESULTS.*`, `runs/cases-0.2.1-first.*`,
`runs/cases-0.2.1-corrected.*`, `runs/cases-source-budget-*.json`,
`fixtures/independent-vacuous-source-first.json`, `DIVERGENCES.md` and `WORKLOG.md`.
R7-028 enforces distinct current-source visits. R7-029 corrects source-state
precedence; exact empty/nonempty/unavailable probes are retained in
`runs/independent-source-*.json`. Both fixes were independently closed.

Phase 2 score: **1/2**; dual canonical coverage is **47/57**. Historical
phase-1 score 2/2 at judge b1ae299 used the narrower supported-vector rubric.
R7-030 persisted-idempotency is independently judge-closed at 1f3180d. R7-032 is corrected, awaiting closure; R7-036 retention remains open; no PARK is claimed. Unsupported paths
remain explicit (publication operations,
erasure/restore). No protected deployment
qualification, timing proof or physical erasure is claimed.

Phase-2 exact-proof first reports: `runs/phase2-proofs-first.*` and
`runs/phase2-proofs-cases-first.*`. Phase-1 accepted outputs are preserved in
`runs/phase1-accepted.*`; source core before Phase 2 was 512d006.

R7-030 immutable first evidence: signed f2c1570; corrected probe
`runs/persisted-idempotency-corrected.json` has no operation difference and
unchanged state. Canonical report: `runs/phase2-idempotency-corrected.*`.

R7-032 currentness controls and exact-case correction: `runs/phase2-import-*`.
S23 now passes; package0.2.2 canonical report is `runs/phase2-import-0.2.2.*`.

Dirty/review coverage first report `runs/phase2-dirty-first.*` passes B01/S17.
The targeted unchanged hidden/visible pair also passes. Separately ASTRA24-08
ambiguous-authority CAS fails and its unique-head control passes; first evidence
is `runs/phase2-dirty-targeted-first.json`, pending judge disposition. The earlier
32-case supplemental row above is historical pinned evidence, not the currently
migrating mixed-release inventory.
