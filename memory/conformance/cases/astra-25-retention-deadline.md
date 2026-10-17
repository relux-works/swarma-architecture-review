# ASTRA25-11: a retained deadline must constrain new storage

Status: first native observations preserved; judge/editor classification and
exact refusal mapping requested. Owner: astra-25. Package `0.2.3-draft`.

## Contract and two readings

The design’s "Context seam" section separates read, task-use, retain and forward and says
summarization cannot extend a retention deadline. K-DISC-1 says retention ends
at the earliest non-null deadline. K-AUTH-1 explicitly keeps existing deadlines
and erasure fences despite independent storage-context authorization; K-API-1
makes replay subject to current retention authority.

One reading checks grants, copies the expired inherited label and admits the
new bytes, filtering later disclosure. The other requires a currently live
retention interval before writing any output, even with all exact grants, and
rejects the entire write at or after its earliest deadline. Recommend the second:
retaining new bytes after retention ends cannot be made valid by hiding them.
This concerns the semantic commit gate; it does not assume a scheduled purge job.

## Minimal inputs and observations

Start from the published authorized ASTRA25-08 control: admitted private input A,
trusted complete deterministic lineage A -> proposed D, all operation and exact
private/read retention grants, no erasure fence. Set `A.retain_until` to
`2026-10-17T00:00:01Z`. All original data and grants are synthetic.

| Probe | Intake time | Source | Package |
| --- | --- | --- | --- |
| Before deadline, positive | `00:00:00Z` | Admits D | Same |
| At input deadline | `00:00:01Z` | Admits D, advances state and replay store | Same |
| After input deadline | `00:00:02Z` | Admits D, advances state and replay store | Same |
| A unlimited; D own deadline reached | `00:00:01Z` | Admits already-expired D | Same |
| Valid first write then identical retry after expiry | `00:00:00Z` then `00:00:02Z` | Returns original successful receipt, state unchanged | Same |

The source runtime is unchanged `36983de` (implementation tree `e1ba8db`);
package runtime is `4af0360` (implementation tree `ea2d21f`). Every initial state
and operation passes closed schema and initial reference checks. Full inputs,
actual replies, stored output records, before/after storage snapshots and module
hashes are frozen in
[`astra-25-retention-deadline-first.json`](astra-25-retention-deadline-first.json).
Source materializes the inherited deadline on D; package preserves the proposed
label and applies the inherited deadline through disclosure evaluation. That
representation difference is not itself this finding.
Native map/tuple/set/bytes state has explicitly tagged lossless JSON encoding;
state comparisons occur before encoding. These probes are outside vector totals.

## Requested mapping and limits

The forbidden fresh-write observation is concrete: D and a replay receipt are
committed after its own or inherited retention deadline. The positive rules out
an implementation that rejects every admission. The replay neighbor has no new
write; its acceptance needs separate adjudication under current-authorized replay.

Please classify the storage behavior and specify the exact refusal code,
retryable flag and validation-order class for expiry, including at the boundary
and on replay. The current table has no explicit retention-expiry row; do not
invent a typed oracle or accept whichever rejection an implementation emits.
Once mapped, add exact vectors and full unchanged-state assertions. This is
separate from missing grants in R7-036/037; both corrected grant checks are present.
No physical deletion, remote custody or protected-deployment qualification follows.
