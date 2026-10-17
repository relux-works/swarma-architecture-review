# R7 verdict — astra-26

Role: adversary for attribution, publication and domains. Identity:
`ivmbp_swarma-memory_astra-26`. Status: active, round 7, 2026-10-17.

## Baseline and scope

- Initial required pull reached `3acfe26`; the checkout was clean.
- Read the complete mission, owner decisions D-001–D-008, kernel v0.2,
  normative companion and bounded-evidence design. No source-reading
  restriction applies to this seat. No project-local skill was present.
- Used the CLI-provided a2a skill, subject to the mission's narrower rules:
  no agents, task-board writes, external builds, installations or web; only
  owned cases, this verdict and this seat's park note may be published.
- `memory/spec/` is absent at this baseline. No package conformance or
  deployment qualification is claimed.

## Work plan and negative expectations

1. Audit the envelope through admission, derivation, export and publication:
   issuer, subject, submitter, perspective, representation and admission class
   must remain distinguishable. Invalid representation must refuse rather
   than silently create an observer statement. Imports must preserve both
   the original issuer and the catalog without minting delegation.
2. Exercise revision, onward-disclosure revocation, unpublication and custody
   erasure as separate effects, plus exclusion without foreign-sequence edits.
   Test valid permitted effects beside the forbidden cross-boundary effects.
3. Audit publication reimport, root independence, stale/current qualification
   and audience-specific subject handles, including identifiers that can link
   otherwise disjoint cards.
4. Inspect executable domain schemas and fixtures for the complete
   archive-home → delete-home continuity scenario and synthetic profile cases:
   multi interests, location slots, self-assessed competence, account control,
   bounded intent and separate relationship/introduction predicates.
5. Once the package lands, encode minimal separating inputs in its vector
   format and submit concrete cases to astra-27. Recheck accepted fixes against
   released package versions, retaining counterexamples and positive controls.
6. Between completed rounds, wait through `a2a wait --timeout 20m`, consume the
   inbox and answer directed items. Finalize and acknowledge only after PARK.

## Evidence and score

Tool readiness was checked with the initial successful pull, `git --version`,
`python3 --version`, `rg` file enumeration, `a2a --help` and successful identity,
join, topics, read and inbox operations. Local evidence is in the seat work
directory `.temp/r7-astra-26/`; the complete CLI skill is `a2a-skill-01.md`.
The `rg` request for `memory/spec/` explicitly reported its absence; that is a
baseline observation, not a validation run.

Provisional R7 row: **0/2** at `3acfe26`, because the package is not yet
published. Both independent evaluator reports and the executable release are
pending. Semantic and protected-deployment evidence will be reported
separately. The source-only audit is not an implementation pass.

This round changes documentation only. Validation consists of scope/diff and
signature checks; product negative tests await the landed fixture format.
No cases or directed requests were outstanding at initialization.

## Round 1 — source-level separating cases

- [ASTRA26-01](../cases/astra-26-import-attribution.md): ordinary publication
  import must preserve original issuer/catalog attribution without implicitly
  granting representation or creating an assertion in the original sequence.
  The source allows competing envelope interpretations that the package must
  resolve. Includes refused impersonation and valid representation controls.
- [ASTRA26-02](../cases/astra-26-publication-currentness.md): an unexpired local
  freshness horizon does not itself establish issuer-current version knowledge.
  Separates identical importer inputs under two possible issuer histories,
  plus successful version-check, known replacement and expiry controls.
- Both cases are submitted for judge classification; neither is presented as
  an observed implementation failure. Concrete vector encoding awaits the
  package grammar. No protected-deployment test has been executed.
- The round-0 verdict was published signed at `daf285d` (signature `G`).

## Round 2 — first released package

- Consumed the convener's `PACKAGE LANDED` marker and pulled `0ef608a`.
  Read the package README, ambiguity choices, complete normative semantics,
  domain definitions and targeted schemas/vectors. The original profile
  reconciliation was also consulted for scenario boundaries.
- `python3 -B memory/spec/checks/validate.py` passes: 90 JSON documents,
  14 closed schemas, 14 domain documents, 61 vectors (53 semantic and 8
  deployment), 49 clauses and 13 intended checker-control detections. Evidence:
  seat `.temp/r7-astra-26/validate-01.log`. This is structural validation only.
- R7-003 and R7-004 were accepted as source requirements by the judge. The
  first package provides their basic encoding. Added three executable-format
  witnesses/controls for importer attribution, refused impersonation and fresh
  imported currentness with/without a current-version check.
- Added [ASTRA26-03](../cases/astra-26-representative-public-alias.md) and a
  success fixture and missing-alias control: a valid representative's distinct public alias is required
  by prose but its lookup in the closed policy needs an explicit definition.
  No source architecture change is proposed.
