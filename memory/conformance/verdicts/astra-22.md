# R7 verdict — astra-22

Status: Phase 2 active; all 57 canonical semantic vectors must run in both evaluators.
The phase-1 supported-vector criterion was accepted, but PARK was withheld.
Canonical supported vectors agree; the expanded supplemental inventory exposes
expired-import and retention defects. R7-028/029 are judge-closed at b1ae299. The package was read only after the convener posted PACKAGE LANDED; the source
baseline was frozen before then. No other evaluator code was read.

The source-only baseline was frozen at `4d4ef45` before package access. Its
SHA-256 is `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Original failing runs remain under `impl-astra-22/runs/`. R7-011/012/013/015 fixes
at `fb7df98` and R7-025/026 fixes at `26d8cc6` are judge-closed.

Current package: 0.2.1-draft, `f31d58f58d05de2ae4159dedaacfa1e32bdc656d`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 44 | 0 | 13 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic (30-case expanded first inventory) | 17 | 2 | 11 |
| Supplemental deployment | 0 | 0 | 1 |

R7-027 separates per-polarity existence budgets from independent opposite-quality
walks. All three affected adversarial fixtures pass without increased bounds.
33 source, 5 adapter, 11 transaction, 5 harness and 4 proof controls pass, including red/green
regressions, real exhaustion, both signed directions, memoization and quality
uncertainty. Current core SHA-256:
`999b53173fb7fe7127b5a1370b31f988e71f1f8a1fecfa922c4febb3eee6b0cc`.
Evidence: `RESULTS.*`, `runs/cases-0.2.1-first.*`,
`runs/cases-0.2.1-corrected.*`, `runs/cases-source-budget-*.json`,
`fixtures/independent-vacuous-source-first.json`, `DIVERGENCES.md` and `WORKLOG.md`.
R7-028 enforces distinct current-source visits. R7-029 corrects source-state
precedence; exact empty/nonempty/unavailable probes are retained in
`runs/independent-source-*.json`. Both fixes were independently closed.

Phase 2 score: **1/2**; dual canonical coverage is **44/57**. Historical
phase-1 score 2/2 at judge b1ae299 used the narrower supported-vector rubric.
R7-030 persisted-idempotency is corrected with exact probe and atomic controls;
independent closure is pending. R7-032 and ASTRA25-08 remain open; no PARK is claimed. Unsupported paths
remain explicit (dirty closure, publication operations,
erasure/restore and unconfirmed import currentness). No protected deployment
qualification, timing proof or physical erasure is claimed.

Phase-2 exact-proof first reports: `runs/phase2-proofs-first.*` and
`runs/phase2-proofs-cases-first.*`. Phase-1 accepted outputs are preserved in
`runs/phase1-accepted.*`; source core before Phase 2 was 512d006.

R7-030 immutable first evidence: signed f2c1570; corrected probe
`runs/persisted-idempotency-corrected.json` has no operation difference and
unchanged state. Canonical report: `runs/phase2-idempotency-corrected.*`.
