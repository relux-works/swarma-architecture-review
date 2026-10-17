# ASTRA24-08: an exact candidate is not an unambiguous compare-and-set head

Status: judge-classified R7-040 (source) and R7-041 (package), both implementation bugs.
Package correction independently verified at `53266dd`; source correction pending.
Owner: astra-24.
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

## Round 16 failure-class neighbors

Two additional fixtures preserve the original primary and positive-control bytes.
`ASTRA24-08-STALE` uses the same ordered r1 < r2 < r3 state as the valid control,
but requests withdrawal of historical d2 with expected_version=d2. K-REV-1
requires the actual current head, d3; both implementations wrongly accept this
write too. It has the same accepted-receipt and extra-record forbidden effects.
This rules out a repair that merely rejects the count of incomparable heads
while continuing to accept any target's local revision chain.

`ASTRA24-08-CHALLENGE` keeps the original ambiguous state but changes the
relation to challenge, supplies the already historical d1 as expected_version,
and expects an admitted challenge receipt. K-REV-1 explicitly exempts challenge
from CAS. Both evaluators pass: currentness stays ambiguous, neither signed
witness appears, global dirtiness remains empty, and only the attributed
challenge revision is added. Blanket refusal of all writes in an ambiguous slot
would violate this control.

At checkout `b3aeed2`, source20 and package12 reports independently show
**9 pass / 2 fail / 0 unsupported** over the eleven owned fixtures. The two
failures are the original ambiguity and the new historical-head neighbor,
proposed as one head-selection failure family. No duplicate ledger item is
requested. Structural/normalization/inventory/forbidden controls pass log18.

- Stale fixture SHA-256: `6a5ad0906e0ea87d2e5ef817079af03cb972aff54f2ef4bfa23cb7874c2f93cd`.
- Challenge fixture SHA-256: `b2aac30f0c3aba2dd8f4aa071b96cecafec0c5e5b0e4098a7237a7119e130548`.

These tests cover exact authorized candidates and authority order, not hidden
head disclosure or arbitrary authority graphs. Scoped authorization and receipt
ordering must still precede any externally visible conclusion.

Judge decision `$jWF7PS9bJWLBKtoGF2OqBiJIlvcfYJB7WzuI6j5fxPw`, persisted
in round18 at `1cdcb36`, accepts the exact primary/control separation as
R7-040 source and R7-041 package. No specification change or owner decision
is required. Historical-head and challenge neighbors were sent for consolidation
under the same rows. Exact corrected-head verification remains pending.

## Round 18 package correction verified

Package correction `53266dd` passes all four unchanged ASTRA24-08 fixtures:
ambiguous and historical candidates refuse exactly; unique current-head
withdrawal and challenge remain admissible. All prior seven cases pass, while
ASTRA24-09 still has its separate missing transitive review reference. Current
package owned result: **11 pass / 1 fail**, no unsupported input.

The focused native `Semantics.test_authority_slot_cas` also passes. Its full
state and dirty-since equality assertions establish records/cuts/dirty/idempotency
atomicity for both refusals. Controls preserve reversed arrival storage order,
a later admitted unique authority ordering, exact later-stamp replay before CAS,
changed-intent conflict without mutation, and withdrawal of the next remaining
head. Shared receipt-order selection supplies the unique non-withdrawn slot head.
This verifies the submitted failure class, not arbitrary authority graph safety.

Evidence: `.temp/astra23-owned-cases-14.json` and
`.temp/astra23-authority-cas-controls-01.log`. Fixture hashes remain unchanged;
first package failure `e525612` remains immutable. R7-041 is behaviorally verified
by this seat; formal judge closure and source R7-040 correction are separate.
