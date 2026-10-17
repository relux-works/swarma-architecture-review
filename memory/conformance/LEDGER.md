# R7 divergence ledger

Sole writer: astra-27 (judge). Contract: `memory/MISSION-R7.md`.
Initial review baseline: `95f974b41667e25d4a3a7630055ef1c20690fb7d`.

## Review contract

Apply source precedence in `memory/designs/kernel.md`: owner decisions D-001–D-008,
kernel v0.2, normative companion, then bounded-evidence design. Do not reopen
settled design. The package supplies concrete grammar and normalization choices
within that contract; it cannot silently change source semantics. A package-only
implementer must be able to reproduce each exact expected semantic output.

Each submitted divergence or adversarial case receives its own row, with a
minimal witness and the relevant source/package clause. Classifications are
`spec-bug`, `impl-bug`, `ambiguity`, or `rejected`. A correction is closed only
against a committed fix and relevant rerun/control evidence. A source-level
choice the contract does not decide becomes an owner question; the judge does
not choose new architecture on the owner's behalf. Rejected cases retain their
reason. Mixed findings are split so a fixed package cannot hide an unfixed
evaluator, or vice versa.

## Items

| ID | Source (seat, file, event) | Vector or clause | Classification | Fix owner | Status | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| R7-001 | astra-24; [premise-quality-alternatives](cases/astra-24-premise-quality-alternatives.md) at `9ecd449`; event `$G4OHTOUl4Wqb3NVg7LDKrGvEjh9H_w7noy_5kFAQBR0` | Kernel §6.1; companion §§4–5; S03/S31 neighbors | Pending release inspection | astra-27 (classification); astra-24 (fixture) | open | A fully checked clean B+ path to C+ coexists with a conflicted A+ path. Explanation truncation/order must not make `conflicted_premises_only` true. Source-level requirement accepted; no package/evaluator failure observed. |
| R7-002 | astra-24; [rule-applicability](cases/astra-24-rule-applicability.md) at `9ecd449`; event `$oVPSMnZ16rOhG4J9bIPYpl0Gz8ahzkjS7HRmnYKAc2c` | Companion §§3–4; kernel §§2, 6; S10 neighbor | Pending release inspection | astra-27 (classification); astra-24 (fixture) | open | An expired checked A+ → B+ rule cannot carry current support; before its exclusive endpoint it can. Source-level requirement accepted; concrete grammar/behavior not yet available. |
| R7-003 | astra-26; [import-attribution](cases/astra-26-import-attribution.md) at `93455d8`; event `$_hBE9WQEffLFwyKMHmaG3P-pHANdFygcHEddq8zxP6A` | Kernel §§2, 6.1, 8, 9.1; companion §3 | Pending release inspection | astra-27 (classification); astra-26 (fixture) | open | Importer B may issue an attributed source report about A via C without claiming to be A. A submitted assertion with issuer A and submitter B still requires representation and may not be silently rewritten. Package must preserve original attribution, classes and witness origin. |
| R7-004 | astra-26; [publication-currentness](cases/astra-26-publication-currentness.md) at `93455d8`; event `$yfHdYWubs0jO06LmD0GiV5hRlAfmwZCeuruA1gvERi8` | Kernel §§1, 6.3–6.4, 9.2 | Pending release inspection | astra-27 (classification); astra-26 (fixture) | open | Freshness at a consumer horizon does not certify issuer-currentness. An unavailable issuer check supports only the last-received state, subject to known replacements and expiry. Exact bounded output labels remain package work. |
| R7-005 | astra-25; [hidden-premise-quality](cases/astra-25-hidden-premise-quality.md) at `5a32468`; event `$D58DR3_cFp-0TYJp-WFZHS95MPjO_CdsU00kf3SSL0w` | Kernel §§6.1, 7.3; S13/S24/S27 | Pending release inspection | astra-27 (classification); astra-25 (fixture) | open | Hidden A- in the same space cannot alter quality of authorized A+ → B+. Quality, budget and all disclosed metadata use the authorized graph. Explicitly admitting A- is the positive disclosure control. |
| R7-006 | astra-25; [declassification-intersection](cases/astra-25-declassification-intersection.md) at `5a32468`; event `$JRP0ZTvwmvjdy9dVvzatgS824Y1K6qZGjz5Az3_rSMw` | Kernel §§6.4, 7.1–7.2, 9.3 | Pending release inspection | astra-27 (classification); astra-25 (fixture) | open | Retained assessments from OA/OB do not authorize new disclosure after OB revokes its exact release. Every constrained owner's currently applicable decision is necessary; model review cannot substitute. |
| R7-007 | astra-25; [surviving-support-erasure](cases/astra-25-surviving-support-erasure.md) at `5a32468`; event `$cV4c9b6aHDM9Swa3VBXyHzHbG5DRKDK_fYgJbVWuabY` | Kernel §7.1/P08; companion §6/S12/S20 | Pending release inspection | astra-27 (classification); astra-25 (fixture) | open | Independent B may preserve C support while A-derived summaries/indexes/cached views require fencing and erasure. An unreachable controlled sink prevents completed erasure. Deployment qualification remains separate. |
| R7-008 | astra-25; [stale-restore-witness](cases/astra-25-stale-restore-witness.md) at `5a32468`; event `$7ed7G5T6VBlEQ1c53ObNr7Ab6sPC9h1GnaD2x8nQ7Nc` | Companion §6/S25; design retention contract | Pending release inspection | astra-27 (classification); astra-25 (fixture) | open | A genuinely external but stale witness covering e4 cannot establish completeness after acknowledged erasure e5. Restore remains closed until current coverage and reconciliation are established; a boolean external-witness flag is insufficient evidence. |

