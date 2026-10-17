# ASTRA25-01: hidden opposition cannot taint visible premise quality

Status: source-contract regression case; package not yet landed.
Owner: astra-25. Source baseline: `4d4ef45`; kernel v0.2.

## Clauses

Kernel §§6.1, 7.3; companion §4 and S03/S13/S24/S27. `premise_quality`
survives every rendering, but its calculation is over the authorized graph.
Non-interference protects disclosed statuses and coverage, not only claim text.

## Minimal separating input

Both stores have the same admitted, real, currently applicable public records:

```text
assertions A and B
admitted root A+
checked sufficient-support rule r: A+ -> B+
query B, same audience/purpose, rule versions, cut semantics and logical budget
```

Store H additionally has root A- hidden from that audience. It is in the SAME
space, with a narrower audience constraint; filtering spaces alone is insufficient.
There is no B- root or rule. The public budget is sufficient for the authorized
graph. Public policy and any pre-admitted availability state are unchanged.

## Two readings and outputs

| Field for B support | Authorized witness, globally computed premise quality | All semantic qualification computed over the authorized graph |
| --- | --- | --- |
| witness in both stores | present | present |
| evaluation in both stores | complete | complete |
| premise_quality without H | clean_path | clean_path |
| premise_quality with H | conflicted_premises_only | clean_path |

The first reading filters proof text after computing a global conflict flag. It
leaks a hidden opposing witness even though B's support bit does not change.
Changing the second response to `not_fully_checked` would still leak H.

## Recommendation and controls

Use the second reading. B opposition remains `not_found` and `complete`; neither
hidden A- nor visible A- automatically derives B-. Handles are compared using a
predeclared normalization that preserves equality relationships and issuance
behavior; a hidden-dependent counter or refusal cannot be normalized away.

Positive disclosure control: explicitly admit A- to the SAME audience, then B
support is still present and its quality becomes `conflicted_premises_only`.
Negative neighbors: revise/erase only H, or put hidden roots ahead of A+ in the
candidate order under the same logical budget. Public quality, completion,
counts, rank, cursor and change semantics must remain unchanged.

## Evidence and limits

This is a separating requirement, not a claimed evaluator failure. It extends
the direct-target hidden-opposition case to the new mandatory quality field.
Package-format vectors and package clauses follow when the grammar lands.
No timing, scheduling or deployment isolation proof is claimed.
