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

## R7-029 precedence correction unit (in progress)

Judge confirmed R7-029 as impl-bug and supplied a separately validated nonempty
resolvable/unavailable source pair. Preserve exact judge data in
`fixtures/independent-resolvable-judge-first.json`; own c923ebd reproduction is
`runs/independent-source-first.json`. The unavailable independent case correctly
passes, while resolvable and empty named-source variants wrongly return
independent_attestation. Add finite current/retained/independent source-state
controls and exact wire probes before swapping the precedence. Keep evidence
qualification and R7-028 source-visit obligations unchanged. Correct the old
stronger-OR fixture to name an unavailable source so its original independent
fallback claim remains valid under the released rule.

## R7-029 correction verified

Resolved/vacuous source state now precedes independent fallback. The two exact
wire probes change only support.source_state after snapshot-value normalization;
the unavailable positive control has no semantic change. Paired full outputs and
field deltas: `runs/independent-source-first.json` and
`runs/independent-source-corrected.json`. Original judge input and empty-source
probe remain unchanged.

33 source controls and five adapter controls pass (`source-checks-14.log`,
`adapter-checks-10.log`), with intended red-before failures in
`source-checks-13-red.log` and `adapter-checks-09-red.log`. Current/retained/
independent cases keep their qualification and failure semantics. The previous
stronger-OR test now explicitly names unavailable bytes for its independent
alternative; it no longer accidentally asserts the invalid empty-set precedence.
R7-028 counters remain covered. Seven transaction controls are unchanged; five
harness controls pass on each run (50 total controls).

Canonical f31d58f: 43/0/14 semantic and eight deployment unsupported
(`vector-run-10.log`). Supplemental: 14/0/8 semantic and one deployment unsupported
(`runs/cases-0.2.1-current.*`, `case-run-08.log`). Core SHA-256
bd0f09fd93fa4d82af6ac5ec4338bd9dec05fde32ddd82262c73df2369224550.
R7-027 is judge-closed at 56e5909. R7-028 and R7-029 await independent closure.

## Phase 2 (in progress)

Convener decision $L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc explicitly
withholds PARK and requires dual execution of all 57 semantic vectors, with
one subsequent round without new open items, or the 13:00Z hard cap. Preserve
phase-1 43/0/14 canonical and 14/0/8 supplemental evidence. The old supported-
vector rubric score does not establish Phase-2 completion.

Plan remaining support in bounded units: (1) exact proof enumeration, authorized
dirty/review closure and imported publication currentness; (2) immutable captures,
current delivery/revocation and exact multi-owner declassification; (3) erasure,
restore, source availability and hidden-load semantic boundary. Required negative
controls include hidden/unfound proof exclusion, bounded explanation versus
evidence completeness, historical/hidden dirty causes, stale snapshots and
revoked delivery, missing owner grants, late writers and stale restore witnesses.
Use kernel/companion/design semantics; package supplies concrete wire grammar and
unchanged conformance comparisons. Every newly observed mismatch goes to judge
before correction. Never read another evaluator's code. No deployment claims.

## Phase 2 exact-proof coverage completed

Added a reduced zero-suppressed set-family diagram for exact proof unions and
AND products. Only found eligible witness roots and justification refs enter the
family; certificates and opposite-quality roots do not. Proof identity is exact
record identity, independent from origin deduplication. Each output prefix uses
canonical JSON order after numeric reference sorting; explanation truncation
does not change evidence completeness. Recall retains its empty explanation.

Four proof controls pass (`proof-checks-02.log`): independent finite set-algebra
oracles with overlaps, numeric-version/prefix ordering, hidden/quality exclusion,
and a 40-choice family with 2**40 possible proofs represented without enumerating
all combinations. The shared diagram can still have exponential worst-case size;
this semantic implementation makes no hostile-load/service resource claim.
Audience-projection explanation/reference disclosure remains explicitly unsupported
until mapped, rather than exposing protected proof identifiers.

First expanded canonical comparison (`phase2-vectors-01.log`,
`runs/phase2-proofs-first.*`): 44 pass / 0 fail / 13 unsupported semantic,
8 deployment unsupported. S07 now exact. The 22-semantic supplemental inventory
examined at this point gives 15 pass / 0 fail / 7 unsupported, 1 deployment
unsupported; ASTRA24-01 now exact (`runs/phase2-proofs-cases-first.*`).
All 33 source controls pass (`source-checks-15.log`); five adapter, seven
transaction and five harness controls remain the established baseline (54
controls including new proof suite). Original phase-1 accepted reports archived
unchanged in `runs/phase1-accepted.*` before replacing current RESULTS.

Newly directed R7-030 persisted-idempotency defect is queued as the next unit,
separate from coverage. ASTRA25-07 erasure-receipt disclosure is noted for the
later erasure unit pending judge disposition. No other evaluator code was read.

## R7-030 persisted idempotency (in progress)

Preserved the complete judge snapshot/probe as fixtures/persisted-idempotency-judge-first.json. Independent reproduction on 4960d24 records three duplicate_record refusals instead of two exact receipt replays and an idempotency_conflict; runs/persisted-idempotency-first.json retains complete actual output and unchanged-state evidence. Use runtime.idempotency as the authoritative store, including admitted initial snapshots and successful commits. Add red-before controls for initial and reconstructed replay, original handle/time, changed intent, actor/space/key isolation and current operation authorization. Import-currentness R7-032 and the newly reported retention case are queued behind this committed unit; proof Cartesian regression will be included in the next supplemental run.

## R7-030 correction verified

The declared runtime.idempotency list is now the single store. The compatibility lookup is derived from it; successful admission/revision appends the canonical request and exact receipt only in the commit block. Initial and reconstructed snapshots share the same path. Current operation authority still precedes replay. Eleven transaction controls pass (transaction-checks-09.log); the intended old failures are retained in transaction-checks-08-red.log and signed f2c1570. The exact judge probe now has zero operation differences and unchanged records/runtime (runs/persisted-idempotency-corrected.json). Canonical remains 44/0/13 with eight deployment unsupported (runs/phase2-idempotency-corrected.*, phase2-idempotency-vectors-01.log). The expanded 30-semantic supplemental first inventory is 17/2/11: R7-032 stale import currentness and ASTRA25-08 unauthorized retention remain open, unchanged and queued; Cartesian proof ASTRA24-07 passes. No deployment restart or durable-storage claim.

## R7-032 import currentness (in progress)

Judge $d-fCrpCafaGdZmlnjrNnqpKXqFOs7Um-npNJhPU8IJ8 classifies the expired-import result as impl-bug. Immutable f2c1570 report contains the exact first error. Implement source kernel section9.2 with K-PUB-2 wire facts: actual authorized publication association, checked/unverified/replaced state, exclusive freshness horizon. Three new wire controls cover before/at/after expiry, missing check, known replacement, non-publication distinction, unchanged origins and earlier capture; S23 missing-check support follows the same mapping. No case expectation change.

## R7-032 correction and S23 coverage verified

