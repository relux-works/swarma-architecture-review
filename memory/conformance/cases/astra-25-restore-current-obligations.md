# ASTRA25-12: current restore obligations absent from the old backup

Status: native first observations; judge classification requested. Recommended
package implementation bug. No exact vector or expected output changed.
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
