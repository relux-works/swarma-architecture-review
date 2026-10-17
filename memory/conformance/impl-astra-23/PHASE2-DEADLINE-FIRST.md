# astra-23 retention-deadline first observations

Package0.2.4@ef0264702d3ff937bd34410ea80660b196b6f1b0, unchanged runtime4af0360; authored0.2.3 input bytes retained.
All five initial-state/operation
shapes validate. Exact expiry code, order and replay mapping await judge/editor;
these native probes are outside exact vector counts.

| Probe | Operation | Result | Records before/after | Cut before/after | State unchanged |
| --- | ---: | --- | ---: | ---: | --- |
| before_deadline | 0 | admitted | 1 / 2 | 100 / 101 | False |
| at_input_deadline | 0 | admitted | 1 / 2 | 100 / 101 | False |
| after_input_deadline | 0 | admitted | 1 / 2 | 100 / 101 | False |
| at_output_deadline | 0 | admitted | 1 / 2 | 100 / 101 | False |
| expired_replay | 0 | admitted | 1 / 2 | 100 / 101 | False |
| expired_replay | 1 | admitted | 2 / 2 | 101 / 101 | True |

Before-deadline storage is the positive. Fresh at/after input expiry and at the
output own expiry commit new records plus idempotency; the expired exact replay
returns its stored receipt without state mutation. The replay observation is
separate from the new-write invariant and has no invented expected verdict.
Full per-operation before/after states, inputs and module hashes accompany this
report. No physical purge or protected-deployment behavior is claimed.
