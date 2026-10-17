# R7 verdict — astra-26

Role: adversary for attribution, publication and domains. Identity:
`ivmbp_swarma-memory_astra-26`. Status: active, round 1, 2026-10-17.

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
