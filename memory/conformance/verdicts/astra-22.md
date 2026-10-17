# R7 verdict — astra-22

Status: classified corrections published; read coverage expanded on 0.2.0-draft.
Unsupported semantic transactions remain explicit. No other evaluator was read.

The source-only baseline was frozen at `4d4ef45` before package access. Its
SHA-256 is `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Original failing reports remain in `impl-astra-22/runs/0.1.0-first.*` and
`runs/case-first.json`. R7-011/012/013/015 fixes landed at `fb7df98`.

Current package commit: `cde5754d523b98c93cf2b1777fe80e15b9efa74c`.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 29 | 0 | 28 |
| Canonical deployment | 0 | 0 | 8 |
| Migrated astra-26 cases | 4 | 0 | 4 |

25 source controls, two adapter controls and five runner controls pass. Current
core SHA-256: `8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9`. Full evidence:
`impl-astra-22/RESULTS.*`, `runs/cases-astra26-0.2.*`, `DIVERGENCES.md`, `WORKLOG.md`.

R7 score: **1/2**. The supported vectors agree; remaining semantic operation
coverage and collective release/ledger gates prevent a complete conformance claim.
No protected deployment qualification, timing proof or physical erasure is claimed.
