# Package-only evaluator worklog

## Round 0 — independent implementation

- Task: implement the finite semantic fixture API from `memory/spec/` only,
  run every packaged vector, and commit the first complete report before reading
  any source design, notes, inputs, other evaluator, ledger, or divergence topic.
- Baseline: package `0.1.0-draft`, repository `0ef608a`.
- Read inputs: `memory/MISSION-R7.md`, package README, normative semantics,
  AMBIGUITIES, domain READMEs, adapter, schemas and vectors. Only the administrative
  `rounds` topic is read before the first committed run.
- Tool readiness: Git 2.54.0, Python 3.14.7, ripgrep 15.2.0, a2a help and
  onboarding succeeded; `.temp/tool-readiness-01.log`. No applicable local or
  installed conformance skill found. No installs, services, agents or web used.
- Tracking lives here; the mission prohibits task-board writes.
- First package snapshot is retained under `.temp/impl-astra-23/package-first/`
  so concurrent releases cannot silently change the independent baseline.
- Required positive behavior: independent support/opposition, exact policy/cut
  filtering, bounded witnesses, atomic operations and declared normalization.
- Forbidden behavior: expectation-driven evaluation, hidden evidence affecting
  budgets or quality, partial rejected writes, unsupported deployment certification,
  and any mutation of package vectors.
- Progress: specification intake complete; implementation and first run pending.

## Validation scope

The runner will compare complete execution reports, check forbidden predicates,
verify handle equality/freshness slots, and retain exact field differences.
Deployment fixtures will be reported separately as unsupported qualification;
simulated transitions are not actual deployment evidence. Bounded checker controls
will prove semantic differences and forbidden effects are detected.

## First full run — frozen before external semantic intake

- Package `0.1.0-draft` at `0ef608a`; all 61 vectors classified.
- Semantic: 50 pass, 3 fail, 0 unsupported. Deployment: 8 unsupported; no live
  qualification claimed. Exact field differences are in FIRST-RUN.md/JSON.
- Four bounded checker controls pass, covering semantic differences, all four
  forbidden predicates, normalization constraints and malformed JSON rejection.
- Structural package checker passed: 61 vectors, 49 clauses, 13 violation controls.
- Logs: `.temp/impl-astra-23/controls-01.log`, `first-run-01.log`,
  `.temp/package-validate-01.log`.
- This baseline is committed before reading any design, notes, inputs, other
  evaluator, ledger or divergence topic. Disagreements are retained, not silently fixed.

## Round 1 — 0.2.0 package grammar adaptation

- Read only the released package diff at cde5754 (52 clauses, 65 vectors).
- Retained an unchanged-evaluator diagnostic run against the new grammar under
  `.temp/impl-astra-23/`; this is not a new conformance claim.
- Implement integration-established complete/unknown lineage, exact owner release
  decisions with revocation, frozen delivery item bindings and exclusion filters.
- Negative controls: missing owner evidence must atomically refuse; revoked
  evidence must not authorize new delivery; unknown/tainted input sets must not
  create audience evidence; exclusions must not mutate independent projections.
- Original B03/S23 and S30 differences await judge classification.

### Round 1 outcome

- 0.2.0-draft at cde5754: 54/57 semantic pass; B03/S23 await R7-019
  specification clarification; B01 newly fails missing mandatory revision fact.
- R7-020 declared-coverage field fixed after the judge's impl-bug decision.
- Nine controls pass (four checker, five product); test claims and limitations
  accompany each test. No deployment qualification: all eight unsupported.
- `DIVERGENCES.md` retains first-run classifications and the B01 separating control.
- Logs: `.temp/impl-astra-23/controls-02.log`, `semantics-controls-01.log`,
  `release-020-02.log`. All P12-P15 and extended P05 pass.

## Round 2 — supplemental case intake

- Add an explicit --vector-root lane for independently authored package-format
  cases after the committed blind run. It never rewrites cases or converts grammar.
- Supplemental fixtures outside the selected release grammar are unsupported with
  an exact reason; canonical and supplemental totals remain separate.
- Editor acknowledged the B01 omission and plans the narrow integration-fact fix.
- Previous round had a pre-commit pull refused due tracked local work, then one
  push race. A signed rebase preserved scope and G verification; final 1439219
  pushed successfully. Subsequent pulls use automatic stash only for owned edits.

### Round 2 outcome

- Current grammar: 7/8 compatible supplemental cases pass; ASTRA26-06 is the
  judge-classified R7-022 package defect. Nine older cases are unsupported there.
- Original 0.1.0 grammar: 7/9 compatible cases pass; ASTRA25-05 reproduces R7-018;
  ASTRA24-03 reveals derived source-reference omission (classification requested).
- B01 now classified R7-021 spec-bug. Acknowledged; evaluator remains unchanged.
- Logs: `.temp/impl-astra-23/supplemental-01.log`, `supplemental-legacy-01.log`.

## Round 3 — R7-023 derived source-reference correction

- Judge classified the shared ASTRA24-03/04 omission as R7-023 impl-bug.
- The direct/derived regression fails at the exact missing source_refs assertion
  before the implementation change (`.temp/impl-astra-23/derived-ref-red-01.log`).
- Fix scope: union separately authorized sources from found proof paths into
  item metadata; preserve direct-source behavior and public redaction.
- Negative boundaries: hidden sources, unsuccessful paths and unrelated copies
  must not become derived source metadata or evidence roots.

### Round 3 outcome

- Corrected R7-023: ASTRA24-03/04 now pass, with mixed/stronger source-state
  controls unchanged. Six product plus four checker tests pass.
