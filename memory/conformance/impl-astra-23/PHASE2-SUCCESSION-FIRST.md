# astra-23 authority-succession first observations

Package0.2.3@23290b3, runtime4af0360. Closed input shapes pass for all three
independently authored probes. Typed negative refusal mapping is pending;
these are observed contract probes, not exact-output conformance vector passes.

| Probe | Actual operation | Records before/after | Cut before/after | Idempotency after |
| --- | --- | ---: | ---: | ---: |
| Ordered control | revised receipt | 5 / 7 | 100 / 102 | 1 |
| Incomparable receipt | revised receipt | 5 / 7 | 100 / 102 | 1 |
| Same receipt | revised receipt | 5 / 7 | 100 / 102 | 1 |

All three also mark the dependent dirty. The two negative cases violate the
required atomic refusal; the ordered control remains valid. No refusal code is
invented. Full input/runtime hashes, actual output and entire before/after states
are retained in the accompanying JSON. Canonical and supplemental pass counts
from4af0360 do not include these new probes. No protected deployment is exercised.