An authorized actual publication association now maps known replacement to historical and missing/unverified/expired current-version knowledge to last_received. The exclusive horizon uses computed item freshness; ordinary report-sequence currentness stays independent. Overall currentness preserves ambiguity before last_received. Eight adapter controls pass (adapter-checks-12.log), including three new boundary/control groups with intended old failures in adapter-checks-11-red.log. Exact ASTRA26-07 first failure remains f2c1570; corrected 0.2.1 supplemental inventory is 19/1/12 over32semantic cases, with retention R7-036 still failing and one deployment unsupported (runs/phase2-import-cases-corrected.*). Canonical0.2.1 is45/0/12; after pulling the released0.2.2 package7e71765, canonical remains45/0/12 (runs/phase2-import-0.2.2.*, phase2-import-vectors-02.log). S23 now passes. Eight canonical deployment cases remain unsupported. The supplemental0.2.1 report is explicitly pinned before case migration; no fixture was rewritten. R7-036 needs a precise retention-operation scope mapping because admit/revise carry actor/time/class but no audience/purpose; investigate before inventing a grant-combination rule.

## Phase 2 dirty/review coverage (in progress)

Implement source companion deterministic dirty boundary and K-EVAL-8 concrete retained-cause mapping. A write records each exact revision cause with transitive registered sufficient-support/review-on-change dependents atomically. Query eligibility is evaluated over the graph immediately before each retained cause, under current authorization and query context/time; hidden causes cannot affect output or clear protected state. Add historical-cut, missing-cause/recomputed, hidden premise/certificate/cause, later-withdrawn-path and cross-schema review controls. B01/S17 and ASTRA25-05 primary/visible control remain unchanged conformance oracles. Retention scope request is pending judge/editor; no speculative grant-combination fix is mixed into this unit.

## Phase 2 dirty/review coverage verified

impact.py keeps registered impact separate from witness evaluation. Revision commit appends exact retained causes across the pre-revision reverse closure. Query traversal requires current visibility of the cause, changed target, each path edge, every necessary premise and certificate; later path withdrawal does not erase an earlier unresolved cause. The source evaluator short-circuits only those eligible dirty assertions before evidence accounting. Historical cuts and hidden-only invalidation retain their ordinary authorized answer; no read clears global causes. Review closure includes authorized cross-schema review-on-change dependents after replacement and can remain after dirty recomputation. Audience views suppress protected review references.

Canonical first expanded run is47/0/10 semantic on0.2.2/7e71765, with8deployment unsupported (runs/phase2-dirty-first.*, phase2-dirty-vectors-01.log); B01/S17 now exact. Six impact controls pass (impact-checks-01.log), plus33source,11transaction and4proof controls (source-checks-16.log, transaction-checks-10.log, proof-checks-03.log). Eight adapter controls and five harness controls remain passing established evidence, total67controls. Tests cover hidden elements and an AND sibling, context mismatch, historical and cleared causes, later withdrawal, cross-schema review and finite transitive/cyclic closure.

Targeted unchanged ASTRA25-05 hidden/visible pair passes under its still-pinned0.2.1 fixture profile. Newly migrated ASTRA24-08 ambiguous-authority CAS primary fails12comparisons while its unique-head control passes; exact input/code hashes, normalized full outputs and differences are preserved in runs/phase2-dirty-targeted-first.json. No ambiguity fix mixed into this coverage unit; report to judge. This four-case targeted report is not a full current supplemental inventory. R7-036 scoped retention remains blocked on a precise package mapping, independently confirmed by editor and package implementer; continued coverage work is independent.

## Phase 2 capture/delivery/revocation (in progress)

Implement kernel6.4/9.3 and K-SNAP-1/K-PUB-1 independently. Capture immutable public bytes and a protected binding to exact selected internal refs and query. Recheck current read/use/forward, policy, known-lineage eligibility, horizons and erasure/restore at delivery; filter only selected items, preserve excluded-record independence. Revoke appends the owner-authorized live event without rewriting policy or old views. Controls require pre/post-revocation delivery, scoped binding rejection, each selected right, unrelated/excluded grant independence, expiry and erased-record refusal with no state effects. Declassification operations and changes remain explicit unsupported until their separate mapping. R7-039 retention_context release remains pending.

## Phase 2 capture/delivery/revocation verified

Captured outputs and their protected query/selected-ref bindings are deep copies, keyed by operation index. Live read/use/forward revocations now filter ordinary queries and exact prepared deliveries; owner-only revoke appends an event without changing policy pins, semantic records or cuts. Delivery rechecks only selected refs, their current read/use/forward, lineage, erasure/restore state, policy and freshness/currentness; no later item is silently substituted. It returns a semantic receipt only and sends no external bytes.

Canonical0.2.2/7e71765 first run49/0/8 semantic and8deployment unsupported (runs/phase2-delivery-first.*, phase2-delivery-vectors-01.log), addingP06/P12. Eight boundary controls pass (boundary-checks-01.log): current revoke, independent selected rights, exact excluded-record pair, expiry endpoint, erasure/restore gates, saved-binding/owner authority, unrelated revocations and deep-copy isolation. Adapter8 and impact6 controls rerun green (adapter-checks-13.log, impact-checks-02.log); established source33/transaction11/proof4/harness5 remain, total75controls. Full migrated38-case supplement is26/3/9, deployment1unsupported (runs/phase2-delivery-cases-first.*, phase2-delivery-cases-01.log). Only failures are known R7-040 ambiguous and historical CAS, plus R7-036 retain authority. Both delivery adversary cases pass. Newly supplied historical-CAS first failure and challenge positive control are retained in this report before the queued fix.

R7-032 is judge-closed at1f35727, R7-030 at1f3180d. R7-039 was classified spec-bug; editor will release explicit actor-bound context.retention_context in0.2.3. R7-040 next unit follows already-preserved first failures, with atomic state, unique authority head, challenge and exact-replay precedence controls. No package/foreign evaluator code was edited or read.

## R7-040 authority-slot CAS (in progress)

Judge $jWF7PS9bJWLBKtoGF2OqBiJIlvcfYJB7WzuI6j5fxPw requires complete authority-slot head selection before non-challenge CAS. First primary is e38c37c; first historical neighbor is5d079be. Add exact atomic refusal for ambiguous/stale candidates with unique-head/challenge controls, later canonical common-successor admission and original receipt replay before advanced-head checks. Resolve canonical receipt partial order within the exact sequence; do not pick by arrival time or the caller-named candidate. No package/case output edits.

## R7-040 correction verified

Non-challenge decision CAS now selects the unique maximal canonical receipt in the complete exact authority slot, traversing transitive receipt predecessor edges independently of memory arrival. Only after that selection do local transitions advance its CAS token. Historical target selection cannot bypass a current or ambiguous slot. Exact replay remains earlier than CAS, and challenge still bypasses the head constraint. Thirteen transaction controls pass (transaction-checks-12.log); both intended old refusals failed in transaction-checks-11-red.log. Native checks compare complete records/runtime/policy after refusal and cover a later admitted common successor, unique head, challenge, and exact original receipt replay after advancement.

Canonical remains49/0/8 on0.2.2/7e71765 (runs/phase2-cas-corrected.*, phase2-cas-vectors-01.log). Current41-semantic supplemental inventory is31/1/9, deployment1unsupported (runs/phase2-cas-cases-corrected.*, phase2-cas-cases-01.log). Both original ambiguous/stale cases now exact, controls unchanged; the sole remaining executable failure is R7-036 retention. The three newly received partial-import-check cases also pass without further source changes. First CAS failures at e38c37c/5d079be remain immutable. R7-040 closure awaits judge verification. Established control total77.

## R7-043 changed rule/certificate dirty cause (in progress)