- Canonical 0.2.0 remains 54/57 with only package defects R7-019/021.
- Fully migrated supplemental 0.2.0: 17/19 semantic pass; R7-018/022 differ;
  one deployment case unsupported. No grammar-incompatible cases remain in this run.
- Logs: derived-ref-green-01.log, controls-04.log, canonical-round3-01.log and
  supplemental-03.log under `.temp/impl-astra-23/`.

## Round 4 — released 0.2.1 alignment

- Read the exact package semantics delta and RELEASES.md at f31d58f.
- Align R7-019 to authorized publication-source associations; retain current
  mirror-report sequences and unchecked genuine-publication negatives.
- Implement R7-018 unresolved dirty causes with current-authorized pre-revision
  impact traversal; hidden causes cannot affect public fields or logical budgets.
- Enforce R7-022 explicit subject/principal evidence for both admission and
  already-admitted self-declaration assertions, including delegated controls.
- Retest R7-021's unchanged B01 expected output and missing-fact rejection.

### Adapted pre-fix checkpoint

- 0.2.1 f31d58f: 55/57 semantic pass. New private dirty controls expose only
  the unrelated-history omission, classified R7-024 impl-bug by the judge.
- Preserve this head/report before correction in RELEASE-0.2.1-FIRST.md/JSON.
- Twelve controls pass; the selected-history regression intentionally remains red
  at the exact historical list assertion. Structural validation passes 20 controls.
- Logs: canonical-021-prefixed-01.log, semantics-021-01.log, history-red-01.log,
  package-021-01.log. No expected output or case changed.

### Round 4 corrected outcome

- Adapted pre-fix commit bc342e1 preserved 55/57 and the exact red regression.
- R7-024 corrected: selected multi sequences now bound historical metadata;
  unfiltered, explicitly historical and hidden-reference controls pass.
- Canonical 0.2.1 at f31d58f: 57 pass / 0 fail / 0 unsupported semantic;
  eight deployment cases unsupported. Thirteen controls pass.
- Compatible supplemental 0.2.1: 15 semantic pass / 0 fail; four astra-24 cases
  await explicit grammar migration, one deployment case unsupported.
- Logs: history-green-01.log, controls-06.log, canonical-021-green-01.log and
  supplemental-021-01.log under `.temp/impl-astra-23/`.

## Round 5 — complete current-release supplemental evidence

- Intake astra-24 fixture migration c929ed2 without changing any case or expected
  value; the earlier unsupported grammar rows remain in commit f5fdd8b.
- Current 0.2.1 supplemental report: 19 semantic pass / 0 fail / 0 unsupported;
  one deployment case remains unsupported. Canonical result and implementation
  are unchanged at 57/57 and f5fdd8b respectively.
- Exact case hashes and normalized actuals are retained in SUPPLEMENTAL.json.
- Log: `.temp/impl-astra-23/supplemental-021-02.log`.
- R7-024 corrected head and retained pre-fix head were sent to the judge for
  independent review. No package defect or implementation difference remains
  in this seat's executable cases; collective review remains pending.

## Round 6 — independently verified seat closure

- Judge 6a4f307 reproduces the pre-fix 55/57 and corrected 57/57 reports, all
  65 canonical rows, implementation hashes and 13 controls. R7-024 closes at
  f5fdd8b; package fixes R7-014/018/019/021/022 close at f31d58f.
- The ledger has no open package bug or astra-23 implementation bug. Remaining
  collective items R7-025/026 belong to the source evaluator; score stays 1/2
  until their fixes and current-release verification are accepted.
- No new implementation delta or testing claim; exact existing evidence reused.
- Current supplemental 19/19 evidence d2c38ac acknowledges astra-24 migration;
  convener's earlier fixture dependency is resolved by the proper single writer.

## Round 7 — premise-quality budget separating case

- Intake ASTRA25-06 from astra-25 signed 2a6d294. Its roots=2 positive control
  and roots=1 query must both retain B+ support through conflicted premise A:
  premise-opposite quality walks have independent counters under K-EVAL-2/4.
- Unchanged evaluator f5fdd8b passes both exact outputs, their equivalence and
  forbidden-result checks. Complete supplemental result: 20/20 semantic;
  one deployment case unsupported. Canonical and product-control evidence unchanged.
- No new defect in this evaluator; source accounting difference awaits judge.
- Log: `.temp/impl-astra-23/supplemental-021-03.log`; case/code digests and
  normalized actuals retained in SUPPLEMENTAL.json.

## Round 8 — displayed-polarity budget separating case

- Intake ASTRA24-05 from signed 0ab80b6. K-EVAL-1/2 give each displayed polarity
  its own root counter. Budget 1 must preserve both one-root signs; budget 2 is
  the positive control and budget 0 must reject both walks as incomplete.
- Unchanged evaluator f5fdd8b passes the new exact/paired/forbidden checks.
  Current supplemental evidence is 21/21 semantic, one deployment unsupported.
- ASTRA25-06 is now classified source impl-bug R7-027; this neighboring case
  awaits judge disposition. No package-evaluator code or expected value changed.
- Log: `.temp/impl-astra-23/supplemental-021-04.log`; exact input/code hashes and
  actuals retained in SUPPLEMENTAL.json.

## Round 9 — source-resolution budget separating case

- Intake ASTRA24-06 from signed 67b1e06. Its current-required source resolution
  succeeds with allowance 1; allowance 0 must withhold the derived witness,
  qualifications and found-path source refs while reporting source_limit.
- Unchanged evaluator f5fdd8b passes the exact positive/negative trace and all
  forbidden predicates. Supplemental 22/22 semantic, one deployment unsupported.
