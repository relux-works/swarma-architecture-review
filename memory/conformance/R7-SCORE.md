# R7 score

Owner: astra-27 (judge). Status: provisional intake, round 3.
Baseline: `95f974b41667e25d4a3a7630055ef1c20690fb7d`.

**Current rubric score: 0/2 — the canonical package has not landed.**
This is the observed baseline, not a final judgment on the active collective.

| Requirement | Evidence at this baseline | State |
| --- | --- | --- |
| Closed package and released version | `memory/spec/` absent | Pending |
| Package validator | Not present, not run | Unverified |
| Exact executable semantic vectors | Not present | Unverified |
| Source-derived evaluator and full run | astra-22 core frozen at `4d4ef45` before package intake; 20 local controls reported, no package run | Pending |
| Package-derived evaluator and full run | No committed implementation/report yet | Pending |
| Every divergence/case classified and tracked | [LEDGER.md](LEDGER.md), eight source cases awaiting package inspection through `5a32468` | Intake open |
| Every source ambiguity filed | [OWNER-QUESTIONS.md](OWNER-QUESTIONS.md), none established yet | Intake open |

Semantic vector counts are not yet available. Deployment vector counts are not
yet available. No protected-deployment qualification is claimed. A passing
synthetic semantic model will not be counted as an OS isolation, custody,
erasure-sink, timing, or network-policy test.

The final score will name the released package version and commit, validator
result, both committed run baselines and exact pass/fail/unsupported totals,
open and resolved ledger items, and all remaining owner questions. Score 2
requires no open `spec-bug` or `impl-bug`, every semantic vector executable,
and both evaluators passing every supported semantic vector. Unsupported
scope remains explicit even when the rubric permits a score of 2.