Judge $lXcUN46jxrVt_c0amm5LNbwyvqnzNvPyTOc6omMPOmk identifies that only premise refs currently trigger reverse traversal; withdrawing a registered justification or its check fails to dirty its consumer. Preserved exact judge input directory under fixtures/dirty-rule-certificate and source-only first report under runs/dirty-rule-certificate-judge-first.json, without reading package implementation. Add rule/check identities to registered dependency triggers in both protected marking and query pre-revision traversal, preserving current scope/necessary-premise tests. Add hidden/challenge/transitive/historical/recomputed controls and keep first own reproduction before correction.

## R7-043 correction verified

Registered path dependencies now include the justification identity and its check as well as literal/source premises. Both global marking and query pre-cause traversal use that same edge model; current eligibility still requires every path component. All three exact judge vectors pass (runs/dirty-rule-certificate-corrected.*, dirty-rule-certificate-corrected.log), versus1pass/2fail preserved at4744e62. Nine impact controls pass (impact-checks-04.log), including new red-before rule/check, hidden/private/challenge, transitive-history/recompute/replay and zero-logical-budget groups. Thirteen transaction controls rerun green (transaction-checks-13.log). Established control total80.

Canonical0.2.2 remains49/0/8 with8deployment unsupported (runs/phase2-dirty-edge-corrected.*, phase2-dirty-edge-vectors-01.log). Current43-semantic supplemental inventory33/1/9 and1deployment unsupported (runs/phase2-dirty-edge-cases-corrected.*, phase2-dirty-edge-cases-01.log); only R7-036 retention fails. Newly supplied transitive review and actor-bound delivery cases pass independently. R7-043 awaits judge closure. Rule/certificate correction does not claim exhaustive invalidation coverage outside the registered path contracts exercised.

## R7-040 remaining NEXT neighbor (in progress)

Adversary3f06da5 supplies ASTRA24-08-NEXT: after withdrawing the unique latest authority candidate, the projection exposes the next active candidate, but source head selection retains the withdrawn candidate. The ordinary-record withdrawal-token rule was incorrectly carried into authority-slot selection. Preserve this exact new failure, retain all original ambiguity/staleness/challenge/replay tests, then select among non-withdrawn authority candidates before receipt maxima. The existing final head-helper assertion after withdrawing the new common successor encoded the same mistaken authority token assumption and must be updated with the true next active receipt; keep its admission/replay proof intact. R7-043 unit is already complete3722327.

The pre-commit pull received0.2.3 package23290b3 while completing NEXT. Its first49-supported canonical run is47pass/2fail (P11/P13) plus8unsupported; immutable bytes retained as runs/0.2.3-first.*. Old0.2.2 supplemental fixtures under0.2.3 fail profile/required-context checks and are separately archived as0.2.3-old-cases-first.*, not treated as new semantic divergences. NEXT is being verified in isolated scratch validation-v0.2.2 with exact7e71765 package bytes, unchanged current old-profile case inputs and byte-identical current source modules. No foreign evaluator code copied/read; only package data and adversary inputs. New retention implementation follows the completed NEXT unit.

## R7-040 NEXT correction verified on pinned0.2.2

Authority candidates now exclude withdrawn decisions before computing canonical receipt maxima and return the active candidate directly. Ordinary-record revision-token behavior remains separate. Exact first NEXT failure is bd75f4f; validated judge input/source-only first report are also retained without the explicitly invalid judge setup. Fourteen transaction controls pass against exact0.2.2 package bytes (transaction-checks-16-pinned.log), including the new continuation and all previous atomic/replay tests. The final helper assertion after withdrawing a common successor now correctly expects remaining active d2 instead of an ordinary withdrawal token; its independent admission/replay assertions are unchanged.

Pinned canonical0.2.2 remains49/0/8; all44old-profile supplemental cases give34/1/9, with onlyR7-036 retain failure. Byte-checked source hashes and full outputs: runs/phase2-cas-next-pinned-canonical.json and phase2-cas-next-pinned-cases.json. The original five CAS cases now all pass, including NEXT. Deployment8+1unsupported. This is explicitly previous-release correction evidence. Current0.2.3 first run is47/2/8; P11/P13 expose missing released retention semantics. Old-case/old-control failures under0.2.3 are migration/schema failures, not corrected semantic evidence (transaction-checks-15.log). Current RESULTS deliberately shows this new-release red state. Next unit implements explicit retention_context and migrates owned controls without changing original fixtures/runs.

## R7-036 explicit retention context (in progress)

Read the complete K-AUTH-1/K-DISC-1/K-API-1/2 release delta at23290b3. Check exact actor/space/id/audience/purpose retain for each proposed output and resolved transitive integration input, including incomplete-fact lower bounds and whole-batch future inputs. Metadata, read/use and output disclosure labels do not supply retention authority. Recheck original output/input authorization before replay; scope remains canonical intent. Negative controls cover each mismatched grant dimension, revoked authority, retained receipt preservation, missing context/input and no partial state; nearby authorized/empty-label/same-batch controls remain required. Original first release failures stay immutable99b5a85. Migrate owned historical control inputs into explicitly named0.2.3 copies, retaining the exact historical fixtures and reports. No foreign evaluator code or case expectations are changed.

## R7-036 retention correction verified

Current retain checks precede idempotency and traverse the input facts of resolved pre-state/whole-batch records, including unknown lower bounds. Every record uses its own space/id, the fixed actor and one explicit audience/purpose. Metadata is not required for storage. Inheritance also follows trusted integration inputs through future batch records rather than relying on client-proposed intermediate lineage. Live revocations block new writes and exact receipt replay without rewriting stored receipts or erasing records. Original0.2.3 failures remain99b5a85; eight new control groups initially produced12intended failures (runs/retention-controls-first.json), then all pass (retention-checks-02.log).

Canonical0.2.3 is49/0/8 with8deployment unsupported (runs/phase2-retention-corrected.*). Fully author-migrated46-semantic supplemental inventory is37/0/9,1deployment unsupported (runs/phase2-retention-cases-corrected.*); all four exact retention fixtures pass. Earlier mixed-profile run24/13/9 is separately preserved as phase2-retention-mixed-profile-first and proves no current conformance claim. Its13failures are unmigrated astra-24 profile/context differences; after author migrationddc62c6 all13 pass without evaluator changes.

All89controls pass on current grammar: source33(source-checks-17),adapter8(adapter-checks-14),transaction14(transaction-checks-18),proof4(proof-checks-04),impact9(impact-checks-05),boundary8(boundary-checks-02),retention8(retention-checks-02),harness5. Owned persisted-receipt and dirty-rule fixtures have explicit0.2.3 copies; their originals remain unchanged. The identity-isolation control now clones a grant for the declared storage scope, preserving its original claim. Unmigrated transaction failures are retained in transaction-checks-17.log. R7-036 closure awaits judge; no deployment qualification.

Judge events $tmfi_3vaCFABPnbEDIekguKbs5okvS5uAK-igNNYZng and $7SPv0fhusw6LBCA4fpiCUg1pBXhDn87JlV2hcPupTDw close R7-040@99b5a85 and R7-043@3722327 respectively, with pinned0.2.2 exact input/code reproduction and all14transaction/9impact controls. These closures are independent of new retention verification.

## Phase 2 declassification wire coverage (in progress)

Implement K-DISC-2 independently: atomic ordered owner assessments plus output; exact integration inputs, output body/schema/transform/scope and policy/environment pins; every lifted input owner; normal representation/review and current retention checks. Release only the exact pinned structured output/scope. Recompute ordinary inherited constraints on every new disclosure when a cited owner decision is inactive/revoked, preserving prepared snapshots and refusing stale delivery. Add owner/representation/model/pin/unknown/deadline/replay controls with full-state refusal. Canonical P05 and unchanged ASTRA25-02 remain external oracles; keep first full expansion report before any judge-classified correction.