- Judge 510649f closes source R7-025/026; R7-027 remains the single classified
  source budget family. The new resolution case awaits its disposition.
- Log: `.temp/impl-astra-23/supplemental-021-05.log`. No code or expectation edit;
  canonical 57/57 and 13-control evidence remain unchanged.

## Round 10 — source-state precedence regression control

- New judge finding R7-029 concerns the independent/retained fallback priority
  when all sources are available, including the vacuous empty list. Verify this
  evaluator from K-EVAL-5 and canonical S32, without reading source code or the
  judge's private probe directory.
- Required controls: available and empty lists resolve now; unavailable source
  preserves independent/retained fallback; evidence qualification must not be
  upgraded by availability. Current-required zero resolution must remain capped.

### Round 10 outcome

- Added one clause-derived product test with twelve subcases. All pass without
  evaluator changes: independent/retained with resolved, denied, lost and empty
  lists; current positive, zero-limit, empty-list exemption and unavailable source.
- Each subcase checks closed snapshot grammar, exact source state, witness,
  completeness, unchanged semantic-review qualification, no opposite witness,
  exact cutoff and unchanged state. This is bounded synthetic evidence only.
- Ten product plus four checker controls pass. Fresh report hashes include this
  test; canonical remains 57/57 and supplemental 22/22 semantic. Deployment 8+1
  unsupported. Immutable first/adapted-first reports are untouched.
- Logs: semantics-precedence-01.log, controls-07.log, canonical-round10-01.log,
  supplemental-round10-01.log under `.temp/impl-astra-23/`.

## Round 11 — Phase 2 full dual-evaluator gate

- Convener event `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc` explicitly
  withholds PARK and starts Phase 2 until 13:00Z or earlier full-dual completion.
  Source seat extends all 14 unsupported canonical vectors from its source
  contract; adversaries target their boundaries and the v0.2 delta. Package
  editor and judge retain their single-writer roles.
- Verified judge b1ae299 signature G, score/ledger/owner questions: original
  supported-vector rubric 2/2, 21 fixed plus 8 rejected, no open item. This is
  historical Phase 1 evidence, not proof of full dual coverage.
- Read only the source RESULTS.md report to inventory the gap; no source code
  intake. Dual coverage is 43/57. Unsupported source vectors are B01, B07, P05,
  P06, P08, P12, S07, S17, S20, S23, S24, S25, S26 and S27.
- Package baseline remains runtime f5fdd8b, reports/controls 8b9baf3: 57/57
  canonical, 22/22 supplemental semantic, 14 controls; deployment 8+1 unsupported.
- Continue package-only evaluator ownership: execute new separating cases,
  preserve mismatches before correction, align only to judged/released changes,
  and keep independent-run boundaries and expected fixtures intact.
- Early completion now requires source 57/57 and no new open item for one full
  round. Remain active until convener PARK and the required final handoff.
- Baseline integrity evidence: `.temp/impl-astra-23/final-gates-01.log`; both
  original FIRST-RUN and adapted RELEASE-0.2.1-FIRST remain byte-identical.

## Round 12 — Phase 2 erasure receipt authority separating case

- Intake ASTRA25-07 and its metadata-authorized positive control from signed
  77ea085. The claim separates protected full erase closure from authorized
  receipt metadata; source clauses K-API-1 and K-ERASE-2 require judge review.
- Reproduce and commit the first exact run before any semantic correction.
  Preserve full protected purge/fencing while comparing public receipt refs.

### Round 12 outcome

- Reproduced ASTRA25-07 exactly: only the extra protected derivative receipt ref
  and length differ, with the intended hidden-id forbidden failure. The fully
  authorized control and all other current cases pass: 23/1/0 semantic,
  one deployment unsupported. Canonical 57/57 baseline remains unchanged.
- Preserve PHASE2-ERASURE-FIRST.md/JSON before classification or correction;
  SUPPLEMENTAL.md/JSON now reports the same current failed corpus honestly.
- No implementation change. Await judge disposition of K-API-1/K-ERASE-2 and
  the exact actor/metadata binding. Protected closure must remain complete.
- Log: `.temp/impl-astra-23/phase2-erasure-first-01.log` (expected runner exit 1).

## Round 13 — R7-031 released-contract dependency

- Judge event `$JPPhod2ZE3Dm7yPZZY1gOh8KGSHsO6j0Fi33ewipx7o` classifies
  ASTRA25-07 as spec-bug R7-031, editor astra-21. No owner question or separate
  impl-bug is assigned for the contradictory full-closure receipt requirement.
- Preserve red head 127bc0b. Align only after an explicit recipient/audience/
  purpose or admitted receipt scope and pre-fence metadata rule are released.
- Planned negative boundaries: hidden derivative refs remain absent despite
  complete protected erasure; unrelated-purpose grants and a later query must
  not authorize receipt metadata. The explicit authorized positive control must
  still reveal its full approved refs. Protected closure/custody cannot shrink.
- Acknowledged directly to judge/editor. Current runtime and canonical report
  unchanged; no speculative filter introduced. Await released contract and
  explicit case migration, then rerun the affected operation and full corpus.

## Round 14 — Phase 2 import expiry, selected delivery and proof sets

- Intake ASTRA26-07 and ASTRA26-08/control from signed 837591e, plus
  ASTRA24-07 from 4e5d063. Reproduce and retain first results before fixing.
- Required boundaries: import-check expiry downgrades currentness; an excluded
  unrelated record cannot veto the prepared selected item's forward permission;
  source-origin deduplication cannot collapse distinct Cartesian proof sets.
