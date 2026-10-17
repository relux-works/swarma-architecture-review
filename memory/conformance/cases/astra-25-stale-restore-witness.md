# ASTRA25-04: an outside-domain witness can still be stale

Status: source-contract regression case; package not yet landed.
Owner: astra-25. Source baseline: `4d4ef45`; kernel v0.2.

## Clauses

Companion §6 and S25; bounded-evidence design, "Retention and derived information";
incorporated erasure-closure finding. Restore stays closed until current erasure
and policy completeness are reconciled against evidence outside the restored
failure domain. An external location alone does not establish current coverage.

## Minimal separating input

```text
t0: backup K contains payload A and erasure inventory through sequence e4
t0: independent witness W, outside K's failure domain, also covers only through e4
t1: authorized erase E at e5 is acknowledged; A is fenced and purged
t2: restore K; W is authentic and reachable but remains complete only through e4
Operation: reopen disclosure of restored A
```

The sequence labels are protected fixture metadata, not public response fields.
There is no authorized recovery that waives E and no evidence that e4 is current.

## Two readings and outputs

| Observation | Outside-domain witness exists | Current obligation completeness established |
| --- | --- | --- |
| Restore gate | open | closed |
| A disclosure | allowed from K | unavailable/refused; no A payload |
| Erasure reconciliation | success because W is external | incomplete because E is uncovered |

Both readings use a real external witness; this is stronger than merely placing
the deletion ledger in the same backup. A digest/signature verifies W's old
statement and does not upgrade its coverage to t2.

## Recommendation and controls

Require complete current reconciliation, not a boolean `external_witness: true`.
Positive control: a current trustworthy W covers e5 and E is replayed/reconciled
before reopening unaffected content; A remains erased. Another positive control
uses a complete current witness showing no later obligation for a different
unaffected payload. Negative neighbors: W is missing, unreachable, has a coverage
gap, or the new policy cannot be reconciled. All keep disclosure closed.

This case prescribes an observable obligation and evidence coverage. It does not
select a distributed protocol, epoch authority or new memory registry.

## Evidence and limits

This is a proposed deployment state-machine counterexample, not an executed
restore or a claimed evaluator bug. Package-format JSON follows if the package
can encode witness coverage; a missing representation must not be silently
treated as a passing boolean simulation.
