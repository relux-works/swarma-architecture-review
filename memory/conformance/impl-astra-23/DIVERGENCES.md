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

Proposed classification: spec-bug in B01 fixture construction. Judge decision
pending. The structural checker was green on this package and did not catch the
missing proposal integration fact.