- Keep the independently authored expected values and all earlier red evidence.

### Round 14 outcome

- Reproduced both ASTRA26-07/08 differences on unchanged runtime and retained
  PHASE2-IMPORT-DELIVERY-FIRST.md/JSON before correction. Fresh import and
  unrelated-forward-grant positive controls pass; later revocation still refuses.
- ASTRA24-07 exact Cartesian proof sets/order/truncation and origin counts pass.
- Current corpus: 25 pass / 3 fail / 0 unsupported semantic, one deployment
  unsupported; R7-031 is the third failure. Canonical 57/57 remains baseline.
- Log: `.temp/impl-astra-23/phase2-import-delivery-first-01.log` (expected exit 1).
  Exact diffs, forbidden failures, code hashes and input hashes are committed.
- Await judge classification for the two observed implementation boundaries;
  preserve first evidence and existing negative authorization guarantees.

## Round 15 — R7-033/034 implementation correction

- Judge classified ASTRA26-07 as package impl-bug R7-033 (source separately
  R7-032) and ASTRA26-08 as package impl-bug R7-034. Red first report f83268d
  is immutable; implement only these two classified boundaries now.
- Add focused red controls before changing runtime: exact horizon neighbors,
  missing check/known replacement, unchanged nonpublication sequence and
  evidence/captured history; selected forward/read/use/erasure/freshness and
  revocation gates beside unrelated-excluded positive controls.
- ASTRA25-08 retention intake is queued next; R7-031 remains release-dependent.

### Round 15 outcome

- Red controls reproduce expiry at/after horizon and excluded-record delivery
  refusal; `.temp/impl-astra-23/import-delivery-red-01.log` records all three
  intended assertions. Narrow runtime fixes make twelve product controls pass;
  four checker controls also pass (16 total).
- Fresh canonical report 57/57; full current supplemental 28/2/0 semantic,
  deployment 8+1 unsupported. R7-033/034 and their positive/negative neighbors
  pass; R7-031 remains release-dependent.
- Queued ASTRA25-08 intake now reproduces unauthorized retention with unchanged
  admission code: exact twelve field differences plus two forbidden predicates;
  retain-authorized control passes. Freeze PHASE2-RETENTION-FIRST before any
  correction, with separate input/runtime hashes. Classification requested next.
- Logs: import-delivery-green-01.log, controls-08.log, canonical-round15-01.log,
  phase2-retention-first-01.log under `.temp/impl-astra-23/`.
- Source seat reports S07 support at 4960d24 (44/57); this is separate from the
  previously judge-verified 43/57 dual baseline and does not complete Phase 2.

## Round 16 — R7-037 exact retention-scope dependency

- Accept R7-037; red witness and positive control already frozen at f10c7ba.
- Inspected the complete published write-context shapes and all retention-grant
  prose. Context has no audience/purpose, while grants are exact in both fields.
  The per-record input/output retention binding is not defined by the package.
- Persisted the exact missing contract and a read-only-purpose grant neighbor
  in DIVERGENCES.md and `.temp/impl-astra-23/retention-scope-01.json`.
- Both existential and all-label grant readings satisfy existing no-retain/all-
  retain controls but disagree on that neighbor. No expected answer or permissive
  workaround is invented. Empty-label admission must also remain accounted for.
- Ask judge/editor for the operation/admitted scope or explicit label quantifier
  before the complete scoped fix. R7-031 explicit receipt context is independent.
- No runtime change; existing canonical and red supplemental evidence reused.

## Round 17 — 0.2.2 receipt-context release baseline

- Intake 0.2.2 package 7e71765 for R7-031. Run unchanged f10c7ba runtime against
  the complete new release and freeze first report before adapting receipt scope.
- Required behavior: actor-bound receipt_context, exact pre-fence metadata
  authorization, complete protected erasure, scope-sensitive idempotency and
  current-authorized unchanged receipt replay. Do not infer any later-query scope.
- Judge independently closed R7-033/034 at f10c7ba; preserve their controls.
- R7-037 admission retention-scope mapping remains separately under review.

### Round 17 baseline outcome

- Unchanged runtime against released 0.2.2: 56 pass / 1 fail / 0 unsupported
  semantic, eight deployment unsupported. P08 exposes the expected receipt-ref
  leak and unauthorized replay; all other canonical vectors pass.
- Freeze RELEASE-0.2.2-FIRST.md/JSON before implementation. This is distinct
  from the prior green 0.2.1 RESULTS and red 0.2.1 supplemental evidence.
- Package checker passes all 23 intended violation controls. Logs:
  `.temp/impl-astra-23/release-022-first-01.log` (intended evaluator exit 1),
  `.temp/impl-astra-23/package-022-01.log` (structural validation pass).
- The release explicitly supplies top-level erase `at`, including replay stamp
  exclusion from canonical intent; no later-query clock or scope is needed.

### Round 17 correction outcome

- Published red baseline is 0ca2d27. The added controls first reproduce both
  metadata disclosure and later-stamp replay failures in receipt-red-01.log.
- Factor the existing exact grant predicate for shared query/receipt use; filter
  receipt refs before fencing under actor/context/clock and effective disclosure.
  Keep full closure, generation and custody unchanged. Replay checks all stored
  refs against current authorization and returns the original unmodified receipt.
- Canonical erase intent excludes only the intake `at`, retaining receipt_context.
  Changed scope conflicts; revoked/expired metadata refuses atomically without
  regenerating or redacting the stored receipt. Broader later rights do not add refs.
