# Parked: macmini_swarma-review_rev4

- Date: 2026-10-12, 07:45 UTC.
- Lens: operations and migration.
- Control: ivan-curator PARK decision in #swarma-review, topic rounds, event `$EB6OzWXmhe2CPevdsra59AzLdOCV0XXzznaJEQfDJUk`.
- Reviewed findings baseline: signed `78c1bf43954944022a180ccb565936f6320f6ed5`, F-1 through F-11.
- Final marker: rev4 round 12, event `$W5-gAc_96EtnwmDOIEcCS2c4qZkB4awUSqCOhfj1tlk`; no new candidate or confirmation.

## Recorded work

- **F-2: Give standing executions a bounded operator migration path.** Signed commit `e50d2cf345dcae1be9ebfb6f1818656a0cecd67a`, pushed. Reuse dispatcher stop and confirmed process absence to bound the maintenance attempt while retaining standing allocations and identities. Topic: f-standing-cutover.
- **F-7: Separate remote effect claims from the ten-minute result cache.** Signed commit `00ed26a9e132ca45b657a6d89d986dfce1907fe4`, pushed. Persist receiver-owned claims before mutation and make expired retry identities inadmissible before discarding evidence. Topic: f-remote-replay-floor.

Independent confirmations are cited in FINDINGS.md. Later rev3/rev5 confirmations remain in the topics. I also validated the peer candidates recorded as F-3, F-4, F-5, F-6, F-8, F-9, F-10 and F-11. The final F-10/F-11 landing preserves completed helper replay and unresolved external-rotation outcomes.

## Open threads

No own candidate, addressed request, disputed refinement or append remains open. All eleven findings remain **proposed**: peer confirmation is not an operator adoption decision or runtime qualification. No specs were changed and no builds or tests were run.

## Limits of my entries

- **F-2:** A bounded attempt can defer maintenance; it cannot guarantee that an unknown stop becomes confirmed absence. Stop/restart authority, persisted progress and supported recovery rows still need publication. v0 cannot promise seamless native-context continuity. F-5 avoids the first command-to-daemon conversion, but later binary/schema maintenance still needs these safeguards. The deadline belongs to maintenance, never to the standing execution.
- **F-7:** Durable claims alone do not bound retention. The authenticated new/retry rule and durable admission floor or freshness window still need publication and qualification, including loss or rollback of claim evidence. Unknown completion remains unknown; no automatic replay or exactly-once completion is promised. This is a draft protocol gap, not a demonstrated runtime defect.

## On an operator-authorized resume

1. Check operator dispositions and changes since the reviewed baseline before reopening any candidate.
2. Map adopted operational changes to implementation gates: one service transport, launch descriptor/staging rules, receiver observations, current revocation verdict and fenced restore before the relevant protected-launch/recovery paths. Keep standing maintenance, recursive delegation, SH2 admission, Codex refresh and remote replay qualification tied to their own activation gates.
3. Examine maintenance/recovery row coverage and interrupted stop, restart and rollback qualification. Reuse existing services and receipts; unsupported or unknown rows stay closed.
4. Revisit ledger retention/scaling only with workload evidence. The earlier review found no high-confidence performance finding. Network-profile/firewall qualification was not independently completed by rev4 and remains a possible later review surface.

No new analysis was started after PARK.
