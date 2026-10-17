# ASTRA24-10: a canonical receipt must also succeed the replaced receipt

Status: new separating case; judge classification and exact refusal code pending.
Owner: astra-24. Package `0.2.3-draft` at `23290b3`; first execution checkout
`d077064`. Both evaluators accept the forbidden replacement variants below.
No architecture change is proposed.

## Contract and competing readings

K-REV-3 requires an authoritative replacement's new receipt to succeed its prior
receipt. Canonical status and issuer identity alone establish a receipted event,
not its precedence over the event being replaced. K-REV-1 requires an exact
current head and atomic immutable replacement. Kernel section 5.3 forbids memory
arrival or revision order from overriding the authority's own order.

The convenient reading checks the current target and the new receipt's canonical
status independently, then accepts any such replacement. The required reading
also checks a strict predecessor path from the new receipt to the old receipt
before storing either proposed record. A memory replacement cannot manufacture
an authority edge. Incomparable canonical events remain separately importable
through plain admission; that exception does not authorize a replacement.

## Minimal separating input

Start from canonical B01 without changing actor, grants, review allowances,
lineage facts, retention context, current head, replacement values or CAS token.
There is one admitted decision d1/r1, an admitted canonical receipt r2, and one
registered dependent. The operation replaces d1 with d2/r2.

- Ordered positive: retain `r2.predecessors = [r1]`; replacement must succeed.
- Incomparable negative: change only `r2.predecessors = []`; replacement must
  refuse atomically because r2 does not succeed r1.
- Reused-receipt negative: keep the original receipt graph but cite r1 in both
  proposed replacement and revision; a receipt does not strictly succeed itself.

The complete input triples are in
[astra-24-authority-succession.input.json](astra-24-authority-succession.input.json).
Their input bundle SHA-256 is
`5dcc51600aaed1a2253c9c8ebbde951556521ccea982a55fa3f60d055965ecd4`.
Closed input grammar and initial-state reference checks pass for all three.
These are contract probes, not falsely reported exact-output vector passes.

## Observed results

Both independent evaluators accept all three variants at `d077064`:

| Observable | Ordered positive | Both forbidden variants | Required negative invariant |
| --- | --- | --- | --- |
| Operation result | revised receipt | revised receipt | typed refusal |
| Stored records | 7 records | 7 records | 5 records |
| Memory cut | 102 | 102 | 100 |
| Dirty dependent | present | present | absent |
| Stored idempotency entries | 1 entry | 1 entry | 0 entries |

The negative probes therefore reach admission and commit observable forbidden
state; they are not parser/setup failures. Full operation results, inventories,
state-equality checks, input hash and every evaluator module hash are preserved
in [astra-24-authority-succession.first.json](astra-24-authority-succession.first.json).
The ordered positive prevents an unconditional rejection from satisfying this
case. No query after an invalid new cut is used as the failure witness.

## Refusal mapping requiring adjudication

The rejection invariant is explicit. Its exact closed wire code is not:
K-REF-1 describes `authority_receipt_required` as a missing canonical receipt,
whereas these canonical receipts exist but lack required succession.
`version_conflict` is a current-head mismatch, which is absent here.
`invalid_reference` and `invalid_domain_value` describe other broad conditions.

Recommend the same atomic refusal for unrelated and reused receipts, with
`authority_receipt_required` if the judge/editor confirm that a required
qualifying successor receipt is considered missing. Do not present that choice
as already normative. Request a classification of both accepted-write failures
and the code mapping; then add exact package-format vectors with the adjudicated
code. This is a narrow package-contract clarification, not an owner product or
architecture question. Existing CAS head-selection fixes remain separately valid.
