# R7 package work log

## Producer baseline: 0.1.0-draft (historical account)

Scope: only memory/spec was written. No commit, publication, network access,
package installation, background process, external recipient or delegated worker
was used. The containing repository and all input documents were left unchanged.
This log is inside the authorized output directory rather than a separate task
tracker or temporary directory, as required by the task's explicit write boundary.

Read in order: owner decisions; consolidated kernel; semantic companion;
bounded-evidence design; review-1 and profile gap notes. The output is entirely
English and the kernel contains no platform names, private links or host paths.

Tool readiness: Python 3.14.7 and ripgrep 15.2.0 returned expected versions. Local
skill directories agents/skills, .claude/skills and .codex/skills were absent;
the initial inventory reported those missing paths. No applicable in-directory
skill or task tracker was found. No external installed skill was read because
this task restricts all project reads to the supplied directory.

Completed work:

1. Closed the normative model in 49 stable clauses, preserving the owner decisions
   and the consolidated kernel's explicit amendments. Recorded 32 closure choices
   and four outstanding deployment-owner inputs in AMBIGUITIES.md.
2. Authored 14 closed schemas, 14 canonical domain documents, one complete small
   decision corpus, and 61 complete vector snapshots. Expected results are hand
   specified; formatting helpers do not evaluate support or infer expected truth.
3. Reviewed evidence signs, tainted premises, deterministic bounds, authority
   partial order, atomic cut visibility, unknown valid time, freshness expiry,
   origin deduplication, disclosure inheritance, declassification redaction,
   independent live revocations and erasure/restore boundaries against the prose.
4. Implemented the stdlib checker and exercised 13 bounded violation controls:
   unknown field, missing query, invalid polarity enum, boolean-as-integer,
   duplicate key, non-finite number, floating point, open object schema,
   overlapping oneOf, out-of-package reference, forbidden outcome, missing domain
   field, and a semantic difference that normalization must preserve. Positive
   nearby controls passed. Controls run in memory without modifying fixtures.
5. Regenerated artifacts after contract fixes and reran the structural checker.
   Linked every normative clause to vectors and every vector to source clauses.
   Separated 53 semantic cases from eight protected-deployment cases. No evaluator
   run, production security qualification, timing proof or statistical randomness
   certification is claimed.

The reusable fixture is already a post-admission snapshot. S04/S05 likewise
supply explicitly recomputed post-withdrawal snapshots. B10 models a witnessed
restore; S25 models an unwitnessed fenced restore with tentatively present backup
payloads. Those are test inputs, not operational claims about a live service.

Final command (exit 0):

```sh
python3 memory/spec/checks/validate.py
```

Final output:

```text
PASS: 90 JSON files parsed; 14 closed schemas; 14 domain documents; 1 fixture corpus.
PASS: 61 vectors (53 semantic, 8 deployment); 49 normative clauses covered; coverage IDs unique.
PASS: references, forbidden predicates, normalization pairs, kernel hygiene; 13 checker controls detected their intended violations.
RESULT: structural package validation passed. Evaluator semantics and protected deployment behavior were not executed.
```

Handoff: the package is ready for the orchestrator's review and independent
implementation/divergence work. No publication or landing was performed here.

## Editor release: 0.2.0-draft

Owner: astra-21, under MISSION-R7. This section supersedes the producer handoff above for current package status. Source baseline: kernel v0.2; initial package commit 0ef608a. Changes address R7-006, R7-008, R7-009 and R7-010.