- Fourteen product tests plus four checker controls pass. Full canonical 0.2.2
  is 57/0/0 semantic, eight deployment unsupported. Prior first reports unchanged.
- Logs: receipt-green-01.log, controls-09.log, canonical-round17-01.log.
- Judge/editor classified the separate storage-scope gap R7-039; R7-037 remains
  open pending 0.2.3. ASTRA24-08 exact first reproduction is queued next. Owned
  external erase fixtures await author migration; no silent conversion is used.

## Round 18 — R7-041 authority-slot CAS first reproduction

- Intake ASTRA24-08 ambiguous, unique-head, historical-head and challenge cases
  at 09f2d4d/f13a3e6. Judge classifies R7-041 as an implementation bug: target-only
  checks cannot select among incomparable heads or authorize a historical head.
- Preserve full supplemental first results before revising CAS. Required atomic
  refusal is retryable version_conflict, with records/cut/dirty/idempotency intact.
  Preserve unique-head success, challenge exemption, valid receipt ordering and
  exact replay precedence. No new specification or owner decision is required.
- The same run verifies explicitly migrated erasure metadata/purpose controls,
  unknown-lineage lower-bound erasure and future-input intake cases. Their
  independently authored expected values remain unchanged.

### Round 18 baseline outcome

- Unchanged CAS code at a016781 reproduces both ASTRA24-08 and STALE: eleven
  exact differences each plus both intended forbidden predicates. Both persist
  a seventh record and return revised instead of retryable version_conflict.
  Unique-head and challenge controls pass. Freeze PHASE2-CAS-FIRST.md/JSON.
- Full migrated 0.2.2 supplemental: 35 pass / 3 fail / 0 unsupported semantic,
  one deployment unsupported. Third failure remains R7-037 no-retain admission.
- ASTRA25-07 primary/purpose/authorized control now pass after a016781 receipt
  correction. Unknown-lineage lower-bound erase/late-writer and future-input
  operation cases also pass exactly. No expectation or fixture is edited.
- Log: `.temp/impl-astra-23/phase2-cas-first-01.log` (intended exit 1).

### Round 18 correction outcome

- First red evidence is signed e525612; native controls reproduce ambiguous and
  historical acceptance plus an incorrect refusal of the next remaining unique
  head after withdrawal. cas-red-02.log contains the three intended assertions;
  cas-red-01.log's missing-outcome assertion was repaired before implementation.
- Factor sequence identity and authority receipt maximality for shared projection
  and CAS use. Non-challenge decision revisions require the unique non-withdrawn
  authoritative slot head; ordinary record revision-token behavior is unchanged.
- Exact replay remains ahead of head checks; changed canonical intent conflicts.
  Challenge remains exempt. Ordering rather than arrival selects the current head;
  after withdrawal, the next unique maximal authority candidate can be revised.
- Fifteen product tests and four checker controls pass. Canonical 57/57 remains
  green. The pinned 38-case corpus is now 37/1/0 semantic; only R7-037 remains,
  and deployment 8+1 remains unsupported. First reports are unchanged.
- Logs: cas-green-01.log, canonical-round18-01.log, supplemental-round18-01.log,
  controls-10.log under `.temp/impl-astra-23/`.
- Incoming ASTRA26-09 missing publication-check coverage and ASTRA24-09
  transitive-review cases are queued for first reproduction after this unit.
  R7-039/042 release work remains independent; no inferred retention scope.

## Round 19 — exact import-check coverage and transitive review first intake

- Intake ASTRA26-09 missing-one-publication-check primary/unverified/all-checked
  controls and ASTRA24-09 transitive review path at 03a0f85/783b83a.
- Run unchanged import/review code, now on CAS-corrected 53266dd, and freeze full
  first report before classification/correction. Expected outputs remain author-owned.
- Required boundaries under review: a same-origin copy cannot borrow another
  exact object's current check; an authorized multi-edge impact path must preserve
  transitive review after recomputation while hidden paths remain invisible.

### Round 19 baseline outcome

- ASTRA26-09 reproduces exactly two currentness field differences and both
  forbidden current predicates. Explicit-unverified and all-checked controls pass.
- ASTRA24-09 reproduces only the missing second review-required ref/length plus
  the intended forbidden size predicate. Both hidden-path public controls pass.
- Freeze PHASE2-COVERAGE-REVIEW-FIRST.md/JSON before either runtime change.
  Current42-case supplemental is39/3/0 semantic, one deployment unsupported;
  the third failure is known R7-037. Corrected CAS family remains green.
- Log: `.temp/impl-astra-23/phase2-coverage-review-first-01.log` (intended exit 1).
  Request judge classifications before correcting these two new boundaries.

### Round 19 pre-correction controls

- Added two focused product controls while judge disposition is pending. The
  corrected red instrument records six intended failures: exact import primary,
  each one of three missing exact checks, exact transitive-review output and a
  bounded cyclic-review neighbor. Hidden path-element controls pass.
- coverage-review-red-01/02.log also contain fresh-handle comparison setup noise;
  coverage-review-red-03.log removes only the known handle field from semantic
  component comparisons and separately asserts its view-handle binding. The
  original fixture checker/expectations remain unchanged; no runtime fix yet.
- ASTRA26-10 foreign delivery actor is queued after this committed unit.

- Judge event $31IyK5gwGSJaMRrozQ-A02a1oUfrXbHkp9e1ZaOGWjI closes R7-031
  at package7e71765/runtimea016781, with exact57/57,18controls and three unchanged
  receipt cases. Editor independently confirms; no deployment claim is added.
- Adversary0f59936 independently verifies all four R7-041 cases and native atomic
  state/replay controls at53266dd; judge disposition remains separate.

