# rev3 parked state — 2026-10-12

Identity: `macmini_swarma-review_rev3`. Lens: reliability, crash/recovery, reconciliation, effect identity, fences and durability ordering.

Parked on ivan-curator's `decision` `$EB6OzWXmhe2CPevdsra59AzLdOCV0XXzznaJEQfDJUk` in `#swarma-review`, topic `rounds`. No new analysis after that decision. The last completed round was 4; rounds 2–4 produced no new own candidate or confirmation.

## Recorded work

[FINDINGS.md](../FINDINGS.md) contains eleven independently confirmed proposals. My F-10 and F-11 were committed together in signed `78c1bf43954944022a180ccb565936f6320f6ed5` and pushed to main. Peers audited the landing and confirmed that the agreed refinements survived.

- **F-10, receiver-owned observations:** expose authoritative pending/recovered effect evidence at the existing helper and broker boundaries. Completed helper mutation replay already handles a recorded result plus current target state; the remaining gap concerns pending, rolled-back, not-recorded and removal/absence observations. Observation must never perform a fresh mutation after caller authority expires. Partial lists, refusals and timeouts remain unknown. Confirmed by rev2, rev4 and rev5; evidence/event IDs are in the entry and `f-effect-observation`.
- **F-11, refresh ownership across broker replacement:** require at most one live vendor refresh writer through daemon crashes, qualified containment/attempt evidence and durable-store reload. Confirmed process absence does not resolve an ambiguous external token rotation or permit blind retry. Unknown writer/store/outcome evidence keeps the account unavailable or requires re-enrolment. Confirmed by rev1, rev2, rev4 and rev5; evidence/event IDs are in the entry and `f-refresh-child-ownership`.

Independent responses also supported the existing archive boundary, standing maintenance, requester delegation, single privileged launch authority, trusted descriptor/staging lifecycle, remote replay floor, current revocation view and local revocation-restore findings. No duplicate entries were appended.

## Open threads

No unanswered candidate addressed to rev3 and no unresolved own peer-validation/refinement thread remain. All findings remain **proposed**; owner acceptance, joint schema publication and implementation qualification are outstanding. Source repositories and board state were left untouched; no builds, tests or vendor experiments were run.

The book was read end to end before module specifications. Current owner decisions/module contracts take precedence over the older VISION explanations. Explicitly open lease cleanup and SH2+ activation schemas were not promoted into duplicate findings.

## Weak spots and limits of my entries

F-10 establishes a missing published observation contract, not a demonstrated runtime failure. An implementation may already make replay observational; its pending/rollback/no-intent and retention semantics still need publication. Complete authoritative absence must be distinguished from missing or expired evidence. The final entry deliberately corrects the original candidate's overbroad completed-create/lost-reply trace.

F-11 establishes a crash/qualification gate, not evidence that a particular vendor or service-manager release leaves a writer alive. Correct existing containment could satisfy it. A durable attempt record proves intent only; neither that record nor child absence proves the vendor rotation's external outcome. Avoid adding a guardian service, generic adoption subsystem or second token-exchange implementation merely to publish this invariant.

## Resume directions

1. Review owner dispositions and any new canonical revisions before reopening analysis. For F-10, examine the chosen authenticated read/observational-replay schema, journal serialization, current target state, unbind tombstones and evidence retention, including authority expiry and interrupted creation.
2. For F-11, examine the selected macOS/Linux containment and restart sequence, persisted attempt/process identity and resolution of rotation-before-store/result crash windows. Qualification evidence must cover daemon replacement and unknown outcomes, beyond normal contention tests.
3. Check the interaction of local observation with F-7 remote claim/freshness rules and F-8/F-9 current revocation/closed restore state without introducing another mutable authority.
4. If the operator expands the next cycle, review egress/proxy/firewall recovery in depth. The network-profiles validator identified that as a remaining coverage area; this cycle produced no independent finding there.

Resume only on the operator's instruction; retain the original candidate topics and require fresh evidence before any further append.
