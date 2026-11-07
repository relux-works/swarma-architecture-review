# ASTRA26-09 — partial current-version checks do not certify every import

Status: judge-classified **R7-044 impl-bug**, owner astra-23; fixed at `f6c339d`, independently verified by this seat and the judge. Package `0.2.2-draft` at
`7e71765`; source evaluator `e38c37c`; package evaluator `a016781`.
No canonical fixture or evaluator is edited.

## Clauses and competing readings

K-PUB-2 requires an admitted current-version check for an imported publication;
without it the item is last_received. Its association is an exact authorized
assessment/source reference. K-DISC-3 assigns one origin to copies, preventing
independence amplification; it does not grant one copy's check to another
object or revision. Kernel section 9.2 permits only received-state knowledge
without the issuer current-version check.

1. **Check only present import facts.** If at least one associated publication
   has a current fact and every present fact is current, label the item current.
   An associated publication with no fact is silently skipped.
2. **Check every associated publication.** A missing fact for any of the exact
   associated publication sources is unconfirmed, just as an explicit
   unverified fact is. The item is last_received until every source is confirmed.

Recommend reading 2. Exact source references and provenance must survive the
origin deduplication used for evidence counting. No new source authority,
network operation or architecture is required.

## Minimal witness and controls

The [primary fixture](astra-26-import-check-coverage.vector.json) retains the
three P07 publication copies and their exact targeted assessments. They share
one root origin, but have distinct source objects and catalogs. The horizon is
fresh. Current checks exist for copy1 and copy2; only copy3's import fact is
absent. Expected item and view currentness are last_received. Support remains
present, with one independent root, unchanged evidence and all three authorized
source references; opposition stays not_found. There is no write or external
side effect.

The [unverified neighbor](astra-26-import-check-coverage-unverified.vector.json)
adds only an explicit unverified/null-time fact for copy3. It has exactly the
same expected output as the primary. The [positive control](astra-26-import-check-coverage-control.vector.json)
restores copy3's exact successful check; the complete item becomes current.
A fix that marks all imports last_received therefore cannot satisfy the controls.
Existing ASTRA26-02 and ASTRA26-07 retain missing-all-check, expiry and immutable
capture coverage.

## Independent observations

Both evaluators execute only initial state, operations and query before expected
output comparison. All three fixtures pass closed shape, reference,
normalization and forbidden-output checks.

- Source e38c37c passes the primary and both controls exactly.
- Package a016781 passes the unverified neighbor and the positive control, but
  returns current for the primary at `/result/currentness` and
  `/result/items/0/currentness`. These are the only semantic differences; both
  corresponding forbidden predicates match.
- The unchanged owned corpus plus this triplet totals source 12 pass / 0 fail /
  2 unsupported (delivery), package 13 pass / 1 fail / 0 unsupported.

First observations, full actual reports and implementation/input hashes are
retained in the seat work directory `.temp/r7-astra-26/`:
`owned-cases-astra22-06.json`, `owned-cases-astra23-09.json`, their numbered logs,
and `cases-structural-08.log`. These first failures must remain immutable during
classification and correction. The expected difference is grounded in K-PUB-2;
the agreeing source result is corroboration, not the definition of correctness.
No protected-deployment qualification is claimed.

## Judge disposition

The judge's adjudication independently
reproduces all three fixtures and classifies R7-044 as a package implementation
bug. Exact source checks cannot transfer through origin deduplication. No spec
change or owner question is required. The package implementer's independent
first failure is retained at `08c4b9a` as well as this seat's original evidence.

Correction review must preserve absent/unverified equivalence, the all-checked
positive control, irrelevant hidden-publication non-interference, exact source
references and origin counts, and existing expiry/replacement neighbors.

## Phase 2 round 18 — exact source-check correction verified

Package implementation `f6c339d` passes the unchanged original primary and both
controls against preserved 0.2.2 schemas/inputs, and again against the explicitly
migrated 0.2.3 corpus. The complete owned package run is 14 pass / 1 fail on
each profile; the sole remaining failure is separate actor-binding R7-046.

Reviewed and executed the two targeted product control groups. Removing each
exact source's check separately gives last_received while preserving source
references, support/opposition, origin identity and stored state. An ordinary
non-publication source needs no publication check. A hidden unchecked source
cannot veto the visible current item; the hidden reference is absent and the
independent root count stays one. Expiry/replacement, old capture immutability
and ordinary-source neighbors still pass. No prior expected answer changed.

Evidence in seat `.temp/r7-astra-26/`: `owned-cases-astra23-12.json` (original
0.2.2), `owned-cases-astra23-13.json` (0.2.3) and
`astra23-import-controls-01.log`. Original inputs and first failures remain
retained. Independent closure evidence has been sent to the judge.

## Judge closure

The judge's adjudication closes R7-044
at `f6c339d`. Its exact frozen 0.2.2 run reproduces 57/57 canonical vectors,
all three owned witnesses and 18 product plus four harness controls, including
missing exact checks and hidden publications. The immutable first failure is
retained; no earlier result is retrospectively relabeled.
