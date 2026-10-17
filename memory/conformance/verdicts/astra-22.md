# R7 verdict — astra-22

Status: all supported current semantic vectors agree; R7-028 fix awaits independent
review; ASTRA22-07 source-state precedence awaits classification. No other evaluator was read.

The source-only baseline was frozen at `4d4ef45` before package access. Its
SHA-256 is `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Original failing runs remain under `impl-astra-22/runs/`. R7-011/012/013/015 fixes
at `fb7df98` and R7-025/026 fixes at `26d8cc6` are judge-closed.

Current package: 0.2.1-draft, `f31d58f58d05de2ae4159dedaacfa1e32bdc656d`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 43 | 0 | 14 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental semantic | 14 | 0 | 8 |
| Supplemental deployment | 0 | 0 | 1 |

R7-027 separates per-polarity existence budgets from independent opposite-quality
walks. All three affected adversarial fixtures pass without increased bounds.
32 source, 4 adapter, 7 transaction and 5 harness controls pass, including red/green
regressions, real exhaustion, both signed directions, memoization and quality
uncertainty. Current core SHA-256:
`4ee2c9010143a21fd124d443421472a6b60245927c02eb8d8663984518d8aaeb`.
Evidence: `RESULTS.*`, `runs/cases-0.2.1-first.*`,
`runs/cases-0.2.1-corrected.*`, `runs/cases-source-budget-*.json`,
`fixtures/independent-vacuous-source-first.json`, `DIVERGENCES.md` and `WORKLOG.md`.
R7-028 enforces distinct current-source visits; R7-027 is independently verified.

R7 score: **1/2** pending judge closure and collective gates. Unsupported paths
remain explicit (exact proof enumeration, dirty closure, publication operations,
erasure/restore and unconfirmed import currentness). No protected deployment
qualification, timing proof or physical erasure is claimed.
