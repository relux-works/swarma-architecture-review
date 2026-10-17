# ASTRA24-01: premise quality quantifies over alternative support paths

Status: source requirement accepted; released prose closes the choice; exact regression vector supplied.
Source baseline: `cca7b6e`; kernel v0.2. Owner: astra-24.

## Clauses

Kernel §6.1 requires `premise_quality` to survive every rendering and adds
`clean_path | conflicted_premises_only | not_fully_checked`. Companion §§4–5
makes alternatives OR, preserves support from conflicted premises, and separates
witness existence from full explanation enumeration. S03/S31 exercise only the
conflicted path, not a clean alternative.

## Minimal separating input

All records are admitted, authorized, real, valid at the same cut and fully
resolved under one policy. Every rule is checked sufficient support.

```text
root A+; root A-; root B+
r1: A+ -> C+
r2: B+ -> C+
query C; evaluation budget sufficient for all signed dependencies
```

There is no B-, C- or rule concluding an opposing literal. Both rules are valid
at the cut. Repeat with the rules stored/enumerated in reversed order and with
an explanation limit of one.

## Two readings and separating output

| Field | A: quality of the first rendered proof | B: quality of the evaluated support alternatives |
| --- | --- | --- |
| C support witness | present | present |
| C support evaluation | complete | complete |
| C support premise_quality, if r1 rendered first | conflicted_premises_only | clean_path |
| C oppose witness | not_found | not_found |

Reading A treats a truncated explanation as the complete set of usable paths.
Reading B treats `clean_path` as existence of a fully checked clean path. The
second rule is such a path; the first rule's conflict cannot remove it.

## Recommendation and controls

Use B. `conflicted_premises_only` asserts that no checked alternative is clean;
that assertion is false here. An explanation cap must not change the evaluated
quality. Reversing rule order must preserve the result.

Controls: remove r2, yielding present support with
`conflicted_premises_only`; remove A- instead, yielding `clean_path` even with
only r1. If B- evaluation is cut off before it can establish absence, a proof
through B+ alone does not certify a clean path: preserve the witness and use
`not_fully_checked` unless another checked clean path already establishes the
existential result. Never manufacture C- from A-.

## Evidence and limits

This is a proposed separating fixture, not a reported evaluator failure.
Package-format JSON and concrete package clauses will be added after release.
The judge decides whether the release already closes this case, needs a fix,
or leaves an owner-level ambiguity about the quality vocabulary.

## Package inspection and exact fixture — round 2

Release `0.1.0-draft` at `0ef608a` already closes the prose choice in
K-EVAL-4: a demonstrated clean path wins; K-EVAL-7 separates explanation caps.
This is regression coverage, not a confirmed package bug. Judge intake is
R7-001. The accompanying `.vector.json` uses abstract A = `rec:a`, abstract
B = `rec:c`, and conclusion C = `rec:b`. It captures the full two-path
explanation, then caps rendering at one path: the retained first path is the
conflicted one, while both outputs must still report `clean_path`. The complete
extended polarity records are normalized-equal. Canonical S03 is the nearby
conflicted-only control.

Structural validation passed using the package validator on the exact owned
fixture: closed shape, initial references, handle normalization and forbidden
predicates. Planting `conflicted_premises_only` in the expected-shaped result
triggers the intended forbidden predicate. No independent evaluator run yet.
Evidence: seat-local `.temp/case-vectors-validate-01.log`; whole-package
validation `.temp/package-validate-01.log` passed 61 vectors structurally
(53 semantic, 8 deployment), with 13 intended checker controls.

Judge disposition, round 3: R7-001 rejected as a spec defect in `0.1.0-draft`;
existing prose is explicit. Regression fixture retained. Any future evaluator
mismatch requires a separate implementation-bug row.

## Source evaluator execution — round 4

The frozen astra-22 adapter explicitly reports `unsupported` because it does
not enumerate exact proof paths. No semantic pass or failure is inferred from
that result. The fixture remains unchanged at SHA-256
`5c480a32fed11b4f508aabf638e5114be40de8be110c808d41cc842cc0b389e9`.
Evidence: source-owner `impl-astra-22/runs/case-first.json` and seat-local
`.temp/astra22-owned-cases-03.json`.

## 0.2.0 migration and independent rerun — round 5

The owned vector now uses 0.2.0 grammar: release version, disclosure decisions,
projection exclusions and explicit direct synthetic integration-lineage facts.
An initial migration check caught missing facts for added fixture records; the
complete corrected fixture passes `.temp/case-vectors-validate-07.log`. Earlier
semantic hashes above refer to their stated historical fixture revisions.

Package-only evaluator `0008dc3` passes the complete original-release fixture
against 0.1.0 schemas, including full versus truncated explanation. Source
evaluator `fb7df98` continues to declare exact proof enumeration unsupported.
Evidence: `.temp/astra23-owned-cases-0.1.json` and
`.temp/astra22-owned-cases-06.json`.

Round 6: the current 0.2.0 package evaluator also passes the exact fixture
(`.temp/astra23-owned-cases-02.json`); no old-profile workaround is needed
for the current result. Source exact-proof enumeration remains unsupported.

## 0.2.1 verification — round 7

The fixture now supplies explicit `policy.subject_principals` and empty
`runtime.dirty_causes`, with the 0.2.1 semantic profile. Its semantic expectations
are unchanged. Closed grammar, references, normalization and intended forbidden
plants pass in `.temp/case-vectors-validate-09.log`.

Current fixture SHA-256: `f4c92da7f78755f0c77540fd0c9e2b680e22fd1de1fc1fdd791481d1779f9065`.
At checkout `4fadedd`, package evaluator fix `7c765fe` passes the entire
fixture. Source evaluator continues to report exact proof enumeration unsupported.
Exact reports: `.temp/astra23-owned-cases-03.json` and
`.temp/astra22-owned-cases-08.json`. Executors receive no expected outputs.

These are semantic fixture results, not protected deployment qualification.

## Package 0.2.2 profile migration

Round 15 explicitly migrated the vector to `0.2.2-draft` at release `7e71765`.
Only semantic_profile metadata changed; no input or behavioral expectation
changed. This seat has no erase operation requiring the new receipt context.
Normalized equality and old/new hashes are recorded in
`.temp/astra24-profile-022-migration.json`. Both evaluators preserve this case's
pass in source report19 and package report11. Earlier hashes above identify
the historical profile-specific runs.

## Package 0.2.3 explicit migration

Round 21 migrates this case to `0.2.3-draft` (`23290b3`). Behavioral expected
results and initial states are unchanged. Read-only operations need no storage
context; each of this seat's six revise operations explicitly binds private/read
under its existing actor/space/record retain grant. No grant is inferred from a
later query. `.temp/astra24-profile-023-migration.json` records old/new hashes,
exact operation contexts and normalized equality. Structural and intended
forbidden controls pass log 22. Earlier hashes identify historical profile runs.

## Round 27 profile migration to 0.2.4

Current exact fixtures explicitly name `0.2.4-draft` from release `ef02647`.
Only expected-view `semantic_profile` values changed; initial state, operations,
queries and behavioral expectations are byte-equivalent after that declared
normalization. All twenty owned fixtures pass structural and intended forbidden
controls (log27). `.temp/astra24-profile-024-migration.json` records old/new hashes
and every changed path. Historical hashes and first reports remain unchanged.
