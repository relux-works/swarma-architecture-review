# ASTRA24-05: opposite polarities must not share one root budget

Status: R7-027 fixed at `4e647ea`, independently verified and judge-closed at `56e5909`.
Owner: astra-24. Package `0.2.1-draft` at `f31d58f`; execution checkout `6a4f307`.

## Clauses and two readings

K-EVAL-1 evaluates support and opposition independently. K-EVAL-2 explicitly
starts separate root, rule and source counters for each displayed assertion
and each polarity. K-EVAL-3 reports completeness of that authorized bounded
walk. K-EVAL-4 makes each root witness a clean path.

Reading A uses one shared root counter for both signs. Reading B gives each
sign its declared root allowance. This is a concrete implementation distinction;
the released package already requires B, so no package amendment is proposed.

## Minimal separating input

```text
One authorized assertion A.
One eligible passing A+ assessment, origin:ep, with no source dependency.
One eligible passing A- assessment, origin:en, with no source dependency.
No rules, no revisions, no dirty state; root budget = 1.
```

Each polarity has exactly one eligible root. Each independently completes its
walk within the bound, preserving both signs and their clean root paths. The
presence of A- does not spend A+'s budget or remove A+'s witness.

| Field at root budget 1 | Required B | Source actual A |
| --- | --- | --- |
| support.witness | present | not_found |
| support.evaluation | complete | incomplete |
| support.premise_quality | clean_path | not_fully_checked |
| support.evidence_qualification | [semantic_review] | [] |
| support.witness_roots | [origin:ep] | [] |
| support.independent_root_count | 1 | 0 |
| oppose witness/evaluation | present / complete | present / complete |
| cutoffs | [] | [root_limit] |

The source adapter supplies roots in reference order, so rec:en consumes its
single global allowance before rec:ep. The core's one used_roots counter spans
both channels. The fixture does not require storage order to decide any result.

## Controls and exact fixture

`astra-24-polarity-budget.vector.json` starts from canonical S02's unchanged
three-record state. It captures root budget 2 and root budget 0, then queries
budget 1. Expected results were authored from K-EVAL-2, before execution.

- Budget 2: both channels present and complete, with exact origins; positive control.
- Budget 0: both channels not_found and incomplete, empty qualifications/roots,
  and root_limit; negative control against ignoring the bound entirely.
- Budget 1: semantically equal to budget 2 after declared handle normalization;
  missing either witness or marking either channel incomplete is forbidden.
- No operation writes a record; exact postcondition inventory remains unchanged.

Both controls pass in both evaluators. Package evaluator passes the entire
fixture. Source evaluator fails the budget-1 result: seven exact-field
comparisons, seven equivalent-output comparisons and two intended forbidden
predicates. No lack of implementation support was declared for this input.
This root-only case does not by itself prove rule/source-counter isolation or
quality-walk isolation; those neighboring requirements remain separately testable.

## Evidence and recommendation

Fixture SHA-256: `b9a356230a843057efa46725671c358946f4104b95db605b338d8983914977ea`.
Source core SHA-256:
`8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9`;
source adapter SHA-256:
`2852392432677a9d2fa41695ea0acdb758d9af7ac60d9e6b17045c77e2f36caa`.
Package evaluator SHA-256:
`8bc6ae4535b4b3b59f612488d80638496b72b55b90ce7e2e74009a6d8fe95e24`.

Seat-local exact reports: `.temp/astra22-owned-cases-10.json`,
`.temp/astra23-owned-cases-05.json`. Both comparison harnesses passed their
bounded intended-violation controls; executors received only input state,
operations, query and profile, never expected outputs.

Closed grammar, references, inventory, handle normalization and the planted
missing-support forbidden value pass `.temp/case-vectors-validate-11.log`.
The first fixture draft had an unsupported capture label and malformed
normalization pair; the structural check rejected it. It was corrected before
these valid runs. `.temp/case-vectors-validate-10.log` and package probe `-04.json`
are setup-failure evidence, not semantic results.

Recommend classifying the source implementation's shared counter as an impl-bug.
Preserve per-polarity counter isolation and zero-budget rejection, and exercise
neighboring rule/source and opposite-quality walks when repairing the counter
scope. Do not change the expected result or multiply a global allowance to make
this single example pass. No deployment behavior is claimed.

## Concurrent finding and consolidation

ASTRA25-06 independently exposes the same shared counter through a rule and its
opposite-premise quality check; the judge classified it R7-027. ASTRA24-05 removes
that rule and quality dependency, demonstrating direct polarity isolation with
zero/two-budget controls. This seat requests one consolidated accounting defect,
not a duplicate count. At `f39af13`, the unchanged ASTRA24-05 still fails in
`.temp/astra22-owned-cases-11.json`; the package run `-06.json` passes.

## Source correction verified — round 10

Judge event `$Dp4_riQyF6haSd2qyOmKMURbHNt2rkZrFJBDw9-Ctlw` consolidates this
case into R7-027. At signed fix `4e647ea`, the unchanged exact fixture passes:
both direct polarities retain their own bound-1 witness, bound 0 still rejects
both walks, and bound 2 remains the positive equal-output control. No fixture
input or expected value was modified. Original failing runs remain preserved.

The correction implements fresh per-polarity DFS walks with local literal memo;
opposite-quality walks use independent counters. Four native source checks
also pass: both polarity directions, incomplete opposite quality, shared-premise
memo/numeric reference order, and genuine insufficient/zero root/rule bounds.
Evidence: `.temp/astra22-owned-cases-12.json`,
`.temp/astra22-budget-controls-01.log`. This verifies the specific root/quality
repair; ASTRA24-06 still exposes the independent omitted source-resolution bound.

## Package 0.2.2 profile migration

Round 15 explicitly migrated the vector to `0.2.2-draft` at release `7e71765`.
Only semantic_profile metadata changed; no input or behavioral expectation
changed. This seat has no erase operation requiring the new receipt context.
Normalized equality and old/new hashes are recorded in
`.temp/astra24-profile-022-migration.json`. Both evaluators preserve this case's
pass in source report19 and package report11. Earlier hashes above identify
the historical profile-specific runs.

## Package 0.2.3 explicit migration

Round 21 migrates this case to `0.2.3-draft` (`23290b3`). Behavioral expected
results and initial states are unchanged. Read-only operations need no storage
context; each of this seat's six revise operations explicitly binds private/read
under its existing actor/space/record retain grant. No grant is inferred from a
later query. `.temp/astra24-profile-023-migration.json` records old/new hashes,
exact operation contexts and normalized equality. Structural and intended
forbidden controls pass log 22. Earlier hashes identify historical profile runs.
