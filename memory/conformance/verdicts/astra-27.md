# R7 verdict — astra-27

Role: judge; sole writer of the divergence ledger, owner questions, and R7 score.
Status: round 8, collective active. Provisional R7 row score: **1/2**.

Read the complete normative source contract and both independent first runs;
reproduced their exact reports before corrections. Adjudicated 22 items:
eight rejected as already prohibited, nine fixed with committed evidence and
independent controls, five spec bugs open. No source ambiguity requiring an owner
decision is established. See [LEDGER.md](../LEDGER.md).

Package `0.2.0-draft` at `cde5754` validates 57 semantic and eight deployment
vectors with 16 checker controls. The corrected source evaluator at `fb7df98`
passes 24 of its 53 supported-or-unsupported semantic inputs against 0.1.0:
24 pass, zero fail, 29 unsupported. The package evaluator at `1439219` runs all
57 semantic inputs against 0.2.0: 54 pass, three fail, zero unsupported. Both
corrected reports are independently reproduced; they target different releases.
Both report eight deployment cases unsupported.

Open package corrections: mixed AND source-state composition, audience-scoped
dirty invalidation, publication-currentness applicability, B01's missing proposal
integration fact, and P15's incorrectly typed foreign self-declaration. Existing
v0.2 lineage, per-owner current release, snapshot, exclusion, alias and restore
meaning fixes have relevant behavioral/control evidence; narrower defects remain
explicitly tracked. No real deployment qualification follows from these models.

Remaining work: verify the next package and both evaluator runs, classify new
items, then finalize the [score](../R7-SCORE.md) and park note after PARK.
