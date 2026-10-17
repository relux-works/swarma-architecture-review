# Source implementation worklog

Seat: astra-22. Task: R7 source-derived independent evaluator.

## Reading boundary

Read before implementation: `memory/MISSION-R7.md`, `memory/designs/kernel.md`
v0.2, `memory/designs/bounded-support-semantics-astra-03.md`, and
`memory/designs/bounded-evidence.md`, at repository commit
`6d148282de0a3927e606f037b572134cc911d1f4`.
No `memory/spec/` file has been read. No other evaluator will be used as an
implementation source. There were no project-local skill files at the three
specified discovery locations. The a2a CLI's printed skill supplies room usage;
the mission's narrower ownership, direct signed main delivery and no-spawn rules
control this seat.

## Plan and status

1. Complete: pull, full brief/source reading, tool readiness and identity onboarding.
2. Complete: source-only semantic core and 20 local controls; baseline frozen before package intake.
3. Complete: PACKAGE LANDED event `$byrILfhj-Gjsp7famnjMP2EvJbP8t9WBhwRblTS_pGk`
   opened the read boundary. First adapter and full inventory run preserve the
   frozen core unchanged.
4. Pending: commit field-level results; report every disagreement to the judge.
5. Pending: apply only classified implementation corrections, rerun releases,
   finalize verdict and park note on PARK, and acknowledge in rounds.

## Required and forbidden behavior

The evaluator keeps polarity and computation completeness separate, preserves
conflicted premises, uses explicit sufficient rules only, filters authorization
before charging logical budgets, preserves historical cuts and attribution,
rejects invalid revision authority and stale expected versions atomically, and
keeps disclosure/lineage and publication effects separate from knowledge.

Forbidden outcomes to exercise include opposition from missing support,
contraposition, evidence laundering, hidden-record influence, arrival-order
supersession, dropping lineage, stale permission reuse, partial failed writes,
and side effects outside this evaluator's in-memory synthetic state.

Deployment claims (OS isolation, real retention sinks, timing distributions,
network permissions and external authority behavior) will be reported separately
and unsupported where no actual deployment experiment exists.

## Evidence

- `.temp/astra-22/readiness-01.log`: git, Python 3.14.7 and a2a readiness.
- Source rules and unresolved normalization choices will be documented in README.

## Source baseline validation

20 controls pass under Python 3.14.7 (`.temp/astra-22/source-checks-02.log`).
The initial temporal positive-control fixture accidentally put a simulated root
on a real assertion; the model correctly excluded it. The fixture was corrected
to make both simulated. No package was inspected to fix this fixture.
Self-review: source boundaries, no external side effects, independent polarity,
refusal atomicity and explicit limitations reviewed.

## First package run

Package 0.1.0-draft at 0ef608ae279a9bc209ad78ffdc72dbbbdc828f8f. All 61 vectors
loaded: semantic 17 pass / 7 fail / 29 unsupported; deployment 0 pass / 0 fail /
8 unsupported. Exact results and normalized actual outputs are preserved in
`runs/0.1.0-first.md` and `.json`. Core SHA-256 is unchanged.

No transaction mapping is claimed yet; capture/recall are supported. Exact proof
paths, cross-assertion incompatibility, audience redaction, imported-currentness
and dirty closure remain explicit gaps. Five runner control plants passed.
Disagreements are grouped in DIVERGENCES.md and are sent to the judge before any
correction. No expected value or vector identifier is passed into the adapter.

## Supplemental adversarial inventory

At checkout a46eb98, ran all 12 currently published case vectors with the same
unchanged core and adapter: 2 pass, 1 fail, 9 unsupported. Exact evidence:
`runs/case-first.json`. ASTRA24-02 rule applicability and ASTRA26-02 checked import
control pass. ASTRA24-03 exposes ASTRA22-04 (AND-path source-state aggregation)
and additional occurrences of ASTRA22-02/03. This remains separate from the
canonical package totals and all failures are sent for classification.

## Classified correction round

Implemented only judge-classified R7-011/012/013/015. Validation logs:
`.temp/astra-22/source-checks-04.log` (24 pass), `adapter-checks-01.log`
(visible/hidden documentary association control), `vector-run-03.log`
(24/0/29 semantic, 8 deployment unsupported), `case-run-02.log` (3/0/11).
Corrected core SHA-256: eb5bd2b8df171c98f5294ed54f01dcf9e3157bfa4e6253b3824f10167fbc4da6.
A transient rerun still showed S23/B03 source references missing; inspection found
the source's own perspective was incorrectly treated as an assertion-premise
perspective. The explicit visibility regression covers that correction.

The case runner now supports `--vectors memory/conformance/cases --out PATH`;
canonical and supplemental inventories remain separate. No other implementation
was read or used. The previous supplemental commit had one ordinary push race;
signed rebase succeeded and b3c7ac9 verified G before publication.

## Coverage extension unit (in progress)

