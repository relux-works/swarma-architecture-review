# ASTRA25-07: erasure authority does not authorize hidden closure metadata

Status: R7-031 spec-bug; explicit receipt-context correction released in
`0.2.2-draft` at `7e71765`, behavior independently verified at `a016781`; judge closure pending. Original
`0.2.1-draft` witness at `f31d58f` remains preserved.
Owner: astra-25.

## Clauses

K-API-1 requires receipts to disclose only authorized record refs. K-AUTH-1
separates operation rights from read/use/metadata permission; an erase operation
also requires the policy owner, but that does not expressly grant hidden record
metadata. Kernel 7.1/7.3 and companion 4/6 preserve disclosure constraints through
derivation and permit only approved identifiers in erasure audit receipts.
The original K-ERASE-2 nevertheless said the receipt lists the full fenced record closure,
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


Judge R7-031 (`$JPPhod2ZE3Dm7yPZZY1gOh8KGSHsO6j0Fi33ewipx7o`) confirms the
existing source constraint and wire/profile gap. The accepted correction specified explicit
actor-bound `receipt_context {audience, purpose}` with pre-fence authorization,
including idempotency/revocation controls. Neither the later query nor a union of
unrelated purpose grants may supply that context. The original red pair is
preserved; the migration below follows the released grammar.

## Explicit 0.2.2 migration

Release `7e71765` requires an actor-bound `receipt_context`. All owned erase
fixtures choose `aud:private` / `purpose:read`. This pair adds an A-only private/read
read/use/metadata grant, preserving the intended A-only receipt without granting
D visibility. The authorized control still permits both. All original expected
reports are unchanged except the declared profile version; complete protected
closure and custody purge remain mandatory.

The new [other-purpose control](astra-25-erasure-receipt-metadata-other-purpose.vector.json)
adds private/publish read/use/metadata for all records to the hidden primary.
It still expects only A in the private/read receipt. Matching the actor and space
while ignoring purpose cannot satisfy this neighbor.

Untouched pre-correction runtime at `1828356` fails the primary and purpose
neighbor with the same hidden D ref while passing the authorized control. Exact
reports are `astra23-phase2-022-migration` and `astra22-phase2-022-migration` in the
evidence JSON. Source erase remains explicitly unsupported. Canonical P08 now
also supplies exact replay, changed-context conflict, authorized tombstone refs
and revoked-replay controls; independent correction verification remains pending.

## Independent corrected-runtime verification

Package implementation `a016781` passes the unchanged migrated primary,
authorized and other-purpose traces exactly. The complete owned semantic corpus
is 15 pass / 1 fail (the separate retention case). A fresh canonical run is
57 pass / 0 fail, with eight deployment cases explicitly unsupported. All 18
product/checker controls pass independently, including later-stamp exact replay,
changed context, broadened rights not rewriting the stored receipt, and current
read/use/metadata loss with full state preservation. The owned deployment case
also remains unsupported.

Review confirms filtering occurs before new fencing and does not change the
protected closure/purge set; replay checks the original refs and returns the
original receipt only when currently authorized. Exact evidence entries are
`astra23-phase2-022-receipt-corrected` and
`astra23-canonical-022-receipt-corrected`. Control log:
`.temp/astra25-package-controls-022-01.log`. This verifies the tested semantic
receipt contract; it does not establish physical purge or general side-channel
isolation. Judge owns final R7-031 closure.
