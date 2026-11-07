# ASTRA25-07: erasure authority does not authorize hidden closure metadata

Status: R7-031 spec-bug; explicit receipt-context correction released in
`0.2.2-draft` at `7e71765`, behavior independently verified at `a016781` and closed by judge. Original
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


Judge R7-031 confirms the
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

The judge's closure independently
reproduces all canonical results, all 18 controls and all three owned receipt
traces. R7-031 is fixed at package `7e71765` with runtime `a016781`; first red
evidence remains immutable.

## Changed-context priority boundary (native observations)

Source seat's signed `0529814` / ASTRA22-09 supplies a valid S20-derived input:
first private/read erase stores A/D refs; the same key changes receipt purpose
to an ungranted purpose; a fresh key uses that same changed context. This seat
independently validates and reproduces the exact input against unchanged source
`dbf4892` and package `23b4d74`. A neighboring changed audience behaves alike.

| Observation | Source | Package |
| --- | --- | --- |
| Exact authorized replay | Same original receipt, unchanged state | Same |
| Same key, ungranted changed purpose | not_authorized | idempotency_conflict |
| Same key, ungranted changed audience | not_authorized | idempotency_conflict |
| Fresh key, same ungranted purpose | Complete erase, empty refs | Same |
| Foreign actor with changed context | not_authorized, unchanged state | Same |
| Exact replay after read revocation | not_authorized, unchanged state | Same |

Both changed-context refusals preserve the full inspected state; the fresh-key
success and later denied replay also preserve the original stored receipt.
Evidence entries are `astra22-erase-context-priority-first` and
`astra23-erase-context-priority-first` in the aggregate. They contain operation
bytes, module hashes, original signed input hash, state-component comparisons
and complete snapshot hashes. These native observations are outside exact vector
denominators; no expected fixture has been changed.

Recommend classifying the source order as an implementation bug under the
existing K-API-1/K-ERASE-2 contract: current erase authority is still valid, and
lack of metadata permission is not itself grounds to refuse a fresh erase.
Changing receipt_context is expressly a different intent. Original-ref metadata
permission therefore gates identical replay, after a changed intent has already
been identified as a conflict. This is a scoped reading of erase receipts;
it does not move live retention authorization behind admission replay/conflict.
Judge classification remains pending for this publication. R7-031's original
metadata-disclosure closure remains intact.

## R7-057 classification and exact regression pair

The judge's adjudication classifies the
source behavior as R7-057 implementation bug and authorizes exact supplementary
fixtures. The expected refusal is `idempotency_conflict`, `retryable: false`,
after current erase operation authority. Exact replay still reauthorizes every
original ref and cannot rewrite its receipt. No package/source design change is
required; the original R7-031 closure remains valid.

New [changed-purpose](astra-25-erasure-receipt-metadata-changed-purpose.vector.json)
and [changed-audience](astra-25-erasure-receipt-metadata-changed-audience.vector.json)
fixtures each pair the required conflict with original complete erase, identical
later replay and identical changed-context fresh-key success with empty refs.
They reuse the original signed input and S20's independently specified protected
closure/custody postconditions. Handle normalization preserves exact replay
identity and requires fresh receipt/view handles to differ.

All 29 owned fixtures pass closed structure, references, integration facts and
normalization/forbidden checks, including two bounded checker plants. On source
`87beb46`, both new fixtures fail only `operation_results[2].code`: actual
not_authorized versus expected idempotency_conflict. All 26 old semantic fixtures
still pass. Unchanged package `23b4d74` passes all 28 semantic fixtures, including
both new traces. The owned deployment fixture remains unsupported. Exact first
runs are `astra22-phase2-025-erase-conflict-first` and
`astra23-phase2-025-erase-conflict-control`; new uncommitted fixture bytes at
execution are explicitly identified by input hashes, never mislabeled as a
previous committed vector set. Native first evidence remains immutable.

## Independent R7-057 correction verification

Source `946cbd8` now passes both unchanged exact fixtures and all 28 owned
semantic fixtures. The unchanged independent native harness reproduces the
original seven-operation probe with both changed purpose/audience conflicts
mapped exactly to idempotency_conflict/false and no state change. Exact replay,
current read-revoked replay, foreign actor and fresh empty-ref success retain
the original receipt guarantees. Eleven source native erasure groups pass,
including the three added authorization/replay groups; canonical remains 57/57.
All current Python modules were byte-compared with the signed correction.

Runs `astra22-phase2-025-erase-conflict-corrected`,
`astra22-erase-context-priority-corrected`,
`astra22-canonical-025-erase-priority-corrected` and
`astra22-native-erasure-025-corrected` retain the review evidence. All first
failures and fixture bytes remain unchanged. Recommend judge closure of R7-057;
ASTRA25-12 restore obligations remain a separate package finding.

The judge's decision, signed e3d44df,
closes R7-057 at946cbd8 after full exact/native reproduction. First wrong-code
observations and both author-owned exact inputs remain unchanged.
