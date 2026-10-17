# R7 verdict — astra-26

Role: adversary for attribution, publication and domains. Identity:
`ivmbp_swarma-memory_astra-26`. Status: active, phase 2 round 16, 2026-10-17.

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

## Round 8 — second evaluator and closed owned defects

- Judge `6a4f307` closed **R7-022 fixed at `f31d58f`** after its independent
  current-release run. Both owned spec defects, R7-010 and R7-022, are closed;
  R7-003/004/016/017 remain rejected defect allegations with executable
  regression controls retained. No owned case awaits classification.
- Independently ran source evaluator `26d8cc6` on the same eight 0.2.1 owned
  fixtures: **7 pass / 0 fail / 1 unsupported**. ASTRA26-06 now exactly verifies
  the source identity fix separately tracked as R7-026. Import attribution,
  location slots, introduction separation and both representative-alias
  controls also pass. ASTRA26-02 is unsupported for unconfirmed imported
  currentness; its checked-currentness control passes. Unsupported is not a pass.
- Source controls pass: 25 core, 3 adapter, 7 transaction, 5 comparator. Exact
  results and implementation/input hashes: seat
  `.temp/r7-astra-26/owned-cases-astra22-02.json`; control logs:
  `astra22-source-controls-02.log`, `astra22-adapter-controls-02.log` and
  `astra22-transaction-controls-02.log`. No foreign file was modified.
- Current package-evaluator evidence remains **8/8 owned**, **57/57 canonical**
  semantic. Source canonical publication is **43 pass / 0 fail / 14 unsupported**.
  A separate source quality-budget case from astra-25 remains under collective
  classification/fix, so this seat keeps the collective row **1/2** pending
  the final ledger. Deployment remains unsupported.

## Round 9 — final correction regression check

The package remains `0.2.1-draft` at `f31d58f`. After the source budget and
source-state corrections, reran the same eight owned inputs without modification:

| Evaluator head | Owned pass | Owned fail | Owned unsupported | Canonical published semantic pass/fail/unsupported |
| --- | ---: | ---: | ---: | --- |
| Source `512d006` | 7 | 0 | 1 | 43 / 0 / 14 |
| Package `8b9baf3` (execution code unchanged from `f5fdd8b`) | 8 | 0 | 0 | 57 / 0 / 0 |

The source's only owned unsupported case remains ASTRA26-02 unconfirmed
publication currentness, with its checked positive control passing. R7-010
alias attribution and R7-022 self-declaration attribution retain both positive
and negative guarantees in both evaluators. Inputs and expected answers were
not changed. Source controls: 33 core + 5 adapter + 7 transaction + 5 comparator.
Package controls: 4 comparator + 10 product. All passed.

Evidence in seat `.temp/r7-astra-26/`: `owned-cases-astra22-03.json`,
`owned-cases-astra23-05.json`, `astra22-source-controls-03.log`,
`astra22-adapter-controls-03.log`, `astra22-transaction-controls-03.log`,
`astra23-controls-04.log` and `astra23-semantics-02.log`. Fresh package validation
(`validate-04.log`) and owned structural checks (`cases-structural-05.log`) pass;
20 package checker controls retain their intended rejection behavior. The
checkout was clean after these read-only executions.

No new case, divergence, owner question or package change arose. The collective
row remains **1/2 pending judge verification/closure of R7-029**; no passing
local regression run substitutes for that review. All canonical deployment
vectors remain unsupported, and no live publication or protected service was
qualified.

## Phase 2 — directed coverage extension

Convener decision `$L-hdV2Wp2yWzysqNiFDI4gGEqZaR1AE4mwL7Pm0cPQc` explicitly
defers PARK and requires two independent implementations of all 57 semantic
vectors, plus targeted attacks on the 14 source-unsupported scenarios and kernel
v0.2 changes. The phase-1 score at `b1ae299` remains historical evidence; it is
not a claim of complete dual implementation coverage or permission to park.

Owned work plan for this phase:

1. Audit S23 imported-publication currentness with horizon expiry, known
   replacement and check availability, retaining root identity and attribution.
   A fresh control must stay current; expiry must not synthesize opposition or
   a known replacement, and stale copies must not be called current.
2. Audit P06/P12 delivery against the prepared exact selected item binding,
   including nonselected/excluded foreign records and independent forward
   rights. Missing rights on a selected item must reject; unrelated records
   must not veto an otherwise authorized delivery.
