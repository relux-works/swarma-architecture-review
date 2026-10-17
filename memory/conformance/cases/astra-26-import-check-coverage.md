# ASTRA26-09 — partial current-version checks do not certify every import

Status: judge-classified **R7-044 impl-bug**, owner astra-23; correction pending. Package `0.2.2-draft` at
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

Judge event `$Y8OHdh7iDMe_LPy7R9JzU80dB6gLZcU1j9HGQrDTFcg` independently
reproduces all three fixtures and classifies R7-044 as a package implementation
bug. Exact source checks cannot transfer through origin deduplication. No spec
change or owner question is required. The package implementer's independent
first failure is retained at `08c4b9a` as well as this seat's original evidence.

Correction review must preserve absent/unverified equivalence, the all-checked
positive control, irrelevant hidden-publication non-interference, exact source
references and origin counts, and existing expiry/replacement neighbors.
