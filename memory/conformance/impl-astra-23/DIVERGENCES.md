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
