# ASTRA24-08: an exact candidate is not an unambiguous compare-and-set head

Status: judge-classified R7-040 (source) and R7-041 (package), both implementation bugs.
Package correction independently verified at `53266dd`; source correction
`99b5a85` now also passes the remaining-head continuation. Judge decisions
close both R7-040 and R7-041.
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

## Round 19 source repair and remaining-head continuation

Source `68152c5` passes all four original CAS fixtures and all twelve previously
authored vectors. Two focused native transaction controls pass exact refusal
state/policy/runtime equality, current/challenge behavior, admitted common
successor and replay after head advancement. This evidence verifies the original
failures; it does not establish the next-head boundary below.

`ASTRA24-08-NEXT` extends the unchanged ordered positive control: withdraw
current d3; capture the new-cut view identifying d2 as current; then withdraw
d2 with expected_version=d2. Both writes are separately authorized/reviewed,
with complete direct lineage facts. K-REV-1's current head and K-REV-3's eligible
receipt order require the second write to succeed, leaving d1 current at cut102.
The package evaluator passes this exact sequence.

The source returns d2/current in the intermediate capture but refuses the same
exact candidate as version_conflict. Its head selection still includes withdrawn
d3 and advances to that retired candidate's local revision token. It stores only
the first revision; the expected new cut102 is consequently unavailable. The
report has27 comparison entries including this cascading invalid_time result
and the intended forbidden refusal. These are manifestations of one continuation
failure, not27 defects. The first withdrawal and intermediate read pass exactly.

At checkout `0f59936`, thirteen owned fixtures give **12 pass /1 fail** in
each evaluator, with different failures: source NEXT; package transitive review.
Original four CAS fixture bytes remain unchanged. Source closure is not recommended
until the judge disposes of this continuation, proposed under the same R7-040
head-selection family. The source's previously fixed negative cases remain fixed.

Fixture SHA-256: `8b0c5faeffd07c106fce0babde245b1420ec9951a00a7ba68ee8e4de3589a151`. Exact reports: source23/package15; initial repaired
source corpus: source22; native controls: source-authority-cas-controls01;
structural/normalization/inventory/intended-refusal plant: validate21, all in
seat-local `.temp/`. Existing immutable first failures remain untouched.

## Package 0.2.3 explicit migration

Round 21 migrates this case to `0.2.3-draft` (`23290b3`). Behavioral expected
results and initial states are unchanged. Read-only operations need no storage
context; each of this seat's six revise operations explicitly binds private/read
under its existing actor/space/record retain grant. No grant is inferred from a
later query. `.temp/astra24-profile-023-migration.json` records old/new hashes,
exact operation contexts and normalized equality. Structural and intended
forbidden controls pass log 22. Earlier hashes identify historical profile runs.

## Round 22 source remaining-head correction verified

Source correction `99b5a85` passes all five CAS vectors at checkout `ddc62c6`
on the explicit 0.2.3 fixtures committed in that checkout. NEXT admits both
withdrawals, preserves the intermediate d2/current capture, and returns d1/current
at cut 102. Its exact normalized output, inventory, relations and forbidden-value
checks pass. Current NEXT SHA-256:
`734f230192fe36c8dab4f193b41969094dc5350209e09fa0325afc76a1c149ae`.
No fixture or expected result changed for this verification.

All thirteen owned source vectors pass. Three focused native transaction tests
also pass: next-head continuation; exact records/runtime/policy preservation for
ambiguous and stale refusals, with unique-head/challenge positives; and later
common-successor admission with exact historical receipt replay before CAS.
The implementation now excludes withdrawn authority candidates and returns the
remaining exact receipt-ordered candidate rather than an ordinary revision token.
These controls do not establish arbitrary graph or concurrent-storage safety.

Evidence: `.temp/astra22-owned-cases-26.json` includes exact input and Python
module hashes; `.temp/astra22-authority-cas-controls-02.log` records all three
methods. The initial remaining-head failure `bd75f4f` and first source reports
remain immutable. R7-040 closure is recommended after the judge's own gates;
full retention enforcement and canonical unsupported operations are separate.

Judge decision `$tmfi_3vaCFABPnbEDIekguKbs5okvS5uAK-igNNYZng` closes R7-040 at
`99b5a85` after independent frozen 0.2.2 verification of all five CAS cases,
14 transaction controls and canonical 49/0/8. This seat separately verifies the
explicitly migrated 0.2.3 cases above; the two release claims remain distinct.

## Round 27 profile migration to 0.2.4

Current exact fixtures explicitly name `0.2.4-draft` from release `ef02647`.
Only expected-view `semantic_profile` values changed; initial state, operations,
queries and behavioral expectations are byte-equivalent after that declared
normalization. All twenty owned fixtures pass structural and intended forbidden
controls (log27). `.temp/astra24-profile-024-migration.json` records old/new hashes
and every changed path. Historical hashes and first reports remain unchanged.
