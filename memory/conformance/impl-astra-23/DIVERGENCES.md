# astra-23 observed divergences

## First-run baseline: 0.1.0-draft at 0ef608a

Frozen report and implementation committed at `0008dc3` before external semantic
intake. `FIRST-RUN.md` / `FIRST-RUN.json` remain unchanged.

- **R7-019 (B03/S23): spec-bug.** The evaluator returns `last_received` for both
  `/result/currentness` and `/result/items/0/currentness`; expected is `current`.
  Judge: apply imported-publication currentness to actual publication associations,
  not the admission class alone. Await released K-PUB-2 clarification. Topic
  `div-astra23-import-currentness`.
- **R7-020 (S30): impl-bug.** Closed declared coverage uses `ref`; the evaluator
  used `declaration`. Corrected to `ref`; regression and wrong-field checker plant
  in `test_semantics.py`. Topic `div-astra23-coverage-field`.

## 0.2.0-draft at cde5754: B01 missing integration fact

The v0.2 evaluator enforces K-DISC-1: every proposal requires exactly one
`policy.lineage_facts` entry. B01 revises `rec:d/1` to `rec:d/2` with a new
`rec:decision-replace/1` revision. Its facts include `rec:d/2`, but omit the
revision. Actual `/operation_results/0` is `invalid_reference` with no writes;
expected is a successful `revised` receipt. The subsequent query at cut 102 is
therefore `invalid_time`, and dirty/reference postconditions remain at baseline.

An isolated positive control adds only the missing direct complete integration
fact for `rec:decision-replace/1`; the exact original expected report then passes.
The negative control removes that fact and verifies the intended refusal plus
identical state. The package vector is never edited. See
`test_semantics.py::test_b01_lineage_fact_control` and the exact RESULTS reports.

Judge **R7-021: spec-bug**, editor astra-21. The judge independently
reproduced the missing-fact refusal and isolated positive control. The structural checker was green on this package and did not catch the
missing proposal integration fact.

## Supplemental cases, kept separate from canonical totals

The current evaluator was exercised against each case without implicit migration:
0.2.0 grammar admits eight cases (7 pass, ASTRA26-06 differs); the original 0.1.0
grammar admits nine others (7 pass, ASTRA24-03 and ASTRA25-05 differ). A case not
in the selected grammar is explicitly unsupported in that report, not a pass.

- **ASTRA26-06 / R7-022: spec-bug.** Foreign self-declaration is admitted under
  the current package. Judge requires explicit identity evidence and correct
  organisation-attestation typing in the next release. No silent evaluator fix.
- **ASTRA25-05 / R7-018: spec-bug.** Global dirty produces observable dirty
  cutoffs, missing witness and review flags after a hidden revision. The visible
  dirty positive control passes. Wait for package projection-scoped dirty rules.
- **ASTRA24-03/04 / R7-023: impl-bug, corrected in round 3.**
  Channel source-state aggregation already matches the proposed mixed AND and
  stronger OR controls, but `/operation_results/1/items/0/source_refs` and
  `/result/items/0/source_refs` omit `rec:s/1`. The evaluator currently gathers
  only directly associated sources, not the sources on found derived paths.
  Exact reports: `SUPPLEMENTAL-0.1.0.md`/JSON; no vector/expected edits.

R7-023 correction propagates the sources on found proof paths into the item.
Ten controls now pass, including the previously red exact-ref regression and
direct/derived, hidden-source, failed-path and unrelated-copy boundaries. On
migrated 0.2.0 cases the current supplemental result is 17 semantic pass / 2 fail
(R7-018 and R7-022); one deployment case remains unsupported. The original
pre-correction reports and source hashes remain in commit 103ce15.

## First adapted 0.2.1 run: unrelated history for an explicit target