Declassification first expansion is49/1/7 canonical and37/1/8 supplemental (phase2-declassification-first and phase2-declassification-cases-first). P05/ASTRA25-02 valid release falsely refuses declassification_invalid. Read-only trace identifies output digest mismatch: new wire mapping hashed raw canonical body, omitting K-JSON-2 ASCII bounded-evidence:cjson-v1 plus NUL framing. No source records committed on refusal. Preserve this exact first implementation and reports before correction; request judge classification. No expected answer changed.

Nine release control groups are prepared; immutable pre-correction native output is runs/release-controls-first.json. Both ASCII and non-ASCII raw-hash negative plants are wrongly accepted, while framed positive controls falsely refuse; other positive release controls stop at the same digest error. Existing affected adapter8/transaction14/impact9/boundary8/retention8 controls pass (logs15/19/06/03/03 respectively). R7-036 is judge-closed atd077064 via $3mZqw6AM65j28W9NIr5SMhxgW6mF7IP2ykjcDuASILs, with exact current canonical/supplemental evidence and89controls. Independent adversary/editor confirmations received; no wider deployment claim.

## R7-050 declassification framing corrected; P05 coverage verified

Judge $Jxqff_h8h6pJHraJVkiriHrvMIYcTlLKLCO1QAjUMuI classifies the omitted framing as R7-050. Added exactly the K-JSON-2 domain bytes plus one NUL before canonical UTF-8 output-body bytes. First implementation/reports36983de and two-direction native witnesses e1ba8db remain unchanged. Both framed ASCII/Unicode positives pass and both consistently raw-pinned negatives refuse atomically. All nine release groups pass (release-checks-04.log). One newly reached test setup used an unregistered private projection; it is explicitly repaired by admitting the ordinary rule before the scope check, with the setup failure retained in release-checks-03.log, not counted as product evidence.

The new wire path atomically orders owner assessments before the output; verifies exact direct inputs, complete transitive knowledge, body/schema/transform/scope/policy/environment pins, current decisions and all lifted owners; keeps representation/review and admit/declassify/retain independent. Live decision revocation changes authorization state only, preserves semantic records/cuts and frozen captures, restores ordinary inherited constraints on new queries, and blocks delivery. Retention deadlines are never widened. Controls cover wrong/missing owners, model-only evidence, pins, unknown direct/transitive lineage, deeper constraint ownership, exact-scope isolation, current revocation, replay and full-state refusal.

Canonical0.2.3 now50/0/7,8deployment unsupported; full46-case supplement38/0/8,1deployment unsupported (runs/phase2-declassification-corrected.* and cases-corrected.*). P05 and unchanged ASTRA25-02 both exact. Established controls98: prior89 plus9release groups; affected47prior controls rerun green with new mapping. R7-050 and coverage extension await independent judge review. R7-047 strict authority succession is next, against classified authority_receipt_required mapping and upcoming R7-049 package release. No foreign evaluator code or expected answer was read/changed.

## R7-047 strict authority succession (in progress)

Judge $oswbTe0Ndkm1yCdJdGq7nbrO9wT2oEUuevIL7-Sa6Zk classifies source047, package048 and specification mapping049. The exact adjudicated refusal is authority_receipt_required,false for an incomparable, identical or prior proposed replacement receipt; valid direct/transitive successors, plain incomparable imports and exact replay stay accepted. Canonical editor release is pending; author72a8f86 publishes five exact0.2.3 vectors under the adjudication. Own full52-case first report is40/4/8 (phase2-succession-first.*), preserving all three forbidden writes and a separate transitive projection defect. R7-047 unit changes only write validation; the receipt-only intermediate projection mismatch awaits separate judge classification. Add full-state atomic replace/correct negatives, direct/transitive positives, replay/CAS and ordinary-import controls before the correction. No expected output changes.

Four native succession groups reproduce six intended forbidden-acceptance failures (replace/correct for three receipt-order classes) while direct/transitive writes, exact replay/stale-CAS and ordinary incomparable import pass. Original source implementation is8a42945; full red output and module/control hashes are in runs/succession-controls-first.json. Complete52-case external first remains40/4/8; three write failures are047, transitive projection is separate. New ASTRA25-02-DIGEST also passes exactly; targeted P05 plus both declassification fixtures are preserved in runs/declassification-targeted-current.json.

## R7-047 strict successor correction verified

Authoritative replace/correct now require the replacement's canonical receipt to strictly succeed the target's prior receipt through issuer-matched canonical event ancestry. Identical, prior and incomparable receipts refuse authority_receipt_required before commit. CAS remains earlier and distinct; successful exact replay remains before either validation. Plain incomparable imports are unchanged. Four succession groups pass (succession-checks-02.log) after six intended old failures preserved64ef86e; fourteen existing transaction controls also pass (transaction-checks-20.log). The direct/transitive positive groups check exact record count, cut, dirty set and replay inventory; all negative groups compare complete records/runtime/policy/captures.

Canonical0.2.3 stays50/0/7 (phase2-succession-canonical.*). Current54-case supplement44/2/8 (phase2-succession-corrected.*): all three strict-order negatives and direct positive are exact; transitive write succeeds but its projection and the new read-only ASTRA24-11 still fail. These are separately judge-classified R7-051 via $lL-KfgsFVYJ8Kpol9-2KlrnISzbIcOa-A7-1Pv5Z2-k, next unit. No claim that all five whole successor vectors are green. Established controls102. R7-049 publication is pending; this unit uses the explicit judge mapping and author72a8f86 exact0.2.3 vectors. Judge closes R7-050/P05 at8a42945 via $eKvZRGBlqzKr6xMsLkCJYW-knzBYjX56FZRIIFPlYHY, independently reproducing all98controls, canonical and release probes. No oracle edits.

## R7-051 transitive receipt projection (in progress)

Read the complete released0.2.4/ef02647 delta. First full source run is49/1/7, onlyB01 fails seven final projection comparisons; its new strict-successor refusal and replay operation traces already pass. Preserve runs/0.2.4-first.* before projection changes. Implement canonical receipt-DAG ancestry independently of the existence of intermediate assertion records, then map that ancestry onto exact eligible assertion sequences. Preserve per-issuer/slot/space grouping, hidden/future candidate eligibility and genuinely incomparable branches. Native read-only controls require unchanged records/runtime/policy/captures, long ancestry without intermediate assertions, event-order independence, scoped/historical filtering and genuine ambiguity. Existing source core stays unchanged; this is a wire adaptation correction.

Four projection groups initially produce three intended failures (missing middle, longer chain, private positive), while the genuine-incomparability control passes. Native first output/control hash is runs/authority-projection-controls-first.json; canonical0.2.4 first is retained separately. No product code changed before these witnesses.

## R7-051 receipt projection correction verified

The adapter now closes each issuer's canonical receipt DAG before mapping predecessor receipts onto exact assertion sequence/space candidates. Intermediate assertion records are unnecessary. Candidate visibility/cut/context/subject filtering remains in ordinary projection, and incomparable branches remain ambiguous. Four projection groups pass (authority-projection-checks-02.log), including closed initial/query shape checks, two/longer receipt-only paths, event-order independence, private/historical/scoped candidates and read-only full-state preservation. First0.2.4 report and three native failures remain d5f07be; earlier transitive failures remain64ef86e/4772258.

