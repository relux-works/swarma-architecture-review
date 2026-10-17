# astra-21 package editor verdict

Status: round 1, active; not a final conformance claim.

Sole package writer for `memory/spec/`. Read MISSION-R7, decisions D-001–D-008, kernel v0.2, the normative companion and design, and the landed package prose and authoring tools. Baseline `0ef608a`, package `0.1.0-draft`. Identity `ivmbp_swarma-memory_astra-21` onboarded and PACKAGE LANDED confirmed in rounds.

## Work and evidence

The initial package passes `python3 memory/spec/checks/validate.py`: 61 vectors (53 semantic, 8 deployment), 49 clauses, 14 closed schemas, and 13 intended checker violations detected. This is structural validation, not evaluator evidence or deployment qualification. Local log: `.temp/astra-21/validate-01.log`; tool readiness: `.temp/astra-21/tool-readiness-01.log`; continuing plan: `.temp/tasks.md`.

The mandatory next release will encode the normalized input tuple, three conflict outcomes, immutable historical snapshots with current applicability checks, integration-established lineage and unknown lineage, per-owner live declassification decisions, projection exclusion, and P12–P15. Judge-accepted spec bugs will be addressed in subsequent or combined versioned releases with exact vector evidence. No source design changes are authorized.

## R7 position

Provisional **1/2**: prose, closed schemas and structurally executable fixtures exist, but v0.2 amendments and two independent full vector reports are pending. No deployment pass is claimed. All source ambiguity must go to the judge and owner-question flow.

## Delivery protocol

Only the package and this seat's verdict/park note are edited. Python standard library only; no installs, web, servers, background workers, additional agents or task-board writes. Signed direct-main delivery follows the mission's explicit exception to the general PR workflow. Await the convener's PARK before finalizing and ending the session.

## Round 1 — 0.2.0-draft release

The v0.2 package upgrade is ready for independent review: P12–P15, normalized inputs, distinct conflict outcomes, immutable historical snapshots with current applicability, integration-established lineage and unknown-lineage blocking, live per-owner declassification, and projection exclusion. R7-006, R7-008 and R7-010 have explicit grammar/prose fixes and neighboring controls. R7-009 is the assigned uplift.

Validation: 65 vectors (57 semantic / 8 deployment), 52 clauses, 16 intended checker controls; deterministic regeneration passes. Of the 61 old expected reports, 59 are unchanged except the semantic profile version; P05 and B10 intentionally add multi-owner and stale-witness controls. Exact commands/evidence are in memory/spec/checks/BUILD_NOTES.md. Self-review checked owned scope, schema/authoring consistency, all new hand-derived reports, preserved old oracles and forbidden outcomes.

Provisional score remains **1/2**, pending judge verification and two independent implementation reports. No source design was amended, no unsupported operation was counted as passing, and no protected-deployment qualification is claimed.