3. Audit P13/P15 lineage and exclusion through public attribution. Preserve
   foreign issuer sequences, admitted classes and private dependencies; no
   exclusion may silently rewrite the issuer's record or public identity.
4. Submit separating fixtures only after closed-format checks, explicit
   positive/negative expectations and independent execution observations.
   Retain old reports; never adjust canonical vectors or another seat's files.

Current uncovered canonical source vectors are B01, B07, P05, P06, P08, P12,
S07, S17, S20, S23, S24, S25, S26 and S27. The renewed publication/delivery
probes specifically target S23/P06/P12 and the P15 exclusion boundary. Other
seats own implementation changes, disclosure/erasure and semantic-budget attacks.

## Phase 2 round 10 — publication expiry and selected delivery

- Added **ASTRA26-07**, a checked-import horizon boundary. The fresh capture
  succeeds; at the exact expiry boundary both evaluators still call the stale
  publication current, contrary to kernel section 9.2 and K-PUB-2. The proposed
  existing-label result is last_received, with no invented replacement or
  negative evidence. Exactly two semantic fields separate the readings.
- Added **ASTRA26-08** and a nearby control. A readable but excluded independent
  assertion has no forward grant; package evaluator f5fdd8b wrongly refuses
  delivery of the separately selected authorized item. Adding only the excluded
  record's forward right makes the exact same expected sequence pass. Both
  retain the later current-right revocation refusal. Source 512d006 reports
  these delivery operations unsupported.
- All 11 owned fixtures pass closed shape/reference/normalization/forbidden
  checks. Package observation: **9 pass / 2 fail**. Source: **7 pass / 1 fail /
  3 unsupported**. No original case changed its semantic expected answer.
  Evidence: seat `.temp/r7-astra-26/cases-structural-06.log`,
  `owned-cases-astra23-06.json` and `owned-cases-astra22-04.json`. New cases await
  judge classification; they are not yet ledger dispositions.
- The renewed current row is **1/2**: dual canonical coverage is still 43/57,
  and the new publication/delivery differences remain unresolved. The earlier
  2/2 supported-vector score is preserved as the phase-1 historical result.
  Protected deployment remains unqualified.

## Phase 2 round 11 — three classified implementation defects

Judge independently reproduced and accepted both new cases: ASTRA26-07 becomes
R7-032 (source astra-22) and R7-033 (package astra-23); ASTRA26-08 becomes
R7-034 (package astra-23). All are implementation defects under existing clauses,
with no package edit or owner decision needed. First failing fixtures/outputs
remain preserved at `837591e` and in the round-10 reports. Requested boundary
and authorization controls are recorded in the case documents. Corrections
and exact-head regression evidence are pending; current score remains **1/2**.
Source proof enumeration has independently reported dual canonical coverage
44/57; it does not close these publication/delivery findings.

## Phase 2 round 12 — package fixes and 0.2.2 migration

- Independently verified R7-033/R7-034 implementation `f10c7ba`: **11/11 owned
  fixtures pass exactly** against original pinned 0.2.1 schemas. First failing
  outputs remain immutable. Neighboring expiry/identity/evidence and selected
  read/use/forward/release/fence/freshness controls are reviewed and green.
- Package 0.2.2 at `7e71765` introduces explicit erase receipt_context for
  R7-031. None of this seat's fixtures contains an erase operation; explicitly
  migrated all eleven semantic-profile stamps only and proved input/expected
  equality after normalizing that stamp. The same implementation passes
  **11/11** on the new grammar. No canonical fixture or foreign file changed.
- Package validation passes with 57 semantic / 8 deployment vectors and 23
  intended checker violations. All owned structural checks pass; package
  evaluator controls pass: 4 comparator and 12 product tests. Evidence: seat
  `.temp/r7-astra-26/owned-cases-astra23-07.json`, `owned-cases-astra23-08.json`,
  `cases-structural-07.log`, `validate-05.log`, `astra23-controls-06.log`,
  `astra23-semantics-04.log`. Original inputs are in `cases-0.2.1-phase2/`.
- Initial control execution immediately after pulling the new package mixed
  old owned stamps with new grammar and failed only semantic_profile equality.
  The retained `astra23-semantics-03.log` is not counted as a product failure
  or a pass; pinned old-package and explicit migrated reruns both pass.
- R7-032 source expiry correction and full dual coverage remain pending, as
  do separate collective findings and judge closure of these package fixes.
  Current score remains **1/2**; no protected deployment is qualified.

## Phase 2 round 13 — source import correction and new S23 coverage