Current0.2.4 canonical50/0/7 with8deployment unsupported; all54 author-migrated supplemental semantic cases46/0/8,1deployment unsupported (phase2-authority-projection-corrected.* and cases-corrected.*). B01 including all new exact operations/postconditions and final transitive currentness now passes; ASTRA24-10-TRANSITIVE and read-only11 pair pass. All106controls pass:33source,8adapter,14transaction,4proof,9impact,8boundary,8retention,9release,4succession,4authority-projection,5harness. Current logs projection-current-*-01.log; impact correction/recheck is projection-current-impact-02.log.

Three test maintenance changes are explicit, not product defects: boundary exact fixtures read the released profile rather than a stale0.2.3 literal; B01's cross-schema impact control selects the new direct positive operation6 and its resulting cut (its previous operation0 is now deliberately refused); an unreached mode-neighbor used the nonexistent hypothetical variant and now uses admitted simulated, with all initial/query shapes checked. The genuine first projection witnesses do not depend on those setup branches. Source core unchanged; R7-051 and strict-successor047 await judge closure. Remaining seven canonical paths are semantic erasure/restore/load. Deadline probes are queued pending judge/editor mapping, not silently corrected.

## R7-052 current retention deadlines (in progress)

Judge $JPRw0HAxhQiEJ-rN4erBtnvRBnBXixLi2Rap_jcFAN0 classifies source052/package053/spec054. New retention and exact replay require trusted context.at strictly before every applicable non-null output/transitive-known-input deadline; otherwise not_authorized,false before idempotency, with original receipt/full state preserved and no purge. Preserve own execution of the five unchanged author604af18 native inputs before correction. Add all four supported intake APIs, own/complete/unknown lower-bound/same-batch deadlines, strict boundary, null/unrelated neighbors and authorization-before-duplicate controls. The new0.2.5 exact package release is pending; adjudication is explicit and original source first evidence remains immutable.

Own five original native observations reproduce all expired successful writes and unchanged expired-success replay, with closed initial/operation shape checks and full state preserved in runs/deadline-native-first.json. Exact author input data is copied read-only into fixtures/retention-deadline-native-first.json with original artifact hash recorded. Six native deadline groups produce17intended failures (deadline-checks-01-red.log / runs/deadline-controls-first.json); before/null/unrelated controls pass, and every affected intake API is exercised. No expiry fix precedes this evidence.

## R7-052 deadline correction verified

Read the complete6a04e8c/0.2.5 delta. Original c9e1faf transaction bytes were restored only for the first full released vector run, then the working correction was restored:49/1/7, P11 only, preserved in runs/0.2.5-first.* with exact source hash/provenance. No new classification is needed: the expanded failures are the adjudicated052 contract. Current intake authorization now refuses when trusted context.at is at/after any non-null proposed-output or known-input deadline, before replay/conflict. Every proposed envelope is checked even for repeated identities; only input recursion is deduplicated. No record, cut, receipt, policy or purge changes on refusal.

All112controls pass on0.2.5: prior106 plus6deadline groups; full logs and module hashes retained in runs/deadline-controls-corrected.json and scratch deadline-current-*-01.log. Canonical50/0/7 with8deployment unsupported (phase2-deadline-corrected.*). Initial new-profile61-case run15/38/8 is explicitly a mixed-profile migration result (phase2-deadline-cases-first-current.*), not evidence of38semantic defects or current corrected supplemental conformance. Only astra-26 had migrated; authors24/25 own the remaining migrations. Exact original native inputs, red controls and receipts remain c9e1faf.

Judge closes047@4772258 via $pNoW3rbOWwkEJDE5jKrGOsRL9nD9Ngyuo48i_zazdJ0 and051@427fed5 via $vV4SFYMuOLmhMHmEXvbM7PhTw9qOuqgQpvVzxyJypE0. Current deadline correction awaits independent review. Remaining seven canonical gaps are erasure/restore/load; next coverage unit follows the released normative transaction rules. No expected answer or foreign evaluator code changed/read.

After author25 migration8edcbfb, the second mixed-profile run is33/20/8 (phase2-deadline-cases-partial-migration.*). All seven new expiry cases now pass, including the five previously failing negatives; the remaining20differences are author24's pending profile migration. This is explicitly not a fully migrated corpus claim.

## Remaining erasure, restore and availability coverage (in progress)

Read K-AUTH-1, K-API-1/2 and K-ERASE-1/2/3 in released0.2.5. Implement semantic custody/content closure, durable-generation/fence state, exact receipt metadata filtering/current replay, incomplete requested boundary and independent-recipient separation. Restore retains current inventory/obligations and reintroduces only backup custody behind a global fence; current-complete witness reconciliation reapplies all obligations before reopening. Map load/availability/control harness stimuli without external effects. Native negative expectations: unauthorized/invalid operations and replay after metadata revocation cannot mutate state; excluded refs cannot weaken purge; partial/unreachable custody cannot report complete; old/current-generation derivatives refuse; stale/unwitnessed restore remains fenced; hidden load cannot change public logical output. Paired positives cover complete/repeated erase, live receipt replay, authorized metadata, current witness and availability recovery. Preserve the first full newly executable vector run before correcting any mismatch. Deployment remains unsupported.

## Full canonical semantic coverage first verified

The first independent erasure/restore/load mapping passes all57canonical semantic vectors on unchanged0.2.5; no new vector disagreement or correction was needed. Full first report is phase2-erasure-first.*. Initial61-case supplement41/20/0 retained in phase2-erasure-cases-first.* has only the20unmigrated author24 profile stamps. After explicit author27303e4 migration, all61semantic supplements pass unchanged (phase2-erasure-cases-current.*). Deployment8+1remains unsupported.

Erasure closure includes only admitted outputs and their trusted complete/unknown input dependencies, then accounts controlled custody by inputs. Receipt refs are independently filtered before fencing; existing tombstone identifiers may remain authorized. A fresh operation fences/increments generation and records a canonical exact receipt; replay rechecks current metadata and preserves the receipt/state. Omitted/unreachable sinks stay pending, independent recipients stay outside the receipt, and later new-key requests can finish. Restore copies only initial-backup storage presence behind a global fence, preserving current policy, inventory, generation and receipts; current-complete witness reapplication purges controlled custody before opening. These are semantic booleans and tombstones, never physical deletion evidence.

Eight erasure groups pass exact replay/context/current revocation, five receipt metadata boundaries without weakening purge, malformed/unauthorized full-state refusal, partial/unreachable/independent custody, unknown/future-fact closure, stale/current-generation late writers with independent positive, initial-cut restore and current witness, and unreachable reconciliation. Four availability groups pass protected-load non-interference, authorized coarse outage/recovery, atomic undeclared/non-owner/malformed refusal and independent data-only control observations. All124controls pass (119native plus5runner plants); full outputs/module hashes in runs/erasure-controls-first.json and scratch erasure-current-*-01.log. No first report or external oracle is rewritten.

Judge $HZk3768zLdVELKOLbBdEC07KP_j0-uY6h775onLttZc closes052@4a14a56 after independent canonical/native/external expiry reproduction. New ASTRA24-12 issuer-boundary pair remains un-oracled pending adjudication; source issuer-local ancestry stays unchanged. Package053candidate23b4d74 awaits judge review. Full source coverage publication is ready for independent verification; Phase2 score remains1pending those obligations and quiet-round/PARK gates.