- Added K-REV-4, K-SNAP-1 and K-PROJ-2; normalized tuple, frozen applicability, controlled-input lineage/unknown lineage, current per-owner release decisions and exact audience alias lookup are normative. No new record kind or source authority is introduced.
- Closed grammar now carries integration lineage facts, per-input owners, exact owner decisions, live decision revocation, plural release assessments and exact excluded_refs. Initial snapshots and all authoring helpers use the same 0.2.0 schema namespace.
- Added P12–P15; P05 pairs missing second-owner refusal, valid two-owner release/delivery and revoked redelivery; B10 pairs stale external witness refusal/continued fencing and current-complete reconciliation.
- The structural checker now verifies integration lineage consistency, unique constraint-owner and alias bindings, and the new grammar. Three additional bounded plants detect incomplete lineage misrepresented as complete, duplicate owner bindings and aliases that merge different principals. Nearby valid snapshots pass.
- `python3 memory/spec/checks/validate.py` passes: 94 JSON files; 14 closed schemas; 14 domain documents; one fixture; 65 vectors (57 semantic, 8 deployment); 52 clauses; 16 intended checker violations detected.
- Python syntax checks and deterministic regeneration of all 94 JSON artifacts pass. A comparison against the original committed expected reports confirms 59 prior reports unchanged apart from semantic_profile; only P05 and B10 intentionally gain controls. No evaluator comparison was used to generate an oracle.

Local evidence: `.temp/astra-21/validate-04.log`, `.temp/astra-21/regeneration-01.log`; ongoing task plan `.temp/tasks.md`. Those are scratch paths in the editor checkout; the exact commands and outcomes are preserved here for other seats. Independent evaluator and adversarial review remain required. Structural checks do not establish semantic correctness or any protected-deployment qualification.

## Editor release: 0.2.1-draft

Scope: R7-014/018/019/021/022; exact changes and migration requirements are in RELEASES.md. Validation: 65 vectors (57 semantic / 8 deployment), 52 clauses, 20 intended checker violations. All 94 JSON artifacts regenerate deterministically; Python syntax and diff-whitespace checks pass. Expected-report changes are restricted to S23, S24, S32, P02, P15 and their B03/B07 derivatives. B01's expected report is unchanged.

New negative controls cover the wrong subject, equal ID strings without identity evidence, accepted writes lacking integration evidence, unqualified global dirtiness, mixed AND-state overstatement and real unchecked publication currentness. Nearby valid controls preserve own/delegated admission, private-visible invalidation and the stronger complete support alternative. The B01 omission was observed by both independent implementation and the strengthened checker before repair.

Local evidence: `.temp/astra-21/lineage-regression-01.log` (intended existing-defect failure), `.temp/astra-21/validate-08.log`, `.temp/astra-21/regeneration-02.log`. Current checks remain structural; independent behavior runs are required. No other seat files were edited.

## Editor release: 0.2.2-draft

Scope: R7-031 erasure receipt metadata versus protected closure. Added explicit erase receipt_context with actor-bound recipient; narrowed only disclosed refs, retained full custody/fences, and specified exact replay/conflict/current-authorization behavior. P08 supplies purpose-separated metadata grants, an erase-only grant, authorized control, exact retry, changed-context conflict and revoked retry refusal. The existing 64 other expected reports remain unchanged apart from profile version. All existing erases receive explicit private/read context.

Structural checks: 94 JSON artifacts, 65 vectors (57 semantic / 8 deployment), 52 clauses, 23 intended checker plants. Missing receipt context and recipient override fail the exact closed operation schema; a hidden-ref output plant triggers P08's actual forbidden predicate. These are checker controls, not proof of evaluator authorization semantics.

The unchanged package evaluator was run against the uncommitted 0.2.2 candidate with an explicitly uncommitted package label. It returned the intended failure: only P08 fails, revealing hidden refs and replaying metadata after revocation. The authorized full-list control, exact same-context retry, changed-context conflict, protected full purge and other 56 semantic vectors pass. Eight deployment cases remain unsupported. This red run must not be reported as corrected conformance. Full state-preservation checks for refused replay belong to the independent evaluator controls; the canonical postconditions assert the declared inventories and custody effects.

