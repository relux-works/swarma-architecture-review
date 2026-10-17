# ASTRA24-08: an exact candidate is not an unambiguous compare-and-set head

Status: both evaluators fail; judge classification requested. Owner: astra-24.
Execution checkout `7e71765`, package `0.2.2-draft`; first valid separating run
was at `1f3180d` on package `0.2.1-draft` with the same semantic expectations.

## Clauses and two readings

Kernel 5.3 requires the current sequence head for `expected_version`; 5.4 keeps
write refusal, ambiguous currentness and signed evidence conflict distinct.
K-REV-1 explicitly says a mismatch or ambiguous head yields `version_conflict`,
committing nothing. K-REV-3 orders canonical decisions by authority receipt
predecessors, not arrival time or numeric version. K-REV-4 forbids any subject
record or dirty marker from the refused write.

The convenient reading checks only the exact target record's memory revision
chain. The required reading first resolves the authorized authoritative slot's
head: selecting one of two incomparable candidates does not remove ambiguity.
This is a proposed implementation defect, not a requested architecture change.

## Minimal separating input

Start from S28: decision d1 has receipt r1; d2/r2 and d3/r3 independently succeed
r1. All records, metadata and the withdrawal are authorized/reviewed, and the
integration supplies the new revision's direct lineage fact. Capture the view,
then request `withdraw(d3)` with `expected_version=d3` under the issuer.

| Observable | Target-chain-only reading | Required slot-head reading |
| --- | --- | --- |
| Initial currentness | ambiguous_current | ambiguous_current |
| Initial signed support/opposition | neither | neither |
| Withdrawal result | revised receipt | version_conflict, retryable |
| Stored record count after attempt | 7 records | 6 records |
| Stored withdrawal revision | present | absent |

The final primary query remains at the original admitted cut. Its exact view
must equal the captured one after handle normalization. The inventory assertion
independently catches a forbidden committed revision; historical-view equality
alone would not prove atomic refusal. Dirty inventory and external effects stay
empty. This fixture does not inspect private idempotency storage directly.

## Positive control

`astra-24-ambiguous-cas-control.vector.json` changes only authority ordering in
the initial state: r3 succeeds r2, which succeeds r1. There is one current head,
d3. The identical authorized withdrawal must now commit its one revision, and
the new-cut view returns d2 as the remaining current candidate. It remains
neither supported nor opposed. Both evaluators pass this complete control,
so unconditional rejection cannot satisfy the pair.

## Execution evidence and limits

On `7e71765`, both evaluators return an accepted revise receipt and retain
`rec:withdraw-candidate` for the ambiguous input. Source comparison reports ten
field/shape differences plus two intended forbidden matches; package comparison
reports eleven differences (its comparator also lists the extra array element)
plus the same two forbidden matches. The capture, historical final query,
currentness ambiguity, and lack of signed opposition otherwise match.

All seven prior fixtures and the new positive control pass both evaluators:
**8 pass / 1 fail / 0 unsupported** in each owned corpus. Expected results were
written before execution and never passed to an evaluator.

- Primary SHA-256: `b7bfc797d0d9307d45ec1ffbabe957610dac89698bba476d868935f30b80a835`.
- Control SHA-256: `ddaff2d030c536d029b1a9aed2b9887e60dcce1be7e96d1904737cfc5ad5012d`.
- Current reports: `.temp/astra22-owned-cases-19.json`, `.temp/astra23-owned-cases-11.json`.
- First valid 0.2.1 reports: `.temp/astra22-owned-cases-18.json`, `.temp/astra23-owned-cases-10.json`.
- Closed grammar, state refs, normalization, exact admitted/refused inventory accounting and intended forbidden-value plants pass `.temp/case-vectors-validate-17.log`.

An initial draft omitted the withdrawal's review allowance, so both evaluators
correctly returned `quarantined`; source17/package09 are setup failures, not
this divergence. A malformed forbidden predicate was also corrected before the
valid runs. The accepted control establishes that the repaired fixture reaches
compare-and-set admission. The 0.2.2 migration changes only profile metadata;
`.temp/astra24-profile-022-migration.json` proves normalized fixture equality.
No protected deployment or general concurrency guarantee is claimed.