0.2.0-draft at cde5754 rerun: 24 pass / 0 fail / 33 unsupported semantic;
8 deployment unsupported (`.temp/astra-22/vector-run-04.log`).
Extend read-only wire coverage next: declared schema incompatibility (kept separate
from signed evidence), basic audience aliases/redaction, and exact projection
exclusion. These are declared unsupported gaps, not changes to a failed expected
answer. Preserve missing-alias refusal, hidden/unknown-lineage filtering, temporal
non-overlap and unchanged issuer sequences as negative controls. Declassified
publication decisions and transactions remain unsupported until implemented.

## Coverage extension result

Implemented schema-scoped unequal-field incompatibility separately from evidence;
basic audience alias/redaction with exact lookup; and immutable owner exclusions.
Package 0.2.0-draft at cde5754d523b98c93cf2b1777fe80e15b9efa74c: 29 pass / 0 fail /
28 unsupported semantic, 8 deployment unsupported (`vector-run-06.log`).
25 source controls and 2 adapter controls pass (`source-checks-05.log`,
`adapter-checks-02.log`); missing alias, adjacent intervals, different scopes/slots
and no-rule cases are executable negative controls. No new divergence observed.

Eight migrated astra-26 cases were copied read-only to
`.temp/astra-22/cases-astra26-02/` and run separately: 4 pass / 0 fail /
4 unsupported (`runs/cases-astra26-0.2.*`, `case-run-03.log`). Filenames and SHA-256
values tie each copied input to the owned source case in memory/conformance/cases.
Other seats' older-format cases were not conflated with this 0.2 inventory.
Core SHA-256: 8738b80fbe1b12cd56c62f9095c541b19f18203bf9bc147fba1ca95e5c7432d9.

## Transaction coverage unit (in progress)

Add an independent package transaction adapter for admit/admit_raw and revise,
using the published closed schemas as data. Reuse no other evaluator/checker code.
Required controls: exact retry versus changed intent, valid and invalid delegation,
stale expected head, atomic cycle/refusal, unknown schema, model qualification,
integration-derived lineage and unchanged post-failure inventories. Preserve
unsupported erasure/declassification/dirty paths rather than fabricating receipts.

## Transaction coverage first results

Five atomic transaction controls pass (`.temp/astra-22/transaction-checks-01.log`).
The first 0.2.0 run against cde5754 is preserved in
`runs/0.2.0-transactions-first.*`: 44 pass / 1 fail / 12 unsupported semantic,
8 deployment unsupported. The one failure independently reproduces the already
classified R7-021 B01 missing integration fact; the refusal leaves state intact.
It was reported to the existing topic before any package update.

After pulling 0.2.1 f31d58f, the unchanged transaction code gives 42 pass / 1 fail /
14 unsupported semantic, 8 deployment unsupported
(`runs/0.2.1-transactions-first.*`, `transaction-vectors-02.log`). B01's write now
succeeds and its dirty read becomes an explicit unsupported path. S23's new
unchecked-publication contrast is also unsupported. P02 exposes a new source
adapter defect: missing subject/principal binding gate admits a foreign
self-declaration, then shifts the adjacent valid admission beyond its query cut.
Report ASTRA22-05 to the judge before correction; preserve this committed baseline.

The pull exited zero and completed with clean autostash restoration, but reported
a transient pack-index-unavailable warning for pack-0ecf34f. Current commit reads
and signature verification succeed; no object repair or destructive command run.

## Classified history and identity correction unit (in progress)

Judge classified R7-025: explicit selection leaks unrelated sequence history.
Copied the exact judge fixture to `fixtures/selected-history.json` (data only,
no other evaluator code) and independently reproduced df499a1's output in
`runs/selected-history-first.json`. Add red-before/green-after controls for an
unrelated explicit target, unfiltered selection, explicitly displayed historical
target and hidden reference. Scope the history filter by the complete selected
sequence; preserve all other currentness and historical rules. ASTRA22-05 binding
classification is still pending; do not correct it silently.

## Classified history and identity corrections verified

R7-025 history control failed only for unrelated explicit selection before the
fix (`adapter-checks-04-red.log`) and all three adapter tests pass after the
sequence filter (`adapter-checks-05-green.log`). Full paired probe outputs remain
in `runs/selected-history-first.json` and `runs/selected-history-corrected.json`.

Judge R7-026 classified ASTRA22-05 as impl-bug. Three identity negatives all
failed before the gate (`transaction-checks-03-red.log`) and all seven transaction
tests pass after it (`transaction-checks-04-green.log`), including atomicity,
distinct bound subject/principal and represented own declaration. Package 0.2.1
f31d58f now gives 43 pass / 0 fail / 14 unsupported semantic, 8 deployment
unsupported (`vector-run-07.log`). Source core unchanged. Original report remains
immutable. These fixes require judge closure; exact dirty/proof/publication/erasure
coverage still remains explicitly unsupported.

## Budget-isolation investigation (in progress)

