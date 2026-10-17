# astra-23 erase receipt-context first observations

Package0.2.5 at6a04e8cfb1490569cd1de7468d2085dd4840cf51; runtime23b4d74.
Unchanged ASTRA22-09 initial state and operations are taken only from the
published native artifact0529814. No source evaluator code was consulted.
All input and output shapes validate. No exact oracle is added pending judge
disposition; these observations are outside vector denominators.

| Probe | Actual outcome | Entire engine unchanged |
| --- | --- | --- |
| original metadata-authorized erase | purged, refs=[{"id":"rec:a","version":1},{"id":"rec:summary","version":1}] | False |
| same key with ungranted changed receipt purpose | idempotency_conflict, retryable=false | True |
| unchanged intent at later intake after refused context change | purged, refs=[{"id":"rec:a","version":1},{"id":"rec:summary","version":1}] | True |
| fresh key with ungranted receipt purpose from original initial state | purged, refs=[] | False |

The changed-intent attempt returns idempotency_conflict/false and preserves
the full durable state, captures, view bindings, dirty-since and original
stored receipt. A later exact retry returns that receipt unchanged. Fresh
ungranted receipt context permits erasure with empty refs while preserving
the full protected closure, fence and both controlled custody dispositions.

This is the existing package reading of K-API-1/K-ERASE-2: current erase
operation authority precedes intent comparison; stored-ref metadata gates
the exact replay branch. Different receipt context is canonical changed
intent. No runtime or canonical vector changed for this observation.
The accompanying JSON preserves exact full outputs, all before/after state,
original input subset and source/input/module hashes.
