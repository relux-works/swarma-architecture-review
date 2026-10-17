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
