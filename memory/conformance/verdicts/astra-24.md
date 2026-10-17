# R7 verdict: astra-24 — semantics adversary

Status: active, round 4. Source baseline: `95f974b`; kernel draft v0.2.

## Scope and method

Read the complete R7 mission, owner decisions D-001–D-008, kernel v0.2,
the bounded-support companion and bounded-evidence design. This seat owns
semantic counterexamples and their package-format vectors, not the package,
evaluators or divergence ledger. Only synthetic, non-sensitive fixtures are used.

The initial audit targets independent polarity completeness, existential versus
universal premise-quality claims, one-way registered rules, exact revision
authority and authority ordering, unknown and half-open valid time, freshness,
and the separation of write collision, ambiguous currentness and evidence conflict.

## Round evidence

- Round 0: `memory/spec/` is absent at baseline `95f974b`; no package conformance
  result is claimed. Source reading and a2a onboarding are complete.
- Tracking and tool-readiness evidence: seat-local `.temp/tasks.md`,
  `.temp/tool-readiness-01.log` and `.temp/a2a-readiness-01.log`.
- No evaluator, deployment qualification or external effect is claimed by this seat.

- Round 1: submitted source-contract cases ASTRA24-01 (alternative-path
  premise quality) and ASTRA24-02 (rule applicability at a half-open endpoint).
  They are counterexample proposals, not observed evaluator failures.

## Package review and R7 row

Release `0.1.0-draft` at `0ef608a` passes the structural checker: 61 vectors
(53 semantic, 8 deployment), 14 closed schemas, 49 covered clauses, 13 intended
checker-violation controls. This is structural evidence only.

K-EVAL-4 and K-RULE-2/K-TIME-1 already specify the recommended readings in
ASTRA24-01/R7-001 and ASTRA24-02/R7-002. Both owned exact JSON fixtures are
structurally valid; they include full-versus-truncated explanation and
inclusive-start/pre-end/exclusive-end controls, respectively. Their expected
outputs were authored from the contract, without using either evaluator.

**Provisional R7: 1 at this baseline.** The package now exists and validates;
independent semantic execution and the editor's kernel-v0.2 update remain
pending. R7-001 and R7-002 are rejected as package-defect allegations; their regression
fixtures remain. ASTRA24-03 now asks the judge to close source-state aggregation
inside a mixed AND witness (independent A, retained-only B). Its structurally
valid exact fixture records the proposed prior-only result and direct-root
controls. The source evaluator exhibits the proposed ASTRA24-03 state disagreement;
its owner independently recorded ASTRA22-04. Judge classification is R7-014 (`spec-bug`, package editor) and R7-015
(`impl-bug`, source implementer). Both fixes remain pending. No source ambiguity has been established.
The judge owns the collective score. No protected deployment is qualified.

## Owned-vector execution

Frozen source evaluator at `3045117`, package `0.1.0-draft`:

| Case | Result | Evidence |
| --- | --- | --- |
| ASTRA24-01 | unsupported | Exact explanation enumeration is explicitly unimplemented. |
| ASTRA24-02 | pass | Both interval controls, exclusive endpoint and surviving alternative match exactly. |
| ASTRA24-03 | fail; confirmed R7-015 | Mixed AND conclusion is independent_attestation; required prior-only result, source references and already-known empty-channel states differ. |

The case documents retain exact field differences, fixture hashes, independent
source-owner evidence and seat-local logs. Structural checks and intended
wrong-result plants pass for all three current fixtures. Execution never reads
expected answers; no other seat's files were changed.

## Remaining work

Continue reviewing package semantics; obtain independent runs on the owned
vectors and judge dispositions; verify any accepted repairs; remain in the round protocol
until the convener posts PARK, then finalize this verdict and the park note.