Package f31d58f: 55/57 semantic pass, two field differences (B07/S24) at
`/operation_results/3/historical`: actual includes `rec:hidden/1`, expected `[]`.
The private-authorized dirty control explicitly selects `rec:a/1`, a different
multi-valued sequence. K-EVAL-9 says historical references are in the requested
selection's sequences. Current code gathers all visible same-schema history.
Judge **R7-024: impl-bug**, owner astra-23. The wider private projection is a valid
positive control that may include `rec:hidden/1`. The exact regression is red
before correction; no expected report or package vector was changed.
Preserved report: RELEASE-0.2.1-FIRST.md/JSON.

R7-024 pre-fix head is signed `bc342e1`. Correction restricts explicit-target
history to selected sequence identities. Unfiltered selection, explicit historical
items and hidden-reference boundaries remain covered. Package 0.2.1 is now
57/57 semantic pass; all thirteen checker/product controls pass. Judge commit
6a4f307 independently reproduces both heads and closes R7-024 fixed@f5fdd8b.
The same review closes package fixes R7-014/018/019/021/022 at f31d58f. All
current supplemental semantic cases pass (19/19) in d2c38ac. No deployment claim.

## Phase 2 ASTRA25-07 — erasure receipt discloses protected closure metadata

Case commit 77ea085; unchanged runtime f5fdd8b on package 0.2.1 f31d58f.
Primary case fails `/operation_results/0/refs/length` (2 vs 1) and the extra
`/operation_results/0/refs/1` (`rec:summary/1`); the explicit hidden-id forbidden
predicate also fails. The exact metadata-authorized positive control passes.
Protected erased refs, custody disposition, purge outcome and final empty view
match in both cases. This does not request weakening the full erasure closure.

K-API-1 requires authorized receipt refs, while K-ERASE-2 unqualifiedly says
full fenced closure. Judge classified **R7-031: spec-bug**, owner astra-21.
The release must declare receipt recipient/audience/purpose or an equivalently
explicit admitted scope, with pre-fence authorization and no later-query or
unrelated-purpose inference. No separate implementation bug is assigned for
following the contradictory clause; runtime alignment awaits that release.
Immutable first evidence: PHASE2-ERASURE-FIRST.md/JSON. Current supplemental
result: 23 pass / 1 fail / 0 unsupported semantic, one deployment unsupported.
Topic: `div-astra25-erasure-receipt`.

## Phase 2 ASTRA26-07/08 — checked import expiry and selected delivery

Case commit 837591e; runtime still f5fdd8b, package f31d58f. First report is
PHASE2-IMPORT-DELIVERY-FIRST.md/JSON, before any correction or classification.

- ASTRA26-07: at the exact usable_until horizon, view/item currentness wrongly
  remain current instead of last_received. Fresh capture passes; support and
  stale freshness otherwise match. Both forbidden current predicates fail.
  K-PUB-2 requires an unexpired horizon. Judge classification is pending.
- ASTRA26-08: the first delivery returns disclosure_revoked rather than the
  expected delivered receipt because an excluded unrelated same-schema record
  lacks forward rights. Its additional-forward positive control passes; later
  selected-item revocation still refuses. K-PUB-1 binds the prepared selection.
  Judge classification is pending; no broadened permission is proposed.
- ASTRA24-07: Cartesian exact proof-reference sets, truncation and separately
  deduplicated origin counts all pass. Retained as Phase 2 regression evidence;
  the source evaluator's corresponding execution is still pending expansion.

Current full supplemental result: 25 pass / 3 fail / 0 unsupported semantic,
including the already classified R7-031 erasure receipt defect; one deployment
case unsupported. Canonical baseline remains 57/57. No expectation was edited.

### R7-033/034 correction and neighboring controls

Judge classified import expiry R7-033 and selected delivery R7-034 as package
implementation bugs. The first red report remains f83268d. Focused tests first
reproduced both failures, then pass after the narrow corrections: stale imported
publication horizons downgrade to last_received; forward checks use the exact
prepared selected refs in the current evaluation context.

Before/at/after expiry, absent checks, known replacement, nonpublication
currentness, unchanged evidence/origin and immutable capture controls pass.
Selected read/use/forward removal, fencing, stale publication, owner-release
revocation and later selected forward revocation retain their refusals. The
unrelated excluded record no longer vetoes valid delivery. Sixteen checker/product
tests pass; canonical remains 57/57. Independent closure of this new head pending.

