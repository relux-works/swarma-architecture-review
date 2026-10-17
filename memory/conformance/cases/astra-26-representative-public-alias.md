# ASTRA26-03 — where is a representative's public alias admitted?

Status: judge-classified **spec-bug R7-010** against `0.1.0-draft` at `0ef608a`;
fix owner astra-21. Seat: astra-26. No owner architecture decision is needed.

## Clauses and gap

- Kernel §2 requires self-declaration, representation and observation to remain
  distinguishable through publication. §9.4 requires audience-specific handles.
- Package K-DISC-4 maps the subject and matching issuer/submitter/perspective
  identities to its audience handle. It also requires an admitted public alias
  for every other disclosed principal and refuses when no alias exists.
- The closed fixture policy has `handles`, whose rows contain subject, space,
  audience and handle. It has no distinct alias field. Neither K-DISC-4 nor
  another normative clause explicitly says that a principal's row in `handles`
  supplies the "other principal" alias.
- Existing P09 only publishes self-submitted assertions: all identity fields
  equal the subject. It therefore cannot detect this missing interpretation.

## Two readings and minimal separating input

1. A row whose subject equals the representative principal is its admitted
   alias; the same audience-handle mapping resolves every disclosed principal.
2. `handles` maps record subjects only. A public alias for a distinct principal
   requires some separate admitted fact, which the closed policy cannot encode.
   Publication therefore refuses even when a representative handle row exists.

The complete fixture is
[astra-26-representative-public-alias.vector.json](astra-26-representative-public-alias.vector.json).
Its distinguishing subset is:

```json
{
  "record": {
    "subject": "subj:h1", "issuer": "subj:h1",
    "submitter": "principal:representative",
    "representation_ref": {
      "id": "delegation:alias", "version": 1, "checked": true
    }
  },
  "handles": [
    {"subject": "subj:h1", "space": "space:main", "audience": "aud:public", "handle": "subj:public-a"},
    {"subject": "principal:representative", "space": "space:main", "audience": "aud:public", "handle": "subj:public-representative"}
  ]
}
```

Both representation and ordinary disclosure rights are valid. The output is an
audience projection of a synthetic self-declaration; no protected id is an
admitted public identity.

| Output | Reading 1 | Reading 2 |
| --- | --- | --- |
| Response | View | `not_authorized` |
| Subject and issuer | `subj:public-a` | No item |
| Submitter | `subj:public-representative` | No item |
| Internal representative id | Omitted | Omitted |
| Representation ref | Redacted | No item |

## Recommendation and controls

Recommend explicitly defining `policy.handles` as the mapping for every disclosed
principal, with exact subject/principal, space and audience lookup. This uses the
existing grammar. Preserve distinct issuer/submitter identity; do not repair the
gap by relabeling the representative as the subject or leaking its internal id.
The [negative control](astra-26-representative-public-alias-missing.vector.json)
removes only the representative's row and must refuse
`not_authorized`; invalid representation still refuses at admission under P02.

The proposed success fixture passes the package's structural validator, reference
checks, normalization and forbidden-predicate checks. This is not evidence that
an independent evaluator has implemented either reading. The expected success
is the recommended closure; judge classification and evaluator execution remain
pending. Local structural evidence: `.temp/r7-astra-26/cases-structural-01.log`
in the seat work directory. Judge decision of 2026-10-17 03:46:35Z accepted this
exact lookup clarification and both controls. The first astra-22 adapter reports
both fixtures unsupported because it has no full audience redaction/alias output;
this is not execution evidence for the proposed fix.

Package `0.2.0-draft` at `cde5754` now explicitly defines that exact mapping in
K-DISC-4, including distinct-principal aliases and missing-alias refusal. The
prose correction is verified. Both controls passed the independent package-only
evaluator's first code at `0008dc3` against the original `0.1.0` grammar. Their
current copies are migrated to `0.2.0` and structurally validate. The updated
package-only evaluator at `1439219` now passes both under package `cde5754`,
including exact response fields, closed response schemas, forbidden predicates
and handle equality/distinctness. Evidence:
`.temp/r7-astra-26/owned-cases-astra23-03.json`, with implementation/input hashes.
The case's prose and targeted behavior corrections are verified; ledger closure
remains the judge's responsibility.
