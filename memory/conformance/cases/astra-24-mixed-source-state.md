# ASTRA24-03: source state inside a mixed AND witness

Status: judge-confirmed package clarification R7-014 and source implementation bug R7-015.
Reviewed release: `0.1.0-draft` at `0ef608a`. Owner: astra-24.

## Clauses

Kernel §6.1 says `source_state` distinguishes currently resolvable sources,
prior immutable assessments, and an independent sufficient attestation.
Companion §6 preserves the exact scope of a surviving assessment. Package
K-EVAL-5 prefers a fully resolvable path, then an independent-attestation path,
then prior-assessment-only; K-RULE-2 makes every premise of an AND rule necessary.
K-REC-2/3 prevent evidence for one exact target from certifying another directly.

The package gives an order across paths but does not explicitly define a mixed
AND path's source state. S32 exercises the three root cases separately.

## Minimal separating input

```text
Source S is erased; its authorized structural header survives.
A+ has a separately admitted independent attestation, source_requirement=independent.
B+ has only a retained semantic assessment over S, source_requirement=retained.
A+ AND B+ -> C+ is a valid checked sufficient-support rule.
No other C+ path, no opposing witnesses, no cutoffs.
```

Both assessments are separately retained and have no content lineage requiring
their deletion. This case concerns how surviving evidence is presented, not an
erasure-closure exception. All records and metadata are authorized.

## Two readings and outputs

| Field for C support | A: prefer any independent root encountered | B: preserve every required premise's limitation |
| --- | --- | --- |
| witness | present | present |
| evaluation | complete | complete |
| premise_quality | clean_path | clean_path |
| source_state | independent_attestation | prior_assessment_only |

Reading A applies the advertised preference to the union of root states.
Reading B first evaluates each complete AND path, then chooses between alternative
paths. C still requires B's retained assessment; A's independent attestation is
not a sufficient independent attestation of C.

## Recommendation

Use B. Specify within-path combination explicitly, separately from alternative
path preference: an essential prior-only premise prevents that entire path from
being described as fully resolvable or independently attested. If another
complete sufficient path is fully resolvable, that alternative may win under
K-EVAL-5. The kernel need not add a new record, state or authority.

If the judge finds the source itself leaves this combination undecided, retain
it as an owner question rather than silently adopting this fixture's proposal.
The accompanying expected output is the proposed B reading, not a settled new
normative rule authored by this seat.

## Concrete vector and controls

`astra-24-mixed-source-state.vector.json` uses A=`rec:a`, B=`rec:b`, C=`rec:c`,
S=`rec:s`. A capture queries the two root claims directly: A must be
`independent_attestation`, B `prior_assessment_only`. The final query covers
only their AND conclusion. It preserves support and qualifications, requires
`prior_assessment_only`, and forbids either upgrading that state or losing the
witness. Source refs retain S as provenance; no erased content is reconstructed.
The opposing channel has no source directly associated with exact C and uses
K-EVAL-5's vacuous `resolvable_now`, not a verified-source claim.

The complete JSON passes the package's closed-schema, reference, normalization
and forbidden-predicate checks. Planting the stronger state is detected by its
intended forbidden predicate. Evidence: seat-local
`.temp/case-vectors-validate-02.log`. No evaluator or protected-deployment run is
claimed; this is a precise request to close a mixed-path interpretation.

## Observed execution and stronger controls — round 4

The committed source evaluator at `b3c7ac9` independently reproduced the
proposed output disagreement (its own ASTRA22-04). The seat-local rerun at
`3045117` used the unchanged frozen core SHA-256
`cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
Executor inputs were only snapshot, operations, query and package version; the
expected report was supplied only to the comparison harness.

The exact new distinguishing field is:

- `$.result.items[0].support.source_state`: proposed expected
  `prior_assessment_only`; actual `independent_attestation`. Its forbidden
  predicate is triggered as well.

Other differences are already-covered families: two direct-root opposite
channels return `resolvable_now` instead of `prior_assessment_only` (R7-012),
and derived `source_refs` omit `rec:s` (an extension of R7-013). Do not classify
these again as new source-state-combination defects.

The fixture now also captures a later valid-time query with an independently
sufficient current root for C. Its `source_state` must be `resolvable_now`
even though the mixed AND path remains. This protects the OR preference from
a repair that simply chooses the weakest state across all roots. The frozen
implementation already agrees on that control's state; its source-ref output
still has the known omission. The root has no required external source, so its
resolution state is the explicitly permitted vacuous current state.

Current fixture SHA-256:
`4d674467390498c37be9bc699e263c40776a7a8975603a9fee09b8d96caf25ca`.
Evidence: immutable source-owner `impl-astra-22/runs/case-first.json` for the
original fixture, and seat-local `.temp/astra22-owned-cases-01.json` through
`-03.json` plus `.temp/case-vectors-validate-04.log`. The judge classified the AND-state gap as R7-014 (`spec-bug`, editor) and
the reproduced source-core behavior as R7-015 (`impl-bug`, astra-22). Exact
target and necessary-premise scope resolve the choice without an owner question.
Expected outputs have not been changed to match the implementation. No deployment behavior was exercised.