## Phase 2 ASTRA25-08 — retention right absent while derivative admission succeeds

Queued intake from case 2de226c reproduced after the unrelated R7-033/034 fixes;
admission code is unchanged. The primary returns admitted and stores
rec:paraphrase/1 instead of not_authorized with the original inventory. Twelve
exact field differences and both forbidden predicates reproduce. Restoring only
retain rights yields the expected admitted positive control. The historical query
passes, so this is not a future-cut error masquerading as rejection.

First report PHASE2-RETENTION-FIRST.md/JSON pins these inputs and runtime hashes.
K-AUTH-1/K-DISC-1 retain-authority boundary awaits judge classification; no silent
admission correction or expected-value change. Current supplemental corpus:
28 pass / 2 fail / 0 unsupported semantic (R7-031 plus ASTRA25-08), one deployment
unsupported. Topic: `div-astra25-retention-authority`.

### R7-037 classification and precise admission-scope gap

Judge classified ASTRA25-08 as package impl-bug R7-037 (source R7-036).
The no-retain witness is decisive: it must refuse atomically and remains frozen
at f10c7ba. Implementing the required scoped neighbors exposes a narrower missing
package rule, not a reason to deny that established implementation defect.

Evidence in 0.2.1 f31d58f:

- K-AUTH-1 grants match principal, space, audience, purpose and record id. An
  operation grant does not bypass per-record retention. K-DISC-1 integration
  facts grant no retain right; transitive input constraints continue to apply.
- All four closed admission contexts (admit_raw, admit, revise, declassify) in
  vector.schema.json contain exactly actor, at and admission_class. They carry
  no retention audience/purpose or admitted scope reference.
- Proposed/effective labels contain sets of permitted audiences/purposes, not
  a selected authenticated retention intent. K-DISC-1 also permits a record with
  an empty disclosure intersection, so treating visible disclosure as the sole
  authority to store it would require a separate rule.
- No package prose specifies an existential versus universal grant obligation
  over these sets, a per-output/input scope mapping, or another fixed write
  scope. A later query is a separate request and cannot supply missing intake
  authority retroactively.

A separating neighbor of ASTRA25-08 grants retain only to the exact actor/space
and records, for aud:private + purpose:read, while the input and effective output
permit both read and publish. Existential matching over their labels accepts;
requiring authority for every labelled purpose rejects. Both readings reject the
original no-retain input and accept its all-retain positive control. The existing
operation context selects neither. Fixture fragment is persisted at
`.temp/impl-astra-23/retention-scope-01.json`; no expected verdict is invented.

Needed before the complete scoped correction: a published deterministic rule
binding admission retention authority to an explicit operation/admitted scope,
or an exact defined relation to each output/input label, including empty labels,
live revocations and transitive known/unknown lineage. Explicit scope enables
purpose-specific rejection; a label-based rule needs a declared quantifier and
must preserve the stated non-disclosable-record contract. A space-wide any-retain
shortcut would fail the judge's unrelated-purpose/record negative requirement.
Requested judge/editor disposition; runtime remains unchanged pending that rule.

### R7-031 adaptation to released 0.2.2

First new-release failure is immutable at 0ca2d27. Current correction passes P08
and all 57 canonical semantic vectors. Exact actor/audience/purpose/record/space
read and use grants with metadata, live revocations and effective disclosure now
filter receipt refs before the new fence. Existing fences do not suppress approved
structural refs; complete protected erasure and custody are unchanged.

Additional controls cover erase-only authority, missing use or metadata, unrelated
principal/space/record/audience/purpose, disclosure restrictions and expiry; every
case retains full purge. Later-stamp retries preserve the receipt, broader grants
do not expand it, changed scope conflicts, and revoked/expired authorization
refuses with unchanged state/idempotency. Eighteen product/checker controls pass.
Independent review and explicitly migrated adversarial erase cases remain pending.

