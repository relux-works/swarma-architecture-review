# astra-23 current restore obligations first observations

Package0.2.5 at6a04e8cfb1490569cd1de7468d2085dd4840cf51; unchanged runtime23b4d74.
The original four ASTRA25-12 input traces are taken from644c793. Every closed
initial-state/operation/query shape and actual output validates. No source
evaluator code was consulted and no runtime or fixture was changed.

| Variant | Last reconciliation | Final query | Present custody | Restore gate |
| --- | --- | --- | --- | --- |
| new_current_obligation | reconciled | [{"id":"rec:a","version":1}] | ["custody:backup","custody:payload"] | open |
| new_obligation_unreachable_sink | reconciled | [{"id":"rec:a","version":1}] | ["custody:backup","custody:payload"] | open |
| known_obligation_control | reconciled | [] | [] | open |
| empty_obligation_control | reconciled | [{"id":"rec:a","version":1}] | ["custody:backup","custody:payload"] | open |

The current external obligation absent from the old local inventory is ignored:
both reachable and unreachable variants reopen disclosure with A readable and
both controlled sinks present. Known-local and genuinely empty obligations
retain their existing outcomes. Every false-witness attempt refuses
erasure_incomplete/true without changing the entire engine, and queries during
the global restore fence refuse erasure_fenced.

K-ERASE-3 requires current outside-domain obligations to be reconciled, and
K-ERASE-2 does not permit a complete claim with affected unreachable custody.
These first observations are preserved before judge disposition and any fix;
they are not included as new exact vector passes or physical purge evidence.
The JSON contains unchanged inputs, full actuals, module/input hashes and
lossless hash-addressed engine snapshots, including ordinary read bindings.