- All five new fixtures pass shape, initial-reference, normalization and
  forbidden-predicate checks using the package checker functions. Evidence:
  seat `.temp/r7-astra-26/cases-structural-01.log`. Fixture authoring corrected
  two shape mistakes detected by those checks; neither was a package failure.
- Decision B01 expresses archive-home replacement, exact authority receipt and
  stale registered dependent. Synthetic domains declare multi interests,
  location kind slots, non-authoritative competence, account-control evidence,
  intent horizons and separate relationship/introduction predicates. These
  declarations are being checked against behavior; existence alone is not a pass.
- Provisional R7 row is now **1/2**: the package exists and validates, but v0.2
  alignment, independent complete reports and case resolution are still pending.
  No protected-deployment execution or qualification has occurred in this seat.

## Round 3 — domain controls and first evaluator probes

- Judge rejected R7-003/004 as spec-defect allegations because `0.1.0-draft`
  already closes their source requirements; retained their executable controls.
- Judge accepted ASTRA26-03 as **R7-010 spec-bug**, owned by astra-21: define
  `policy.handles` lookup for every disclosed principal, including a distinct
  representative, without leaking identity or silently merging attribution.
- Added [ASTRA26-04](../cases/astra-26-location-slots.md): residence/current
  location coexist without replacement or incompatibility across their slots.
- Added [ASTRA26-05](../cases/astra-26-relationship-introductions.md): relationship
  status cannot fill a missing introductions predicate; an explicit declaration
  is accepted as data without contact effects. These are regression challenges
  for existing semantics, not asserted new package defects.
- Inventory check found no original semantic fixture using competence,
  account_link, availability, intent, relationship_status or open_to_introductions.
  The new introduction fixture now exercises the last two in this seat's corpus.
  The remaining domains have declarations but no behavioral qualification here.
- All seven owned fixtures pass structural/reference/normalization checks at
  the initial package version; evidence is seat
  `.temp/r7-astra-26/cases-structural-02.log`.
- Ran the seven fixtures against the first astra-22 adapter at `0216fbb`, with
  the unchanged source core hash `cfcf7e70d13f9054511b76ec26578b7d0299b5a33dbf2c6963d2f51816c27246`.
  The executor received only initial state, operations and query. Its existing
  five harness controls passed. Result: **1 pass, 0 fail, 6 unsupported**.
  The checked-currentness positive control passed exactly; all unsupported
  reasons are explicit in `.temp/r7-astra-26/owned-cases-astra22-01.json`.
  Nothing was written into the implementation seat's files.
- The collective's first source report is 17 pass / 7 fail / 29 unsupported
  semantic, with all 8 deployment vectors unsupported; its own divergences are
  already filed. This seat does not reclassify those results. Provisional row
  remains **1/2** pending the v0.2 release and independent runs.

## Round 4 — v0.2 review and independent baseline execution

- Package `0.2.0-draft` at signed `cde5754` validates: 94 JSON documents,
  14 closed schemas, 14 domain documents, 65 vectors (57 semantic / 8 deployment),
  52 clauses and 16 checker-control detections. Evidence:
  `.temp/r7-astra-26/validate-02.log` in the seat work directory.
- Verified R7-010's K-DISC-4 prose correction: exact existing-handle lookup for
  every disclosed principal, preserving a distinct representative and refusing
  a missing alias. Independent current-version execution is still pending.
- After astra-23 committed its blind first run at `0008dc3`, ran its untouched
  code against this seat's seven baseline fixtures using the original committed
  `0.1.0` schemas. Four comparator controls passed. The first run found one
  fixture-author error: location expected support was copied from P04 after the
  root assessment was removed. Corrected it using K-EVAL-1; no implementation
  change or weakening of a source requirement occurred. The corrected run is
  **7 pass / 0 fail** with exact output, forbidden and shape checks.
- Full run evidence and implementation/input hashes are retained in seat
  `.temp/r7-astra-26/owned-cases-astra23-02.json`; the original author-error run
  remains `owned-cases-astra23-01.json`. Baseline schema and input copies are
  retained under `spec-0.1.0/` and `cases-0.1.0/`, with old commits immutable.
- Migrated all owned fixtures to v0.2: explicit integration input facts, array
  release references, empty owner-decision/revocation inventories and exact empty
  exclusion sets. Structural/reference checks pass in
  `.temp/r7-astra-26/cases-structural-03.log`. No current-version semantic pass is
  inferred from this migration or from the old-version run.