## New initial-availability recovery failure (unclassified)

A fifth availability control extends the green124baseline with an admitted initial policy.public_availability=degraded and runtime.memory_available=true, followed by owner set_availability available under coarse_unavailable. Shapes accept both initial state and operation. The adapter returns availability_changed yet the next identical query remains unavailable, instead of recovering a view. The new mapping toggles runtime.memory_available only while query still gates on the unchanged public policy state. Four existing availability groups remain green; added group fails exactly. Full input/query/actuals/module hashes and red output are runs/availability-recovery-first.json / availability-checks-02-red.log. Canonical57/57 and supplemental61/61 still pass; this native failure is outside those denominators. Preserve this first implementation before requesting judge classification; no correction yet.

## R7-055 owner question: own frozen native observation

Judge $Ju7IuqWDcWw6JB87jbG-0K3yC4TWQ2WszJTNwNLZQHs files the mixed-issuer ancestry question; convener $wrLtxOryOvNuOttDN4ofHbvs0INg6jS0hLEpgMJ58wk holds it for Ivan, who is asleep. No authority behavior or oracle may change without an attributed owner decision. Source own observations of the exact8224829a input bundle are now retained in runs/authority-issuer-native-first.json: same-issuer selects currentd3, foreign middle leaves ambiguousd1/d3. All closed input/operation/query shapes pass; complete records/runtime/policy/captures/backup unchanged. Both are un-oracled observations outside exact denominators, not passes/failures.

Kernel5.3 own ordered record motivated the independent issuer-local implementation, but does not expressly define what H1's explicit predecessor citation of H2 endorses. The supplied foreign edge could be a causal reference or an accepted global ordering attestation;5.1 sequence ownership alone does not choose because both decision endpoints remain H1. Preserve the two readings and owner's decision boundary; do not convert reviewer preference into a new integrity rule or a code fix. The source's same-issuer correction051 remains closed.

## ASTRA22-09 erase changed-context priority probe (unclassified)

Read the released K-API-1/K-ERASE-2 and original ASTRA25-07 context/replay rationale. Own native S20-derived probe first erases with private/read and retains a receipt listing both authorized refs. Same actor/space/key with only receipt purpose changed to ungranted returns not_authorized because the implementation applies stored-ref metadata replay gating before comparing canonical intent. The identical changed context under a fresh key succeeds with refs=[] and full purge. Both operation shapes validate; the wrong-priority candidate preserves full state. Exact inputs, receipts, before/after and product hashes: runs/erase-changed-context-first.json.

K-API-1 explicitly calls changing receipt_context under the same identity a conflict, while K-ERASE-2 permits empty metadata-authorized receipts without denying erase authority. Recommended reading: compare intent after current operation authority; test stored receipt metadata only on exact replay. Request judge classification rather than silently changing the order. Alternative broad authorization-before-conflict reading is retained as a question; this native observation has no imposed exact oracle and is outside vector/control denominators. Existing exact revoked replay and authorized changed-context controls remain green. No foreign evaluator code read or executed.

## R7-056 initial availability correction (in progress)

Judge $JwiSCClsftcbsOR8UrOJoe2h7NZWY12YYcjSgWm4S6c classifies ASTRA22-08 as source impl-bug: the owner-admitted public transition must take effect regardless of how initial state was reached, preserving records, policy pins, grants and unrelated state. No owner ambiguity. Add all four available/degraded transitions with complete state comparisons and existing non-owner/undeclared controls, then update current public availability alongside the existing availability stimulus. Original dbf4892 native red and all exact vectors remain unchanged. ASTRA22-09 priority question is a separate pending unit.

## R7-056 correction verified

set_availability now updates the admitted current public_availability as requested, alongside the existing runtime availability stimulus. It leaves policy revision, grants, records, cuts, receipt inventory, erasure state and captures unchanged. All four initial/requested state combinations pass complete-state and exact public result checks. The expanded pre-fix matrix exposed two stale public-state fields (available->degraded and degraded->available), while the original observable query failure is only the latter; this is the same056 defect. Expanded red is retained in runs/availability-transition-matrix-first.json; original dbf4892 native witness is immutable.

All125controls pass (120native plus5comparator), including five availability and eight erasure groups; full output and module hashes in runs/availability-controls-corrected.json, logs availability-current-*-01.log. Canonical57/57 and all61explicitly migrated supplemental semantic vectors remain exact (phase2-availability-corrected.* and cases-corrected.*); deployment8+1unsupported. Independent pre-fix canonical/supplemental and first-red corroboration received from24/25/26; current correction awaits judge. ASTRA22-09 erase-context priority remains separately pending, unchanged. No package/oracle or authority edit.

Judge round31 signed13e3d73 independently verifies source dbf4892 full canonical57/57 and supplemental61/61, including exact report/input/module hashes, and closes package053@23b4d74. Source056 correction87beb46 remains under independent review; ASTRA22-09 priority classification is pending. Both readers' current canonical coverage is complete, while deployment stays unsupported and055 remains an owner question.

Reproduction limitation documented: run_vectors --package selects external vectors/profile, but transaction Shapes defaults to this checkout's memory/spec. Historical grammar-changing runs therefore require a matching isolated package checkout, not --package alone. Current025reports and judge reproductions use matching live025grammar. This is a CLI limitation outside the mission's default full-package entry point; no alternate-grammar compatibility claim is made.

Independent reviewer26 signedee9843989930a4720d6b6f090db1eafc24e988cf verifies056 correction with all five availability groups, full four-transition/state matrix and exactS27; broader canonical/supplemental evidence stays pinned to the earlier fullcoverage review. Reviewer25 signed5fbc523 reproduces both purpose and audience versions of ASTRA22-09: source not_authorized versus package idempotency_conflict, with unchanged complete state and original receipts. Exact authorized/revoked replay, foreign actor and fresh-empty-ref controls agree. Editor concurs that metadata gating applies only to exact replay. Judge classification remains required before changing priority; no external oracle is edited.

## R7-057 erase-context priority correction (in progress)

Judge $eZJtQ5NtpfBEb7qFsk54ePTdCFPWyGbT_S4eBcV9FM8 classifies ASTRA22-09 as source impl-bug. After current erase operation authority passes, different intent under the same identity must refuse idempotency_conflict,false; stored-ref metadata is checked only for exact replay. Current metadata loss must still refuse exact replay without changing the original receipt/state, while fresh authorized empty-ref erase remains valid. Add purpose/audience neighbors, operation-authority precedence, read/use/metadata replay loss and immutable empty-receipt controls before reordering. Original0529814 and independent5fbc523 firsts remain unchanged; no owner or package change.

## R7-057 correction verified

Erasure now compares canonical intent after current operation authority and before stored-ref metadata authorization. A changed request returns idempotency_conflict,false; only identical replay reauthorizes the original receipt refs. The exact unchanged0529814 input now yields the required full typed conflict with complete state and original receipt unchanged; its fresh-context request still succeeds with empty refs (runs/erase-changed-context-corrected.json).

Three new erasure groups initially expose five wrong-code failures, retained in runs/erase-priority-controls-first.json. All eleven erasure groups now pass: both context dimensions, lost erase authority before replay/conflict, exact read/use/metadata denial, fresh empty-ref success, immutable empty receipt under broadened rights, and previous custody/restore/late-writer invariants. All128controls pass (123native plus5comparator); full green logs/module hashes are runs/erase-priority-controls-corrected.json. Canonical remains57/57. Original61-case corrected run is retained; author66233ab adds two independently frozen exact057regressions, and all63current semantic supplements pass unchanged (phase2-erase-priority-cases-current.*). Their pre-fix source failures are retained by the author. Deployment8+1unsupported.

