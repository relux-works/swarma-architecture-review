# R7 verdict — astra-27

Role: judge; sole writer of the divergence ledger, owner questions, and R7 score.
Status: round 10, collective active. Provisional R7 row score: **1/2**.

Read the complete normative source contract and both independent first runs;
reproduced their exact reports before corrections. Adjudicated 23 items:
eight rejected as already prohibited, ten fixed with committed evidence and
independent controls, five candidate spec fixes awaiting behavioral verification. No source ambiguity requiring an owner
decision is established. See [LEDGER.md](../LEDGER.md).

Package `0.2.1-draft` at `f31d58f` validates 57 semantic and eight deployment
vectors with 20 checker controls. Its five candidate corrections are reviewed;
new-release evaluator results remain pending. The extended source evaluator at `8b97e1e`
reports 29 pass, zero fail, 28 unsupported semantic against the same 0.2.0 package. The package evaluator at `7c765fe` runs all
57 semantic inputs against 0.2.0: 54 pass, three fail, zero unsupported. Both
latest verified reports are independently reproduced against 0.2.0.
R7-023 derived-source-reference correction passes separate exact regressions
and hidden/unfound/unrelated-copy controls.
Both report eight deployment cases unsupported.

Open package corrections: mixed AND source-state composition, audience-scoped
dirty invalidation, publication-currentness applicability, B01's missing proposal
integration fact, and P15's incorrectly typed foreign self-declaration. Existing
v0.2 lineage, per-owner current release, snapshot, exclusion, alias and restore
meaning fixes have relevant behavioral/control evidence; narrower defects remain
explicitly tracked. No real deployment qualification follows from these models.

Remaining work: verify the next package and both evaluator runs, classify new
items, then finalize the [score](../R7-SCORE.md) and park note after PARK.
