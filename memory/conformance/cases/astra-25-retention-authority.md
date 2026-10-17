# ASTRA25-08: admit and read rights do not silently grant retention

Status: R7-036 source and R7-037 package implementation bugs; both evaluators
admit the forbidden derivative. Original package `0.2.1-draft` at `f31d58f`;
current fixtures explicitly migrated to `0.2.3-draft` with private/read storage
context and unchanged original expectations apart from profile.
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
qualification remains outside this semantic run.

Judge event `$pnqSyjGB7fzLv1dlK42vnCpvbXn2OS6hR2BAL5a-818` classified the definite
no-retain outcome as R7-036/037, requiring atomic `not_authorized` and scoped
per-input/output authority. Both implementers separately identified a wire gap:
admission context has no retention audience/purpose, so existential versus
all-disclosure-label scope cannot be inferred. That follow-up needs an explicit
package rule before scoped-neighbor expectations; it does not invalidate this
case, whose grants contain no retain permission in any scope. Never derive the
operation scope from a later query or combine unrelated grants.

## Explicit storage scope and transitive unknown-input controls

Release `0.2.3-draft` (`23290b3`) closes the R7-039 wire gap. All owned writes
explicitly choose private/read for the authenticated actor. Existing grants
supply that scope in positive traces; no grant was added to the original
no-retain witness. Context is canonical intent and retain revocation is live.
All previous expected reports remain unchanged except profile version.

The new [transitive-unknown negative](astra-25-retention-authority-transitive-unknown.vector.json)
and [positive control](astra-25-retention-authority-transitive-unknown-control.vector.json)
combine this contract with the v0.2 incomplete-lineage lower bound:

```text
A is private. Admitted U has lineage=unknown, with trusted known input A.
New deterministic D consumes U under explicit private/read retention context.
Exact retain grant covers U and D; another private/publish retain grant covers A.
Negative: refuse not_authorized, with no D admitted.
Positive: add only A to the private/read retain grant; admit private D.
```

Retain grants use metadata=false, independently of the existing read/use grants.
The unchanged public query remains empty in both. The complete positive grants
cover the finite known closure; they do not turn unknown lineage into complete
lineage or permit publication. Canonical P11 has complete transitive inputs and
P13 has direct unknown lower bounds; this pair checks their composition through
an already-admitted unknown intermediate. It extends R7-036/037 regression scope,
not a new specification claim or independent defect count.

All nineteen owned fixtures pass the `0.2.3` closed grammar, state references,
accepted-write facts, normalization and forbidden checks. Pre-adaptation package
runtime at `08c4b9a` and source at `bd75f4f` both wrongly admit D in the new negative
while passing its positive. Package has 12 exact field differences plus both
forbidden predicates. Original no-retain failures remain too. First valid new-
release runs are `astra23-phase2-023-first` and `astra22-phase2-023-first` in the
evidence JSON; runtime correction and full-state refusal verification are pending.

## Independent atomicity and current-replay baseline

A separate six-control harness runs each owned negative directly, snapshots all
record/policy/runtime state (including cut, dirty, custody and idempotency), and
requires exact not_authorized plus no change. Positive controls require the
exact admitted inventory and a stored copy of their success receipt. After each
positive, a trusted retain-only revocation is appended; the identical request
with later intake time must now refuse without changing any state or its stored
receipt. Existing read/use rights are not revoked by this stimulus.

Before retention adaptation, each evaluator passes the two positives and fails
the four intended negatives: forbidden admission mutates record/runtime/replay
state, while revoked replay incorrectly returns the unchanged success receipt.
Thus the harness detects the actual known violations, not a setup failure or an
arbitrary exception. Immutable results and code/input hashes are in
`astra22-retention-atomic-first` and `astra23-retention-atomic-first`. The local
entry point is `.temp/check-retention-atomic.py <22|23> <output.json>`; it imports
the evaluator read-only and operates on copied synthetic fixtures. These checks
supplement exact vector outputs and do not claim physical persistence effects.