- P15 correctly includes the pre-exclusion two-item control, post-exclusion
  one-item card, unchanged organisation view and unchanged record inventory.
  It now uses the competence schema, but labels a distinct organisation's
  attestation about the subject as `self_declaration`. Filed
  [ASTRA26-06](../cases/astra-26-foreign-self-declaration.md) with a proposed
  refusal/valid-self-declaration control to resolve that attribution issue.
  This eighth fixture awaits judge classification; no implementation bug claimed.
- R7-016/017 are retained regressions, rejected as spec defects. Provisional row
  remains **1/2**; no protected-deployment qualification is claimed.

## Round 5 — current-version execution verification

- Ran all eight owned fixtures against the package-only evaluator at signed
  `1439219`, using the actual `0.2.0-draft` grammar at `cde5754`. Its four
  comparator controls passed. No evaluator file was modified.
- All **seven previously classified fixtures pass exactly**, including both
  R7-010 representative-alias controls, import attribution/refusal, checked and
  unchecked import currentness, independent location slots and the explicit
  introduction-data positive control. R7-010's prose and targeted behavior fix
  are verified and the evidence was sent to the judge.
- ASTRA26-06, still awaiting classification, returns an admission receipt where
  the proposed correction expects `invalid_domain_value`. The separating effect
  is now observed; it is not prematurely labeled an implementation bug.
- Full exact outputs/differences, forbidden/shape checks and implementation/input
  hashes: seat `.temp/r7-astra-26/owned-cases-astra23-03.json`; comparator controls:
  `astra23-controls-02.log`. Provisional collective row remains **1/2** while
  other package/evaluator corrections and ASTRA26-06 are unresolved. Deployment
  qualification remains unsupported.

## Round 6 — explicit self-declaration identity

- Judge closed **R7-010** after the alias behavior evidence. Judge accepted
  **R7-022** as a package/source attribution mismatch, with editor astra-21
  owning the fix; no failure under the old package is relabeled an impl-bug.
- Reviewed `0.2.1-draft` at `f31d58f`: K-ENV-1 requires an explicit trusted
  subject/principal binding for self-declarations. P02 covers wrong-subject
  refusal and valid distinct-string identity; P10 preserves delegation. P15's
  foreign organisation facts retain all exclusion/unchanged-sequence controls.
- Migrated all eight owned fixtures to the new identity/dirty-cause grammar,
  with semantic expectations unchanged apart from the package-version stamp.
  Previous inputs are retained in seat `.temp/r7-astra-26/cases-0.2.0/`.
  Structural/reference/normalization checks and accepted-proposal integration
  facts pass. A valid admitted self-declaration passes; foreign issuer and
  equal-ID-without-binding plants fail for the intended attribution invariant.
- Package structural validation passes: 57 semantic vectors, 8 deployment
  vectors, 52 clauses and 20 checker controls. Evidence: seat
  `.temp/r7-astra-26/validate-03.log`, `cases-structural-04.log` and
  `attribution-controls-01.log`. These are structural checks; a current-contract
  evaluator run is pending. Collective row remains **1/2** while the new release
  and implementation corrections await independent evidence and judge closure.
  Protected deployment is still unqualified.

## Round 7 — current release behavior confirmed

- Package-only evaluator `f5fdd8b` against `0.2.1-draft` / `f31d58f` passes
  **all eight owned fixtures exactly**. R7-022 now rejects the foreign
  self-declaration without partial writes and accepts the actual subject's own
  declaration; R7-010's existing positive/negative alias guarantees still pass.
- Independently executed canonical P02/P10/P15 and B01: **4 pass / 0 fail**,
  including distinct-ID identity evidence, valid delegation, concurrent refusal,
  exclusion without foreign edits, and archive-home -> delete-home continuity.
  The implementation's four comparator and nine product controls also pass.
  No foreign implementation file or expected semantic output was edited.
- Exact behavior evidence with input/implementation hashes: seat
  `.temp/r7-astra-26/owned-cases-astra23-04.json` and
  `attribution-domains-astra23-01.json`. Control logs:
  `astra23-controls-03.log`, `astra23-semantics-01.log`. R7-022 verification
  was sent to the judge; its ledger closure remains independent.
- Finished a bounded domain-declaration review: intent remains attributed data,
  availability/intent use explicit freshness horizons, and account control needs
  an exact account_control assessment for stronger claims. Domain requirements
  do not create kernel inference/contact actions. Research/limits are retained
  in seat `.temp/r7-astra-26/domain-boundaries-02.md`. No new divergence was
  established. Declaration review is not runtime qualification of each domain
  schema or future services.
- The package evaluator's published canonical report is **57 pass / 0 fail /
  0 unsupported semantic**; the source report at `df499a1` still records
  **42 pass / 1 fail / 14 unsupported** before its new identity correction.
  Thus the collective row remains **1/2** pending outstanding implementation
  fixes and judge closure. All 8 canonical deployment vectors remain unsupported.
