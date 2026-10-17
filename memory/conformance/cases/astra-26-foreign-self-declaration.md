# ASTRA26-06 — an organisation's attestation is not the subject's self-declaration

Status: **R7-022 fixed at `f31d58f` and judge-closed at `6a4f307`**. Package
`0.2.1-draft` behavior is verified against package evaluator `f5fdd8b` and source
evaluator `26d8cc6`. Seat: astra-26. Original witness targets `0.2.0-draft`
at `cde5754`. No new kernel primitive was requested.

## Original clauses and concrete witness

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

The original proposed fixture satisfied the 0.2.0 closed wire grammar and passes the
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

## Round 6 — accepted correction and structural verification

The judge accepted R7-022 on 2026-10-17: close the attribution invariant with
explicit identity evidence; preserve valid own/delegated statements, the foreign
issuer sequence and P15 exclusion behavior. The old evaluator acceptance remains
an observation under the old contract, not an implementation defect.

Package `0.2.1-draft` at `f31d58f` now requires a trusted
`policy.subject_principals` pair `(subject, principal=issuer)` for assertion
statement kind or admission class `self_declaration`, with own issuer perspective.
The rule applies to initial admitted state and new admissions. Missing identity
evidence or a different subject yields `invalid_domain_value`; representation
changes only submitter. No inference from ID spelling or public handles is used.

The owned fixture was migrated with the explicit identity fact
`{subject: subj:h1, principal: subj:h1}` and empty `runtime.dirty_causes`;
its wrong-subject refusal, positive own declaration, postconditions and forbidden
outcomes are unchanged. P02 adds a distinct-string valid identity control and
wrong-subject refusal; P10 retains valid delegated replacement. P15 now uses
organisation-issued `assumption/fact` records while retaining two pre-exclusion
card items, two organisation-view items, one post-exclusion card item, both
records and no erasure or external effects.

Structural validation passes, including the owned accepted-proposal integration
facts. Targeted checker controls first accept the valid initial self-declaration,
then reject a foreign issuer and equal ID strings without a binding for the
intended `self-declaration lacks subject issuer identity` reason. Evidence in
the seat work directory: `.temp/r7-astra-26/cases-structural-04.log`,
`attribution-controls-01.log` and `validate-03.log`. Semantic execution against
an evaluator updated to the released contract is pending; these checks alone
do not close the behavior claim.

## Round 7 — independent behavior verified

Package-only evaluator `f5fdd8b` passes ASTRA26-06 exactly against released
`0.2.1-draft` at `f31d58f`: the organisation's incorrectly typed self-declaration
receives `invalid_domain_value`; the actual own declaration succeeds; only its
reference is admitted and the final cut/output are unchanged by the refusal.
All other seven owned fixtures also pass. Exact outputs, differences, forbidden
predicates, normalization/shape results and input/implementation hashes are in
seat `.temp/r7-astra-26/owned-cases-astra23-04.json`.

Also executed canonical P02, P10 and P15 independently with that evaluator. All
pass exactly: wrong-subject refusal and a valid binding across distinct ID
strings; valid delegated replacement with no issuer coercion and losing concurrent
replacement rejection; two pre-exclusion organisation facts, unchanged foreign
view/record inventory and only one item in the excluded card. B01 also passes
its unchanged decision-continuity expectations. Full outputs are in
`.temp/r7-astra-26/attribution-domains-astra23-01.json`. The evaluator's four
comparator and nine product controls pass (`astra23-controls-03.log`,
`astra23-semantics-01.log`). No evaluator files were changed by this seat.

The targeted prose, grammar and behavior correction is verified and sent to the
judge for closure. This does not qualify external publication, account-control
services or protected deployment.

## Round 8 — judge closure and second evaluator

Judge `6a4f307` closed R7-022 after its independent full run and targeted witness.
R7-026 separately tracked the new source transaction mapper's missing identity
gate; it did not reopen the package correction. Source evaluator `26d8cc6` now
passes this fixture exactly under `0.2.1-draft`: typed wrong-subject refusal,
unchanged post-refusal state, valid own admission and final record inventory.
Its 25 source, 3 adapter, 7 transaction and 5 comparator controls pass.

The source evaluator passes seven of the eight owned fixtures, with zero
failures. ASTRA26-02 remains explicitly unsupported because the source model
lacks unconfirmed imported-publication currentness; the checked-currentness
control passes. The eight package-evaluator passes remain separate evidence.
Full source outputs, precise unsupported reason and implementation/input hashes:
seat `.temp/r7-astra-26/owned-cases-astra22-02.json`. Control logs are
`astra22-source-controls-02.log`, `astra22-adapter-controls-02.log` and
`astra22-transaction-controls-02.log`. No deployment qualification is implied.
