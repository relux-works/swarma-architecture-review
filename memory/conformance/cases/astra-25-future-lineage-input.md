# ASTRA25-10: future integration inputs are checked at admission

Status: R7-042 package-checker spec-bug, assigned to astra-21; correction pending.
Package `0.2.2-draft`, release `7e71765`. Owner: astra-25.

## Clauses and separating input

K-DISC-1 explicitly permits protected integration facts for future proposals;
these facts are not admitted records. K-API-1 validates an operation against its
hypothetical post-batch state and commits no state or idempotency entry on refusal.
K-API-2 rejects an actually missing reference. K-VEC-1 requires valid initial
state, rather than pretending that future records already exist.

```text
Initial records: empty.
Protected facts: direct A with no inputs; deterministic B with exact input A.
1. admit(B), key B: invalid_reference; A is not yet admitted.
2. admit(A), key A: admitted.
3. retry the identical admit(B), key B: admitted, now with lineage [A].
Final cut: 102, with exactly A and B; query B succeeds.
```

This is an integration-controlled deterministic fact, not an untrusted citation.
It describes the input of a future intake after A becomes available. Neither
presence of that fact nor the first rejected attempt materializes A or B.

| Reading | Initial fixture | First B admission | B after A admission |
| --- | --- | --- | --- |
| Every fact input must exist in the initial record set | rejected before execution | never reached | never reached |
| Future facts remain protected admission evidence | valid | invalid_reference, no write | admitted |

Recommend the second reading. Restrict initial-state reference integrity to
already-admitted records; validate future fact inputs when their corresponding
operation is evaluated against the current hypothetical batch. Do not globally
allow missing inputs for admitted records or auto-admit a fact's output.

## Reproduction and controls

The exact [vector](astra-25-future-lineage-input.vector.json) passes the closed
JSON schema, normalization and accepted-proposal fact checks. Current
`memory/spec/checks/validate.py:check_state` rejects it with
`dangling integration input ('rec:a', 1)` because its fact loop checks all inputs
against the initial record inventory, including facts for unadmitted outputs.

Two bounded state controls use the same fixture:

- Add A from operation 2 as an admitted record at sequence 1, with empty lineage:
  the checker accepts. This shows the failure is specifically the input's initial
  absence, not the fact's shape, schema, identity, or integration profile.
- Instead add B from operation 1 at sequence 1 with lineage `[A]`, leaving A
  absent: the checker rejects the actual dangling admitted input. This rejection
  must survive a correction; accepting every state would not satisfy the pair.

Both independent evaluators pass all three operations and the final exact report
on the unchanged contract expectations. Source `1f35727` and package runtime at
`1828356` were not edited. The successful retry with the same key and final cut
102 checks the observable no-partial-record/no-reserved-key result of the first
refusal; this vector does not inspect every internal runtime field.

The prior `0.2.1` probe also passed both evaluators and produced the same checker
rejection. Immutable evidence entries are `astra22-phase2-future-input-021`,
`astra23-phase2-future-input-021`, `astra22-phase2-022-migration`,
`astra23-phase2-022-migration`, and `checker-future-lineage-022` in
[the evidence JSON](astra-25-evaluator-results.json). Input and implementation
hashes identify the executed bytes. The current canonical package's own 65
vectors still structurally validate; this additional fixture is explicitly a
known checker rejection, not reported as a structural pass or runtime defect.

Judge event `$GMbY9p6_pemnZ4YJ4kSkLz6M9eJTAjloeXsRPKzFrmA` independently
confirms the exact future-fact failure and both evaluator passes. It additionally
checks unknown-lineage admitted B with missing known input A: this must remain
invalid too. Defer input existence only for facts with unadmitted outputs; keep
duplicate/direct-fact integrity and accepted same-batch reference checks. No
evaluator change or owner architecture question is required.