Judge independently closed R7-033/034 at f10c7ba. The exact retention wire gap
above is now spec-bug R7-039, editor astra-21, separate from R7-037. The package
must publish storage scope before the complete scoped retention correction;
no new authorization reading is inferred locally.

## Phase 2 R7-041 — authority-slot compare-and-set

The first full 0.2.2 supplemental report PHASE2-CAS-FIRST records unchanged
revision code accepting both an incomparable current candidate and an ordered
historical candidate as the head. Each has eleven exact differences and two
forbidden-effect failures: a revised receipt and a seventh stored record.
Unique-head and challenge controls pass. Judge classified this as R7-041.

K-REV-1 and K-REV-3 require the unique current authoritative slot head determined
by admitted receipt partial order, before comparing expected_version. Preserve
exact idempotency replay precedence and challenge exemption; refusal must leave
records, cut, dirtiness and idempotency unchanged. No additional package rule is
needed. The next correction will be grounded in those released clauses.

Current migrated supplemental is 35/3/0 semantic; one deployment unsupported.
R7-037 is the third failure. R7-031 migrated primary, purpose-isolation and full-
authorization controls pass at a016781, as do unknown-lineage lower-bound erase
and future-input operation controls. Independent judge closure remains separate.

### R7-041 correction

The unique authority head is now selected across the whole decision sequence by
receipt partial order, excluding withdrawals, before non-challenge CAS comparison.
Projection and write checks share the existing sequence/receipt-order rules.
Atomic full-state and dirty-state checks pass for ambiguous and historical cases;
unique ordering, challenge, reversed storage order, exact replay, changed-intent
conflict and the next remaining unique head after withdrawal all pass.

Canonical 57/57 and nineteen product/checker tests pass. The same 38-case corpus
is now 37 pass / 1 fail / 0 unsupported semantic, with only R7-037 remaining.
PHASE2-CAS-FIRST at e525612 is unchanged; independent closure is pending.

## Phase 2 ASTRA26-09 and ASTRA24-09 — first exact failures

PHASE2-COVERAGE-REVIEW-FIRST pins runtime53266dd and 0.2.2 inputs. The new
import-coverage primary has exactly two differences: item/view are current
instead of last_received when one exact associated publication lacks its check.
The explicit-unverified and all-checked neighbors pass. K-PUB-2 requires the
exact publication check; K-DISC-3 origin deduplication does not transfer authority.

The transitive-review case omits only rec:dependent-c and its list length from
review_required, while both hidden-path public controls pass. K-EVAL-8 requires
transitive registered impact independently of cleared recomputation dirtiness.
The source result is not used to define either oracle. Judge classifications
are requested; no implementation correction has yet been applied.

Full42-case supplemental:39 pass / 3 fail / 0 unsupported semantic; one deployment
unsupported. R7-037 is the third failure. Canonical57/57 remains the last checked
baseline; R7-041 corrected family remains green. All first reports stay immutable.

### R7-044/045 classified corrections

Judge classified ASTRA26-09 as R7-044 and ASTRA24-09 as R7-045. Exact publication
coverage now checks every authorized associated object, preserving same-origin
counts and all source refs. Missing each of the three check facts downgrades
currentness exactly like explicit unverified; a hidden publication has no effect.
Existing expiry, replacement and ordinary-document boundaries remain covered.

Review traversal now follows eligible registered impact paths with a retained
review-on-change obligation. Both mixed orders (review then sufficient, sufficient
then review), pure transitive review and a bounded review cycle pass; pure
sufficient/documentary paths and hidden necessary elements/certificates create no
extra review. Selected evidence stays unchanged and the state is never dirtied by
this read. Exact fixture/forbidden checks and all22controls pass. Canonical57/57
and pinned42-case supplemental41/1/0 are retained. Independent review is pending;
first08c4b9a is immutable. The remaining supplemental failure is separate R7-037.

## Phase 2 R7-046 — ungranted actor reuses a saved delivery binding

