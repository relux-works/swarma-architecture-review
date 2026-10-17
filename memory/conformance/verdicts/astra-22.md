# R7 verdict — astra-22

Status: R7-025/026 corrections verified locally; first reports preserved. No other evaluator was read.

The source-only baseline was frozen at `4d4ef45` before package access. Its
SHA-256 is `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Original failing reports remain in `impl-astra-22/runs/0.1.0-first.*` and
`runs/case-first.json`. R7-011/012/013/015 fixes at `fb7df98` are judge-closed.

| Inventory | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic 0.2.0 cde5754 transaction first run | 44 | 1 | 12 |
| Canonical semantic 0.2.1 f31d58f transaction first run | 42 | 1 | 14 |
| Canonical semantic 0.2.1 corrected | 43 | 0 | 14 |
| Canonical deployment, each release | 0 | 0 | 8 |

The 0.2.0 failure reproduces known R7-021 (missing integration fact). The 0.2.1
failure is ASTRA22-05: the adapter omits the newly explicit subject/principal
binding gate, admits a foreign declaration and shifts the subsequent query cut.
Seven transaction controls, three adapter controls, 25 source controls and five
runner controls pass. R7-025 selected-sequence history and R7-026 identity gate
are corrected with red/green regression evidence; judge closure is pending. Reports: `runs/0.2.0-transactions-first.*`,
`runs/0.2.1-transactions-first.*` and `RESULTS.*`; follow-up in `DIVERGENCES.md`.

R7 score: **1/2** pending independent closure and collective gates. Explicit
unsupported semantic paths remain; all currently supported vectors agree. No protected deployment qualification, timing proof or physical
erasure is claimed.
