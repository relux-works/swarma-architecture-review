# ASTRA25-07: erasure authority does not authorize hidden closure metadata

Status: phase-2 package-clause conflict and observed receipt disclosure;
submitted for judge classification. Package `0.2.1-draft` at `f31d58f`.
Owner: astra-25.

## Clauses

K-API-1 requires receipts to disclose only authorized record refs. K-AUTH-1
separates operation rights from read/use/metadata permission; an erase operation
also requires the policy owner, but that does not expressly grant hidden record
metadata. Kernel 7.1/7.3 and companion 4/6 preserve disclosure constraints through
derivation and permit only approved identifiers in erasure audit receipts.
K-ERASE-2 nevertheless says the receipt lists the full fenced record closure,
without qualifying this list by the recipient's metadata authority.

## Minimal separating input

```text
Same space, admitted public A and private summary D whose content lineage is A.
Caller is policy.owner, with erase authority.
Public grants: read/use/metadata for A only.
Private grants: erase only; no read, no use, metadata=false.
Both controlled custody sinks are reachable and named in the request boundary.
Operation: erase exact A; no reference to D appears in the request.
```

The request names the two approved custody labels, not D's internal record id.
Neither ordinary query rights nor policy ownership imply a read grant to D.
Erasure must still close A and D and purge their controlled custody. This case
does not ask the operation to skip hidden derivatives or weaken closure.

| Observation | Unqualified full-closure receipt | Recipient-authorized receipt |
| --- | --- | --- |
| Receipt outcome/status | purged / purged_within_boundary | same |
| Public receipt refs | A, D | A |
| Protected erased_refs | A, D | A, D |
| Controlled custody after operation | empty | empty |
| Later public query | no erased payload | no erased payload |

Recommend the authorized receipt. The protected closure may retain D while its
id is absent from the public operation result. A separate explicit metadata grant
can authorize the full list. If operation receipts need an audience/purpose
binding beyond the existing actor, that boundary needs an explicit contract;
erase authority alone must not silently supply it.

## Exact fixtures and controls

[`astra-25-erasure-receipt-metadata.vector.json`](astra-25-erasure-receipt-metadata.vector.json)
expects the complete protected erasure and only A in the receipt. The positive
[`authorized-control`](astra-25-erasure-receipt-metadata-authorized-control.vector.json)
changes only the private grants to include read/use with metadata=true and expects
A plus D. Both retain the exact complete purge outcome and custody dispositions.
The hidden record is already admitted; no questionable admission is needed.

All eleven owned fixtures pass closed structure, references, normalization and
forbidden checks (`.temp/astra25-vector-structure-08.log`). Untouched package
evaluator `f5fdd8b` (latest report/control revision `8b9baf3`) passes the authorized
control and fails the hidden case at `/operation_results/0/refs/length` and the
extra `/operation_results/0/refs/1`, disclosing `rec:summary`. The explicit
forbidden predicate catches that same disclosure. The outcome, protected closure,
custody and empty final view otherwise match.

Exact input/code hashes, full actual result and field differences are in
[`astra-25-evaluator-results.json`](astra-25-evaluator-results.json), run
`astra23-phase2-erasure-receipt`. The source erase implementation is part of the
phase-2 coverage work; no dual execution claim is made. This is semantic metadata
disclosure evidence, not proof of actual storage purge or timing isolation.