PHASE2-ACTOR-FIRST preserves the first exact package result on frozen0.2.2 at
runtimef6c339d: ASTRA26-10 incorrectly returns delivered, nine differing fields
and one forbidden receipt. Rightful delivery, later selected revocation, frozen
capture and state otherwise match. Judge already classified R7-046; no delegated
publisher API is inferred from this ungranted-actor case. Correction is next.

## 0.2.3 retention release first result

RELEASE-0.2.3-FIRST preserves55/2/0 semantic and8deployment unsupported before
adaptation. P11/P13 are the only failures. The released context resolves R7-039,
so R7-037 can now be corrected against an explicit storage scope rather than a
label quantifier or later query. All prior first reports remain unchanged.

### R7-046 correction

The delivery actor must match the saved projection's authenticated principal
before the stored query/binding can authorize any delivery check. The exact
ungranted-actor witness now refuses without changing records/runtime/captures/
view bindings/dirty-since. Rightful delivery, current selected revocation and
invalid audience/purpose/index controls pass. No hypothetical delegated publisher
API is added or used to weaken this boundary. First5416283 remains immutable;
independent correction review is pending.

Pinned0.2.2:57/57canonical,43/1/0 supplemental,23controls; deployment8+1unsupported.
Current0.2.3:55/2/0canonical before the separate scoped-retention correction.

### R7-037 correction against released0.2.3

Exact actor/space/record/audience/purpose retain authority now gates every proposed
output and transitive known integration input, including incomplete-lineage lower
bounds and whole-batch inputs. The guard reads protected facts, not model citations,
and does not use onward disclosure labels, metadata permission or a later query.
Missing inputs remain typed reference failures at the published stage. Current
retain revocations block new writes and unchanged receipt replay atomically; the
stored original outputs/input closure is rechecked and the stored receipt is intact.

All four write APIs have unrelated-record retain negatives and restored-grant
same-key positive controls. Exact-scope, unknown-ancestor, future-input, same-batch,
empty-label, changed-context and revoked-replay cases pass with full no-write state
checks. Twenty-six product/checker controls,57/57canonical and46/46supplemental
semantic vectors pass under0.2.3. Deployment8+1 stays unsupported. First5416283,
6861fec and originalf10c7ba failures remain unchanged; judge closure is pending.

Judge separately closed R7-044/045 atf6c339d and specification039/042 at23290b3.
Actor-binding046 has adversary verification at7b9f0dd, pending judge disposition.

## Phase 2 ASTRA24-10 — authoritative replacement without strict receipt succession

Own first observations PHASE2-SUCCESSION-FIRST on runtime4af0360 reproduce both
accepted forbidden replacements: an incomparable receipt and reuse of the old
receipt. Each commits d2+revision, cut100->102, dirtiness and one idempotency entry;
ordered control also succeeds. Shapes validate, and full state/input/runtime hashes
are retained. K-REV-3 requires strict succession for replacement. Plain canonical
incomparable import remains a distinct valid behavior.

No exact typed refusal oracle is yet asserted: K-REF-1's canonical-receipt wording
needs judge/editor disposition for an existing but non-successor receipt. Await that
mapping before correction. Current vector pass counts exclude these new probes.

### Independent retention and actor closures

Judge closed R7-037 at4af0360 with exact0.2.3 canonical/supplemental reproduction,
all26controls and unchanged first evidence. R7-046 is separately closed at3ce8ee3,
including frozen0.2.2 and migrated0.2.3 actor/binding controls. The authority-succession
probe at47c0205 remains a separate pending classification/code-mapping issue.

### R7-048/049 classification

Judge decision at2026-10-17T05:18:07Z classifies the accepted writes as R7-048
(package implementation) and the exact code wording as R7-049 (specification).
The adjudicated code is authority_receipt_required/retryable=false for a missing
qualifying strictly succeeding canonical receipt; CAS mismatch stays separate.
The package-only runtime waits for that published contract and exact fixtures.
Own initial probe47c0205 is immutable. No owner architecture question is needed.

