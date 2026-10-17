# astra-23 — final package implementer verdict

> Reopened on 2026-10-17 for D-009 / R7-055. The PARK and scores below
> record the completed 0.2.5 round. Package 0.2.6 intake, conformance and new
> PARK are pending; D-009 has resolved the owner choice. See the current worklog.

**PARK accepted: 2026-10-17 06:33Z. R7 score: 2/2.** Convener event
`$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg` confirms full dual semantic
coverage, no open specification or implementation bug, and a quiet round from
every seat. [Park note](../parked/astra-23.md) records the remaining limits.

Package: **0.2.5-draft**, `6a04e8cfb1490569cd1de7468d2085dd4840cf51`.
Package evaluator: `104fbe8dd5be973698e1b226fd9a52bcb79a1d2c`. Judge closure
`9d2cdd4` and quiet record `73408ec` independently verify the final result.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Supplemental semantic | 68 | 0 | 0 |
| Canonical deployment | 0 | 0 | 8 |
| Supplemental deployment | 0 | 0 | 1 |

All 30 product tests and four checker controls pass. The unchanged package
release validates 94 JSON files, 65 canonical vectors and 52 clauses, including
34 intended violation plants. Both independent evaluators exactly pass all
125 semantic vectors. Source control coverage is 129: 12 erasure groups rerun
plus 117 unchanged controls with explicit prior evidence reuse.

The latest correction, R7-058, reconciles the supplied current-witness closure
before reopening restored disclosure. The existing coverage check for retained
local erasures remains. Every affected controlled sink must be reachable before
mutation; newly learned deletion refs enter erased/fence state and advance
generation. Unreachable custody refuses atomically with the restore gate fenced.
Known, genuinely empty and repeated recovery remain valid. Independent content,
uncontrolled recipients and unrelated current-generation writes remain supported.

Three new native groups cover the four original restore traces, complete and
incomplete-known derived closure, unaffected content/custody, atomic refusal and
late writers. Old-generation and current-generation derivative writes refuse
exactly; an unrelated write with the same previously refused key succeeds.
Judge validation covers nine constructed initial states and all exercised shapes.
The new tests reproduce seven intended failures on the old engine without setup
errors. Independent reviews `a7fa673`, `b949afb`, `21221cb` and `45dbd67` agree.

The evaluator remains package-derived. The original blind first run `0008dc3`
is immutable, and no other evaluator implementation was read. Every subsequent
first failure and author-owned fixture is preserved. Native restore first
`b805582` predates correction; exact first `390b208` records 65/3/0 on byte-exact
old runtime `23b4d74`, with only the three adjudicated restore failures.

[The divergence record](../impl-astra-23/DIVERGENCES.md) and
[worklog](../impl-astra-23/WORKLOG.md) retain the other corrected findings,
release transitions, first observations and independent closure evidence.
Final exact reports are [canonical](../impl-astra-23/RESULTS.md) and
[supplemental](../impl-astra-23/SUPPLEMENTAL.md), with complete actuals and hashes
in their adjacent JSON files. [README](../impl-astra-23/README.md) gives entry points.

The final ledger contains 58 items: 47 fixed, 10 rejected and one unresolved
[filed owner question, R7-055](../OWNER-QUESTIONS.md). Ivan must choose whether
a deciding issuer's canonical predecessor path can adopt a foreign issuer's
transitive order. Both readings and the separating input remain preserved; no
authority change or exact mixed-path oracle was inferred. The native pair stays
outside executable denominators.

Deployment vectors remain unsupported. Synthetic erasure, restore, delivery and
control checks do not establish physical purge, an actual outside-domain witness
or hostile-writer isolation. There is no pending owned correction or unanswered
directed request at PARK; resuming the held authority question requires an
attributed owner decision.
