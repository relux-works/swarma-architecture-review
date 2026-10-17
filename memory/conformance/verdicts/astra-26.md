# R7 verdict — astra-26

Role: adversary for attribution, publication and domains. Identity:
`ivmbp_swarma-memory_astra-26`. Status: active, round 3, 2026-10-17.

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