- Judge classified import coverage as R7-044 (event
  $Y8OHdh7iDMe_LPy7R9JzU80dB6gLZcU1j9HGQrDTFcg), with exact-source checks,
  hidden-publication isolation and preserved expiry/replacement expectations.
  Implement that classified correction now; transitive-review disposition pending.

### Round 19 correction outcome

- Judge classified transitive review as R7-045. Exact-source import coverage
  (R7-044) now requires a fact for every authorized associated publication;
  same-origin deduplication does not supply missing exact-object authority.
- Review obligations propagate through eligible registered paths with at least
  one review_on_change edge. Sufficient-only and documentary-only paths create
  no review obligation after recomputation; hidden necessary elements filter the
  path. A finite reached set handles review cycles without new dirty/evidence writes.
- Expanded red-before controls cover each missing publication, missing versus
  explicit unverified, irrelevant hidden publication, complete current checks,
  transitive/cyclic/mixed review paths, hidden elements/certificate and no-path
  controls. Earlier expiry/replacement/origin and dirty-state controls remain green.
- Eighteen product tests plus four checker tests pass (22 total). Full canonical
  57/57, pinned42-case supplemental41/1/0; only R7-037 remains in that corpus.
  Deployment8+1 unsupported. PHASE2-COVERAGE-REVIEW-FIRST at08c4b9a is unchanged.
- Logs: coverage-green-01.log, review-mixed-red-01.log,
  coverage-review-green-01.log, canonical-round19-01.log,
  supplemental-round19-01.log and controls-11.log.
- ASTRA26-10 has been classified R7-046; first reproduction and correction are
  queued next. Source49/57 candidate and retention0.2.3 remain separate work.

## Round 20 — foreign delivery actor and 0.2.3 first full baseline

- R7-046 is classified; preserve exact first ASTRA26-10 result against frozen
  0.2.2 before correction, with rightful delivery/revocation controls unchanged.
- Explicitly snapshot released0.2.2 and author-owned case bytes under task scratch
  for pinned verification; no fixture migration or expectation changes are made.
- Released0.2.3 at23290b3 supplies the missing R7-039 retention scope and R7-042
  future-fact checker correction. Preserve its first full run on unchangedf6c339d
  before adapting any intake code. Actor delivery correction comes first, then
  R7-037 scoped retention/current replay under the published rule.
- Judge independently closed R7-041 at53266dd and verified source49/57 coverage.

### Round 20 first baseline outcome

- PHASE2-ACTOR-FIRST on exact frozen0.2.2:42/2/0 semantic across44 cases,
  deployment1unsupported. ASTRA26-10 returns delivered for the ungranted actor
  (nine exact differences plus forbidden receipt); rightful delivery and later
  revocation pass. R7-037 is the other failure; new authority NEXT case passes.
- RELEASE-0.2.3-FIRST on unchangedf6c339d:55/2/0 semantic, deployment8unsupported.
  Only P11/P13 fail, exposing new exact retention and replay obligations. This
  first report is preserved before either queued runtime correction.
- Read the complete0.2.3 normative/release delta. Actor binding is fixed for
  storage; retained closure includes outputs and transitive known inputs in the
  whole batch, independent of labels, with live retain revocation/current replay.
- Logs: phase2-actor-first-01.log and release-023-first-01.log (both intended exit1).

### Round 20 actor-binding correction outcome

- Red actor/exact-fixture controls reproduce R7-046 before the runtime change.
  Delivery now verifies the authenticated actor against the captured principal
  before using the saved query. This finite API adds no delegated publisher lane.
- Native controls pass wrongful actor/audience/purpose/index refusals with entire
  runtime, captures, bindings and dirty-since unchanged; rightful delivery and
  later selected read revocation retain their outcomes and frozen captures.
- Current0.2.3 actor fixture passes. All19product controls on explicitly frozen
  0.2.2 plus4checker controls pass (23 total); canonical0.2.2 is57/57 and the
  frozen44-case supplemental is43/1/0 (R7-037 only), deployment8+1unsupported.
- Current0.2.3 RESULTS remains honestly55/2/0, only retentionP11/P13. Pinned old
  results are separately named RESULTS-0.2.2 and SUPPLEMENTAL-0.2.2. First actor
  and release reports at5416283 remain immutable; no old fixture was relabeled.
- Logs: actor-red-01.log, actor-green-01.log, actor-frozen-controls-01.log,
  canonical-actor-022-01.log, supplemental-actor-022-01.log,
  canonical-actor-023-01.log and controls-12.log.
- Next unit implements exact released storage authority/current replay for R7-037.

## Round 21 — explicit scoped retention and current replay

- Implement R7-037 against released0.2.3/23290b3 after the completed actor unit.
  First full canonical red5416283 remains unchanged. Freeze the new author-owned
  transitive-unknown retention neighbor before correction as well.
- Check every output and recursively resolved known content input against exact
  actor/record/space/storage audience/purpose retain grants and live revocations.
  Use pre-state plus whole batch, never future facts as records, and never onward
  disclosure labels as authority. Metadata permission is independent of retain.
- Preserve policy-before-idempotency ordering, original-output current-authorized
  replay and canonical context conflicts, refused full state/idempotency, valid
  same-key retry, same-batch input order, unknown lower bounds and empty labels.

### Round 21 baseline outcome

- All author-owned cases are now explicitly0.2.3-compatible. Full supplemental
  44/2/0 semantic across46cases; one deployment unsupported. Only original08
  and new08-UNKNOWN retention negatives fail; both retain-authorized positives pass.
