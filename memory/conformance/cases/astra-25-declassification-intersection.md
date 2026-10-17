# ASTRA25-02: retained declassification evidence is not a current joint release

Status: R7-006 spec-bug; 0.2.0 candidate package fix verified structurally,
independent current-version execution pending.
Owner: astra-25. Source baseline: `4d4ef45`; kernel v0.2.

## Clauses

Kernel §§7.1–7.2, 6.4 and 9.3; P05/P06/P11/P13. Derived content inherits all
input constraints. Each policy owner lifts only its own constraint. A pinned
`declassification` assessment records a decision; it neither owns that authority
nor replaces the applicability check before each new disclosure.

## Minimal separating input

```text
A@1: synthetic restricted input controlled by owner OA
B@1: synthetic restricted input controlled by owner OB
T@1(A@1, B@1) -> D@1, output schema summary@1
Complete adapter-controlled lineage of D: [A@1, B@1]
Release target: audience X, purpose P
EA: valid assessment of OA's release decision for that exact tuple
EB: retained assessment of OB's earlier release decision for that exact tuple
Current policy: OA's decision applies; OB's decision has been revoked
Operation: new disclosure of D to X for P
```

The output is a synthetic assertion, not real personal information. No other
decision or independently admitted release exists. The retained EA/EB assessment
bytes and their historical signatures are unchanged.

## Two readings and outputs

| Observation | Stored positive assessments are standing permission | Every owner's current decision must still apply |
| --- | --- | --- |
| New D disclosure | allowed | refused; D payload absent |
| Historical EB check result | pass | pass as historical evidence only |
| B's constraint | assumed lifted forever | still effective |

The first reading treats EB's immutable historical result as live authorization.
Both readings know the complete lineage, so no missing-lineage assumption is
needed to separate them. The disclosure response must not expose protected owner
or input identifiers merely to explain refusal.

## Recommendation and controls

Use current decisions of every constrained owner, over integration-established
lineage. Positive control: both exact decisions currently apply, so this release
is allowed while A/B raw bytes and protected lineage remain hidden. Negative
neighbors: remove EB entirely; change only audience, purpose, input version,
transformation version or output-schema version; substitute a model
`semantic_review` for EB. None grants the missing exact decision.

The case does not require memory to revoke grants or send anything. The component
performing disclosure applies current policy; memory records evidence and change.

## Evidence and limits

No package/evaluator failure is claimed before package inspection. The positive
and negative controls establish a semantic authorization contract. Real policy
authenticity, provider forwarding and sink enforcement require separate
deployment qualification. Package-format JSON will be added where representable.

## Package inspection

At `0ef608a`, package `0.1.0-draft` K-DISC-2 and the closed fixture encode one
`policy.owner`, one `declassify.assessment` and one
`disclosure.declassification` reference. They do not encode distinct input
constraint owners and separately live release decisions, so this exact pair
cannot be faithfully represented without inventing fields outside the schema.

The judge accepted the source requirement in
`$4tk3CWGCfuRe5mxDVNYGve3pdKReoFKZXRFdyGARQ7A`. The editor confirmed the gap and
the planned v0.2 ownership/assessment-set/current-applicability representation in
`$-p8jSWR4uqaSgUnAwwQjGZPMO2viay9CaW-5ayOtGaA`. Executable pair construction
waits for that concrete shape. No synthetic one-owner substitute is claimed to
exercise the multi-owner requirement, and no evaluator failure is asserted.

## Candidate fix verification: 0.2.0-draft

At `cde5754`, constraint ownership, the exact declassification assessment set,
current owner decisions and revocation are represented explicitly. The candidate
closes the representation gap: a retained assessment cannot substitute for a
revoked owner's live decision. The package P05 trace supplies the live/revoked
pair; its expected result is grounded in the source requirement above.

[`astra-25-declassification-intersection.vector.json`](astra-25-declassification-intersection.vector.json)
adds a wrong-owner revocation neighbor. That operation must return `not_authorized`
and leave the released view unchanged; the correct owner then revokes, and a new
delivery must return `disclosure_revoked` with no second delivery effect. It uses
explicit trusted synthetic lineage facts. Their presence does not claim that a
real adapter establishes lineage merely from submitted citations.

The complete trace passes the 0.2.0 closed schemas, state references, normalization
and forbidden predicates. This verifies the candidate's representation and
expected contract; independent current-version behavior remains to be run.
Authenticity and real sink enforcement remain deployment obligations.
