# ASTRA26-01 — importing a publication does not mint representation

Status: submitted for classification; source-contract case, package not yet
available. Seat: astra-26. Baseline: `daf285d` (kernel v0.2).

## Clauses

- Kernel §2: every record has issuer, authenticated submitter, subject and
  perspective; differing submitter/issuer requires checked representation.
  Failed representation refuses, rather than downgrading the request.
- Kernel §8: an imported publication is quarantined until human review and
  attributed to both catalog and original issuer; its class survives derivatives.
- Kernel §§9.1–9.2: a participant imports a publication as a source, and copying
  it cannot increase confidence. §6.1 identifies witnesses by root origin.
- Companion §3: a documentary source supports attribution, not the reported
  proposition itself. An authenticated mirror does not establish source authority.

## Two readings

1. **Original issuer is the imported record's envelope issuer.** The importer
   is its submitter and needs a representation grant from the original issuer.
   Without that grant, even a reviewed public-source import must refuse; an
   implementation that accepts it anyway silently bypasses §2.
2. **The importer issues a report about the publication.** The source's envelope
   identifies the principal responsible for this import, while protected/allowed
   source provenance retains catalog, publisher, original issuer and origin.
   This is an imported report, not a new declaration issued on the author's
   behalf. No representation is invented. A separately authenticated request
   actually claiming to speak as the author still requires representation.

## Minimal separating input

The following is source-level notation, not an invented package fixture format.
All principals and content are synthetic.

```json
{
  "publication": {
    "id": "pub-synthetic-1", "revision": 1,
    "original_issuer": "person-A", "subject": "public-subject-A",
    "statement": {"interest": "botany"},
    "original_admission_class": "self_declaration",
    "catalog": "catalog-C"
  },
  "import": {
    "authenticated_submitter": "reader-B",
    "human_review": "accepted",
    "admission_class": "imported_publication",
    "representation_from_person_A": null
  }
}
```

The operation is source import, not a request by B to revise A's self-description.
Assume ordinary source read/retention admission is satisfied. The human review
accepts storing an attributed report; it grants no representation authority.

## Separating outputs

| Observable | Reading 1 | Reading 2 |
| --- | --- | --- |
| Import result after review | Refused: no representation from A | Admitted imported-publication source issued by B |
| Original attribution | A, if anything is returned | A via C, retained as source provenance |
| New declaration in A's sequence | None | None |
| Authority/semantic support gained | None | None from import or review alone |

Reading 2 must retain the distinction between the importer's report, the
catalog's relay and the original attributed statement through summaries and
publication. It must not solve the problem by discarding the original issuer.

## Recommendation and controls

Recommend reading 2 for ordinary source imports. It exercises §9.1 without
turning public-source copying into an implicit delegation, and preserves the
five-record model. Ask the package to specify the concrete provenance fields
and how the original class survives the transport class; the judge should
decide whether the existing source already determines this encoding.

Nearby negative control: B submits an assertion with `issuer=A` and attempts
to replace A's current interest without representation. That request must
refuse atomically; it must not be rewritten into an observer statement.
Positive control: the same replacement with a checked, applicable representation
reference may proceed subject to the ordinary version and admission checks.
Three catalog copies still have one root origin and three attributed copies.

No evaluator failure is claimed. A package-format vector is pending publication
of the actual closed grammar; this file records the separating behavior first.