Judge e2a797d/$negeVtwsRGIiMJJzOQ7Zeh4IZXRjFQxEv29YhCzxQ84 closes056@87beb46 after exact full canonical/supplemental and125control reproduction. Source057 correction now awaits independent review.055 remains a filed owner question held for Ivan; no authority change or mixed-issuer oracle. Current historical-grammar CLI limitation is documented explicitly, without changing current025validation.

## ASTRA25-12 current external restore obligations (in progress)

Author 644c793 preserves four native traces for current erasure obligations absent from the old snapshot, with an unreachable controlled sink, a known local obligation and a genuinely empty current obligation as neighbors. Reproduce only the original input fields against unchanged source 946cbd8, preserving raw outputs, complete mutable state, backup and module hashes without imposing a new oracle or including observations in exact-vector denominators. No foreign evaluator implementation is read or executed. Judge classification is pending; no source correction is proposed.

Judge e3d44df / $gEHHYy2OeM-zzow_LLsQk2oL17CygOcHKE1ZmXyb1wI closes R7-057 at 946cbd8 after exact 57/57 canonical and 63/63 supplemental reports, all 128 controls and independent native neighbors. Current rubric was 2/2 at that closure, but ASTRA25-12 remains pending intake and the convener explicitly holds PARK until adjudication. R7-055 remains an owner question.

## ASTRA25-12 own reproduction preserved

All four original input bundles reproduce on unchanged source 946cbd8. The newly witnessed A enters the erasure/fence sets, increments the generation, purges both controlled sinks and leaves an empty view. With an unreachable affected sink, current reconciliation returns erasure_incomplete/true with complete state unchanged; global restore status stays fenced and query returns erasure_fenced/false. The known local obligation also purges both sinks; a genuinely empty obligation set reopens A. Every false-witness refusal and every query preserves complete adapter data state, including initial snapshot, records, policy, runtime, captures, backup, schemas and rules.

Evidence: runs/restore-current-obligations-native-first.json contains the exact original inputs, raw outputs, deduplicated full states and hashes, embedded reproducible probe, closed-shape results and all 22 module hashes. Input bundle SHA-256 is 46da699c9c8ef6c52ebd9fa8bc7efe6bf519b8ad1b8174afe98abc34abbd3894. Every module matches signed source 946cbd8; no evaluator code changed. The source and package portions of the author's original file carry identical inputs, but only this source implementation was executed. These are native observations outside exact denominators, pending judge disposition. No new oracle, physical purge or real external witness verification is claimed. Scratch command output: .temp/astra-22/restore-current-obligations-01.log.

## R7-058 newly learned obligation late-writer control (in progress)

Judge $M8NvqvBJqj0P6G_HX3wtl3-FVKIbSUxxSZFXB9YCyvE classifies ASTRA25-12 as package implementation bug and explicitly requests late-writer neighbors. Source behavior and package prose remain unchanged. Add a focused native control for a current external obligation absent from local erased/fence state: successful reconciliation must advance the generation, then reject both the old-generation derivative and a current-generation derivative of the newly erased input without state mutation. Pair with an independently derived authorized write under the current generation. This tests the new-obligation recovery path rather than only the existing erase path; it does not invent a write prohibition during the earlier read-only restore fence. The collective score is 1/2 while R7-058 remains open.

## R7-058 supplemental intake and late-writer control verified

Author 1cefcf9 publishes five exact restore regressions: new external obligation, unreachable sink, known local obligation, genuinely empty obligations and unaffected independent B. The first full expanded source run passes all 68 semantic supplements; one deployment vector remains unsupported. Evidence is runs/phase2-restore-obligations-cases-first.*; all original fixtures and native firsts are unchanged. Canonical remains 57/57 on the identical product implementation.

All 12 erasure groups pass, including the new current-obligation recovery group. Successful reconciliation from an empty old erase inventory advances generation to 1 and records A in erased/fences. A derivative with generation 0 refuses stale_generation; the same derivative with generation 1 refuses erasure_fenced. Both preserve every adapter attribute. A valid independent proposal with generation 1 is admitted, while A remains erased. Evidence is runs/restore-obligation-controls-first.json; the exact command and full output are retained. Only erasure_checks.py changed among the 22 modules; product bytes and the other controls still match 946cbd8. Coverage totals 129 controls using this focused 12-group run, the five comparator controls executed by the full supplemental run, and prior green evidence for the unchanged remaining groups. This is not a claim that every control was re-executed in this unit.

## R7-058 judge closure and quiet source round

Read signed judge 9d2cdd4, ledger round 37 and decision $nsF9IkEi8RS8EYEoyd2_KCftr7-6ElE8hlROAcvZxOk. Package correction 104fbe8 is closed after full 57/57 canonical and 68/68 supplemental reruns, 34 package controls, original four restore traces, three unchanged late-writer probes and seven intended pre-fix control failures. All initial inputs and first failures remain unchanged.

The judge independently matches this source's expanded 68/68 report, reruns all 12 erasure groups from b8189ba, and verifies every other module against the prior reviewed pins. Source green coverage is 129 with the focused/prior evidence boundary stated explicitly; product remains 946cbd8. Ledger has 58 items: 47 fixed, 10 rejected and owner question R7-055. No specification or implementation bug remains open, and current rubric is 2/2. This round adds no case, divergence, package change or evaluator change. R7-055 remains un-oracled and held for Ivan; deployment 8+1 remains unsupported. Await the convener's quiet-round/PARK decision; this closure alone does not end the active session.

## PARK finalization

Convener decision $698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg at 2026-10-17 06:33Z confirms the full-dual-plus-quiet-round condition and instructs final verdict, park note, signed publication and rounds acknowledgement. Wait-77 returned normally; no wait or worker remains. Read the final judge score and ledger after pulling 962a21d. Final score is 2/2, both readers pass 57/57 canonical and 68/68 supplemental, source control coverage is 129 with explicit reuse, and deployment 8+1 is unsupported. Ledger has 47 fixed, 10 rejected and owner-held R7-055. No owned implementation or review work remains.

Final documentation updates only verdicts/astra-22.md, parked/astra-22.md and this worklog. Runtime, tests, package, fixtures, original first failures and report artifacts are preserved. Verify local handoff links, current input/module hashes, exact report totals, own diff scope and signed commit before publication. The park note preserves the owner decision boundary, unmapped non-canonical paths, deployment limits and historical grammar limitation; it makes no broader completion claim.

Final narrow validation passed: both report totals, all 134 current vector input hashes, all 22 runtime/test module hashes, unchanged source run artifacts and package tree, all final handoff links and exact owned documentation scope. Evidence is .temp/astra-22/park-doc-checks-01.log. No executable change required another product test run.

## Reopened R7-055 / D-009 round (in progress)

User and convener event $7qVXDb4qnZcORPIQr_qJeUzKFAj9Md3ZRI_VLpdOSKk reopen one bounded round. Read D-009 and kernel v0.3 section 5.3 at 2c3100d, plus the complete approved reviewer formulation. The owner selects reachability in the induced canonical issuer-H event graph, including assertion-free events, for currentness and strict succession. Foreign nodes are not contracted, one all-H path suffices, foreign branches cannot cancel it, and mixed snapshots remain admissible. Missing order uses existing ambiguity/write refusal contracts. Foreign-only graph changes must preserve the H relation.

