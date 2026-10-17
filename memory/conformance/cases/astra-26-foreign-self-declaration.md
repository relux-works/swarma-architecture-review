# ASTRA26-06 — an organisation's attestation is not the subject's self-declaration

Status: submitted for classification against `0.2.0-draft`, package commit
`cde5754`. Seat: astra-26. Proposed classification: spec-bug in attribution/domain
closure and P15's chosen record shape. No new kernel primitive is requested.

## Clauses and concrete witness

- Kernel §2 distinguishes an issuer's statement about itself (`subject=issuer`,
  own perspective), a representative relaying that statement, and an observer's
  own hypothesis about someone else. Those distinctions survive publication.
- Kernel §§4 and 11.2 distinguish self-assessed competence from evidence-backed
  assessments. §8's self-declaration class is a statement about the issuer itself.
- Package K-ENV-1 checks that an own perspective names the issuer, but does not
  close what a `self_declaration` statement kind means when subject differs.
- `profiles-synthetic/competence.json` fixes `statement_kind=self_declaration`.
  Its README describes self-assessment, not another issuer's assessment.
- New P15 nevertheless calls both records organisation attestations and sets
  `subject=subj:h1`, `issuer=principal:organisation`, own perspective of the
  organisation, `admission_class=machine_observation` and
  `statement_kind=self_declaration`. The output repeats that statement kind.

The organisation and the described subject are distinct principals in this
synthetic scenario. This is not a claim inferred from identifier spelling. No
representation grants the organisation the right to issue the subject's own
statement; it owns its separate attestation sequence.

## Two readings and separating outputs

1. **Self-declaration means any issuer's own utterance.** P15's organisation
   statement about another subject is accepted under the self-assessment schema.
   The same output kind covers self-description and third-party evaluation.
2. **Self-declaration is about the issuer itself.** The organisation's distinct
   evaluation needs an appropriately typed attestation/assessment representation.
   It cannot become a self-declaration merely because the organisation issued it.

[Complete proposed fixture](astra-26-foreign-self-declaration.vector.json): admit
an organisation-issued `competence` self-declaration about `subj:h1`, with valid
actor rights, review, direct lineage and no impersonation. Then admit the same
typed content as the subject's actual own self-declaration.

| Observable | Reading 1 | Recommended reading 2 |
| --- | --- | --- |
| First admission | Success | Typed refusal, proposed `invalid_domain_value` |
| Actual self-declaration control | Success | Success |
| Final admitted assertion inventory | Organisation claim and self claim | Self claim only |
| External effect or foreign-sequence rewrite | None | None |

The rejection is about using the wrong domain/statement kind, not a prohibition
on storing third-party assessments. Correctly typed organisation attestations
must remain possible and under the organisation's own revision authority.

## Recommendation and limits

Keep P15's valuable exclusion controls: before exclusion both attestations appear,
after exclusion one disappears from the card, and the organisation's own view
and record inventory remain intact. Change the attestation representation so it
does not describe another subject's competence as the organisation's self-assessment.
Close the envelope/domain invariant and retain a valid actual-self-declaration
control; do not coerce issuer, subject or perspective to make the fixture pass.

The proposed fixture satisfies the current closed wire grammar and passes the
package's structural/reference/normalization/forbidden checks. Its refusal is a
recommended semantic correction awaiting judge classification, not a claimed
existing evaluator obligation or an observed implementation failure. Initial
snapshots must also satisfy whatever invariant the package closes; P15 currently
provides the direct already-admitted witness.

## Execution observation before classification

The package-only evaluator at `1439219` admits the first proposal under
`0.2.0-draft` at `cde5754`, producing a receipt instead of the proposed
`invalid_domain_value` refusal. Both record references then remain admitted;
the extra admission also advances the transaction cut before the valid control.
The exact report is seat `.temp/r7-astra-26/owned-cases-astra23-03.json`, with
implementation and input hashes. This confirms that the fixture distinguishes
the readings; it does not turn a proposed correction into an established
implementation obligation before judge classification. The other seven owned
fixtures pass that same evaluator and package exactly.
