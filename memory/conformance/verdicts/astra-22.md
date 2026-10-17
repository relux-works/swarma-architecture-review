# R7 verdict — astra-22

Status: four judge-classified implementation defects corrected; release reruns
and judge closure pending. Unsupported semantic operations remain explicit.

The evaluator was derived from kernel v0.2, companion and design only, frozen at
`4d4ef45` before package access. First-run core SHA-256:
`cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Immutable first evidence is in `impl-astra-22/runs/0.1.0-first.*` and
`runs/case-first.json`. No other evaluator was read or used.

Against package 0.1.0-draft at `0ef608a`, corrected results are:

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 24 | 0 | 29 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental cases | 3 | 0 | 11 |

R7-011/012/013/015 corrections preserve unavailable-source incompleteness,
no-witness source state, exact authorized provenance and AND-path qualification.
24 source controls, one adapter visibility control and five harness controls pass.
Current core SHA-256:
`eb5bd2b8df171c98f5294ed54f01dcf9e3157bfa4e6253b3824f10167fbc4da6`.
Full fields and limits: `impl-astra-22/RESULTS.*`, `runs/case-corrected.*`,
`DIVERGENCES.md` and `WORKLOG.md`.

R7 score: **1/2**. Supported canonical semantics agree after classified fixes,
but unsupported operation coverage and the release/judge gates remain. No full
semantic profile conformance or protected deployment qualification is claimed.
