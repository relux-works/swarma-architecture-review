# ASTRA25-11: a retained deadline must constrain new storage

Status: judge-classified R7-052 source implementation, R7-053 package
implementation and R7-054 specification mapping. First native and exact vector
failures preserved. Owner: astra-25. Initial package `0.2.3-draft`; first exact vectors `0.2.4-draft`, explicitly migrated to `0.2.5-draft`.

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

## R7-054 release verification

Released `0.2.5-draft` at `6a04e8c` explicitly matches the judge's boundary, code,
ordering, output/known-input closure and current replay mapping, with no purge
side effect. Independent comparison confirms only P11 changes beyond profile
stamps across all 65 canonical vectors. Its first 16 operations and expected
results are unchanged, as are the other 64 vectors and decision pilot bytes.
All 94 JSON artifacts, 52 clauses and 34 intended structural controls validate.
The added expiry-replay plant detects a forbidden successful receipt.

All 27 owned fixtures migrated by semantic_profile only, checked field-for-field.
Fresh pre-correction 0.2.5 runs preserve the five exact owned expiry failures each,
with both new positive vectors passing. Canonical source is 49 pass / 1 fail /
7 unsupported; package is 56 pass / 1 fail. Both failures are P11, beginning at
operation18, after the original prefix and before-expiry positives. The separate
atomic harness remains 3 positive pass / 7 intended negative fail each.
These results verify the amended specification and its separating witnesses,
not runtime correction. Evidence keys end in `025-deadline-first`,
`deadline-atomic-025-first`, `canonical-025-first` and `astra25-release-025-audit`.
R7-054 closure is recommended to the judge; R7-052/053 remain implementation work.

## Source correction verification

Source `4a14a56` passes all seven unchanged expiry vectors under0.2.5. The ten
independent operation-level checks now all pass: exact denial, no partial records,
no cuts/dirty/custody/replay mutations, preserved original receipt, and valid
before-deadline/output-first-batch successes. The whole owned source semantic
corpus is18 pass /0 fail /8 unsupported. Fresh canonical is50 pass /0 fail /
7 unsupported; all deployment boundaries remain unsupported.

All six source native deadline groups also pass. They exercise admit, admit_raw,
revise and declassify, including each proposed output, complete and incomplete
known ancestry, both batch orders, live/expired replay, null/unrelated expired
records and authorization precedence over duplicate-reference rejection. The
per-proposal deadline gate executes before traversal deduplication and idempotency;
the tested late retries preserve the prior receipt. These are concrete fixture
and state checks, not a physical-purge claim. Evidence runs are
`astra22-phase2-025-deadline-corrected`, `astra22-deadline-atomic-corrected`,
`astra22-canonical-025-deadline-corrected` and
`astra22-native-deadline-025-corrected`.

Judge event `$SbEXLoMfdvIL1PJIOlfGVne-nAiumUitpRJTZRnx5Z4` closes R7-054 at
`6a04e8c`. This seat recommends R7-052 closure at `4a14a56` on the verified
coverage above. Package R7-053 correction remains a separate verification unit.

## Package correction verification

Package runtime `23b4d74` independently passes all seven unchanged expiry vectors,
all 26 owned semantic vectors and all 57 canonical semantic vectors under0.2.5.
The independent ten-control state harness and all31 package product/checker tests
pass. Native deadline tests cover all four intake APIs, before/at/after expiry,
live and expired exact replay, original receipt and full-state preservation,
known/unknown inputs, batch ordering, conflict precedence and unlimited same-key
recovery. The shared traversal checks each deadline before deduplication and
idempotency, then separately checks the original stored outputs on replay.

Exact corrected evidence is `astra23-phase2-025-deadline-corrected`,
`astra23-deadline-atomic-corrected`, `astra23-canonical-025-deadline-corrected`
and `astra23-native-deadline-025-corrected`. Earlier native and exact-vector
failures are unchanged. Judge event `$HZk3768zLdVELKOLbBdEC07KP_j0-uY6h775onLttZc`
closes source R7-052 at `4a14a56`. This seat recommends package R7-053 closure
at `23b4d74`. All deployment fixtures remain unsupported.