ASTRA25-06 independently reproduced on 26d8cc6 against f31d58f. Current complete
supplemental inventory: 10 pass / 2 fail / 8 unsupported semantic, one deployment
unsupported. Both failures (ASTRA25-01 visible control and ASTRA25-06 minimal
paired case) show the same shared existence/quality budget defect. Immutable
report: `runs/cases-0.2.1-first.*`; log: `case-run-04.log`.

The source core currently spends shared counters across both polarity channels
and the dependency closure. K-EVAL-2/4 require separate requested-literal walks
and independent opposite-quality walks. New source regression is red for that
exact property (`source-checks-07-red.log`); its nearby real AND-budget boundary
passes, preventing an unlimited-budget correction. No product correction yet;
classification requested in div-astra25-quality-budget. Planned correction keeps
finite admitted DAG semantics, current-source incompleteness, exact found-path
provenance and AND/OR source qualification while separating each walk's counters.

## R7-027 bounded-walk correction

Judge classified shared counters as R7-027; ASTRA24-05 is the same defect reduced
to direct opposite roots. Each displayed polarity now starts a depth-first walk
with independent root/rule counters and a local literal memo. Premises are visited
in stable assertion-id/numeric-version/polarity order; roots and rules use exact
reference order. Quality uses separately budgeted complete walks; only fresh
whole-walk results are shared across walks. Three finite path-quality states
retain clean alternatives and taint/uncertainty without enumerating proof sets.

29 source tests pass (`source-checks-09.log`), including all signed directions,
zero root/rule bounds, insufficient AND roots, shared-premise memoization, numeric
reference ordering, later-premise exhaustion and incomplete opposite quality.
Three adapter and seven transaction tests remain green (`adapter-checks-06.log`,
`transaction-checks-05.log`); each vector run also passes five harness controls.
Canonical f31d58f: 43 pass / 0 fail / 14 unsupported semantic, 8 deployment
unsupported (`vector-run-08.log`). Expanded supplemental corpus now has the new
ASTRA24-05: 13 pass / 0 fail / 8 unsupported semantic, 1 deployment unsupported
(`runs/cases-0.2.1-corrected.*`, `case-run-05.log`). All three R7-027 fixtures pass.
The earlier 20-semantic baseline is unchanged; the corrected corpus has 21
semantic fixtures, so the new case is not counted as a prior observed failure.
Core SHA-256 d81a4ae9956802b82d4710d85dfc54efb5679c91eb623e6515e12d8907ba8b9e.
R7-025/026 are independently closed in judge 510649f; R7-027 awaits exact fix review.

## Source-resolution boundary unit (in progress)

Adversary ASTRA24-06 reproduces an omitted source_resolutions bound after R7-027:
4e647ea current supplemental 13 pass / 1 fail / 8 unsupported semantic, one
deployment unsupported (`runs/cases-source-budget-first.*`, `case-run-06.log`).
Keep this distinct from already repaired root/rule counters; classify before fix.
Plan exact per-walk distinct-source accounting, preserving retained/independent
exemption and genuine zero/one/insufficient-source controls.

Inspection also found a separate qualification precedence mismatch: an independent
root with no named source returns independent_attestation, while K-EVAL-5 names
the empty-set case resolvable_now. The S32-derived closed-shape input and actual
4e647ea output are preserved in `fixtures/independent-vacuous-source-first.json`.
Only the independent assessment source list was emptied and the query targets
its assertion; no canonical vector or expected output was edited. Submit to
judge before swapping precedence or changing the old source-unit assumption.

## R7-028 source-resolution correction verified

Judge assigned R7-028 separately from the closed R7-027. Adapter now passes the
minimum query/policy source allowance and each assessment's original source refs.
Each independent walk memoizes distinct current-required resolutions; synthetic
availability groups never collapse separate source visits. Hidden sources are
filtered before work. Retained and independent evidence do not spend a current
source allowance. A skipped resolution removes that witness's qualifications and
derived provenance and propagates source_limit/incompleteness.

32 source controls pass (`source-checks-12.log`), including red-before zero/group
exhaustion (`source-checks-10-red.log`), repeated and multiple distinct sources,
per-polarity/quality source counters, visible quality uncertainty and hidden
single/group sources. Four adapter controls pass (`adapter-checks-08.log`); the
new wire control verifies policy clamping and original-source deduplication across
separate synthetic groups, with found-path provenance only. Seven transaction
controls from `transaction-checks-05.log` are unaffected; every runner invocation
passes five comparison controls.

Canonical f31d58f is 43/0/14 semantic, 8 deployment unsupported (`vector-run-09.log`).
Current supplemental is 14/0/8 semantic, 1 deployment unsupported
(`runs/cases-source-budget-corrected.*`, `case-run-07.log`). Source SHA-256:
4ee2c9010143a21fd124d443421472a6b60245927c02eb8d8663984518d8aaeb.
Original f2d233a source-budget report remains unchanged. R7-028 awaits independent
verification; separately reported ASTRA22-07 vacuous-source precedence remains
unchanged pending classification.
