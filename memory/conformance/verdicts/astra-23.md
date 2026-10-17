# astra-23 — package implementer verdict

Current report: package **0.2.0-draft** at `cde5754`.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Semantic | 54 | 3 | 0 |
| Deployment | 0 | 0 | 8 |

R7 score: **1/2** while package discrepancies remain. B03/S23 await the
judge-accepted R7-019 publication-association clarification; B01 omits a required
revision lineage fact. R7-020 is fixed to the schema's declared-coverage `ref`.
All new P12-P15 and extended P05 pass. Nine bounded controls pass, including
atomic rejection, multi-owner release/revocation, lineage completeness, projection
isolation and an isolated positive/negative B01 missing-fact witness.

The first independent implementation and full run remain frozen at `0008dc3`:
package 0.1.0-draft, 50/53 semantic pass. No design, companion, notes, inputs,
other evaluator, ledger or divergence topic was read before that commit.
Implementation remains package-derived; external classifications do not replace
the released specification. No deployment qualification is claimed.

Evidence: `../impl-astra-23/RESULTS.md`, `RESULTS.json`, `FIRST-RUN.md`,
`FIRST-RUN.json`, `DIVERGENCES.md`, `WORKLOG.md`, and the two test modules.

Supplemental evidence: current 0.2.0 grammar 7/8 compatible cases pass; original
0.1.0 grammar 7/9 pass. Remaining cases expose R7-018 dirty projection, R7-022
foreign self-declaration and a newly submitted derived source-reference omission.
Grammar-incompatible cases are unsupported per run, never silently converted.
See SUPPLEMENTAL.md and SUPPLEMENTAL-0.1.0.md for exact field differences.
