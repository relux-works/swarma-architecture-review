# ASTRA25-06: premise quality must not spend the existence budget

Status: R7-027 impl-bug; source correction independently verified and judge-closed.
Owner: astra-25. Package: `0.2.1-draft` at `f31d58f`.

## Clauses and separating input

K-EVAL-2 starts counters independently for each displayed assertion/polarity.
K-EVAL-4 explicitly evaluates each opposite premise under an independent walk;
quality checks do not spend the conclusion's existence counters. Source companion
requires distinct support/opposition and preservation of support through a
conflicted premise. This is the visible positive-control boundary encountered
while executing ASTRA25-01; its hidden-pair observations themselves remain equal.

```text
Public admitted A+, A-, checked sufficient rule A+ -> B+.
No B- evidence. Exact query selects B.
Capture: roots=2, rules=1.
Final query: roots=1, rules=1; everything else unchanged.
```

The existence walk for B+ visits exactly one A+ root and one rule. Its quality
walk independently finds A-. The authorized graph and admissibility are identical
in both queries. The second root slot in the first query is unnecessary capacity.

| Field | Global root counter across quality/existence | Independent polarity/quality walks |
| --- | --- | --- |
| B+ with roots=2 | present, complete, conflicted_premises_only | present, complete, conflicted_premises_only |
| B+ with roots=1 | not_found, incomplete, not_fully_checked | present, complete, conflicted_premises_only |
| B- | not_found, complete | not_found, complete |
| Final cutoff | root_limit | none |

The global outcome above is the actual source evaluator result: its reference
order visits the negative assessment first, leaving no existence root budget.
Even a different iteration order that preserved B+ would still incorrectly spend
its budget on opposite-quality work and could change quality/completeness.

## Executable control and evidence

[`astra-25-quality-budget-isolation.vector.json`](astra-25-quality-budget-isolation.vector.json)
is S03's admitted graph with the two bounded queries and exact equivalent-output
requirement. It contains no write operation beyond a harness capture, isolating
read accounting from the new transaction adapter. Expected values are grounded
in K-EVAL-2/4, not inferred from two implementations agreeing.

Source evaluator `df499a1` passes the roots=2 capture but fails the roots=1 query
in seven fields, the same seven paired fields, and two forbidden outcomes.
Package evaluator `f5fdd8b` passes the complete trace exactly. Original
ASTRA25-01 fails only at its visible-opposition final control on this source
version; its two hidden/non-hidden captures pass. Thus no new hidden-data leak
is inferred from this particular failure.

Code hashes, exact input hashes and field-level results are in
[`astra-25-evaluator-results.json`](astra-25-evaluator-results.json), runs
`astra22-v0.2.1-budget` and `astra23-v0.2.1-budget`. The nine owned fixtures pass
closed schema/reference/normalization/forbidden checks. Source harness controls
also pass; the valid larger-budget capture prevents a reject-everything result
from satisfying this witness. This is semantic accounting, not physical timing
or deployment isolation evidence.

## Classification and fix verification

The judge classified this as R7-027 in
`$7rEaswg27z-hkIdE5isHAV_uJfgKZEugsBVak3pMDu8`, independently reproducing both
owned failures. ASTRA24-05's direct two-polarity reduction is consolidated under
the same defect and supplies zero/one/two root-budget controls.

Source correction `4e647ea` passes ASTRA25-01 and ASTRA25-06 exactly with the
original bounds and expected reports. I also independently ran its 29 source
controls and the ASTRA24-05 fixture: all pass. Those controls include both signed
directions, genuine zero/insufficient root and rule allowances, within-walk memo,
stable reference order, continued premise visits and uncertain opposite quality.
The fix separates displayed-polarity and quality walks; it does not increase
budgets. Run `astra22-v0.2.1-budget-fixed` in the evidence JSON records exact
code/input hashes. First failures remain preserved. The judge closed R7-027 in `56e5909`;
its independent exact rerun and exhaustion controls agree with this verification.
