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