Local evidence: `.temp/astra-21/erasure-receipt-review.md`, `.temp/astra-21/validate-11.log`, `.temp/astra-21/package-evaluator-022-red.md` / `.json`, `.temp/astra-21/package-evaluator-022-red-01.log`, `.temp/astra-21/expected-delta-022-01.log`, `.temp/astra-21/regeneration-03.log`. No other seat artifacts were edited. Semantic closure requires new-release evaluator runs and judge review.

## Editor release: 0.2.3-draft

Scope: R7-039 explicit retention context and R7-042 future-fact checker correction. Source requirement: bounded-evidence Retention section requires an explicit retention purpose; independent retain is already mandatory. The package now binds that purpose/audience to the authenticated actor and requires exact current authority for each output and transitive known content input. Same-batch resolution, unknown-lineage lower bounds, empty onward labels, independent retain revocation and current-authorized replay are explicit. All four write contexts require the new field. Only P11/P13 expected reports change after profile normalization; the other 63 reports are unchanged. See RELEASES.md for exact migration and controls.

The future-fact checker false positive was reproduced before correction using unchanged ASTRA25-10. Existence is deferred only for facts whose outputs are not admitted. Successful writes are checked against prior admitted records and the whole current batch; admitted complete and unknown-lineage inputs still require actual records. Duplicate/direct-fact checks are preserved. The original independent fixture and expected outputs were not edited.

Validation: 94 JSON artifacts; 14 schemas; 65 vectors (57 semantic / 8 deployment); 52 clauses; 32 intended structural controls. New plants reject missing retention_context in each of four operation variants, a principal override, an unauthorized receipt, an accepted batch missing an actual input, and dangling complete/unknown admitted inputs. Nearby valid same-batch/future-fact states pass. All 94 JSON artifacts regenerate byte-for-byte; Python syntax and diff-whitespace checks pass.

Unchanged package runtime at checkout 53266dd gives 55 semantic passes and only P11/P13 failures on the explicitly labelled uncommitted 0.2.3 candidate; 8 deployment cases are unsupported. The first unauthorized admissions and their subsequent state effects are retained as red evidence. Isolated prescribed positive traces for both vectors match every expected field after only opaque-handle normalization, including exact replay, same-batch inputs and empty-label non-disclosure. These positives do not prove retention refusals. Independent release adaptation and full-state atomic-refusal checks remain necessary; canonical inventories do not expose every internal state component.

Evidence in editor scratch: validate-15.log, regeneration-04.log, expected-delta-023-01.log, retention-future-fact-red-01.log, future-fact-correction-01.log, retention-positive-controls-01.log, package-evaluator-023-red.md/json and adjacent run log. Task continuity is .temp/tasks.md. No evaluator, adversary or source-design file was edited.

## Editor release: 0.2.4-draft

Scope: R7-049 exact authority-successor refusal mapping, K-REV-3/K-REF-1.
Missing/prior/identical/incomparable receipts refuse `authority_receipt_required`,
false; direct/transitive successors, authorized exact replay and ordinary
incomparable import remain positive boundaries. CAS remains separate.

Validation: 94 JSON artifacts, 65 vectors (57 semantic / 8 deployment),
52 clauses, 33 intended checker violations. `validate-17.log` records the
structural result; `regeneration-05.log` proves byte-identical regeneration and
Python syntax; `expected-delta-024-01.log` proves only B01 changes after version
normalization, with the original fixture byte-identical. All logs are under the
editor's task-scoped scratch directory.

The unchanged runtime's full canonical red run is retained in
`package-evaluator-024-red.md/json` and its adjacent command/exit log: 56/1/0
semantic, eight deployment unsupported. Separate `succession-024-probes.py`,
its JSON and log record full before/after states for each invalid receipt class,
all-field comparison of prescribed positive direct/transitive/replay/CAS traces,
and ordinary incomparable import with no replacement/dirty effect. No evaluator
receives expected output; comparison follows execution. Negative state mutation
is the known failure witness, not a passing implementation. R7-047/048 runtime
corrections and independent release runs remain separate work.
