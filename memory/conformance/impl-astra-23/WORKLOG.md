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
