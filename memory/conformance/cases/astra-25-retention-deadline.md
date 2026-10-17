# ASTRA25-11: a retained deadline must constrain new storage

Status: judge-classified R7-052 source implementation, R7-053 package
implementation and R7-054 specification mapping. First native and exact vector
failures preserved. Owner: astra-25. Initial package `0.2.3-draft`; exact vectors `0.2.4-draft`.

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

## Adjudicated mapping and exact witnesses

Judge event `$JPRw0HAxhQiEJ-rN4erBtnvRBnBXixLi2Rap_jcFAN0` requires live retention
iff trusted `context.at` is strictly before every applicable non-null deadline.
At or after expiry, return exactly `not_authorized`, `retryable: false`, in the
current retention-authorization class before idempotency. Replay checks original
outputs and their transitive known inputs, preserving the old receipt and full
state on refusal. Null adds no deadline. No refusal runs a purge job. The editor
will make this mapping explicit in R7-054's next release.

Seven exact fixtures exercise that ruling:

| Fixture | Required behavior |
| --- | --- |
| [ASTRA25-11](astra-25-retention-deadline.vector.json) | Both at-deadline and later attempts refuse; no D or replay entry |
| [BEFORE](astra-25-retention-deadline-before-control.vector.json) | Matching live deadline admits D |
| [OWN](astra-25-retention-deadline-own.vector.json) | D's own expired deadline refuses the whole operation |
| [REPLAY](astra-25-retention-deadline-replay.vector.json) | First valid admission succeeds; late identical retry refuses without a new receipt |
| [UNKNOWN](astra-25-retention-deadline-transitive-unknown.vector.json) | A known ancestor's deadline survives an unknown intermediate |
| [BATCH](astra-25-retention-deadline-same-batch.vector.json) | Expired future input refuses both proposal orders with zero records |
| [BATCH-CONTROL](astra-25-retention-deadline-same-batch-control.vector.json) | Live future input admits the output-first batch atomically |

The existing ASTRA25-08 authorized control supplies the null-deadline positive.
All 27 owned fixtures pass closed structure/reference/accepted-write checks.
Both runtimes pass the two new positive vectors and fail all five new negative
vectors before correction. Independent operation-level assertions produce three
positive passes and seven intended negative failures per runtime. They compare
all records, policy, runtime/cuts/custody/dirty state, captures/bindings and replay
storage before/after each rejection; the late replay returns success without
state mutation, which still fails the exact required refusal. A wrong rejection
or crash cannot count as passing this check.

First complete runs and code/input hashes are `astra22-deadline-vectors-first`,
`astra23-deadline-vectors-first`, `astra22-deadline-atomic-first` and
`astra23-deadline-atomic-first` in `astra-25-evaluator-results.json`. Exact first
0.2.4 vector text is additionally frozen in
[`astra-25-retention-deadline-vectors-first.json`](astra-25-retention-deadline-vectors-first.json).
The original native evidence file remains byte-identical. No forbidden storage
observation or expected rejection was changed to agree with a runtime.