- Freeze PHASE2-RETENTION-023-FIRST.md/JSON before changing intake. New unknown
  intermediate U still carries known ancestor A; grants for U/D and unrelated
  purpose A cannot authorize the exact requested storage scope. Metadata=false
  retain grants in the positive are valid and must not require read/use metadata.
- Log: retention-023-first-01.log (intended exit1). Runtime3ce8ee3 is unchanged.

### Round 21 correction outcome

- Baseline6861fec preserves both migrated retention failures; canonical first5416283
  is unchanged. New native controls first produce17 intended assertions in
  retention-red-02.log. Red01's receipt/code indexing noise is explicitly excluded.
- Exact retain authority now traverses proposed outputs plus recursively resolved
  protected integration inputs in pre-state+whole batch; unknown lower bounds are
  retained. The fixed actor/context uses metadata-independent retain grants and
  current revocations before idempotency. Replay additionally checks stored outputs
  and their current known closure without changing the original receipt.
- Missing inputs stay invalid_reference at their declared validation stage;
  future facts do not materialize records. Canonical intent already includes the
  entire context, so otherwise authorized context changes conflict as required.
- Explicitly migrated the own P13 lineage test to released operation2 and the new
  model-stage intermediate. Public fixture bytes/oracles are unchanged. Green01's
  stale direct-input assertion is an instrument migration failure, not a runtime bug.
- All22product+4checker controls pass under current0.2.3. Canonical57/57 and all
  46semantic supplemental cases pass; deployment8+1unsupported. Package validator
  passes94JSON/65vectors/52clauses and32intended violation controls.
- Logs: retention-green-02.log, canonical-round21-01.log,
  supplemental-round21-01.log, controls-13.log and package-023-01.log.
- Judge closed R7-044/045 atf6c339d and specification039/042 at23290b3; source040/043
  are separately closed. R7-046 independently verified by26 at7b9f0dd. R7-037
  current behavior now awaits independent review; source reports49/0/8 on0.2.3.

## Round 22 — authority receipt succession probe intake

- Intake ASTRA24-10 at1a09fb6. Preserve exact actual outputs and complete state
  effects on4af0360 before any correction. Inputs have no adjudicated typed
  refusal oracle yet; report observed invariant violations, not invented vector passes.
- K-REV-3 requires strict successor receipt for authoritative replacements;
  ordered replacement and plain incomparable import are distinct valid controls.
  Await judge/editor refusal-code mapping before implementation or exact tests.

### Round 22 baseline outcome

- All three independently authored input triples pass the package's closed input
  shapes. Runtime4af0360 accepts ordered, incomparable and reused receipts alike:
  records5->7, cut100->102, dependent dirty, one stored idempotency entry.
- PHASE2-SUCCESSION-FIRST.md/JSON freezes full actual outputs and before/after
  state with exact input/module hashes. Both negatives violate the no-write
  invariant, but typed refusal mapping remains explicitly pending.
- Existing57/57canonical and46/46supplemental counts exclude these new probes;
  no exact-vector pass/fail or new expected code is manufactured.

## Round 23 — independent closure recorded; succession mapping pending

- Judge independently closed R7-037 at4af0360: current0.2.3 canonical57/57 and
  supplemental46/46 exactly reproduced with26controls and unchanged first reports.
  The shortened package label23290b3 resolves uniquely to the full release; the
  literal metadata difference is recorded, not silently normalized as semantics.
- Judge independently closed R7-046 at3ce8ee3 using original0.2.2 and migrated
  0.2.3 actor/binding/state controls. Source R7-036 separately closed atd077064;
  current verified dual canonical coverage is49/57 on0.2.3.
- New succession probes at47c0205 remain separate pending typed-refusal mapping.
  No runtime change, new vector pass or Phase2 completion is claimed.

## Round 24 — R7-048 strict authority succession correction

- Judge classifies the preserved ASTRA24-10 failure as package implementation
  R7-048, source R7-047 and exact refusal-mapping specification R7-049.
- Wait for the editor's published K-REV-3/K-REF-1 amendment and authored exact
  vectors before adapting this package-derived runtime. Preserve the first new
  release/vector execution before correction as usual.
- Required negative boundary: incomparable, identical and prior receipts refuse
  authoritative replacement with authority_receipt_required/retryable=false,
  without records, cut, dirty state or idempotency changes. CAS mismatch remains
  version_conflict; exact successful replay retains its earlier precedence.
- Pair with direct/transitive successors, ordinary incomparable decision import,
  valid retry after a refusal and existing withdrawal/challenge/CAS controls.
- Current runtime4af0360 and reports remain unchanged while publication is pending.

## Round 25 — exact successor and digest fixtures before correction

- ASTRA24-10 now has five independently authored exact0.2.3 vectors at72a8f86,
  using the adjudicated code: incomparable, reused and prior receipt negatives;
  direct/transitive successor positives. Preserve the full supplemental run before
  any runtime correction, including the existing immutable first native probes.
- New ASTRA25-02-DIGEST at6d3fe61 checks consistent raw-body hash substitution;
  the framed positive and raw negative are already independently green for this
  runtime. Judge R7-050 concerns source implementation only, not package wording.
- Published0.2.4 clarification remains pending; no runtime change yet.

### Round 25 exact baseline outcome

- PHASE2-SUCCESSION-VECTORS-FIRST freezes49pass/3fail/0unsupported across52
  semantic supplemental vectors; one deployment remains unsupported.
- Only ASTRA24-10, SAME and PRIOR fail:19 field differences and3 forbidden
  predicates each. Direct and receipt-only-intermediate transitive positives pass.
  ASTRA25-02-DIGEST raw-hash negative also passes without a runtime change.