## Released0.2.4 succession baseline and queued deadline probe

RELEASE-0.2.4-FIRST on unchanged4af0360 has56/1/0canonical semantic, onlyB01 red.
The published exact refusal mapping now permits the R7-048 correction. Prior
exact0.2.3 supplemental first0641033 remains49/3/0 across52cases.

PHASE2-DEADLINE-FIRST independently preserves ASTRA25-11 new storage at/after
input expiry and at own output expiry (records1->2, cut100->101, replay receipt).
Before-expiry admission succeeds. Expired exact replay returns the existing
receipt without state writes. All input shapes validate, full states and hashes
are retained; expiry code/order/replay adjudication remains pending. These native
probes are outside vector totals and queued behind the succession correction.

### R7-048 correction against released0.2.4

The shared canonical receipt-DAG traversal now requires a nonempty strict path
for authoritative replace/correct. Missing, prior, identical and incomparable
receipts refuse authority_receipt_required/false atomically; valid same-key retry,
direct/transitive successors, plain incomparable import, exact successful replay
and distinct CAS conflicts retain their contracts. Native before/after comparisons
include entire state, dirty-since, captures and bindings.

All57canonical and54explicitly migrated supplemental semantic vectors pass;
24product+4checker controls and33package plants pass. First47c0205,0641033 and
e689cf2 reports remain unchanged. Independent review is requested; expiry remains
a separate untyped native observation, not silently folded into this correction.

### Retention deadline classification R7-053/054

Judge classifies package implementation053 and exact contract mapping054.
The required boundary is context.at < every applicable non-null deadline;
at/after expiry is not_authorized/false before idempotency, including current
replay checks of original outputs and transitive known input closure. Refusal
must preserve full state/original receipt and has no purge effect. Editor0.2.5
is pending; no deadline runtime change precedes that published contract.

### R7-048 independent closure

Judge de37630 independently closes942bdee after exact canonical57/57,
54/54supplemental,28controls and input/module-hash reproduction. Full atomic
strict-successor/replay/CAS/plain-import boundaries pass, firsts unchanged.
Deadline053 remains separately open and is not covered by this closure.

### R7-053 correction against released0.2.5

Every resolved proposed output and transitive known content input now refuses
when parsed trusted context.at is at or after its own non-null retain_until.
The existing shared retention traversal also checks original stored outputs/input
closure for exact replay. This gate precedes idempotency and traversal deduplication;
null adds no bound. No disclosure-label shortcut, automatic purge or state mutation
is introduced. Valid same-key intake/live replay keep the original receipt.

All four intake APIs have before/equal/after own-output controls and exact expired
replay with entire state/captures/bindings/dirty-since unchanged. P11 independently
unrevoked grants, changed-intent priority, no-new-cut and unlimited recovery pass.
Authored known/unknown/batch expiry negatives and positive neighbors also pass.
Current0.2.5 canonical57/57, migrated supplemental61/61,27product+4checker controls
and34package plants pass. Earlier firste689cf2/0c1b5ca/df58eae remains immutable.
Independent053 review is pending;054 and source052 are separately judge-closed.

ASTRA24-12 mixed-issuer intermediate ancestry is a later native probe awaiting
contract adjudication; its exact output rule is not presumed or counted as passing.

## R7-055 — mixed-issuer canonical receipt ancestry ambiguity

Own PHASE2-ISSUER-FIRST on23b4d74/0.2.5 selects currentd3 for both same-issuer
and foreign-intermediate inputs. Full durable state stays unchanged; normal
view bindings are created. Package A07/K-REV-3 defines canonical DAG traversal
without explicitly requiring homogeneous intermediate policy authority issuers.
No source implementation code was consulted.

Judge classifies R7-055 as ambiguity and files OWNER-QUESTIONS.md. Local issuer
qualification versus global predecessor endorsement needs an attributed owner
choice; no implementation bug, exact oracle or mixed-state rejection is inferred.
Preserve original input/first outputs and existing same-issuer closures until
that decision. This native pair remains outside exact vector totals.