- Source `1f35727` against 0.2.2 / `7e71765` gives **9 pass / 0 fail / 2
  unsupported** on the unchanged owned corpus. R7-032 expiry is fixed; the
  original unconfirmed-import case now also executes and passes. Only the two
  selected/excluded delivery fixtures remain unsupported in this source head.
- Canonical S23 independently passes exactly, with mirror-report sequence
  currentness distinct from genuine unconfirmed publication currentness. Eight
  adapter controls pass after review, retaining expiry boundary, replacement,
  ordinary-source and immutable-output/evidence controls. Evidence: seat
  `.temp/r7-astra-26/owned-cases-astra22-05.json`, `s23-astra22-01.json` and
  `astra22-adapter-controls-04.log`. Source canonical report is now 45/0/12.
- Judge independently verified package R7-033/R7-034 at `f10c7ba`; this seat
  retains the 11/11 old/new package evidence from round 12. R7-032 source
  correction is sent for separate exact-head review.
- No new case, expectation change or owner question. Full dual coverage and
  separate collective findings remain unresolved; current row **1/2**, with
  deployment still unqualified.

## Phase 2 round 14 — exact import check coverage

- Judge independently closed R7-032 at `1f35727`; all previously classified
  owned implementation and specification defects are fixed. Source canonical
  extension `e38c37c` reports 47/0/10, adding B01/S17; full dual coverage is
  still incomplete.
- Added ASTRA26-09 with a missing-one-source check, explicit-unverified neighbor
  and all-checks-current positive control. An admitted check for copy1/copy2
  must not silently certify copy3's different exact source object. Root origin
  deduplication remains one; evidence and attribution remain unchanged.
- Independently ran all fourteen owned fixtures on current 0.2.2. Source
  `e38c37c`: **12 pass / 0 fail / 2 unsupported** (delivery pair). Package
  `a016781`: **13 pass / 1 fail / 0 unsupported**. Only ASTRA26-09 fails there,
  in the two currentness fields; both new neighboring controls pass in both.
  This is submitted for judge classification, not a self-assigned ledger row.
- All fourteen shape/reference/normalization/forbidden checks pass. Evidence:
  seat `.temp/r7-astra-26/cases-structural-08.log`,
  `owned-cases-astra22-06.json`, `owned-cases-astra23-09.json` and matching logs.
  Earlier reports and first failures remain preserved. No expected answer in
  an existing fixture changed. Current row **1/2**; deployment unqualified.

## Phase 2 round 15 — source delivery and actor-binding challenge

- Source `5d079be` executes the previously unsupported selected/excluded pair:
  both pass unchanged. Independently verified canonical P06/P12 and reviewed/ran
  eight boundary controls for current rights, binding, expiry, fences, frozen
  captures and unrelated revocation scope. Canonical source report is now
  **49/0/8**; full dual coverage is still not claimed.
- Added ASTRA26-10: an ungranted foreign actor reuses the owner's saved delivery
  index. Package `a016781` returns a delivered receipt, whereas the actor-rights
  contract requires not_authorized. Source returns the exact refusal. The same
  trace retains the owner's successful delivery and its later post-revoke refusal.
- Current owned totals on 0.2.2: **source 15/0/0; package 13/2/0**. Package
  differences are the newly submitted ASTRA26-09/10; neither is self-classified.
  All fifteen owned structural checks pass. No pre-existing oracle changed.
- Evidence: seat `.temp/r7-astra-26/owned-cases-astra22-07.json`,
  `owned-cases-astra22-08.json`, `owned-cases-astra23-10.json`,
  `delivery-astra22-01.json`, `astra22-boundary-controls-01.log` and
  `cases-structural-09.log`. First failures are preserved for judge review.
  Current score remains **1/2**; no protected deployment or actual send is tested.

## Phase 2 round 16 — new publication defects classified

Judge independently reproduced and classified ASTRA26-09 as **R7-044 impl-bug**
and ASTRA26-10 as **R7-046 impl-bug**, both owned by astra-23. No specification
change or owner question is required. Case documents record the mandatory
positive/negative neighbors and preserve first failures; the actor finding is
limited to a caller with no authority, not hypothetical delegation semantics.

Corrections and exact-head review remain pending. Owned evidence stays source
15/0/0 and package 13/2/0 on the previously pinned 0.2.2 implementations. This
round only records dispositions; scope/diff checks apply and no new runtime pass
is inferred. Current row remains **1/2**, with protected deployment unqualified.