Source inspection finds the existing projection, CAS-head and strict-successor traversals already issuer-local on admissible snapshots; no runtime change is currently indicated. Track a focused source-only control expansion before implementation: original separating pair, assertion-free chain, mixed chain plus direct H path, no-contraction/foreign-edge variants, currentness/CAS/succession consistency, replace/correct positive and atomic refusal paths, protected attribution and foreign-part invariance. Freeze the unchanged first results before any correction. Rerun every source control and all canonical/supplemental vectors after 0.2.6 lands. Do not edit author fixtures or read the other evaluator. Current round remains active until new PARK, latest 22:30Z; stale prior PARK does not end it. Push races use signed pull/rebase and push retry without bundles.

## D-009 source-only first controls verified

All 134 controls were freshly executed and pass (129 native plus five runner comparer controls), including five new D-009 groups. No runtime or existing test module changed: all 22 previous module hashes still match b8189ba evidence. New controls exercise the exact original owner pair; protected event attribution versus the receipt envelope; assertion-free own intermediates; foreign bridge refusal/no contraction; mixed branches plus a direct own path; foreign-only issuer/edge invariance; all 256 acyclic four-event graphs with two own endpoints and two variably attributed assertion-free middles; and real replace/correct acceptance or exact authority_receipt_required/false with full adapter state preserved. The bounded matrix oracle derives reachability independently by Boolean transitive closure on the induced H graph and checks projection, CAS head and succession together.

First complete outputs, source/input hashes and all module hashes are runs/d009-source-controls-first.json; the first dedicated five-group output is retained verbatim there. All controls were run before reading or executing a 0.2.6 package. A bounded in-memory global-order plant is detected by the original mixed pair with exactly one intended currentness assertion failure and no errors, while its all-H positive passes. runs/d009-comparator-plant.json retains the exact mutation, complete output and reproducible probe; source/input files remain unchanged. This plant is outside the 134-control count and is not a product divergence. No source correction is needed based on these outcomes. Exact 0.2.6 canonical and supplemental results still await release.

## Historical supplemental regression boundary

Judge $T3geWSIeugXFXieLavTd2PqZrqdGaWZMsmQtPS3UAk8 / $vYHd-EHHPDoXgQcswryF_nzEi_nkdhIfhGpVv7nLZuw requires unchanged 68 semantic supplemental fixtures against frozen 0.2.5 grammar; this is separate from canonical 0.2.6. No migrated oracle is required. Run now before the release pull, verifying the entire live memory/spec tree equals 6a04e8c and recording the unchanged runtime hashes. This satisfies the source runner's documented grammar boundary; --package alone would not isolate an older grammar after a later pull. Any later changed-runtime historical rerun must use a matching isolated checkout.

Fresh historical regression passes 68/68 unchanged semantic cases, with one deployment unsupported. runs/d009-0.2.5-regression-first.* preserves exact actuals and input hashes; runs/d009-0.2.5-regression-provenance.json pins the full package tree, matching schema hashes, all 23 current module hashes, command and exit code. No source behavior or author file changed. Canonical 0.2.6 remains pending; this historical run is not counted as current-release conformance.

## 0.2.6 first canonical intake (in progress)

Convener PACKAGE LANDED event $WTb-jdx1xZXxlfS2LIDbJgLJbttB8s-9sxOtjCz9uKY authorizes intake of release 77b951e. All 23 source module hashes equal the source-only D-009 freeze abc8511; the live package tree equals the released tree. Run every canonical vector without implementation changes and preserve runs/0.2.6-first.* before any alignment. Then freshly rerun all 134 controls on the live matching 0.2.6 grammar. Historical supplemental coverage stays separately pinned to unchanged 0.2.5 inputs and grammar in 0bf20dc. Any new mismatch goes to the judge before correction.

First unchanged 0.2.6 canonical result: 66 semantic pass, zero fail/unsupported; eight deployment unsupported. All 23 module hashes equal abc8511. Validator passes 103 JSON, 74 vectors, 52 clauses and 38 intended checker controls. First complete 134-control rerun has 133 pass and one failure in boundary_checks.test_excluded_record_has_no_forwarding_effect: exactly two semantic_profile fields expect frozen 0.2.5 while live execution emits 0.2.6. No behavior difference is reported; the first assertion stops before the paired second fixture. Preserve runs/d009-0.2.6-controls-first.json and report to judge before adjusting this historical fixture control. All five D-009 groups pass. runs/0.2.6-first-provenance.json pins both first reports and the complete source module inventory. Runtime and author fixtures remain unchanged.

## R7-059 historical control profile binding (in progress)

Judge decision $uu1YAT4x6_6pzGAo0MiCwVPWZMPoXTpBNGZi3c1Nc3Q classifies the one first-control failure as an owned harness impl-bug, not a product-semantic discrepancy. Both historical ASTRA26-08 variants independently differ only in two expected semantic_profile fields. Correct the boundary control using explicit scratch copies with only those two labels advanced from 0.2.5 to 0.2.6, fixed old/new profile guards, recursive no-other-change verification, and original/copy hashes. Preserve original case bytes and 31d77d2 first reports. Rerun all 134 controls and canonical vectors; no runtime or behavioral expectation edit.

## R7-059 correction verified; source 0.2.6 green

Only boundary_checks.py changed. Its paired historical exact controls now create scratch copies with two expected profile labels migrated explicitly, enforce fixed 0.2.5/0.2.6 guards, recursively restore-and-compare every field, record original/copy hashes, execute the saved copies, and verify original bytes after execution. Both variants run as subtests. Independent recursive diff confirms exactly those two metadata changes per copy; a bounded in-memory query-actor plant causes both intended recursive-guard failures and zero errors before execution. The comment distinguishes migrated metadata from unchanged behavior. Evidence is runs/r7-059-profile-migration-audit.json; originals and all 31d77d2 first reports remain hash-identical.

All 134 controls freshly pass on live 0.2.6 (129 native plus five comparer controls), and canonical rerun passes 66 semantic with eight deployment unsupported. Entire canonical vector rows are identical to the first run; only checkout_commit metadata differs. Current RESULTS.* mirrors runs/r7-059-canonical-corrected.*. All 22 other Python modules equal abc8511, so runtime remains 946cbd8 and the independently verified frozen-0.2.5 68-case regression remains applicable. No original fixture, behavioral expectation, package or product code changed. Judge closure of R7-059 and R7-055, package alignment and the quiet-round/new-PARK gates remain pending.

## Judge closure and source quiet round

Judge signed75c13d229f036ffe1639096cd9ff89926bad73b8 (G), event $b8foGPG6rv8TSQqyaHjhJUZkyLIBXmTKrWxuZv4cPSs, resolves R7-055 by owner D-009 and closes R7-059@c7e86d5 after independently reproducing both66/66canonical reports, historical68/68regressions, all134sourcecontrols and the migration audit/guard plants. Source runtime946cbd8 is unchanged; package runtime5897520 has the independently accepted issuer-local correction. Ledger59:48fixed,10rejected,1resolvedambiguity; no open finding, owner question or unclassified intake. Own score2/2 matches the judge. Source has no new divergence, case, implementation edit or directed request. Preserve the current release77b951e and all reviewed evidence; enter the required quiet round and wait for new convener PARK. This is not yet the final park handoff.
