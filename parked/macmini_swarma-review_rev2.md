# Parked review: macmini_swarma-review_rev2

Parked on 2026-10-12 at the convener's convergence decision, room `#swarma-review`, topic `rounds`, event `$EB6OzWXmhe2CPevdsra59AzLdOCV0XXzznaJEQfDJUk`. Last own marker: round 11, zero new candidates or confirmations. Findings baseline audited: signed main `78c1bf4`, F-1 through F-11.

Lens: simplicity, component count, privileged surfaces, duplicated state and recovery responsibility. Read all sixteen book chapters and the four core module specifications; checked relevant launcher, Curator, spm and trust contracts against the current source hierarchy. This was a documentation review; proposals await owner decisions, contract publication and qualification.

## Completed findings and their limits

| Own finding | Signed landing | Remaining choice or weak spot |
| --- | --- | --- |
| F-1: deterministic retirement and narrow export | `21f9ca9` | Explicitly challenges the unnumbered 2026-10-10 default home-archive decision (`wiki/decisions.md:585`). Existing exclusion of unknown material can fail closed; the simplification trades automatic home recovery for a smaller root boundary. The operator must choose retention. Closed metadata still needs exact field/provenance and confidentiality rules; code, logs and worker text cannot inherit its assurance. |
| F-4: dispatcher as sole privileged starter | `e947677` | The durable host permit spanning physical start remains essential and unpublished. Removing tickets/host sudo does not remove the joint admission protocol. Fence withdrawal, epoch changes, ambiguous receipts and host failure need a qualified interlock before I4 activation. Dispatcher availability and future offline-start requirements may affect the tradeoff. |
| F-5: daemon transport from slice 0 | `7010e82` | Service installation/readiness moves earlier; operational cost is unmeasured. Initial capacity refusal and later queueing remain separate. It removes one transport conversion, while later binary/schema maintenance still needs F-2 operator stop/absence safeguards. Deployed-client acceptance and all phase references must change together. |
| F-8: broker-owned current revocation evidence | `0515236` | The bounded verdict/read interface is not selected or frozen. Broker availability becomes an early-admission dependency. Evidence is exact-context and point-in-time, not a future-start permit; final bind/lease/renew checks remain independent. F-9 separately establishes trustworthy history after restore. |

Independent confirmations and refinements are cited in [FINDINGS.md](../FINDINGS.md) and retained in topics `f-archive-boundary`, `f-single-launch-authority`, `f-daemon-first` and `f-local-revocation-view`. Late rev3/rev5 confirmations reinforce the landed entries without requiring duplicate findings.

Confirmed peer work: standing maintenance (F-2), requester-signed delegation (F-3), launcher descriptor lifetime (F-6), remote replay floors (F-7), local revocation restoration (F-9), receiver-owned effect observations (F-10), and vendor-refresh child ownership (F-11). Final F-10/F-11 entries preserve completed helper replay and unknown external rotation even after writer absence.

## Open threads and resume directions

No unresolved own candidate, unfinished append or unanswered addressed candidate remains. All eleven findings remain `proposed`; peer confirmation is not operator adoption.

On an operator-authorized resume:

1. Re-read cycle control and the updated canonical specs. Build the smallest initial protected-launch contract around F-5/F-6/F-8/F-10; keep recursive orchestrator authority deferred until F-3 bootstrap is published. Align deployed clients and qualification prerequisites across module owners.
2. Validate the F-4 durable permit with explicit crash/cancel/fence cuts. Distinguish that permit, held through physical start, from F-8's point-in-time revocation evidence; avoid adding another privileged starter or treating a read verdict as launch authority.
3. Resolve the F-1 retention decision and publish exact export provenance. Account retirement, caller-key cleanup and standing identity preservation must keep their distinct owners and D-IDENTITY semantics.
4. Qualify the selected descriptor/staging, daemon recovery and service-containment mechanisms on the supported OS/provider tuples. Measure global root-lock and startup costs before proposing finer locks, additional services or pools. These are evidence needs, not further confirmed defects.

Explicitly open publication work (keeper adapters, standing/team wire, goal-free receipts, lease cleanup by channel and provider support) was not converted into extra findings without a concrete counterexample. Resume from the recorded evidence and peer topics; do not infer runtime qualification from this review.
