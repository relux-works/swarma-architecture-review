# ASTRA25-08: admit and read rights do not silently grant retention

Status: phase-2 separating case; both evaluators admit the forbidden derivative.
Judge classification pending. Package `0.2.1-draft` at `f31d58f`.
Owner: astra-25.

## Clauses and minimal input

The normative companion section 6 requires independent read/use/retain/forward
checks and says read permission does not grant persistence. Kernel 7.1 requires
all derived records to inherit input constraints. Package K-AUTH-1 says an
operation grant does not bypass retention checks; K-DISC-1 says integration facts
grant no read/use/retain rights. K-API-1 requires atomic refusal with no writes.

```text
Already admitted private input A with known complete lineage.
Actor has admit, read and use rights; all retain rights are absent from all grants.
Trusted deterministic integration fact says new paraphrase D consumed A.
Input representation and review are valid, generation is current.
Operation: ordinary admit(D), storing new content derived from A.
```

This is a synthetic fixture, not an attempted real storage operation. The
pre-existing input remains a lawful admitted record; the request is for new
retention of a derivative under the actor's current authority. No owner decision
or grant waives the missing right. There is no unknown-lineage excuse: this
probe uses an exact complete input inventory.

| Observation | Admit right implicitly includes persistence | Retain remains independently required |
| --- | --- | --- |
| Result | admitted receipt | not_authorized refusal |
| New D in admitted inventory | present | absent |
| Existing A | unchanged | unchanged |
| Public output of private paraphrase | hidden | hidden |

Recommend independent retention authorization. Making D private after storing it
prevents forwarding but does not repair unauthorized persistence. A valid
integration fact establishes provenance, not retention permission. If a narrow
fixture operation intentionally combines these independent rights, that must not
silently contradict the source contract or leave a retain bit with no effect.

## Exact negative and positive controls

[`astra-25-retention-authority.vector.json`](astra-25-retention-authority.vector.json)
derives from P11 and removes only retain rights. It expects `not_authorized` and
no new admitted record. The paired
[`authorized-control`](astra-25-retention-authority-authorized-control.vector.json)
restores retain rights and expects the exact admitted derivative. Both use the
same historical query at the initial committed cut, so an invalid future cut
cannot masquerade as the intended authorization rejection. The public view stays
empty in both; the protected inventory proves whether persistence occurred.

Both vectors pass the closed schema, state references, normalization and forbidden
checks. The existing corpus remains unchanged. Package evaluator `f5fdd8b` and
source evaluator `512d006` each pass the authorized control and fail the refusal
case: they return a receipt and add D. The package report has 12 exact field
changes (receipt/refusal shape and retained record inventory), plus the explicit
forbidden receipt/retained-derivative predicates. This is not merely an arbitrary
error or a disagreement between evaluators: expected authorization follows the
independent source requirement above.

Exact actuals, code/input hashes and differences are in
[`astra-25-evaluator-results.json`](astra-25-evaluator-results.json), runs
`astra23-phase2-retain` and `astra22-phase2-retain`. No evaluator, canonical vector
or source policy was edited to obtain agreement. Physical persistence/erasure
qualification remains outside this semantic run. Judge disposition determines
whether this is a missing package operation rule, implementation defect(s), or
an unresolved source boundary.