Pending intake rows are not adjudicated bugs. Every row will receive one of
the four mission classifications after its release evidence is available.
The package and both full evaluator reports remain pending.

## Judge worklog

### Round 0 — intake and source review

- Completed the required initial pull and identity onboarding as
  `ivmbp_swarma-memory_astra-27`; subscribed to room events for case intake.
- Read the entire R7 mission, decisions, kernel v0.2, companion, and design.
  No project-local skills were present. The CLI's printed a2a skill supplies
  coordination guidance; the mission's narrower ownership, no-spawn, no-board,
  and signed direct-main rules govern this collective.
- `memory/spec/` is absent at the baseline; no `PACKAGE LANDED` marker was
  present in rounds. Source implementer astra-22 has committed its source-only
  reading boundary and work plan at `95f974b`.
- Next: validate the landed release, inventory semantic versus deployment
  vectors, inspect both independent committed runs, classify all received
  items, and track fixes to evidence. Preserve the package implementer's blind
  first-run boundary when addressing it.
- Final gate: finalize the score and verdict, write the park note, push signed
  artifacts and acknowledge only after the convener's PARK marker.

This initial change records process and evidence only; it changes no executable
contract. Its relevant checks are ownership/diff review and signature
verification. Product negative tests wait for the concrete cases and runners;
no passing behavior is claimed from this documentation-only initialization.

Local tool readiness evidence: seat work directory
`.temp/tool-readiness-01.log` (git, Python, rg, a2a). Initial git pull completed
successfully from `6d14828` to `95f974b`; working tree was clean before this work.

### Round 1 — source cases queued for package inspection

Reviewed ASTRA24-01 and ASTRA24-02 in full at `9ecd449`. Both source-level
requirements are supported by the cited contract. Neither is an observed
implementation divergence, and an unreleased/absent package cannot yet decide
whether there is an additional specification bug. Accepted both for release
inspection and package-format fixtures; no owner decision is needed on these
requirements at present. Their negative controls protect against explanation
order altering semantic quality and historical rule qualification overriding
current applicability; neighboring valid paths prevent reject-all behavior.

### Round 2 — publication and attribution source cases

Reviewed ASTRA26-01/02 at `93455d8`. Kernel §9.1 expressly permits source import;
companion §3 separates an attributed report from the reported proposition. An
explicit importer-issued source report therefore needs no invented grant from
its subject, while an actual issuer/submitter mismatch remains governed by §2.
This is a distinction between two submitted record meanings, not permission to
downgrade an unauthorized issuer-A request into an issuer-B observation.

Kernel §9.2 separately requires issuer-version evidence and says that without
it the importer knows only the last state received. §6.3's consumer freshness
horizon cannot supply that missing knowledge. These source-level requirements
need no owner decision; classification of the concrete encoding and output
awaits the package. Both cases include valid controls and forbidden authority
or currentness upgrades. Source evaluator freeze reported at `4d4ef45`, with
20 source-derived controls; no package-vector result exists yet.

### Round 3 — disclosure and erasure source cases

Reviewed ASTRA25-01–04 at `5a32468`. All four recommended constraints follow
explicit normative boundaries: authorized-graph computation, current per-owner
release decisions, content/custody lineage independent of support, and current
restore reconciliation against outside-domain evidence. No source ambiguity
is established by these pairs. The release inspection must distinguish missing
grammar/prose from an actual evaluator defect and from a properly declared
unsupported deployment claim. Synthetic state transitions alone do not prove
real sink deletion, rollback resistance or isolation. The adjacent positive
controls in each case prevent a deny-all implementation from qualifying.
