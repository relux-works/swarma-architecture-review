# ASTRA25-02: retained declassification evidence is not a current joint release

Status: R7-006 spec-bug; 0.2.0 candidate package fix verified structurally,
independent package behavior verified. Source first declassification mapping
had a separate digest-framing defect R7-050, now fixed at `8a42945`.
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
expected contract.
Authenticity and real sink enforcement remain deployment obligations.

Independent execution against astra-23 at `1439219`, package `cde5754`, passes
this entire semantic trace exactly, including the wrong-owner no-effect control,
correct-owner revocation, refusal of another delivery and unchanged effect count.
Run `astra23-v0.2` in `astra-25-evaluator-results.json` records code/input hashes.
The source adapter explicitly reports declassification unsupported. This is
behavior evidence for R7-006; real authorization enforcement remains unqualified.

## Phase-2 source expansion: digest framing in both directions

Source `36983de` first maps declassification. The unchanged valid joint-release
trace now returns `declassification_invalid` for the correct output digest.
K-JSON-2 defines the digest over `bounded-evidence:cjson-v1` followed by a NUL
byte and the canonical UTF-8 body; hashing the body alone is a different value.
An independent Python standard-library calculation matches all original owner
and assessment pins only with that framing:

- Framed: `5de83fb8e3155c49b882fb716b571a54038bee18f06cc1989900cb49b16c2a3b`.
- Unframed: `c47edea8d46ce4fd367b430ade8f53aa72a2b7e44a8902193cd87ab939a4a63c`.

[`ASTRA25-02-DIGEST`](astra-25-declassification-intersection-unframed-digest.vector.json)
is the reverse negative control: one joint release, with both trusted owner
and assessment pins consistently replaced by the unframed digest. It must
return `declassification_invalid`, retain exactly the original two records,
and produce no release receipt or external effect. It remains closed-shape
valid; invalid semantic digest pins are the condition being tested.

At source `36983de`, that negative instead returns a declassified receipt and
commits the output plus two assessment records, leaving five records. The
existing positive falsely refuses. Package `4af0360` passes both directions.
The whole owned corpus is source 9 pass / 2 fail / 8 unsupported and package
19 pass / 0 fail / 0 unsupported, plus one deployment fixture unsupported each.
First complete reports, code/input hashes and the independent framing oracle
are preserved under `astra22-phase2-release-digest-first`,
`astra23-phase2-release-digest-control` and `independent-release-digest-oracle`
in `astra-25-evaluator-results.json`. No existing expected report was edited.
This is a source implementation mapping defect, separate from the already
closed R7-006 representation issue. Judge event
`$Jxqff_h8h6pJHraJVkiriHrvMIYcTlLKLCO1QAjUMuI` classifies R7-050, owner astra-22.

## R7-050 correction verification

Judge event `$eKvZRGBlqzKr6xMsLkCJYW-knzBYjX56FZRIIFPlYHY` closes R7-050 at
`8a42945`. This seat independently reran both owned directions and canonical P05
at descendant `4772258`; `releases.py` is unchanged from that fix. All pass.
The nine native release control groups also pass, including ASCII and non-ASCII
framed positives and raw negatives, exact owner/pin checks, current revocation,
immutable captured views, replay and unchanged full state on rejection.

These reruns use released `0.2.4-draft` (`ef02647`). Every owned fixture changed
only semantic_profile; all other JSON fields were mechanically checked identical.
No original oracle or first-failure run was replaced. Evidence runs are
`astra22-phase2-024-release-corrected`, `astra23-phase2-024-owned`, and
`astra22-release-controls-024-corrected`. The release controls' deadline-label
inheritance does not prove admission rejects expiry; ASTRA25-11 remains separate.
