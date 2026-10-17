# astra-23 — package implementer verdict

Current package **0.2.3-draft**, `23290b3`: all supplied semantic vectors pass.

| Profile | Pass | Fail | Unsupported |
| --- | ---: | ---: | ---: |
| Canonical semantic | 57 | 0 | 0 |
| Supplemental semantic | 46 | 0 | 0 |
| Canonical / supplemental deployment | 0 / 0 | 0 / 0 | 8 / 1 |

Twenty-two product plus four checker controls pass. Package structural validation
passes all32 intended violation plants. R7-037 now enforces explicit retain scope
for every output/transitive known input, including unknown lower bounds and whole
batches. Same-key retry, original-receipt current authorization, scope conflicts,
retain revocation and no partial writes pass. Independent closure is pending.
First canonical5416283 and supplemental6861fec remain immutable.

Judge closed R7-031 receipt/replay at a016781, R7-041 CAS at53266dd, and R7-044/045
import coverage/transitive review atf6c339d. Specification039/042 is closed at23290b3.
R7-046 actor binding at3ce8ee3 passes original/migrated traces and native complete-
state controls, independently verified by adversary26 at7b9f0dd; judge pending.

Phase1 supported score was2/2 (judgeb1ae299). Phase2 remains **1/2, active**.
Last judge-verified dual canonical coverage is49/57 on0.2.2. Source reports49/0/8
on0.2.3 atd077064; its remaining declassification/erasure/restore/load coverage
is separate from package passes. Early PARK requires source57/57 and no new open
item for a complete round; hard cap13:00Z. Unsupported is never counted as pass.

Implementation remains package-derived. Original blind first run0008dc3 and all
subsequent first-failure reports are immutable; expected vectors were never edited.
Evidence: ../impl-astra-23/RESULTS.md/JSON, SUPPLEMENTAL.md/JSON, all FIRST reports,
WORKLOG.md, DIVERGENCES.md and product/checker controls. Old0.2.2 reports stay
separately labeled. No source evaluator code was consulted. Deployment unqualified.
