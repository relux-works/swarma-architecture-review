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
