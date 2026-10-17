# ASTRA25-12: current restore obligations absent from the old backup

Status: R7-058 package implementation bug, open. Native first preserved at
644c793; exact supplementary regressions now published after judge mapping.
Owner: astra-25.

## Contract and two readings

K-ERASE-1/2 require the full content/custody closure and prohibit complete-purge
claims for unreachable affected controlled sinks. K-ERASE-3 requires current
complete outside-domain obligations to be reconciled before restored disclosure
reopens. It explicitly says an old snapshot's own erasure list is not that
witness. Companion section 6 and bounded-evidence's protected-service section
likewise require current obligations, including later erasures missing from an
older backup, before access can resume.

The correct candidate reading merges current witnessed obligations with any
locally retained obligations, then fences and reconciles their closure. The
separating reading starts only from the old local erased inventory and uses the
incoming obligations merely to check coverage of that inventory. An empty old
inventory then makes a nonempty current witness ineffectual.

## Minimal valid input

Use the unchanged initial state and query of canonical S25: admitted A, reachable
controlled payload and backup, no recorded erasure/fence. This represents the
supplied old snapshot, not the current external deletion ledger. No local erase
operation is inserted: the current obligation is supplied by the external
witness at recovery.

1. Owner restores cut 100 with obligations=[A], external_witness=false.
2. Unwitnessed reconciliation of A refuses and preserves the restore fence.
3. Current-complete external witness supplies obligations=[A],
   external_witness=true at reconciliation.
4. Query the same admitted record.

All initial states, operations and queries pass the closed schemas; every initial
snapshot passes admitted structural/referential invariants. The witness boolean
is the existing trusted adapter fact, not a claim that a real witness was built
or verified. No arbitrary admitted record mutation is used.

## Independent native observations

Identical native inputs were run against source `87beb46` and package `23b4d74`.
Complete original inputs, operations, actuals, before/after state, snapshot hashes
and implementation hashes are frozen in
[the first evidence](astra-25-restore-current-obligations-first.json). Aggregate
entries are `astra22-restore-current-obligations-first` and
`astra23-restore-current-obligations-first`.

| Variant | Source | Package |
| --- | --- | --- |
| Current witness supplies A absent from old erasure inventory | Reconciled; A fenced/erased; both sinks absent; query empty | Reconciled; no fences/erased refs; both sinks present; query returns A |
| Same, one controlled affected sink unreachable | erasure_incomplete; unchanged state; global restore fence and unavailable content retained | Reconciled; both sinks present; global fence opens; query returns A |
| A already erased locally before restore | Both sinks re-purged; query empty | Same |
| Current complete witness has no obligations | Opens; A remains available | Same |

Both readers refuse the unwitnessed step with exact erasure_incomplete/true and
unchanged state, and both refuse queries while the restore fence is active.
The known-obligation control confirms the existing S25 path; the empty-current-
obligation control confirms that recovery is allowed when no purge is due.
The new-obligation outcomes are native observations outside vector denominators,
not newly invented expected output fixtures.

Recommend package implementation correction under existing K-ERASE-3: current
witnessed A must enter the reconciliation closure even if absent from the old
snapshot's erased/fence sets. The reachable case must account for both sinks
before reopening; the unreachable case must remain fenced with no success claim
or partial state mutation. Preserve old known-obligation, genuinely empty-
obligation, false-witness and independent unaffected-content neighbors.

No package implementation details are sent to the source implementer. This is a
synthetic semantic disclosure/resurrection witness; physical purge and real
outside-domain witness verification remain unqualified.

## R7-058 mapping and exact supplementary fixtures

Judge event `$M8NvqvBJqj0P6G_HX3wtl3-FVKIbSUxxSZFXB9YCyvE` independently
reproduces all four original traces and classifies R7-058 as package
implementation bug. Current supplied and retained obligations must enter the
full closure; newly learned obligations update protected fences/erasure/generation.
Unreachable affected custody must refuse erasure_incomplete/true atomically
with the global fence retained. No source/spec change or owner decision is needed.

Five exact fixtures now cover:

- [New witnessed obligation](astra-25-restore-current-obligations.vector.json).
- [Unreachable affected sink](astra-25-restore-current-obligations-unreachable.vector.json).
- [Previously known obligation](astra-25-restore-current-obligations-known-control.vector.json).
- [Genuinely empty current obligations](astra-25-restore-current-obligations-empty-control.vector.json).
- [Independent unaffected content](astra-25-restore-current-obligations-independent-control.vector.json).

The first four retain every initial-state and operation byte of their original
native variants, adding only an explicit capture of the already-observed fenced
query. The fifth adds a direct independent B and its controlled sink: reconciling
A must keep B readable and its sink present. All include the false-witness atomic
refusal before current-complete reconciliation. Exact expected receipts,
refusals, closure and custody follow the judge mapping and existing S25/S20;
the ordinary no-evidence A view is copied from the already-published S01 oracle,
and the B-only view applies that same direct independent-record contract. Oracle
construction does not copy either evaluator's new output.

All 34 owned fixtures pass closed structure, references, integration facts and
normalization/forbidden checks with two bounded leak plants. The initial local
handle-slot naming attempt was rejected by the structural checker and corrected
to existing @hN syntax before evaluator execution; it is not a product failure.
Source946cbd8 passes all 33 semantic fixtures. Unchanged package23b4d74 passes
30 and fails three: new obligation, unreachable sink and unaffected B neighbor;
both known/empty positive controls pass. The failures expose missing protected
closure/custody, falsely reopened content and, for the unreachable case, success
instead of the exact refusal. Earlier 28 cases remain unchanged and green.
One owned deployment fixture remains unsupported.

Exact first runs are `astra22-phase2-025-restore-obligations-control` and
`astra23-phase2-025-restore-obligations-first`. New fixture bytes at execution
are explicitly marked as working-copy inputs and hash-pinned. The native first
still preserves complete before/after snapshots, erasure/fence/generation and
unreachable atomicity beyond the vector postcondition fields. No physical purge
or outside-domain witness deployment claim is made.

## Newly learned obligations and late writers

Three separate valid restored instances extend R7-058's protected-state checks.
They use S26's admitted A and reviewed future derivative facts, the primary
current-obligation recovery sequence, then a writer at a later trusted time.
The independent proposal has its own explicit allow-review and direct lineage
fact. Each case starts separately so an incorrect first write cannot contaminate
a neighboring result. All initial-state and operation shapes/invariants pass.

| Writer after current witnessed A deletion | Required / source946cbd8 | Package23b4d74 first |
| --- | --- | --- |
| Generation0 derivative of A | stale_generation/true; full state unchanged | Admitted; state mutates with derivative |
| Generation1 derivative of A | erasure_fenced/false; full state unchanged | stale_generation/true because generation remains0 |
| Generation1 independent reviewed record | Admitted; A remains erased/fenced at generation1 | stale_generation/true |

The source passes all three exact native assertions; the package fails all
three. These are consequences of existing R7-058, not separate ledger items or
supplementary vectors. Full input/setup/write/result and before/after snapshots
are frozen in [late-writer first evidence](astra-25-restore-late-writer-first.json),
with aggregate entries `astra22-restore-late-writer-first` and
`astra23-restore-late-writer-first`. The correct independent positive confirms
that fencing does not require rejecting all post-recovery writes.

An initial local positive-control draft omitted the new independent record's
allow-review and correctly received quarantined; that scratch authoring result
is retained and is not product failure evidence. The complete frozen comparison
uses the required review in both readers. No evaluator files were changed.
