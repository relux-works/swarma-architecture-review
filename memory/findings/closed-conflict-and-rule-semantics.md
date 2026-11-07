# Four evidence labels do not define an inference calculus

- Lens: semantics and formal core.
- Author: astra-03 (five 1).
- Status: proposed.
- Confidence: high.

## Problem

The base combines ATMS, a justification DAG and Belnap-style statuses without stating which consequences follow from conflicting premises. Ordinary ATMS labels filter inconsistent assumption environments; independent positive/negative evidence channels can preserve both. Neither name resolves the choice.

A second ambiguity is the notation `C=(A AND B) OR (D AND E)`. Two sufficient one-way support rules do not license deriving opposing C from opposing A and D. Treating the notation as a full definition can introduce that consequence. Losing support is also not the same as acquiring opposing evidence.

Documentary attribution, a reason to review an adopted decision, and a checked sufficient rule are three different edge meanings. A source signature cannot turn the first into the third.

## Evidence

- Base part 1 §§3–5. The base already separates epistemic, verification and decision status; retain that separation and make the rules concrete.
- de Kleer, *An assumption-based TMS* (1986), pp.144–145, https://dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf .
- Sutcliffe, Pelletier and Hazen, *Making Belnap's Useful Four-Valued Logic Useful* (2018), https://cdn.aaai.org/ocs/17599/17599-77711-1-PB.pdf . Four-valued representation does not settle the rule conditional. Accessed 2026-10-14.
- Proposed signed-rule counterexamples S02,S03,S05,S08,S21,S22 in [semantics companion](../designs/bounded-support-semantics-astra-03.md).

## Proposed change

Name and version a finite signed-rule profile separately from evidence rendering. Use explicit one-way all-of sufficient rules and multiple alternative rules; no completion, contraposition, default negation or explosion. Preserve conflicts and source qualification. Distinguish documentary_basis, review_on_change and sufficient_support. Scope claims by exact revision, perspective/context and valid time. Reject unsupported inference cycles in the first profile; domain graph cycles remain legal.

## Rubric rows affected

R1 (minimal closed kernel), R6 (honest epistemics), R7 (deterministic conformance).

## Confirmed by

- astra-06, five 2, `$9Og11QdbR3N1C-_IDJ_7DOz5rCLDQFEO0JmC0FlyiBM` in `f-conflict-semantics`: independently confirms signed support versus ATMS nogood distinction, withdrawal versus negation and distinct edge meanings.
- astra-06 adversarial refinement `$xo9GjCq6DOlYLcCGOM8NsGmf8ax8frBJtWAL_Iq2YmE`; author response/adoption `$Wn4qxVWxqyUWx27i2Mf6KkDW5KjKhEmULrFXAuAT2IU`.
- Candidate event `$S11M0JLIejp2VDPHjWALSFSFEJXh6sGbPwOxpC91fzo`.
