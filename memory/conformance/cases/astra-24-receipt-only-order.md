# ASTRA24-11: authority order traverses receipt-only intermediate events

Status: judge-classified R7-051 source implementation bug; correction pending.
Owner: astra-24. Package `0.2.3-draft`; first exact execution at `a970a95`.
No write, replacement, challenge or CAS operation is performed in either vector.

## Contract and competing readings

K-REV-3 defines currentness by transitive canonical receipt succession, not by
which authority events currently have cached assertion records. Kernel section
5.3 places current decision order in the deciding authority's own ordered record.
K-EVAL-9 keeps non-current candidates historical. K-REV-4 does not turn currentness
ambiguity into signed opposition or a write refusal.

One reading first converts every direct predecessor receipt to an assertion ID,
drops receipts with no assertion, then walks that reduced assertion graph. The
required reading walks the eligible admitted authority-receipt graph first and
only then compares the actual decision candidates. Absence of an intermediate
assertion does not delete its known canonical receipt or predecessor edges.

## Minimal read-only pair

Both inputs contain three canonical receipt sources and the exact graph
`r1 <- r2 <- r3`, all admitted, readable and resolvable for the same issuer and
caller. The decision slot has d1/r1 and d3/r3. There is no hidden or absent receipt.
No operation is executed; the query reads the existing admitted cut.

The positive control additionally contains d2/r2, as in the already verified
ordered ASTRA24-08 capture. The separating input removes only d2 and its own
lineage/review metadata; all receipt bytes, authority events and permissions
are identical. Exact expected output is derived from that established control:
d3 remains the sole current candidate and d1 remains historical. The absent d2
cannot appear in the historical list. Neither polarity gains a witness.

| Read-only input | Required selected decision | Source | Package |
| --- | --- | --- | --- |
| Every intermediate assertion present | d3, current | pass | pass |
| Receipt r2 present, assertion d2 absent | d3, current | d1 and d3, ambiguous_current | pass |

The source returns no history for the separating input. Eight exact field/shape
differences and two intended forbidden predicates capture this mismatch.
Inventories, dirty state, control observations and external effects stay unchanged.
This independently isolates the projection failure first exposed by the valid
ASTRA24-10-TRANSITIVE replacement; it does not rely on write admission behavior.

## Evidence and proposed disposition

Both vectors pass the current closed grammar, initial-state references, handle
normalization, inventory and intended wrong-result plants in structural log26.
All eighteen previous vector hashes are unchanged. At `a970a95`, the full owned
corpus is source 15 pass / 5 fail and package 17 pass / 3 fail. Three failures in
each implementation are the already classified R7-047/048 replacement refusals;
source additionally fails the two manifestations of receipt-only projection order.
Do not count those two manifestations as two independent defects.

First exact paired outputs, input hashes and every implementation module hash
are retained in
[astra-24-receipt-only-order.first.json](astra-24-receipt-only-order.first.json).
Full local reports are `.temp/astra22-owned-cases-29.json` and
`.temp/astra23-owned-cases-19.json`. The source adapter maps immediate receipt
predecessors through `receipt_to_assertion` before the core traversal, losing the
intermediate node. This code observation explains, rather than defines, the
independently specified expected result.

Recommend classification as a source implementation bug under K-REV-3, distinct
from replacement refusal mapping and the repaired current-head CAS contract.
No specification or owner architecture change is required. This pair covers
publicly eligible same-issuer receipt ancestry; it does not qualify hidden-event
non-interference or arbitrary authority graphs.

- `astra-24-receipt-only-order-control.vector.json` SHA-256: `e357454d4d7919c51bea3b383a010e5f93260dbfc4bcf25f8cbf5c3ee00beeb0`.
- `astra-24-receipt-only-order.vector.json` SHA-256: `1e2c14dd3ce47a3885565cc10793256516d751c63e5c5a6ad3c2095dae134815`.

## Round 27 profile migration to 0.2.4

Current exact fixtures explicitly name `0.2.4-draft` from release `ef02647`.
Only expected-view `semantic_profile` values changed; initial state, operations,
queries and behavioral expectations are byte-equivalent after that declared
normalization. All twenty owned fixtures pass structural and intended forbidden
controls (log27). `.temp/astra24-profile-024-migration.json` records old/new hashes
and every changed path. Historical hashes and first reports remain unchanged.

Judge decision `$lL-KfgsFVYJ8Kpol9-2KlrnISzbIcOa-A7-1Pv5Z2-k` independently
reproduces the transitive projection in a fresh read-only snapshot and assigns
R7-051 to source. ASTRA24-11 and ASTRA24-10-TRANSITIVE are the same family.
Source `4772258` fixes only replacement admission; both projection witnesses
remain failing after explicit 0.2.4 migration. Package passes both exactly.