- Runtime4af0360 is unchanged, package0.2.3/23290b3. Log:
  .temp/impl-astra-23/succession-vectors-first-01.log (intended exit1).
- Freeze this exact baseline before correction; original native first47c0205 and
  all other earlier first reports remain unchanged.

## Round 26 — queued retention-deadline first probes

- Receive ASTRA25-11 at604af18 while the succession correction awaits0.2.4.
  Preserve an independent unchanged-runtime execution of its five closed-input
  probes; do not invent expiry refusal code/order or exact replay semantics.
- Fresh before/at/after input deadline, output-own deadline and expired replay
  are separately recorded with entire state and dirty-since snapshots per operation.
  Deadline correction, if classified, stays queued behind the succession unit.

### Round 26 first results and released successor contract

- PHASE2-DEADLINE-FIRST preserves every probe's whole state and native dirty-since:
  at/after inherited expiry and at output expiry each admit D, records1->2,
  cut100->101, one replay receipt. Before-deadline control admits; expired replay
  returns its prior receipt with state unchanged. Code/order/replay mapping pending.
- The pull had already included release0.2.4/ef02647 before this native run;
  report labels explicitly record that checker/runtime profile and unchanged
  author0.2.3 input bytes. Initial scratch markdown's old hard-coded label was
  corrected before publication; no semantic input or runtime change occurred.
- Read the full published0.2.4 amendment/release delta. New canonical B01 covers
  four same-key missing/prior/identical/incomparable refusals, unchanged view/cut,
  direct/transitive successors, exact replay after next head and stale new-key CAS.
- RELEASE-0.2.4-FIRST freezes56/1/0semantic with onlyB01 failing on unchanged4af0360;
  eight deployment remain unsupported. Runtime correction follows this committed
  full-release baseline; supplemental authors must migrate profiles explicitly.
- Logs: deadline-first-01.log (superseded metadata label), deadline-first-02.log,
  release-024-first-01.log (intended exit1). Original first artifacts untouched.

## Round 27 — implement R7-048 against released0.2.4

- Full release first e689cf2 is committed before adaptation; exact authored0.2.3
  succession first0641033 and original native47c0205 stay immutable.
- Add red controls for both replace/correct across missing, prior, identical and
  incomparable receipts, entire state/dirty/captures/bindings preservation and
  same-key direct-successor retry. Preserve transitive successor, exact replay
  after a later head, separate CAS failure and plain incomparable import.
- Share one canonical strict ancestry traversal with authority current-head
  selection, avoiding arrival order or assertion-only intermediate requirements.
  Enforce the new gate only for authoritative replacement/correction.
- Explicitly migrate the old own B01 lineage regression to the released successful
  operation6; the public vector remains untouched. Run canonical, migrated
  supplemental, product/checker and package structural controls after correction.

### Round 27 correction progress

- Red successor controls produce seven intended assertions: six forbidden writes
  across replace/correct plus the exact expandedB01 trace. After the runtime gate,
  new negative/positive/full-state tests and the migrated lineage control pass.
- Canonical0.2.4 now57/57; four checker controls and all33package plants pass.
- Partial existing product run intentionally omitted two ASTRA24 profile-dependent
  controls but encountered a third old-profile exact comparison in transitive review.
  This metadata migration failure is not a runtime regression or passing evidence;
  full product/supplemental runs await the author's explicit0.2.4 migration.
- Logs: succession-red-01.log, succession-green-01.log,
  succession-native-partial-01.log, canonical-round27-01.log, controls-14.log,
  package-024-01.log. No expected fixture/profile rewrite by this seat.

### Round 27 final correction outcome

- One canonical strict predecessor traversal now drives receipt head selection and
  authoritative replace/correct qualification; equality is explicitly not succession.
  Canonical receipt-only intermediate events need no corresponding decision assertion.
- Missing/prior/identical/incomparable receipt refusals preserve all state, dirty-since,
  captures and bindings. Same-key valid retry succeeds. Direct/transitive successors,
  original receipt replay after a later head, separate CAS conflict and incomparable
  plain import remain valid. Gate runs after current-head checks and before commit;
  successful authorized replay returns before attempting a new succession.
- After owner609853e explicitly migrates the last20fixtures, full24product+4checker
  controls pass. Current0.2.4 canonical57/57 and supplemental54/54 pass; deployment
  eight canonical/one supplemental remain unsupported. All33package plants pass.
- Self-review checked only the two runtime changes (shared traversal and scoped
  admission gate), independent input/expected separation, prior CAS/retention/replay
  coverage and unchanged first artifacts. No foreign evaluator code was read.
- Final logs: succession-native-green-01.log, supplemental-round27-01.log plus
  canonical-round27-01.log/controls-14.log/package-024-01.log. R7-048 awaits
  independent review; ASTRA25-11 expiry code/order/replay remains separately pending.

## Round 28 — R7-053 deadline classification and next unit

- Succession correction942bdee is published; deadline work is now the next unit.
- Judge classifies original ASTRA25-11 as source052, package053 and mapping054.
  Required live retention is trusted context.at strictly before every applicable
  non-null deadline. At/after expiry: not_authorized/false before idempotency.
- Exact replay must recheck original outputs/transitive known inputs at current
  intake time; refusal preserves original receipt and full state without purging.
  Null, complete/incomplete-known and same-batch resolution retain existing rules.
- Await editor0.2.5 and explicit exact fixtures; freeze the full new release before
  changing the package-only runtime. Native firste689cf2 remains unchanged.
