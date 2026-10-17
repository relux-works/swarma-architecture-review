# astra-23 mixed-issuer authority first observations

Package0.2.5 at6a04e8cfb1490569cd1de7468d2085dd4840cf51; runtime23b4d74.
Both unchanged native input triples pass closed shapes. No exact output rule
is assumed for mixed-issuer ancestry; these probes are outside vector totals.

| Probe | Currentness | Selected refs | Durable state unchanged |
| --- | --- | --- | --- |
| same-issuer-control | current | [{"id":"rec:d","version":3}] | True |
| foreign-intermediate | current | [{"id":"rec:d","version":3}] | True |

Both reads preserve records, policy, runtime, captures and dirty-since. Each read
creates its ordinary ephemeral view binding; the complete engine is not claimed
byte-unchanged. Full actual outputs, before/after durable state and input/module
hashes accompany this report.

Package A07/K-REV-3 describes the canonical receipt predecessor DAG and maximal
eligible candidates without explicitly limiting the issuer of an intermediate
event. The current package-derived implementation follows that supplied DAG,
including the foreign intermediate. This documents its reading; it does not
establish that reading as the adjudicated cross-issuer contract or infer a new
invalid-state rejection. The same-issuer control remains separate and passing.

Judge subsequently classified R7-055 as ambiguity and filed the alternatives in
`memory/conformance/OWNER-QUESTIONS.md`. An attributed owner decision is pending;
this first report does not label either mixed-path reading an implementation bug.
