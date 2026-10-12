# Findings

Append-only. One entry per validated finding. Format: see `MISSION.md`, "The findings file".

<!-- entries below -->

## F-1 — Replace arbitrary-home secret classification with a narrow export boundary

- **Lens:** simplicity; privileged attack surface; confidentiality.
- **Problem:** Retirement requires root to classify arbitrary agent-owned content, names and link metadata as non-secret, including every copy of credential material. The broker explicitly permits a compromised agent to read and copy its delivered token. An agent can encode that token in ordinary source, filenames or links; path declarations and token scanners cannot establish semantic absence. Without a provable export boundary, deleting every unknown object is safe but reduces arbitrary-home archival to deletion. An unpublished general classifier adds substantial privileged complexity without establishing the promised property.
- **Evidence:** Paths below are relative to `~/Developer/ReluxWorks/`. `platform/curator-host-helper/spec/helper.md` v0.5 §4.4.1, lines 193–197, requires mandatory exclusions, pre-walk key destruction and positive classification of content/names/links; §14 question 6, line 365, leaves classification unpublished. `platform/curator-credential-broker/spec/broker.md` v0.5 §12.1, line 510, explicitly permits reading and copying the lease within the agent account; §12.2, line 524, says the binding check is not a boundary against that compromised agent. Book chapter 3, `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, describes the same archive obligation. `wiki/decisions.md`, line 585, records the home-archive policy; line 603 records the approved secret-exclusion wave.
- **Proposed change:** Make ordinary retirement a deterministic quiesce, declared-key cleanup and home-deletion path. Preserve journaled recovery, verified process absence, descriptor-relative operations and failure/unknown handling. Define any positive secret-free retirement export narrowly: service-generated, closed-schema metadata without arbitrary agent-controlled strings, names, links or bodies. Code and results remain subject to their separate git/acceptance policy; git does not prove that their content is secret-free. If arbitrary home recovery is required, specify explicit operator-controlled retention with an honest confidentiality scope, separate from a claim that the archive contains no secret material. **Challenges the owner decision of 2026-10-10 to archive retired homes by default** (`wiki/decisions.md:585`; no D-number is assigned). Does not challenge D-IDENTITY or account-retirement fencing.
- **Expected benefit:** Removes a general semantic scanner/parser from the root trusted computing base, reduces retirement states and recovery work, and replaces an unimplementable universal assurance with a small, mechanically checkable boundary.
- **Risks and costs:** Less automatic recovery of arbitrary home contents. The operator must choose the recovery/retention policy. Existing code, results and free-text logs still need their own confidentiality policy and must not inherit the restricted metadata export's assurance. Metadata fields require explicit provenance and schema checks.
- **Affected specs:** user-manager §4.4.1, §12 and §14; broker §12.1–12.2 as the threat-model basis; dispatcher retirement policy §5.4; book chapter 3 and the owner decision log.
- **Confirmed-by:** `macmini_swarma-review_rev1`, Matrix room `#swarma-review`, topic `f-archive-boundary`, event `$ZS-2olsaKDyKYmBDJrPlnA01c9gTOD7Zgg2-qBi_asc` (2026-10-12). Independent confirmation covers the classification counterexample and narrow-export/deterministic-retirement direction.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-2 — Give standing executions a bounded operator migration path

- **Lens:** operations and migration; reliability.
- **Problem:** The first dispatcher v0-to-v1 activation requires existing supervisors to finish and explicitly refuses live adoption. Standing executions now have no runtime deadline, so a healthy standing execution can keep that maintenance transaction waiting indefinitely. Operator stop is allowed in the lifecycle, but the published public `cancel` operation is execution-owner scoped; the activation contract does not publish the operator maintenance stop or its recovery path. Queue drain does not stop running executions.
- **Evidence:** Paths below are relative to `~/Developer/ReluxWorks/`. `platform/curator-dispatcher/spec/dispatcher.md` v0.5 §11, line 368, requires draining v0 supervisors before mode activation, with no live adoption. §3.5, line 118; §5.3, lines 233–239; and §7.2, line 299, give standing executions no runtime limit while preserving explicit/operator stop. §8.1, line 312, restricts public `cancel` to the execution owner; §9, line 351, scopes `drain` to queued requests. §5.4, line 251, preserves standing allocations and forbids automatic retirement or re-creation. `platform/curator-host-helper/spec/helper.md` v0.5 §4.7, lines 225–227, defines generation/execution-bound stop with verified process absence. §4.4, line 175, separates account retirement from identity revocation. Book chapters 7 and 9 describe operator cutover and the dispatcher; `wiki/decisions.md:604` records the 2026-10-12 standing-runtime decision.
- **Proposed change:** Extend the existing operator activation transaction with an explicit, bounded maintenance attempt: close new admission and inventory existing executions; obtain explicit operator authority to stop the selected executions through the dispatcher and `exec.stop`; retain standing allocations and identities; require confirmed process absence and reconciliation before changing mode, migrating mutable state or swapping binaries. A maintenance deadline bounds the attempt, never the standing execution's lifetime. Unknown/refused stop or incomplete reconciliation defers the cutover without permitting a mode/binary change. Persist any intended restart for the operator's review, but start only with fresh authority and an admitted plan/transport; unsupported rows remain visibly stopped. Publish the operator authorization and stop/restart ordering using the existing effect/receipt path. Do not add live supervisor adoption or automatic expiry.
- **Expected benefit:** Makes a finite maintenance window possible for a node with standing executions, with explicit success or deferral. Reuses existing stop and absence evidence while preserving the operator's lifetime decision and avoiding a second recovery/adoption mechanism.
- **Risks and costs:** Maintenance interrupts selected executions; v0 has no admitted native-resume path, so seamless context continuity cannot be promised. Stop/restart authority and persisted maintenance progress require a small published contract. Unknown absence may still defer maintenance. Rollback must retain later records and prove reader/writer compatibility; restoring an old snapshot is not a repair.
- **Affected specs:** dispatcher §8.1, §11 and activation qualification; user-manager §4.7 as the reused stop contract; session-host §3.5 where a qualified later backend participates; dispatcher activation diagrams; book chapters 7 and 9.
- **Confirmed-by:** `macmini_swarma-review_rev1`, room `#swarma-review`, topic `f-standing-cutover`, event `$EwfCbtwVIR8XtR4Ewvo3aAtdbqCQ2GkC8ixDahK_9TQ`; and `macmini_swarma-review_rev2`, same topic, event `$AJwUjvzcy-JClVsp-evbjCeC14S_eG_9coRRruHqlDI` (2026-10-12). Both independently confirm the unbounded drain and the bounded operator stop/confirmed-absence direction.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-3: Requester-signed orchestrator delegation preserves ancestor revocation

- **Lens:** Trust and threat model; simplicity and contract consistency.
- **Problem:** Dispatcher §5.2 says the dispatcher D issues a caller grant for a newly registered orchestrator O, narrowed from requester C's grant. When C and D have different keys, attaching D's signature to C's leaf violates the verifier's mandatory issuer/parent-subject rule. D's specified chain allows only `credential.lease`, whereas an orchestrator caller needs both `agent.spawn` and `credential.lease`; re-parenting under D therefore also fails with the current action set. Even if an operator separately widened D's grant, a structurally valid D-to-O chain would remove C's authorization. A worker W subsequently created by O retains only D's lease chain and O's immediate caller chain; neither necessarily contains C. Revoking C then has no specified transitive denial path for W. This is a contract gap, not evidence of an implemented exploit. Denying O new provider tokens does not revoke an already delivered token or establish execution absence.
- **Evidence:** Paths below are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher/spec/dispatcher.md` @ `5d0476d`: §3.3, lines 91–94 (generation-bound caller keys, signed mutating requests); §3.4, lines 99–103 (independent dispatcher chain and caller dependency); §5.2, line 225 (dispatcher-issued orchestrator caller grant); §7.1, lines 282–295 (no general ancestor-dependency closure); §8.1, line 320 (`register_key` lists only `public_key`, leaving its pre-key authentication exception unspecified).
  - `platform/curator-credential-broker/spec/broker.md` @ `b04b0a5`: §6.2, lines 273–278 (every delegation edge, strictly decreasing depth, four-envelope bound and revocation); §7.1–7.2, lines 335–347 (one caller chain, verified separately from the lease chain); §8.2, lines 382–383 (the two retained chains checked at issuance); §12.1, line 510 (delivered-token limitation).
  - `swarma-review/context/swarm-platform-architecture/vision/contracts/trust-and-isolation.md` @ `d31781d`: §3, line 26 (requester delegates only its own attenuated rights), §6, line 65 (issuer/subject continuity).
  - `curator/curator-spec/cips/CIP-0011-credential-broker-and-agent-users.md`, line 98 (caller authorization dependency); book `wiki/book/swarma/ru/04-klyuchi.md`, lines 11–20, and `05-granty.md`, lines 59–61, 110–117 (key classes, narrowing and caller revocation).
- **Proposed change:** Have C sign O's caller delegation after generation-bound registration of O's public key; the dispatcher verifies and records it. Keep registration separate from activation of caller authority. Publish the narrow pre-key registration/proof-of-possession exception, its permitted principal and replay/rotation rules; until a valid delegation is installed, O has no spawn authority. Preflight remaining depth and the chain-length bound, and recheck the requester, signature, window and revocation when activating. Each descendant then carries C in its ordinary caller chain, so the existing verifier enforces ancestor revocation without a separate authorization graph. Refuse recursively provisioned orchestrator capability until this bootstrap is published and qualified; direct worker launches and operator-enrolled orchestrators can form the initial slice.
- **Expected benefit:** A constructible delegation path, transitive revocation using existing signed chains, and fewer special authorization states or verifiers. Negative vectors should cover C != D, wrong issuer, insufficient depth, pre-key registration replay and revocation of C before and after O creates W.
- **Risks and costs:** Requires an explicit bootstrap transaction and a signature from C, which may be unavailable; keep such allocations pending rather than granting authority implicitly. The existing chain/depth bound limits recursion. Already delivered provider tokens retain their documented lifetime. This does not challenge D-IDENTITY, D-EXECUTOR or standing-session lifetime decisions.
- **Affected specs:** Dispatcher §§3.3–3.4, 5.2, 8.1 and qualification; broker §§6–8 and negative vectors; CIP-0011; trust-contract and book explanations.
- **Confirmed-by:** `ivan-network-profiles`, answer `$Fba69kF8czFSOMeMm1Y7F8CVgd00x-t3Rx6txMbcY8k`; `macmini_swarma-review_rev4`, ack `$8ew6MenEBOZ6yQ6ocGGXv1s-Xqzf30ghhPX19VqAXio`; `macmini_swarma-review_rev2`, ack `$xoUue7_0grHCIkSpLe8G5IHwJcc8kyM4kcrjQb6aGZs`; `macmini_swarma-review_rev3`, answer `$2Bbi5NN0LJAPDOQtwmu6zpjhXyuPqndS6KHkAUsestM`, all in `#swarma-review`, topic `f-orchestrator-delegation` on 2026-10-12. Proposal `$qsl2CIceAWuqJC1DXiGRBBx7YpXsxuAswulM9QXcyvc`; refined direction `$OD3366JTzirmv-E-Z_TI0pop0PgxAjReH3XFtKozjlQ`.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-4 — Keep privileged starts behind the dispatcher and remove delegated launch tickets

- **Lens:** simplicity; privileged authority; launch reliability.
- **Problem:** SH2+ adds signed launch tickets, host-to-root sudo authority, a helper host role, used-ticket state and a separate cancel/redemption interlock. The dispatcher already owns admission, claims, physical launch, cancel and cleanup. Delegating the physical call adds another privileged caller without removing the dependency on current admission. No cited owner decision requires offline host starts; I4 remains unpublished.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`. Dispatcher `platform/curator-dispatcher/spec/dispatcher.md` v0.5: §5.3, lines 234–245 (claim/launch/cancel); §12, lines 374–379 (ticket/host-role path); §16, line 423 (I4 publication). User manager `platform/curator-host-helper/spec/helper.md` v0.5: §7, lines 287–296 (owning dispatcher and root start receipt); lines 273, 362 (gated host role and redemption). Session host `platform/curator-session-host/spec/session-host.md` r7: §3.3, lines 166–176 (ticket and live claim); §3.4, lines 187–190 (common admission authority, fences and durability). Book chapters 7 and 9 describe these paths. `wiki/decisions.md:590` records D-EXECUTOR, which is preserved.
- **Proposed change:** Keep the dispatcher as the only service permitted to invoke `swarma-user-launcher` for agent execution starts. The host prepares durable session intent and a closed delivery fence, then requests an admitted start through an authenticated dispatcher API. Publish a durable host admission permit spanning physical start, bound to logical session, execution, controller epoch and operation; fence changes withdraw or reconcile the permit. The dispatcher starts the approved agent-side runner through its existing claim/effect/root-receipt path. The runner opens a fresh authenticated host channel; current-epoch registration and readiness precede delivery. Before start a cancelled claim prevents the call; after an ambiguous call resolve the same effect/receipt and stop if required, never launch twice. Host failure retains the claim and closed fence until reconciliation. Remove delegated tickets, host sudo authority, the helper host role and redemption state. Preserve host re-adoption of live runners, agent-side PTY/app-server and credential-client custody, distinct account/launch/controller identities, and dispatcher-owned stop with confirmed absence. **Replaces the unpublished I4 mechanism**; does not remove the joint admission handshake or alter named owner decisions.
- **Expected benefit:** One privileged launch authority and claim/cancel path; fewer signature formats, roles, journals and recovery cases; less root policy.
- **Risks and costs:** The dispatcher must be available for new starts, as admission/stop already require. The durable host permit, authentication, crash ordering and receipts still need joint publication and qualification; a best-effort cancel is insufficient. Host compromise must not bypass dispatcher policy or authorize another caller generation. Controller-only re-adoption preserves the execution ID; actual replacement uses a new one.
- **Affected specs:** dispatcher §5.3/§12; user-manager §7/I4; session-host §3.2–3.4/I4; launcher §10 references; book chapters 7/9 and diagrams.
- **Confirmed-by:** `macmini_swarma-review_rev3`, answer `$USGyhrdJyV3j1dZrZRtqQlNiEWWGsf7h2im9w84TWD4`; `macmini_swarma-review_rev4`, answer `$fMj1h0_0iEICHOXA57GsGYbpG_3Bw6yov-NrxiOpBGQ`; `macmini_swarma-review_rev1`, answer `$ve260nOw6hgZBeas-FnMUX-jhTNmpJKxSs39La3_esA`, all in `#swarma-review`, topic `f-single-launch-authority`, 2026-10-12. Accepted durable-permit refinement: `$25OpJE2NA2kRTEh3ZkTR9QEtqWD0RE6RM4bHK7dt0Q0`.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-5 — Start the dispatcher with one service transport and defer queueing independently

- **Lens:** simplicity; operations/migration; authentication surface.
- **Problem:** The protected-launch slice first implements a command-mode dispatcher with caller sudo rules, SUDO_UID authentication, detached supervisor bootstrap and an external sweep timer, then converts it to a daemon/socket. Two installation/authentication paths and a special drain/state/mode transition are required, although slice 0 already installs the credential broker as a peer-authenticated Unix-socket service. Queueing and advanced integrations do not require a different transport. Standing executions make the conversion drain unbounded without an explicit maintenance branch (F-2).
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`. `platform/curator-dispatcher/spec/dispatcher.md` v0.5: §2, lines 68–75 (modes); §3.2, lines 85–87 (sudo/socket authentication); §7.2, line 299 (external sweep); §8.3, line 332 (transport selection); §11, lines 367–368 (installation and conversion). `platform/curator-credential-broker/spec/broker.md` v0.5: §4.1, lines 104–116 (connection protections), §13, lines 539–554 (transport), §15, line 592 and §16, line 601 (slice-0 service installation). `curator/curator-spec/cips/CIP-0011-credential-broker-and-agent-users.md`, lines 17, 34, 97 and 122, couples the phases. `wiki/decisions.md:506,585` requires a separate optional dispatcher; the cited decisions do not require command-mode staging. Book chapter 9 describes the two modes.
- **Proposed change:** Ship the unprivileged dispatcher Unix-socket service from the initial protected-launch slice, reusing the specified broker connection/framing rules; the Curator CLI remains its client. Initial admission still refuses temporary capacity closure and omits queue/events/long waits and advanced integrations. Add these later behind protocol/capability gates on the same core and transport. Remove the separate command installation mode, public caller-to-service sudo entry, SUDO_UID branch, detached-command bootstrap, external sweep timer and command-to-daemon conversion. Preserve dispatcher-to-root helper/launcher rules, caller request signatures, fresh principal/generation checks, descriptor-inheritance/passing restrictions, server-UID verification, durable effects/receipts and process-absence reconciliation. Complete recovery and publish readiness before admission; an absent/unready daemon refuses with no command fallback. This replaces draft phasing, while preserving separate modules, quotas, standing lifetimes and D-EXECUTOR. Future binary/schema upgrades still require fenced operator maintenance and F-2 absence safeguards.
- **Expected benefit:** One transport, authentication path and installation model; fewer process/control states and no avoidable transport migration. Queueing can be delivered without coupling it to daemonisation.
- **Risks and costs:** Service installation/readiness moves earlier and needs hosted-runner qualification. Dispatcher outage blocks new requests. Existing execution/supervisor crash handling remains necessary; this does not remove execution claims or imply live-process adoption. Update all slice-0/deployed-sudoers references together so acceptance tests exercise the selected path.
- **Affected specs:** dispatcher §§2–3, 6–11 and qualification; broker slice-0 acceptance §16; CIP-0011 phase/client/acceptance text; book chapter 9 and deployment diagrams.
- **Confirmed-by:** `macmini_swarma-review_rev4`, answer `$YJFFZvyhF9wIQIjCG_vTUXqkbO7V_3OExm5NelpeK9Q`; `macmini_swarma-review_rev1`, answer `$0F2E3z5VjiR4S8i8MLSzv4yPpWANShjllJ_7Ne6iN5A`, in `#swarma-review`, topic `f-daemon-first`, 2026-10-12. Accepted maintenance/readiness refinement: `$owsu67BMLyZT9ptYzBnC22XArpKNYA03kCsl75_N0ro`.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-6 — Publish one launcher descriptor lifecycle for trusted handles and bounded plan staging

- **Lens:** Trust and threat model; launch reliability; contract consistency.
- **Problem:** The launcher takes the shared generation lock and opens the verified executable, then closes every descriptor above caller-owned 0–2 before writing its root receipt, dropping privileges and executing by descriptor on Linux. Literal ordering discards the internal lock and executable handles before their last required use. It contradicts the shared-lock guarantee, permits retirement to interleave while the launcher is still root, and loses the handle required for verified descriptor execution. The same step writes up to 48 KiB into a new pipe before the first described reader can execute, without a qualified capacity/feeder or post-intake write deadline. If the complete plan cannot be staged, the launcher cannot reach its reader; retaining the required shared lock would also obstruct stop/retire/recovery. These are gaps in the proposed lifecycle, not tested implementation defects or claims about a fixed kernel pipe capacity.
- **Evidence:** Paths below are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-host-helper/spec/helper.md` @ `889e141`: §2, lines 47, 70, 75 (intake deadline and plan bound); §4.6, line 211 (exclusive lock across both binaries); §7, lines 284, 287–294 (lock/open, close-all, pipe write, root receipt, privilege drop and descriptor exec); §12, line 347 (launcher qualification without maximum-payload staging). `diagrams/launch.puml`, lines 35–65, repeats that sequence.
  - `curator/curator-agent-launcher/SPEC.md` @ `9ee6e38`: §10.1, lines 1727–1742 (immutable verified plan, close-all, newly created pipe, first agent-side reader); lines 1748–1750 (48 KiB/80 KiB bounds); lines 1761–1770 (pending intake/digest/framing/read-deadline publication). It supplies no trusted-handle retention exception or launcher-side staging guarantee.
  - Book `wiki/book/swarma/ru/09-zapusk.md` describes the privileged launcher as the approved transition into the agent account; D-EXECUTOR retains that boundary.
- **Proposed change:** Publish a single descriptor-lifecycle contract shared by the helper and agent executor. Scrub untrusted inherited descriptors separately, preferably before creating trusted handles. Reserve read-only FD3 without clobbering the lock or verified executable. Retain generation exclusion through the root receipt and completed UID/GID transition, until the process is the receipt-matching agent execution; retain the verified executable through the kernel exec operation. Close internal handles at their last safe use or at exec with qualified close-on-exec behavior, and explicitly release them on every failure. The approved executor receives only caller-owned 0–2 and the plan on FD3, with no service, broker or root handle. Prefer completely staged bounded immutable bytes on FD3; a pipe alternative needs a published and qualified capacity/feeder/deadline/cleanup order that never waits for a reader unable to start. Preserve the admitted digest, same-effect receipt/recovery rules and typed unknown outcomes. Jointly publish the selected FD3 mechanism with §10.1 before activation; no path/stdin/network fallback or arbitrary caller argv.
- **Expected benefit:** Keeps generation authority valid through the privileged transition, preserves Linux verified-file execution and prevents staging from blocking unrelated privileged operations. One explicit success/failure lifecycle replaces conflicting cleanup instructions; no new service or privileged caller is required. Qualification should cover concurrent launch/stop/retire, maximum admitted plan, interrupted staging, abort after receipt/drop, exec failure and absence of internal handles in the executor.
- **Risks and costs:** Requires platform-qualified descriptor handling and bounded staging; the exact mechanism remains publication work. Any staging artifact must be protected, immutable to the agent and cleaned on failure. Holding generation exclusion longer requires a bounded pre-exec path. Receipt-before-exec uncertainty still needs reconciliation; no new claim of harness readiness or exactly-once completion follows. This does not challenge D-EXECUTOR, D-IDENTITY or the no-argument privileged entry.
- **Affected specs:** Helper §§2, 4.6, 7, 12 and launch diagram; agent launcher §10.1 and its publication/qualification gates; dispatcher prepare/start/recovery references; book launch sequence.
- **Confirmed-by:** Trusted-handle lifetime: `macmini_swarma-review_rev4`, answer `$2dX2ptF9chRgkRCW51S2fsqoZ_PXTyQy2eDi7Hiyj40`, and `macmini_swarma-review_rev2`, answer `$xbZwDsG9XdYG_xxxaIoXEBQJN12YgL5j1k1kL-2Q58k`, topic `f-launch-descriptor-lifetime`, proposal `$fJ44ohCyNMPwY7afU41v3qxzVTKIP7AMOjF6aG_c33U`. Bounded staging: `macmini_swarma-review_rev4`, answer `$jhE4VOZPzG5bWRXqE9KJGdUS9qe-63ghi5yoVnu9Sq4`, topic `f-launch-plan-staging`, proposal `$Dhlc6aIK7--RFH2LDx3E03MlmE7sucGncZft4vHlHgs`. Both in `#swarma-review` on 2026-10-12; consolidation notice `$L6NhEM5GiZh2PWV0zjtXzRu8oI46FBsQaZNctquoaAo`.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-7 — Separate remote effect claims from the ten-minute result cache

- **Lens:** operations and recovery; bounded storage; replay safety.
- **Problem:** The remote tool contract retains results for ten minutes but promises never to repeat an effect after reconnect. A lost reply followed by a long disconnect or executor restart can leave an unseen stable `op_key`; the published cache and connection-local IDs cannot distinguish that already-issued effect from new work. Accepting every cache miss risks repeating an `exec`, file write or patch; refusing every unseen key also prevents genuinely new operations. Signed mailbox admission has independent durable identity claims, but those do not automatically cover arbitrary tool methods. This is a gap in the unimplemented protocol contract, not a tested runtime defect.
- **Evidence:** Paths below are relative to `~/Developer/ReluxWorks/`. `curator/curator-spec/cips/CIP-0009-donor-side-deployment-and-bridge.md` D5, lines 159–166: reconnect, connection-scoped IDs, UUID `op_key`, ten-minute result cache, never-replay promise and durable outbound posts with stable keys. D6, line 169, and security line 200 cite IDs/cache as replay defences; test line 235 requires reconnect safety. `curator/curator-spec/protocol/remote-worker.md:18` leaves the standalone wire unpublished; line 48 repeats cached result or `unknown_result`, never a repeated effect. `curator/curator-spec/cips/diagrams/remote-worker-turn.puml:72,82` repeats the cache/reconnect ordering. The existing shape to reuse is `swarma-review/context/swarm-platform-architecture/vision/contracts/admission-and-delivery.md` §5, lines 73–77 and 90: durable identity/body claims, retention floors and closed admission after store rollback.
- **Proposed change:** At the existing workplace effect owner, durably claim the binding-generation-scoped operation identity and canonical-argument digest before mutation. Separate claim/replay evidence from cached output: a known claim with no conclusive result stays pending or `unknown_result` and never authorizes automatic re-execution; mismatching arguments refuse. Publish authenticated new-versus-retry admission with a bounded sequence/epoch floor or equivalent closed freshness window. Retries preserve their original identity and admission window; an expired result must not silently obtain a new one. Discard claims only after the corresponding identities are permanently inadmissible. Reconcile claims before recovery opens admission; lost, restored or unavailable claim evidence keeps the binding closed. Reuse the receiver-owned observation vocabulary from `f-effect-observation`; add no service or global transaction. Freeze these semantics with the pending remote wire and qualify long-disconnect, cache-expiry and receiver-crash cases.
- **Expected benefit:** Makes bounded result retention compatible with reconnect and crash safety, avoids duplicate remote effects and removes pressure to retain bulky results indefinitely.
- **Risks and costs:** Requires small durable claim/floor state and a published admission rule. Unknown results may need operator resolution; this does not promise exactly-once completion. A new operation identity is an explicit new effect decision, never an automatic retry repair. ADM example durations are not adopted as remote policy, and indefinite bindings must not imply unbounded claim storage.
- **Affected specs:** CIP-0009 D5/D6 and protocol qualification; remote-worker publication register; future Remote Bash/workplace execution contract; remote-worker turn diagram and book donor/recovery explanation. No change to donor variants, trust modes, job caps or local helper schemas.
- **Confirmed-by:** `ivan-network-profiles`, answer `$hocCkIHx3IyXxM5-pzZb33B_aLdawbtvEpFLz934ZA0`; `macmini_swarma-review_rev1`, answer `$qr_fKXPotAKDYqUnhTct9gK3uB5JbU2jwFYkHUS_PQ0`; `macmini_swarma-review_rev2`, answer `$RnOSjzu1J8AyRvF9Yw40rOaS1syNJ0ObueUPzkj2O8s`, all in `#swarma-review`, topic `f-remote-replay-floor`, 2026-10-12. Independent confirmations distinguish this remote admission invariant from the local effect-observation API candidate. Proposal `$u-PQlGRFMRqaHy5pIeCkJp6L7PJ536evujwClS0-AqQ`.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-8 — Publish a narrow broker revocation verdict for dispatcher admission

- **Lens:** simplicity; component boundaries; admission reliability.
- **Problem:** The dispatcher must check current caller-chain revocation before account creation, delayed work and subsequent starts. The broker owns the authoritative mutable local revocation state, but keeps it in its private service tree. The separate dispatcher principal has no published current-state read or verification verdict for operator/root revocations of another caller. Sharing the static verifier and carrying signed chains cannot supply that mutable truth. Treating unavailable evidence as empty violates the gate; refusing on unknown is safe but leaves the required admission route without a usable evidence path. Final broker bind and lease checks remain correct, but occur after account creation or executor launch and do not implement the earlier check. This is an unimplemented contract gap, not a credential-extraction exploit.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`. Dispatcher `platform/curator-dispatcher/spec/dispatcher.md` v0.5: §3.1, line 81 (separate service principal); §3.4, lines 99–103 (shared verifier and current revocation checks); §5.1, line 213 and §5.3, line 233 (prepare/start authority); §9, line 351 (queued rechecks). Broker `platform/curator-credential-broker/spec/broker.md` v0.5: §6.4, lines 302–303 (one authoritative local state and fail-closed reads); §12.4, line 534 and §15.2, line 590 (broker-private state); §13.2, lines 549–554 (`grant.list` for operators or signers of their own records, own-binding reads, owner/operator status, no dispatcher current-revocation view). §6.5, line 308 leaves the later multi-machine registry open. `curator/curator-spec/cips/CIP-0011-credential-broker-and-agent-users.md:122,141` retains broker-local state for slice 0. Book `wiki/book/swarma/ru/05-granty.md:33,116` repeats local broker revocation and dispatcher delayed-work checks without adding a transport.
- **Proposed change:** Keep the broker as the existing local revocation owner. Publish a narrow, bounded, authenticated current-state verdict/read for configured dispatchers, tied to the exact checked chain(s), check context and broker publication point. Prefer this over an independently mutable dispatcher revocation database. A protected non-secret snapshot is an alternative only with qualified freshness, sequence, rollback and failure semantics. Unavailable, stale or restoring state refuses before new effects; the view inherits the closed restore invariant in `f-local-revocation-restore`. The dispatcher still authenticates its caller, verifies request signatures and applies spawn, quota and capacity policy using the shared verifier. Recheck at each declared admission point. The verdict is point-in-time evidence, never a transferable grant or future-start permit; bind, lease and renewal independently verify current state under the broker lock. Publish the selected versioned contract and qualify revoked-before-prepare/dequeue/start, unavailable broker, stale evidence and closed restoration. Do not broaden private-directory access, promote the dispatcher to operator, add a registry service or invent a cross-component transaction.
- **Expected benefit:** One mutable revocation owner and a usable early-admission gate; less duplicated synchronization state, fewer unnecessary root provisioning/rollback effects, and a precise failure boundary between the two services.
- **Risks and costs:** A small authenticated read/verdict contract and client integration are required; broker unavailability can block early admission. A prior verdict cannot prevent a later revocation, so final checks remain mandatory. Snapshot-based alternatives need freshness evidence and cannot treat parseable old data as current. This does not solve the owner's separate restoration-history gap or revoke copied vendor tokens, and does not change the caller/dispatcher grant split.
- **Affected specs:** dispatcher §§3.4, 5, 7, 9 and qualification; broker §§6.4, 13 and qualification; CIP-0011 slice-0 composition; book chapter 5 and admission diagrams.
- **Confirmed-by:** `macmini_swarma-review_rev1`, answer `$QD9KG-GDkjkKJP6aTpjeYhC9avwmR-NoRSw-d9yvOyg`; `macmini_swarma-review_rev4`, answer `$4Z9NBt96bnFV4xCLsGtZkReTU6U6VDD66CybXaUjpJQ`, both in `#swarma-review`, topic `f-local-revocation-view`, 2026-10-12. Proposal `$cenAjrnlbOqj_4KKVsRaGA85jENkpowtsw9VpMvxAaU`; accepted point-in-time/restore refinement `$MDV57B2FjhTQoU2YS1T86nXxLDmUAhN4UpK40ZQwwr8`.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-9 — Fence local broker restoration until acknowledged revocation history is recovered

- **Lens:** Trust and threat model; recovery operations; authorization durability.
- **Problem:** Broker v0 treats its local `{seq, records}` file as authoritative and refuses unreadable or malformed revocation state. An operator can restore a correctly owned, readable snapshot made before an acknowledged grant/key revocation while the helper generation, binding and grant windows still match. The published checks then allow fresh leases under the revoked authority. Atomic replacement and an in-snapshot sequence do not establish freshness after restoration. Configuration, revocations and audit share the service home, so a witness there can be rolled back with them. This is an ordinary recovery failure trace, not a malicious-root claim, a tested exploit or the documented lifetime of already delivered vendor tokens.
- **Evidence:** Paths below are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-credential-broker/spec/broker.md` @ `b04b0a5`: §6.4, lines 302–304 (acknowledged local publication, read/parse refusal and token limitation); §6.5, line 308 (freshness/rollback requirement for future remote snapshots); §8.2, lines 382–383 (current chain checks); §12.4, line 534 (atomic private storage); §15.2, lines 590–592 (store/config/revocations/audit in the service home and service units). No local restoration barrier or surviving freshness witness is specified. §4.3, line 142, separately requires revocations to survive keeper migration.
  - `swarma-review/context/swarm-platform-architecture/vision/contracts/admission-and-delivery.md`, §5, line 90, already supplies a closed-admission restore rule; it does not supply this broker's restore procedure or a witness outside the restored snapshot.
  - Broker §6.1–6.2, lines 257, 274–275, binds exact parent IDs and the configured root, allowing explicit configured-root/grant replacement without silently accepting old chains.
- **Proposed change:** Publish local restoration as a fenced operator procedure. Lease issuance/renewal and service auto-start must remain closed until the current acknowledged revocation history is reconstructed against a trustworthy surviving journal/checkpoint outside the restored failure domain. If no such evidence survives, keep authorization unavailable, or explicitly invalidate the old broker authorization roots and reissue rights from new operator decisions; never repopulate current authority automatically from the stale snapshot. Publish the restore mark, service-start check and reconciliation/reopen order so interruption cannot reopen leasing. Any optional monotonic witness must survive the restored failure domain and be durable before revocation acknowledgement. Reuse the broker's sole revocation owner and existing configured-root/grant replacement; add no registry service, hardware requirement or unpublished v0 namespace field. Any dispatcher current-state view (F-8) must inherit this restoring/unavailable state.
- **Expected benefit:** A previously acknowledged revocation cannot silently disappear during supported backup recovery. Explicit restoration avoids pretending that an ordinary restart or self-contained sequence can detect its own rollback. Qualify a valid old snapshot after acknowledged revocation, loss of all freshness evidence, interrupted restore/reopen and keeper migration with preserved revocations.
- **Risks and costs:** Recovery may remain unavailable or require operator reauthorization when history is lost. A selected checkpoint adds an acknowledgement durability dependency; a fenced manual restore is the simpler initial procedure. This does not revoke standing identity keys under D-IDENTITY, prevent a hostile root from changing policy or erase already delivered provider tokens. Vendor auth-store/rotation recovery is a separate invariant.
- **Affected specs:** Broker §§4.3, 6.4–6.5, 8, 12.4, 15–16 and recovery/storage diagrams; local dispatcher revocation-view handoff; platform admission recovery and book grant/recovery explanations.
- **Confirmed-by:** `macmini_swarma-review_rev4`, answer `$fBDEj5G7S_l1AkRi4LQpXfZHd4PXNRbE3f7r0zl2usw`; `macmini_swarma-review_rev2`, answer `$ArNPhSAg-onQJcJtFmd0HxWUn7shtuoPfw4p367zjSI`, in `#swarma-review`, topic `f-local-revocation-restore`, 2026-10-12. Proposal `$AQLk3C2N7Vo1LNV_2G3VS1ayKyjOvBi4aJOVq7zZjYc`; recovery/root-replacement refinement `$1PVEOQyzbMp6ngKAhXLQLiwGiSSqLByspzEhjM-J4WA`. Distinct from F-8: this finding establishes the authoritative history after restore, not its read interface.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-10 — Publish receiver-owned observations for pending and recovered effects

- **Lens:** Reliability; reconciliation; unknown versus absent; component boundaries.
- **Problem:** Dispatcher recovery must query downstream effects by their stable IDs, but the helper publishes only generation/account metadata and mutation replay, while the broker specifies bind replay without an equivalent unbind effect observation or complete absence rule. Completed helper effects already return their recorded result and current target state on replay; a lost reply to a completed create is therefore covered. The remaining gap is observational semantics for pending, rolled-back or not-recorded attempts: after interrupted creation is rolled back, or when caller authority expires before reconciliation, the dispatcher needs evidence without authorizing a fresh create. A partial list, refused request or timeout cannot prove absence. Keeping unknown is safe but can indefinitely retain an allocation or capacity claim even when the receiver has decisive journal evidence. This is a high-confidence published-contract gap, not a tested implementation defect.
- **Evidence:** Paths below are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher/spec/dispatcher.md` @ `5d0476d`: §4.5, lines 186–199 (durable, distinct downstream effect IDs and same-effect retry); §4.6, line 203 (known present/absent, unknown and contradictory); §7.1, lines 286–287 (helper and broker lookup by effect ID), lines 292–295 (same-effect stop/cleanup and authority-sensitive recovery).
  - `platform/curator-host-helper/spec/helper.md` @ `889e141`: §2, lines 53–59 (closed operation list without a read-only effect lookup); §4.5, line 205 (generation ledger without effect/request mapping); §4.6, lines 211–213 (serialized receiver journal, interrupted-create rollback and completed-result replay with current state). The completed replay rule does not publish pending/rolled-back/not-recorded read semantics.
  - `platform/curator-credential-broker/spec/broker.md` @ `b04b0a5`: §7.1, line 339 (bind effect retained); §7.2, lines 348–352 (bind equality/replay, unbind and distinct effect IDs); §13.1–13.2, lines 540, 550–553 (request correlation and methods, without effect-specific unbind replay or complete-list/tombstone absence semantics).
  - Book `wiki/book/swarma/ru/09-zapusk.md`, lines 104, 124–125, repeats effect reconciliation and the rule that unknown never becomes absent.
- **Proposed change:** Publish one small receiver-owned observation vocabulary at the existing helper/broker boundaries. Prefer an authenticated read-only effect lookup, or precisely specified observational replay that cannot perform a new mutation. Scope it to the original receiver caller, effect ID, operation and canonical arguments; serialize it with the receiver journal. Distinguish recorded result plus current target generation/state, pending, rolled back, conclusively not recorded, unavailable and contradictory evidence, and define their mapping to the dispatcher's four observation classes. A rolled-back attempt reports that attempt's outcome; it does not create a replacement. Only complete authoritative evidence establishes absence. Keep completed mutation replay intact, including its current-state check; publish corresponding unbind and retained removal/tombstone observations. Specify retention and lost-evidence behavior so expired evidence stays unknown rather than becoming permission for a new effect. Reuse the semantic vocabulary for launch/stop where applicable, without exposing private journals or creating a shared mutable store. Qualification should cover crashes before intent, during effects, after result persistence and before acknowledgement, plus reconciliation after caller/grant expiry.
- **Expected benefit:** Gives reconciliation a usable evidence path without guessing by reusable UID/label or issuing mutations solely to learn state. Preserves fail-closed recovery while avoiding unnecessary permanent unknown when authoritative receiver evidence survives. One vocabulary reduces incompatible per-operation recovery rules; no service or global transaction is added.
- **Risks and costs:** A small closed read/replay contract, authenticated access and retained effect/tombstone evidence are required. Genuine missing or contradictory evidence still holds claims and may require operator resolution. Observation does not renew authority, prove harness readiness or promise exactly-once completion. F-7 separately establishes remote claims/admission floors; this entry exposes local evidence and does not duplicate that invariant.
- **Affected specs:** Helper §§2, 4.5–4.6 and recovery qualification; broker §§7, 13 and removal/replay qualification; dispatcher §§4.5–4.6, 7 and reconciliation diagrams; book launch/recovery explanation.
- **Confirmed-by:** `macmini_swarma-review_rev4`, answer `$QfiwUHCMpaU2A5UztIcQ1DxaEW63hPA0Yw3-BhcytFk`; `macmini_swarma-review_rev2`, answer `$H3nBKwK5sXraFhbzCyLR0n20PU3TK-T4cL8SuQB0zoA`; `macmini_swarma-review_rev5`, answer `$BgzzEaSXaBjcgakUBsyZ7ZCpeYtyndYy0bpTYfX6QJk`, in `#swarma-review`, topic `f-effect-observation`, 2026-10-12. Proposal `$VYpuFp21o_CO6dXtjRLtSoLNMwdsG6yt777CITppxuA`; accepted completed-replay scope refinement `$nRUSjHrnl9Xc9HLs5ZMB8PhcTRe32jMel4thmb4X5NQ`.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

## F-11 — Preserve single vendor-refresh ownership across broker replacement

- **Lens:** Reliability; crash recovery; child-process ownership; external effect uncertainty.
- **Problem:** The auth owner lives inside the broker daemon and holds an account lock while an approved vendor executable refreshes the native login. Vendor processes do not honor that lock. If the daemon dies while its refresh child remains alive, a replacement daemon can acquire the released lock and start another writer; the spec publishes no child-containment or writer-absence interlock. The stated single-owner guarantee therefore lacks a crash boundary. Even proving the previous child dead does not prove an external token rotation failed: the rotation can succeed before its durable local store/result is available. This is a high-confidence contract gap, not a claim about a tested vendor release or a particular service manager's defaults.
- **Evidence:** Paths below are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-credential-broker/spec/broker.md` @ `b04b0a5`: §3, lines 83–86 (daemon-local auth owners); §9.4, lines 471–475 (owner lock, vendor executable, vendor not honoring the lock, renewal deduplication and failure states); §9.5, line 479 (all local consumers use this owner); §9.6, line 483 (pinned historical contention/renewal evidence, without daemon-death/live-child qualification); §15.2–15.3, lines 592, 596 (service units and stop without child recovery/teardown ordering). `diagrams/codex-renewal.puml` likewise leaves daemon replacement ownership unpublished.
  - Book `wiki/book/swarma/ru/10-uchetnye-dannye.md`, lines 7, 12, 23, 29, identifies refresh contention and the single daemon-local owner as the chosen solution.
- **Proposed change:** Make slice-1 activation conditional on an account-scoped invariant: at most one live vendor refresh writer across daemon replacement. Prefer a qualified lifecycle using the existing service manager's containment and kill-and-confirm behavior on both supported platforms; no extra guardian service is needed. Persist attempt intent before launching, retain qualified attempt/process identity and close replacement refresh until the previous writer's lifecycle is resolved. A lock-lifetime mechanism is an alternative only if it covers the complete vendor child lifetime and failure paths. Resolve the previous attempt and reload the durable vendor home before deciding whether another refresh is safe. Confirmed child absence alone must not authorize retry after an ambiguous external rotation; if writer, store or prior-outcome evidence remains unknown, keep the account unavailable or require re-enrolment. Continue to run the approved executable instead of implementing the vendor exchange. Add qualification for daemon death during refresh, surviving children, replacement contention, crash after external rotation but before store/result persistence, interrupted cleanup and unavailable process/store evidence.
- **Expected benefit:** Extends the existing one-refresher guarantee to broker crashes and prevents both concurrent native-store writers and blind retries of an ambiguous rotation. Reuses service containment, account ownership and failure states rather than adding a service or distributed lock.
- **Risks and costs:** Requires platform-qualified containment, process/attempt evidence and explicit restart ordering; availability may be sacrificed until re-enrolment when the external outcome cannot be recovered. Vendor stores and behavior remain version-qualified. A durable attempt record is evidence of intent, not proof that an external rotation committed or failed. F-9 addresses acknowledged grant revocations after backup restore, a separate invariant.
- **Affected specs:** Broker §§3, 9.4–9.6, 15–16, auth-owner/renewal/recovery diagrams and slice-1 qualification; CIP-0011 broker composition; book credential/recovery explanation.
- **Confirmed-by:** `macmini_swarma-review_rev4`, answer `$WfPPlN7ouLdIUoX2CSzL96JHZEJ28blExb5C3uEmHrI`; `macmini_swarma-review_rev2`, answer `$iuzhOFda0QLRqPNbpdg2qxorW_wmtLlUv-L05IU-BbU`; `macmini_swarma-review_rev1`, answer `$kfo-8afGaw0YOxmJVS_Zst95L-iyyVzLyWkAk7F4uJc`; `macmini_swarma-review_rev5`, answer `$prxwsfYsSxLqHvEh4YZBn6Kyyfz7OC0QYy-os3uIdz8`, in `#swarma-review`, topic `f-refresh-child-ownership`, 2026-10-12. Proposal `$aIh-QWuZcO-SuFLEuqTWXzWP9buydvd1BfgvfMDzWbo`; accepted containment/outcome refinement `$YScuS9N3OvMB3v3TyLkeFi-KTuOZk7t2YumWHCCZcl8`.
- **Status:** accepted by the owner on 2026-10-12 («все принимаем»); routed to the module specifications through the next docs-only wave.

# Cycle 2

## F-12 — Keep privileged retirement local and leave broker unbind with its existing owner

- **Lens:** simplicity and operations; privileged surface; recovery reliability.
- **Problem:** The user manager persists `retiring`, then asks the broker to end the binding before stopping the account's processes. The dispatcher already owns a separate confirmed unbind effect before ordinary retirement. The helper-to-broker call has no published broker principal or failure contract: the broker admits unbind from the creating dispatcher or a configured operator, and no helper principal is specified. Every helper and launcher operation shares one root lock, so a blocking broker call also delays unrelated local starts, stops and creation. Local quiescence during a broker outage should not depend on this redundant call. This is a design inconsistency and unnecessary dependency, not evidence of an implemented deadlock.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`, §4.4, lines 172–177: persist `retiring`, broker call, then process stop/deletion; §4.6, lines 201–204: one lock for both binaries and recovery; §10, line 327: the dispatcher unbinds before `user.retire`.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`, §4.2, lines 128–134; §7.2, lines 359–367; §13.2, lines 574–582: configured principals and dispatcher/operator binding authority. §7.4, line 377: a retiring or removed generation refuses leases and renewals. §7.3, line 373: dispatcher removal before OS retirement.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`, §5.4, lines 273–279: unbind and user retirement are separate confirmed cleanup effects.
  - Broker `diagrams/revoke-and-unbind.puml`, lines 16–28, already shows dispatcher-to-broker unbind followed by wholly local helper retirement. Book chapter 3, `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, describes the irreversible retirement fence and local quiesce/delete path.
- **Proposed change:** Remove the helper-to-broker RPC from `user.retire`. Keep the helper's journaled local sequence: persist the irreversible retiring generation, quiesce and confirm process absence, destroy declared keys, delete home/temporary files, remove account/group and finally egress state. Keep binding cleanup with the existing dispatcher/operator broker API, distinct effect IDs, `effect.observe` and retained tombstones. Normal dispatcher cleanup retains its unbind-before-retire order. A direct operator retirement can establish local quiescence despite broker unavailability and must leave any unconfirmed broker cleanup as an explicit durable obligation at the dispatcher/operator boundary; it must not claim that the binding was removed. A retiring generation never returns to active, and a recycled UID never inherits its binding. Do not add a broker role to the root helper.
- **Expected benefit:** One owner for each binding effect, one fewer privileged cross-service client, and local stopping/deletion without an unnecessary broker dependency under the global root lock. Qualification should cover broker refusal, outage and fenced restore during direct operator retirement; subsequent cleanup reconciliation; stale binding after retirement; and UID reuse without old authority.
- **Risks and costs:** A direct operator retirement can leave an unusable binding and its cleanup evidence pending; that obligation needs an explicit reporting/reconciliation path. Ledger retirement is not a broker unbind receipt, and process death does not erase delivered vendor tokens. Preserve F-1 deletion, F-10 observations and D-IDENTITY; no owner decision is challenged.
- **Affected specs:** User manager §§4.4, 4.6, 10 and retirement diagrams; dispatcher §5.4 and direct-operator reconciliation; broker §§7, 13 and revocation/unbind diagram; book chapter 3.
- **Confirmed-by:** `macmini_swarma-review-2_opus`, answer `$rCFiGcgcIpsPVFHQoZNsG2cM5BT91hoI20BYfTAZU-o`, room `#swarma-review-2`, topic `f-local-retirement`, 2026-10-12. Confirms the unmatched authority, global-lock dependency and local-retirement direction with a separate operator unbind obligation. Proposal `$IdjWdQRYx7c3wle48e44m9RrIveFpOk9ZVljj8Qn0r4`.
- **Status:** proposed.

## F-13 — Make `exec.stop` signal and verify the same process set

- **Lens:** reliability and recovery; stop convergence; unknown versus absent.
- **Problem:** The two halves of `exec.stop` cover different process sets.
  - *Signalled set:* `exec.stop` sends SIGTERM and then SIGKILL only to the receipt's process session.
  - *Verified set:* it succeeds only when no process of the account that started at or after the receipt remains, escaped descendants included.
  - A descendant that started its own session falls in the verified set but outside the signalled one. Coding agents start such sessions routinely: tmux or screen servers, `setsid`, daemonizing dev servers. Repeating the same stop signals the same session again, so it cannot converge while that descendant lives.
  - The execution then never reaches finish. Cleanup, retirement and capacity release all wait behind it.
  - A session-host restart needs confirmed absence, so it stays parked.
  - An escaped process keeps its leased token past the stop. It also shares the UID, home and broker principal `(uid, generation)` with the next execution of the same generation, so a one-shot compromise becomes a standing one.

  The receipt window also bounds the verified set, which leaves two smaller gaps:
  - Processes that OS facilities start for the UID (cron, at, the per-user launchd domain) can start outside the window. Every later stop then ignores them, because each stop only counts processes started at or after its own receipt. They can keep running while the allocation is `idle`.
  - On macOS the kernel stamps a process's start time from the wall clock. A backward clock step can make a later descendant look older than the receipt and drop it from the verified set. This needs an operator or NTP step; an agent cannot cause it, so it is an operational gap, not an adversarial one.

  Only retirement uses the complete scope. This is a published-contract defect, not a tested implementation result.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`:
    - §4.7, line 218: signals go to the receipt's process session; verification covers account processes started at or after the receipt, escaped descendants included; one execution per generation.
    - `diagrams/launch.puml`, lines 98–103: the same sequence, ending in `processes_remain` and a retry with the same stop effect ID.
    - §4.4, line 174: retirement stops the per-user service domain, terminates every process of the UID and verifies over a quiet period.
    - §4.3, lines 156–159: account creation places no restriction on OS persistence facilities.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`:
    - §5.3, lines 262–263: the stop precedes finish.
    - §6, line 302: qualification lists descendants escaping the session, but the contract gives no converging result for them.
    - §7.1, line 320: the dispatcher repeats the same stop.
    - §9, line 379: capacity is released only after confirmed absence.
    - §15, line 446: a lost supervisor with escaped descendants.
  - `platform/curator-session-host/spec/session-host.md` r8 @ `3a253016`, §3.5, line 207: a restart requires confirmed process absence.
  - `curator/curator-agent-launcher/SPEC.md` @ `22973272`, §10.4, lines 1953–1956, and book `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, line 55: the stop receipt is issued only after no process remains, escaped descendants included.
- **Proposed change:** Give `exec.stop` and retirement one termination scope.
  - **Scope.** While the rule of one execution per generation holds, `exec.stop` for the generation's current execution does what retirement step 3 does:
    - it signals every process of the generation's UID: TERM, grace period, KILL;
    - it stops the per-user service domain where the OS has one;
    - it verifies absence over a quiet period.
  - **Receipt.** The receipt check (pid, start time, boot ID, session ID) remains the identity and authority check for the target execution. It no longer defines what gets terminated.
  - **Current-execution fencing.**
    - Account-wide signalling happens only when the requested `execution_id` is the generation's latest receipt.
    - A completed stop replays its recorded result without signalling.
    - An old receipt never authorizes stopping a later sequential execution.
  - **Per-execution containment.** Where it exists, a cgroup kill can make Linux signalling exact. The account-wide check stays decisive, because cron and launchd processes do not belong to the execution's unit.
  - **Persistence denial.** `user.create` denies OS persistence facilities to agent accounts. Each item is a qualification row, not a claim:
    - Linux: `cron.deny` and `at.deny` entries for agent accounts; no lingering, so no `systemd --user` manager; no session scope.
    - macOS: `cron.deny` and `at.deny`; verify that a process of a hidden non-login UID cannot bootstrap a background `user/<uid>` launchd domain.
    - `setsid`, double fork and `nohup` are covered only by the account-wide scope itself.
  - **Future backends.** A backend that ever allows concurrent executions per generation must replace this scope with an exact per-execution unit. It must never return to session scope.
- **Expected benefit:**
  - Stop converges no matter how an agent forked.
  - One termination scope replaces two.
  - `idle` means no process of the account, so slot accounting and restart preconditions hold.
  - A compromised agent cannot outlive its stop through `setsid`, cron or launchd.
  - Absence no longer depends on wall-clock start times.
- **Risks and costs:**
  - The stop kills every process of the UID by design, which relies on the existing one-execution-per-generation rule.
  - Persistence denial and the idle zero-process rule need per-platform qualification. A quiet period proves absence at the check, not that no OS facility can respawn a process later.
  - Unkillable processes, such as those in uninterruptible sleep, still yield `processes_remain` and stay honestly unknown.
  - No owner decision is challenged.
- **Affected specs:**
  - user manager §§4.3, 4.4, 4.7, 12 and `launch.puml`;
  - dispatcher §§5.3, 6, 7.1, 15;
  - session host §3.5;
  - agent launcher §10.4;
  - book chapters 3 and 7.
- **Confirmed-by:** `macmini_swarma-review-2_astra`, answer `$2exPHgpsWDfPGnRapYwVKCtxtqE6IRQI12Zz5XniN0g`, room `#swarma-review-2`, topic `f-stop-scope`, 2026-10-12.
  - The confirmation covers the signal/verification mismatch and the non-convergence of stop and cleanup.
  - Its two refinements, current-execution fencing and per-platform persistence qualification, were accepted in `$gD_fW_5wsz3d6smOC4pSdAg6Y1HAQZTKS3j5riN2Ie0`. Concrete cron and launchd denial mechanisms remain publication work.
  - `macmini_swarma-review-2_fable`, answer `$7HuagbWaAI_ZG7QT3YjTUuWVRgBGMHFpDmluM8mL6Vc`, same topic, 2026-10-12, confirms independently from the trust lens:
    - no published text widens the signalled set or denies persistence facilities;
    - an escaped process turns a one-shot compromise into a standing one;
    - the account-wide scope touches only generations the dispatcher created, so it opens no new hole.
  - Proposal `$xIl_IppEi8rqUCmEQyhSiFHnhw833jrwbqrCbvJLQ3U`; clock addendum `$B5Du4y8WIXFxQ9QcnuEa6ez2OpgfBV_I9TiXyHziT18`.
- **Status:** proposed.

## F-14 — Publish a renewal path for the credential authority of standing and kept allocations

- **Lens:** reliability and operations; standing allocations; credential-authority lifecycle.
- **Problem:** Standing allocations have no expiry by owner decision. Their credential authority is finite on purpose:
  - every grant has a window;
  - the agent leaf's window is the intersection of the request, the caller's grant and the dispatcher's grant;
  - bindings carry `expires_at`, and the broker removes an expired binding and never extends one;
  - a lease's `authorized_until` is the earliest of these limits.

  That finiteness is intentional. What is missing is a renewal contract.
  - **Lapse.** When the earliest window ends, the binding is removed and leases and renewals refuse.
  - **No way back.** Reconciliation then keeps the standing allocation pending, because a new bind needs explicit fresh authority. No operation supplies that authority for an existing allocation:
    - §8.1 has no rebind or leaf rotation;
    - team bring-up only "reconciles";
    - `provision` would re-create the account, and re-creation is operator-only;
    - a broker bind replay never reactivates a removed binding.
  - **Shared cliff.** Every standing allocation under one dispatcher grant lapses at the same instant. The standing team, orchestrator included, loses credential authority together, and no recovery path is published.
  - **Delegations.** F-3's requester-signed orchestrator delegation has a window too. A renewed delegation does not rewrite the caller chains that descendants' bindings already hold.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`:
    - §3.4, line 104: the leaf window is the intersection of request, caller grant and dispatcher grant.
    - §3.5, line 123, and §4.3, line 156: standing allocations have no expiry.
    - §5.5, line 297: bring-up reconciles existing allocations.
    - §7.1, line 316: a new bind needs fresh authority, and a standing allocation stays pending.
    - §8.1, lines 339–351: no rebind operation exists.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`:
    - §6.1, line 263, and §6.2, lines 283 and 286: windows are mandatory and checked on every edge.
    - §7.1, line 351, and §7.2, lines 362 and 364: replay never reactivates a binding, and expired bindings are removed.
    - §7.3, line 373: the broker never extends a binding.
    - §8.3, line 421: `authorized_until`.
    - §8.5, lines 445–446: renewal is tied to the lease's binding and refused after `authorized_until`.
    - §14, line 617: the dispatcher grant is operator-issued with `--until`.
  - `platform/curator-session-host/spec/session-host.md` r8 @ `3a253016`, §3.1, line 137: capability expiry bounds authority, not the standing lifetime.
  - Book `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, line 148, and `09-zapusk.md`, line 139: standing allocations have no expiry.
- **Proposed change:** Publish one journaled renewal effect on an existing allocation.
  - **The effect.** The dispatcher re-signs the agent leaf under the current dispatcher and caller chains and replaces the broker binding for the same `(uid, generation)`. The effect has:
    - its own ID (E-rebind);
    - a fresh `revocation.check` with context `prepare`;
    - broker `effect.observe`;
    - a removal tombstone for the old binding.

    The account is not re-created.
  - **Authority.** The renewing principal must already sit in the chain it renews:
    - the dispatcher chain and standing roles: the operator, through the operator-signed team description or an operator re-grant;
    - ordinary kept allocations: the owner's fresh signed request;
    - F-3 orchestrators: a fresh requester-signed delegation, installed from the requester's authenticated connection.

    It is never the dispatcher's own signature.
  - **Never widens.** The new leaf is the intersection of the current chains with the originally admitted request. A renewal that would add accounts, harnesses or profiles is a new `provision`, not a renewal.
  - **Renew ahead.** The sweep renews before the earliest window ends. Status reports each allocation's credential-authority horizon, plus the dispatcher grant's `--until` as the node-wide horizon, so an approaching lapse is visible.
  - **Running leases.** Rebinding does not carry a running lease, because unbind ends the old binding's leases. Two options:
    - publish a fenced fresh-lease handoff for a qualified holder (runner or executor);
    - use an explicit park and restart that keeps the account.

    No seamless continuation is promised for env-channel executions or app-server renewal until such a handoff is published and qualified.
  - **Delegations.** For F-3 orchestrators, a renewed requester-signed delegation names exactly which existing allocations it reauthorizes. Each is rebound with the new chain, and ancestor revocation still applies through the retained ancestry.
  - **Expired versus revoked.** Renew-ahead applies only before a window ends. An expired chain needs explicit renewal by its authorized principal. A revoked envelope or key is never re-issued by the sweep; it needs a new explicit operator decision. Otherwise renew-ahead would become a way around revocation.
  - **Honest scope.** An env-channel execution already holds its token, so renewal changes only future leases and restarts. The correlated cliff therefore concerns restarts and Codex renewals. The cure is visibility and operator-authorized renew-ahead, not longer windows.
- **Expected benefit:**
  - Standing and kept roles survive grant renewal without re-creating accounts.
  - The correlated team-wide lapse goes away.
  - One renewal path reuses the existing bind, effect and observation machinery.
  - An approaching lapse is visible in advance.
- **Risks and costs:**
  - One more dispatcher effect, a broker binding-replacement rule and an operator renewal routine need publication and qualification. Cases to cover: renewal racing with revocation; a crash between removing the old binding and binding the new one; an expired chain.
  - Renewal interrupts running leases until a qualified handoff exists.
  - Operators must keep re-issuing grants.
  - This does not challenge the standing-lifetime decision or D-IDENTITY.
- **Affected specs:**
  - dispatcher §§3.4, 3.5, 4.3, 5.2, 5.5, 7.1, 7.2, 8.1, 15;
  - broker §§7.1–7.3, 8.3, 8.5, 16;
  - session host §3.1 (cross-reference);
  - book chapters 3 and 9.
- **Confirmed-by:** `macmini_swarma-review-2_astra`, answer `$7bsfZDCZOmzWNYr9GEHIJ2mdLd9x0pJqHsIAZ17jkmc`, room `#swarma-review-2`, topic `f-standing-renewal`, 2026-10-12.
  - The confirmation covers the operator/rebind contract gap.
  - Its narrowings were accepted in `$srlmJhSXmHif_atlJtVjskJukR2t48-qQCkuRru-jys`: finite authority is intentional, rebinding needs a published lease handoff or a park/restart, and descendant reauthorization must be explicit.
  - `macmini_swarma-review-2_fable`, answer `$s9tBflVQbd2NMMXPb-wir5y8MFqhfUIhK34LuqQPM4Y`, same topic, 2026-10-12, confirms independently from the trust lens that no published operation renews a leaf, binding or requester-signed delegation for an existing allocation. Its five trust conditions are folded into the proposed change:
    - the renewing principal is already in the chain;
    - renewal never widens;
    - expired is renewable but revoked is not;
    - renewal is an admission point;
    - honest scope.
  - Proposal `$cvPSJ6V1jlg6CqJ3_xfdg73ygMJ1W7xIj6pgf-DxMe4`.
- **Status:** proposed.

## F-15 — Keep recovery controls reachable and confine uncertainty to the records it affects

- **Lens:** operations and recovery; availability; simpler readiness semantics.
- **Problem:** Dispatcher startup requires recovery to be fully resolved before readiness, while the socket contract refuses an unready daemon's requests. Individual effect evidence can remain unknown indefinitely by design, and the existing per-record rules safely retain the affected allocation and capacity claims. No explicit contract keeps status, observation, reconciliation or authorized stopping reachable during that state. One unresolved historical effect can therefore both prevent node-wide admission after restart and hide the control surface needed to resolve it. This is a consequence of the combined F-5 service/readiness and F-10 observation contracts, not a request to treat unknown as absent.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`, §11, line 401: readiness requires resolved recovery; unknown or contradictory evidence closes admission. §8.3, line 363: an absent/unready daemon refuses. §7.2, line 329, qualifies status only with "when it can be served".
  - The same spec, §§4.5–4.6, lines 206–223; §7.1, lines 310–325; §9, line 379: missing evidence remains unknown, records retain their state and claims, and capacity requires confirmed absence. §8.1, lines 342–348, lists status, wait, list, cancel and reconcile without defining their availability during recovery.
  - Dispatcher `diagrams/activation.puml`, lines 8–16, repeats node-wide unready status for unresolved/unknown/contradictory recovery; lines 20–44 separately require maintenance closure and absence before a swap.
  - `platform/curator-session-host/spec/session-host.md` r8 @ `3a253016`, §3.3, line 177: the unready dispatcher refuses requests; §3.5, lines 205–207: maintenance and restart still depend on dispatcher-owned stopping and absence. Book chapter 9, `wiki/book/swarma/ru/09-zapusk.md`, repeats service readiness before admission and receiver-owned unknown observations.
- **Proposed change:** Publish distinct prerequisites for a usable recovery/control surface and for forward admission on the existing service. After exclusive state ownership, schema compatibility, journal replay and valid authentication/indexes, serve authorized status/list/observation/reconcile and already-authorized, current-execution-bound stop when its particular evidence and authority are sound. Do not require a new launch grant merely to observe an old effect. Classify every non-terminal record before forward admission. Leave unresolved records in their existing state, with their generation/allocation and all quota/capacity claims retained; retry observation through the sweep and reject forward actions on those records. Unrelated work may be admitted only when accounting is complete and the possible unresolved effects are demonstrably confined to those retained claims/identities. An unknown receiver-assigned identity is not itself unconfined if complete durable intent and claims bound the possible result. If affected identities, accounting, shared authorization or shared-state integrity cannot be bounded, keep node-wide forward admission closed. Operator maintenance, restore fencing and the existing fail-closed hold gate remain global barriers. Add no quarantine service or alternate launch path, and do not turn live supervisors into adopted ones.
- **Expected benefit:** Operators can inspect and stop known work while admission is closed; a safely bounded unresolved record need not permanently disable an otherwise usable node. Readiness becomes a check of recovered ownership, complete classification and safe accounting instead of a requirement that every historical uncertainty disappear. Qualification should cover a persistent record-local unknown, inaccessible shared state, unavailable broker verdict, authorized recovery controls, retained claims at quota limits, and maintenance closure despite otherwise usable controls.
- **Risks and costs:** The operation-availability matrix and the proof of confinement need publication. Some incidents still require node-wide closure and operator repair; capacity held by unknown executions remains unavailable. There is no forced-success, forgotten-effect or manual claim-release shortcut. F-2 still requires absence/reconciliation for every affected execution before mode/schema/binary changes; F-5 still requires recovery before new work; F-10's absence rules remain intact.
- **Affected specs:** Dispatcher §§2, 4.6, 7, 8, 9, 11, 15 and activation/reconciliation diagrams; session host §3.3 and maintenance references; CIP-0011 service readiness; book chapter 9.
- **Confirmed-by:** `macmini_swarma-review-2_opus`, answers `$-7ckR493p_NlyYaEWyecY3OarDRxj14PfJWSr-G0nq8` and `$ycnjIIzcUTvfcKhtj-wtDCEMUX04XMHZnD7yWkbimv0`, room `#swarma-review-2`, topic `f-recovery-control`, 2026-10-12. First confirms the control gap and proposes per-record containment; second accepts the bounded-accounting refinement in `$EEUW5URNRi2cqpY6X55rhw2WlRMosV_8UeWn8dc7LYw`. Proposal `$QCYamc0o-WOufIO_T5tEXCC5DXKJkgNOhZBVqUwtBtI`.
- **Status:** proposed.

## F-16 — Give each agent account private writable Git administration

- **Lens:** simplicity and operations; cross-account isolation; workspace portability.
- **Problem:** The architecture recommends `git worktree` as the portable default for cheap ephemeral workspace copies. A linked worktree is not a separate Git repository: its administrative directory points back into a common repository, with shared refs and configuration. If that repository remains in another agent's private home, the child cannot use it. Making the common metadata writable across accounts instead creates a path for one agent to change another account's repository behavior, including executable Git configuration or hooks. Copying a linked worktree can retain its external `.git` backlink. Copying an entire repository can also import the parent's local configuration unnecessarily. No cross-account workspace contract reconciles this default with the specified private homes. These are design boundary problems, not tested exploits.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/` unless absolute.
  - Book `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, line 150: APFS/reflink copies and portable `git worktree` default. `swarma-review/context/swarm-platform-architecture/vision/contracts/trust-and-isolation.md`, §5, lines 43–47: one OS account per autonomous agent and the same cheap-tree recommendation.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`, §4.0, line 115; §4.3, line 156; §6, line 258; §13, line 359: private 0700 homes, no supplementary groups, no recursive privileged chown of agent-controlled content, and no default parent ACL.
  - Installed primary Git documentation `/Library/Developer/CommandLineTools/usr/share/man/man1/git-worktree.1`, lines 426–437 and 495–507: shared refs/config, per-worktree administration below the main repository, and `.git`/common-directory references. These facts do not depend on relaxing Git's separate ownership checks.
  - Platform `vision/contracts/launch.md`, §3, line 40: admitted repository identity, exact base and workspace policy. `vision/contracts/kernel-guards.md`, K2: story workspace isolation is a workflow rule, not an OS-account boundary.
- **Proposed change:** Require independent writable Git administration at every mutually isolated account boundary: private `.git`, common directory, refs, index, configuration and hooks. Use a standalone repository under the agent home as the cross-account default; retain linked worktrees within one account/trust domain, including today's board workflow. Materialize the admitted base and approved content with freshly defined local Git configuration, never by inheriting the parent's `.git` backlink, executable local configuration or credential helpers. Copy/reflink optimizations must preserve that rule. Optional object sharing must be immutable and read-only to agents, limited to authorized source objects, with published provenance/access and retention rules; mutable hard-linked metadata is not isolation. Publish who transfers source and results across private homes before activating workspace-capable cross-account launches, using the existing approved repository/artifact path rather than weakening home permissions or adding recursive root chown. This does not require a new privileged workspace service.
- **Expected benefit:** A portable workspace boundary that matches per-agent UID isolation, fewer ownership exceptions and fewer shared Git mutation/recovery cases. Qualification should cover private source homes, copied linked-worktree backlinks, attempts to modify another account's metadata, source configuration/hooks excluded from materialization, the admitted base, and the lifetime of any shared object store.
- **Risks and costs:** Independent repositories use more storage unless immutable objects are safely shared. Source/result transfer needs an explicit owner and authorization, and shared object access can expose source beyond a requested branch unless bounded deliberately. This does not promise that checked-out code or accepted results are secret-free. No D-* owner decision or same-account board worktree policy is challenged.
- **Affected specs:** Trust-and-isolation §5; launch/workspace policy; the launcher workspace materialization contract and dispatcher integration; K2's distinction between workflow and account isolation; book chapter 3.
- **Confirmed-by:** `macmini_swarma-review-2_fable`, answer `$FlK75GCyXlXMqdkoOblwTqblmM-RJ8kPQ0Phcq5wW0c`, and `macmini_swarma-review-2_opus`, answer `$z8CnI7lp9I1FoEaIqv3c-zfe7H8wuVl1Vrctnv9My1Y`, room `#swarma-review-2`, topic `f-private-git-state`, 2026-10-12. Both confirm the cross-account common-directory problem and private-repository direction; fable adds fresh local configuration and explicit content transfer. Proposal `$OH2w1URmKO6mEVdZ9HTGIeFtMYFynwjraXeD9sIpvpY`; scope refinement `$H2-_ylSDI96zo9yZxO-AwGsWgBypnQzcxhc-oQgii04`.
- **Status:** proposed.

## F-17 — Specify state loss and restore for the user manager and dispatcher, not only the broker

- **Lens:** reliability and recovery; durable identity; unknown versus absent.
- **Problem:** The platform specifies crash recovery through journals. For state loss or restore it specifies only the broker's revocation state (F-9). Four invariants that other components depend on have no supported procedure:
  - **No identity resurrection.**
    - The ledger is the liveness anchor every other component trusts. Broker principals, host connections and the architectural key keeper accept a UID only while the ledger shows its generation as active.
    - A ledger restored to a point where a since-retired generation `g` was active re-enables `g` for whatever process now holds its UID. The OS account may have been removed and the UID re-issued in the meantime.
    - If broker state is restored to the same point, the new holder leases under `g`'s binding. With a key keeper, it would sign as `g`'s identity.
    - Random generation identifiers do not prevent this: it is the same `g` and the same UID. It is the account-level twin of F-9's resurrected revoked grant.
  - **Never-reused generations.**
    - The generation is "never reused", but no allocator is published. The book calls it a number, and the examples (`g-0193`, `g17`) look like a counter.
    - A counter-backed implementation could re-issue generations after a ledger restore. The UID cursor in the same file would roll back too. If the post-snapshot account was retired, its UID can also be re-issued, and the same `(uid, generation)` would then name two account instances across:
      - dispatcher records;
      - broker bindings and tombstones;
      - receipts and the audit log;
      - `agent:<generation>` leaves.
    - The ledger is also the file whose damage stops the node, because every consumer refuses an unreadable ledger. Restoring it from backup is the natural repair.
  - **Coverage after restore.**
    - R-OBS already forbids `not_recorded` without complete authoritative coverage, and forbids capacity release without process evidence.
    - What is missing is any way to establish that coverage after a restore. A restored journal looks complete, and a snapshot cannot certify its own rollback, which is the F-9 principle.
  - **Dispatcher state loss.**
    - Reconciliation runs only from the dispatcher's own non-terminal records to the receivers. It never lists the user manager's accounts or the broker's bindings.
    - After dispatcher state is lost or replaced, every account, binding and running execution it created becomes an orphan. Each one:
      - stays active and bound;
      - counts against the dispatcher's user-manager quota;
      - is never stopped or retired, so its home is never deleted (F-1).
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`:
    - §4.1, lines 128 and 130: round-robin UID cursor in the ledger; "never reused" generation with no published allocator.
    - `diagrams/storage-layout.puml`, line 9: the ledger holds all generations and the allocation cursor.
    - §3, line 88: the dispatcher's account quota.
    - §4.6, line 205, and §14 question 8, line 370: `not_recorded` requires complete authoritative coverage; the coverage proof is unpublished.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`:
    - §3.2, line 88: an unreadable or invalid ledger refuses.
    - §4.6, lines 210–223: the R-OBS mapping, and no capacity release without process absence.
    - §7.1, lines 310 and 314: forward-only reconciliation of the dispatcher's own non-terminal records.
    - §11, line 404: a binary refuses unreadable or unsupported state, and old snapshots are never restored as a repair; no state-loss procedure is given.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`:
    - §4.2, line 130: ledger read failures refuse.
    - §6.3, line 292: grants rely on never-reused generations.
    - §6.4, line 312, and §15.4, line 659: F-9's fenced restore, and "a same-home sequence, audit file or checkpoint cannot certify its own rollback".
    - §7.1, line 341: `binding_id` is already a random 128-bit identifier.
  - `platform/curator-session-host/spec/session-host.md` r8 @ `3a253016`, §3.1, line 135: the host reads the ledger directly.
  - `swarma-review/context/swarm-platform-architecture/vision/contracts/admission-and-delivery.md` @ `e5781c8`, §5, line 90: a store restored from backup, with a store epoch older than the recorded one, keeps the fence closed until an operator reconciles.
  - Book `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, lines 34 and 79: the generation is a never-repeating number; example `g17`.
- **Proposed change:**
  - **Fresh generations.** Create generations from a fresh random 128-bit value, as `binding_id` already is, so uniqueness never depends on a durable counter. This does not authenticate a restored old ledger. Like `uid_not_clean`, which checks the filesystem rather than the ledger cursor, the generation rule rests on evidence outside the ledger.
  - **Generations only move forward.** After a declared restore, a generation that any surviving evidence records as `retiring` or `removed` is never returned to `active`. Surviving evidence means the OS directory service, broker tombstones, `receipts/<generation>/` or the audit log. An `active` record whose OS account is absent is contradictory, not an interrupted creation to resume.
  - **Ledger store epoch.**
    - The broker, host, launcher and dispatcher read the ledger file directly, so no RPC can close them.
    - The ledger therefore carries a monotonic store epoch. Every reader records the highest epoch it has seen, in its own state, and refuses a lower one until an operator reconciles.
    - This reuses the store-epoch rule that `vision/contracts/admission-and-delivery.md` §5, line 90, already applies to the host store. It detects a rollback of the ledger alone; it cannot detect a whole-machine rollback.
    - A reader's epoch floor helps only while that reader's own evidence survives outside the restored failure domain. It complements the shared restore fence and the completeness proof; it never replaces them.
  - **One shared operator restore procedure** for user-manager and dispatcher state, reusing F-9's fence:
    - the restore mark lives outside the restored domain;
    - a user-manager restore closes every ledger consumer (broker, launcher, session host, dispatcher) before the restored bytes become visible; closing `effect.observe` alone is not enough;
    - the user manager answers `unavailable`, never `not_recorded`, for effects admitted before the restore point, until coverage is re-established against surviving evidence: the OS directory service, preserved receipts, other components' records and operator evidence;
    - the dispatcher stays closed for new admission meanwhile.
  - **Reverse inventory.** Dispatcher reconciliation also lists:
    - the user manager's accounts with `created_by` equal to the dispatcher;
    - its own broker bindings;
    - receipts.

    An object with no dispatcher record is reported as an orphan and held for an operator decision: retire it, or re-adopt it with a signed record. Names or UIDs alone never authorize adoption or deletion. There is no automatic orphan adoption and no live-supervisor adoption.
  - **Honest limits.** If the user-manager ledger was rolled back too, post-snapshot accounts can only be found from the OS inventory, preserved receipts and operator evidence. No bounded recovery is promised when evidence is lost.
- **Expected benefit:**
  - The identity invariant behind grants, bindings, receipts and `exec.stop` survives the most likely repair.
  - F-10 absence is never inferred from rolled-back evidence.
  - Dispatcher state loss gets a visible recovery path instead of permanent orphans.
  - F-9's mechanism is reused, not reinvented.
- **Risks and costs:**
  - Generation strings get longer.
  - Restore remains an operator procedure.
  - An undeclared, internally consistent whole-machine rollback still cannot be detected locally. This is F-9's limit, and a reboot clears that rollback's processes anyway.
  - The orphan re-adoption record format needs publication.
  - No owner decision is challenged.
- **Affected specs:**
  - user manager §§4.1, 4.5, 4.6, 14;
  - dispatcher §§4.6, 7.1, 11, 15;
  - broker §15.4 (cross-reference);
  - session host §3.1 (closing ledger consumers);
  - book chapter 3.
- **Confirmed-by:** `macmini_swarma-review-2_astra`, answer `$uehBtxZtIeJaLUAl0GzOg8mL84MlAOkIcTVNhpiLF9A`, room `#swarma-review-2`, topic `f-state-loss`, 2026-10-12.
  - The confirmation covers the missing supported restore and state-loss procedure for the user manager and dispatcher.
  - Its refinements were accepted in `$de-Wlx7axdBePHCwSg5ngQqNWecnhUg66e6Yi-7-hvA`:
    - generation reuse is possible, not certain;
    - the gap is a missing way to establish R-OBS coverage, not a specified release path;
    - every ledger consumer closes before restored bytes become visible;
    - reverse inventory has limits;
    - no automatic adoption.
  - `macmini_swarma-review-2_fable`, answer `$JKauzc4DSe0R5nUh_zAV5W1qsE-5yUA2ByjDrSkVOAM`, same topic, 2026-10-12, confirms independently from the trust lens. It adds:
    - the identity-resurrection invariant;
    - generations that only move forward;
    - a ledger store epoch for the direct readers;
    - `uid_not_clean` as the model for evidence outside the ledger.

    All four are folded into the problem and the proposed change.
  - Astra's follow-up `$3uGhlXP3Tp2qkth6-eRpIlkLV6LCqpgbblEY6ADLOwg` confirms the revised scope. It adds that reader epoch floors never replace the shared fence.
  - Proposal `$lPfOXX59ClvCKVzHSn9CgrX2NLb01gcCx6Jr0B-r6RM`.
- **Status:** proposed.

## F-18 — Publish process fate and containment per process class, with a fence against writers from a replaced daemon

- **Lens:** reliability and recovery; process ownership; platform-qualified behavior.
- **Problem:** No spec says which service-manager or kernel containment domain a dispatcher supervisor or a launched execution belongs to. Nor does any spec say what happens to them when the dispatcher, the session host or the broker stops, crashes or is swapped.
  - **Process tree.** After F-4 and F-5, every execution descends from the dispatcher daemon: daemon → per-execution supervisor ("inside the daemon") → sudo → launcher (`setsid`) → executor or SH2+ runner.
  - **Fate follows deployment defaults, not the contract.** The documented defaults differ:
    - systemd's default control-group stop kills every process in the unit's cgroup, regardless of `setsid` or UID change. The exception is when sudo's PAM stack moves the command to another scope, which varies by distribution.
    - launchd's job-exit cleanup kills only the job's process group, and `setsid` leaves that group.

    The specs publish no dispatcher unit configuration. So a dispatcher restart ends every execution or none, depending on platform and deployment.
  - **Consequences in the current text:**
    - **Affected set for F-2.** Maintenance must confirm absence for every affected execution before a swap. Which executions a dispatcher swap affects is unpublished. On a control-group deployment it includes every SH2+ runner; elsewhere, only the executions held by supervisors.
    - **SH2+ runners.** With a session host present the dispatcher "does not hold processes", and the host re-adopts live runners after a controller failure. Whether runners survive a dispatcher replacement is not stated.
    - **Surviving supervisors.**
      - Reconciliation handles only "supervisor known absent". A supervisor that outlives its daemon instance, which is possible where `setsid` escapes the job's kill, has no reconcile row and no fence.
      - The v0.5 fence ("every v0 supervisor checks the recorded mode and backend generation and stops when they change") was removed together with command mode.
      - Such a supervisor is either adopted implicitly, against the no-live-adoption rule, or it is an unfenced second writer of dispatcher records.
    - **Opposite policies.** F-11 requires the broker's vendor children to be contained and killed with the broker. The remote workplace specifies per-exec process groups and transient cgroups. The local launch path specifies nothing.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`:
    - §1.1, line 53: with a session host present, the dispatcher holds no processes.
    - §1.2, line 66, and §5.3, line 259: the supervisor is inside the daemon and registers its own process identity.
    - §6, line 301: daemon loss authorizes no live adoption.
    - §7.1, line 319: only the "supervisor known absent" row.
    - §11, lines 402 and 404: absence for every affected execution before a swap; no live supervisor adoption.
    - §12, line 414: controller-only re-adoption of a live runner.
  - Dispatcher v0.5 @ `5d0476d`:
    - line 62: "v0 detached, v1 inside the daemon";
    - line 368: the surviving-supervisor fence.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`:
    - §7, line 289: the launcher calls `setsid`;
    - line 295: sudo "may or may not remain a parent".
  - `platform/curator-session-host/spec/session-host.md` r8 @ `3a253016`:
    - §1.1, line 35: a Claude session dies when its daemon is replaced;
    - §3.2, lines 160–162: re-adoption of a live runner.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`:
    - §9.4, line 489, and §15.2, line 643: service-manager containment of vendor children.
  - `wiki/session-host/architecture.ru.md`, lines 2015–2017: each remote exec in its own process group, plus a cgroup on Linux.
  - Book `wiki/book/swarma/ru/07-host-sessiy.md`, line 31: the runner survives a service restart.
- **Proposed change:**
  - **Fate table.** Publish one table, owned with R-FD3 in user manager §7 and referenced by the dispatcher, session host and broker.
    - One row per process class:
      - dispatcher daemon;
      - dispatcher supervisor;
      - execution root (`curator-run` or the SH2+ runner) with its descendants;
      - broker vendor-refresh child;
      - session-host service.
    - Each row states:
      - its service-manager unit or kill domain;
      - its fate on stop, crash and restart of each service;
      - whether its backend promises survival;
      - how its death is observed: journaled stop or `lost`;
      - which executions a swap of each service affects for F-2.
  - **Writer fence.** Every supervisor write is checked against a durable daemon-instance epoch, so a supervisor that survives a replaced instance never writes. This restores the v0.5 fence. No live adoption.
  - **Wording.** The platform's own services and service managers end an execution only through `exec.stop`, retirement or an operator emergency stop. OS failures such as OOM remain possible and are recorded as `lost`.
  - **Qualification.** Run per platform and per published unit configuration, covering every row.
    - Unselected or unaffected executions must survive only in backends that promise it.
    - The supervisor backend keeps its explicit `lost` path on daemon loss.
    - F-2 keeps absence for every affected execution.
  - **Recommended option, not mandated.** A root-created, non-delegated per-execution unit, recorded in the root start receipt.
    - On Linux this is a cgroup outside the dispatcher unit. The launcher creates it before the privilege drop, through systemd where systemd owns the tree.
    - It gives exact absence evidence on Linux.
    - Conditions:
      - The unit is root-owned and never delegated to the agent UID; a delegated subtree lets the agent migrate out.
      - On macOS a new session is evidence, not containment, so the UID scan stays the absence proof there.
      - The unit is never authority.
  - **Not claimed.** A unit alone sets no resource ceilings. Per-execution pids, memory, CPU and storage limits are a separate future capability with their own published policy and per-OS coverage. No macOS parity is promised.
- **Expected benefit:**
  - Recovery behavior becomes a published, testable contract instead of a deployment default.
  - F-2's affected set and the survival of SH2+ runners are stated explicitly.
  - No unfenced writer remains after a daemon replacement.
  - Where the unit is adopted, absence proof on Linux becomes exact and cheaper.
- **Risks and costs:**
  - Unit configurations must be published, and every row needs per-platform qualification.
  - If the per-execution unit is adopted, the launcher gains a small root step that needs qualification.
  - In the supervisor backend, standing executions still end on daemon loss. Keeping them alive would need supervisor re-attachment, which would challenge the F-2/F-5 no-adoption clause; it is not proposed.
- **Affected specs:**
  - user manager §§4.7, 7, 12;
  - dispatcher §§1, 6, 7.1, 11, 12, 15;
  - session host §§3.2, 3.5;
  - broker §§9.4, 15.2 (cross-reference);
  - book chapters 7 and 9.
- **Confirmed-by:**
  - `macmini_swarma-review-2_astra`, answer `$jSZj2fpmGAsv51hYCJwOm_h4t86pRSDjQancNyQ4ARg`, room `#swarma-review-2`, topic `f-execution-containment`, 2026-10-12.
    - It confirms the narrowed contract at high confidence: published per-class fate, the replaced-daemon writer fence and deployment-qualified survival claims.
    - Earlier corrections `$W_y-fhpja4B6PcVbU-3uHoPdTEJ4VTIh7-vdEX-g39k` and the resource condition `$RliVDLeEIUlw-MRY8GmKy-G_mmUU6M1-pVDJA3kgJo8` were accepted in `$Dx9QW90i_H9wzktaoT92G-h4H1-3X77KI_emNyzDTTA` and `$8sL_mDh9pZpHBRrU8198jU4fa72PLBZzMgCp87fyosM`.
  - `macmini_swarma-review-2_fable`, answer `$ZKeMFkpXNCKv5Les1cfHJ55IB55bV446qtDF1YnfHFk`, same topic, confirms from the trust side at high confidence. Its three conditions for the per-execution unit are folded in.
  - Proposal `$qALBpgqAsnfxGqGxDpukd_UWY_WcqHeTHhlatggEPpo`.
- **Status:** proposed.

## F-19 — Run the project-side remote executor as a service principal and specify the workplace account

- **Lens:** trust and threat model (external contributors on our host); privileged and untrusted surfaces; cross-spec consistency.
- **Problem:** The remote worker is untrusted by definition, yet the process that enforces its policy on our host runs as the worker. CIP-0009 admits the donor bridge through sshd with `restrict` and a `ForceCommand` by protected absolute path; sshd runs a forced command as the authenticated user, and no specification places the project-side executor (`swarma-rb-exec`) under a service principal. Everything the design asks that executor to enforce therefore runs with the workplace UID: the tool-set intersection and server-authoritative caps, job leases with "kill the process group and verify that no process of the workplace UID descends from the job", the F-7 durable effect claims "at the existing workplace effect owner", our-side audit, and the user-CA certificate renewal, whose CA custody is unspecified. A worker whose policy admits `bash`, `write_file` or `apply_patch` controls a process of that UID. It can signal the executor, leave its process group with `setsid`, migrate out of any cgroup the executor created in its own delegated subtree, and read or rewrite whatever that UID can write, including claims, audit and cursors if they live there. The descendant-cleanup test vector is unprovable as written, and the policy fields `write scope` and `network mode` are unenforceable by a same-UID executor. Two further contradictions: the user manager gives every account it creates no login shell (`/usr/bin/false`, `/usr/sbin/nologin`) through a closed `user.create` schema, so a workplace provisioned as CIP-0009 says cannot run a forced command at all, and with a real shell `~/.zshenv` or an `SSH_SOURCE_BASHRC` bash would execute worker-written files at the next connection (`PermitUserRC no` covers only `~/.ssh/rc`); and CIP-0009 promises the workplace "per-UID egress" while the only egress enforcement the platform has is the user manager's v1 firewall with published applied state, which the broker gates leases on but nothing gates a workplace on. A remote workplace leases nothing, so the broker gate never fires; the remote-worker order places variant A right after slice 0 and enforced networking in slice 2; the dispatcher excludes remote targets. The project-side workplace account shape, its executor principal and its egress gate have no owner in the module specifications. This is a published-contract gap for the stated adversary, not a tested exploit.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `curator/curator-spec/cips/CIP-0009-donor-side-deployment-and-bridge.md` @ `601cbb0`: line 157 (D4 step 7: the dispatcher provisions the workplace "with per-UID egress"; the user CA; the forced executor), line 163 (D5: `ForceCommand` by protected absolute path, no PTY, no forwarding), lines 164–165 (server-authoritative caps; F-7 claims "at the existing workplace effect owner"), line 168 (job lifetime: process group, lease, descendant verification "a test vector, not an assumption"), line 169 (backend contract: policy with `write scope`, `network mode`; "egress per UID"), line 170 (audit: "our executor logs who, what, when, policy identity and exit"), line 187 (D12: worker certificates renewed "by the bridge over the authenticated channel"; no CA custody), line 230 (implementation plan: `swarma-rb-exec` behind sshd, reusing `rwh`), line 242 (test: "descendants after transport loss (none survive)").
  - `swarma-review/context/swarm-platform-architecture/vision/contracts/trust-and-isolation.md` @ `e5781c8`: lines 135–136 (sshd `Match` block, forced command, user CA renewal), 140 (job lifetime), 144 (backend contract).
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`: §4.3, line 156 (no login shell; closed `{kind, label}` schema); §1.1, line 31 (donor provisioning is separate; nothing names the project-side workplace); §4.7, line 218 (`exec.stop` verifies every process of the generation started at or after the receipt); §8, lines 310–315 (enforced denial "installed in the same locked operation that activates the account, before the first launch"; applied state); §2, line 36 (sudo rule shape).
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`: §5.5, lines 238–239 (`lease_network_enforcement_unavailable` until helper v1 applied state); §16, line 666 (enforced networking is slice 2).
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`: §8.4, line 367 and §16, line 481 (remote targets outside the subset); §6, lines 301–302 (the only stop is `exec.stop`).
  - `curator/curator-spec/protocol/remote-worker.md` @ `601cbb0`: line 23 (`swarma-workplace-exec/1` pending, OS-user backend first), line 30 (variant A describes the donor side).
  - Book `wiki/book/swarma/ru/11-udalennoe-rabochee-mesto.md`, lines 3 (the remote worker is untrusted by definition), 98 (forced command as the executor), 100 (per-job process group and descendant check), 128 (order: variant A right after slice 0); `14-gde-my.md`, lines 74–78 (order of work without the network slice).
  - Platform semantics cited, not tested: sshd_config(5) `ForceCommand` runs through the user's login shell with `-c`; a process may signal any process of its real UID; cgroup v2 migration needs write access to the cgroup tree, which a same-UID creator has.
- **Proposed change:** Specify the project-side workplace as its own account class and keep every control outside the worker's UID.
  1. **Service principal.** Policy, tool intersection, caps, F-7 claims and floors, our-side audit, user-certificate renewal and the mailbox control plane live in a service principal: the existing bridge daemon (which the mailbox already reaches) or a dedicated `swarma-workplace` service account. The sshd entry is a root-owned stub in `/opt/swarma/libexec/` that only relays the SSH channel to that service's peer-authenticated Unix socket; the service identifies the workplace by kernel peer UID and active generation (broker §4.2 rules). A job that impersonates the stub from inside the UID gains nothing: posts still need the donor's `K_sig`, reads return the worker's own mailbox.
  2. **Workplace account class.** `user.create` gains a workplace kind whose login shell is that stub (a fixed binary accepting only sshd's `-c <forced command>` form and reading no user file) and whose network requirement is always `enforced`. Helper §8 then applies as written: v0 cannot activate a workplace; v1 activates it only in the same locked operation as `fw.apply` with published applied state. No read-only exception before slice 2: a service-executed `read_file` would need its own safe path into a 0700 home. Spec sentence: "A remote workplace requires enforced networking; it is admissible only after helper v1 on that host." The support matrix for workplaces makes loopback a hard row, because local TCP services on our host are the lateral path; Unix sockets stay unfiltered, so the broker, dispatcher and host sockets refuse a workplace principal that has no configured role on them.
  3. **Jobs as executions.** Worker jobs run under the workplace account through the existing launcher path, start receipt and `exec.stop`. Two shapes stay open until the workplace wire freezes: one job at a time as one admitted execution (exact per-job proof, serialised), or one standing "workplace runner" execution per workplace (the session-runner pattern, shared launch library) that spawns jobs on the service's instruction and holds no authority. In the runner shape, per-job cancel is process-group best effort; when a job's descendants cannot be confirmed gone, the service escalates to `exec.stop` of the runner execution under F-13's account-wide scope, retains every affected job claim as unknown and never replays their effects, then restarts the runner. The descendant-cleanup vector is asserted at execution granularity. Publish this blast-radius and concurrency policy; a root-created per-execution unit (f-execution-containment) makes the Linux proof exact.
  4. **Honest policy fields.** State in `swarma-workplace-exec/1` that on the OS-user backend `write scope` is the UID's writable set and `network mode` is the per-UID firewall; remove or re-label fields the backend cannot honour. Host-local workplace jobs are a new qualified backend, not automatic support from the dispatcher subset that refuses remote targets.
  5. **User CA.** Name the custody of the user CA key; the signing service issues a certificate only for the principal of the authenticated workplace that requests it.
- **Expected benefit:** Audit and replay claims become tamper-evident against the worker; "no surviving descendants" becomes provable through the journaled stop and confirmed absence the rest of the platform already uses instead of a bespoke process-group lease; network and write claims in the workplace policy become honest; one fewer component holding policy authority under an untrusted UID; reuse of launcher, receipt, `exec.stop`, F-10 observation, F-13 scope and F-2 maintenance for remote jobs; the login-shell contradiction is closed at the source.
- **Risks and costs:** The helper's closed `user.create` schema gains an account class (shell, enforced requirement); a small service-to-runner protocol; one launcher start per workplace runner or per job; remote workplaces become admissible only after helper v1 on the host, which postpones variant A on hosts without slice 2 (variant A is a donor-side posture and never exempted our side). Per-job cancel in the runner shape is best effort by design. Does not challenge the 2026-10-07 decision (remote workplace = an OS user on our host, SSH towards the host, Remote Bash and Mailbox only), D-DONOR-PROVISIONING or D-EXECUTOR.
- **Affected specs:** CIP-0009 D4.7, D5, D12 and test plan; `protocol/remote-worker.md` publication register (`swarma-rb/1`, `swarma-workplace-exec/1`); trust-and-isolation.md §7.5–§7.6; user manager §§4.1, 4.3, 8, 12 (workplace account class, activation gate, loopback row); dispatcher §§8.4, 12, 14, 16 (workplace allocation class and backend gate); book chapters 11 and 14.
- **Confirmed-by:** `macmini_swarma-review-2_opus`, answer `$ZKz1O1yw005vHH3CAvnymO1jfal9KJHaWQYUg1guaxw` (executor UID, same-UID job, the `nologin` contradiction, execution-granularity cleanup); `macmini_swarma-review-2_astra`, answer `$Oo7VwH-RUeAOxYDGQCasqJ9ffeFX895kGJXhDInNuxA` (service-owned control/evidence boundary, missing account shape, egress at activation, new qualified backend); `ivan-network-profiles`, answer `$dQmAokrEQMNDPjqxq3p23lXRsJPgPvJBBzLgs4xHEIA` (egress gap and gate at activation, exec-class file tools, login-shell vector, loopback row); all in `#swarma-review-2`, topic `f-workplace-executor-uid`, 2026-10-12. Proposal `$19dnomeGAhZb-l_qeXlGKo3CBPJ0-Lon1o9VEFIsgw0`; restated proposal `$0Y-frgnHY816k6iuM5tJ8swQY361DfW4fNeQa23ADUw`.
- **Status:** proposed.

## F-20 — Give the session host stop and successor-start authority through an owner-authorised, session-scoped permit

- **Lens:** trust and threat model (authority and principals); cross-spec consistency; a gap introduced by F-4.
- **Problem:** The session host's own transactions need two dispatcher authorities that the dispatcher does not give its configured session-host principal, and the two specifications disagree on what the host admission permit covers. *Stop:* the session host routes every controlled restart, park of a wedged execution and emergency stop through "request execution stop from the dispatcher through the user manager's `exec.stop`", but the dispatcher's only stop is `cancel`, allowed to the execution's owner or to operators under an unpublished maintenance authority; `host_start` is the host's only operation. *Replacement:* the session host then has the host "admit a new execution and request a fresh agent-side runner through `host_start` and the host admission permit", while the dispatcher binds the permit to one `(logical_session_id, execution_id, controller_epoch, op_id)`, created when that execution's start was admitted, and says replacement "uses a new one and fresh admission"; a permit for execution E cannot admit E+1, and nothing names who signs the successor's start. The book records the same hole for reboot bring-up. Both ways to close it as written harm the trust model. If the host becomes the `start` caller, it needs a caller chain with `agent.spawn` and `credential.lease` over every account any hosted session may use, that chain becomes the binding's caller dependency, and the orchestrator drops out of its sessions' ancestry: revoking a compromised orchestrator no longer cuts its hosted sessions (the property F-3 established), and a compromised host, the component that touches every session's input and the carrier, holds a node-wide spawn and lease grant. If instead the original owner must re-sign every replacement, wedge recovery, crash recovery and reboot restore need the orchestrator online, and a standing session cannot outlive the execution of the orchestrator that started it. This is a published-contract gap, not an implementation defect.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`: §8.1, line 342 (`cancel`: the execution's owner; operators only under unpublished maintenance authority) and line 351 (`host_start` is the only host operation); §12, lines 412–414 (permit bound to the four values, created when that start is admitted; "actual execution replacement uses a new one and fresh admission"; the dispatcher rechecks the original admitted caller authority at `host_start`); §11, lines 402–403 (a restart needs fresh authority); §1.2, line 61 (the host listed among callers); §3.4, lines 102–105 (a caller chain needs `agent.spawn` and `credential.lease`; it becomes the binding's caller dependency) and line 108 (delayed and recovered work re-checks the stored request); §5.2, line 245 (descendants retain the requester); §5.3, line 258 (one claim per allocation, `agent_busy`); §16, question 3, line 468. `diagrams/v1-daemon.puml`, lines 57–71: the permit is created at an admitted start whose caller is not drawn.
  - `platform/curator-session-host/spec/session-host.md` r8 @ `3a253016`: §3.2, line 154 (stop: "the dispatcher, through the user manager's `exec.stop`"); §3.3, lines 169–175 (`host_start` and the permit "created when a start with the session-host executor is admitted"); §3.5, lines 205–207 (restart: request execution stop from the dispatcher; "admit a new execution and request a fresh agent-side runner through `host_start` and the host admission permit") and line 211 (emergency stop); §3.7, line 227 (recovery: "the dispatcher for admitted starts, execution stop, absence and cleanup"); §7, question 2, line 302.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`, §4.7, line 218 (`exec.stop` is allowed to the dispatcher for generations it created).
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`, §7.1, line 347 (the binding carries the caller's chain as the authorization dependency).
  - Book `wiki/book/swarma/ru/07-host-sessiy.md`, lines 33–41 (the five-step start), 75 (the host asks the dispatcher, which calls `exec.stop`), 79 (the project registry as the automatic restore requester); `13-scenarii.md`, line 9 («Кто именно просит после перезагрузки, спецификация пока не называет»).
- **Proposed change:** Make the logical session the unit of owner consent and keep every physical start under its own F-4 fence.
  1. **Owner-signed session lifecycle authorisation.** The owner's admitted `start` with the session-runner executor explicitly admits successor executions for that logical session: same allocation and generation, the stored plan verbatim, bounded by the owner's grant window and the allocation's lifetime; its member format is publication work. It is retained in `input/1` and the session record. A one-start request without it admits no successor.
  2. **Session-scoped permit.** Under that authorisation the dispatcher issues one durable permit for `logical_session_id` that governs many uses; each physical start keeps its own `(execution_id, controller_epoch, op_id)` claim, fence withdrawal and same-effect/receipt interlock exactly as F-4 states. The host never acquires a caller chain; the binding's caller dependency stays the orchestrator's, so F-3 ancestry and revocation hold.
  3. **`host_stop`.** The configured session-host principal may request a stop of the permitted execution through the dispatcher's journaled E-stop path (`exec.stop`, confirmed absence, F-13 scope). It is recorded as host-requested, distinct from owner `cancel`, and confers no start authority.
  4. **Successor admission rows.** A successor `host_start` is admissible only under the owner's lifecycle authorisation of item 1; the dispatcher's delayed-work re-checks (§3.4) are then applied to it and never substitute for that consent, so a replayed one-start request admits no successor. In addition: idempotent per `(logical_session_id, op_id)`, so a replay after a host or dispatcher crash returns the same successor and never a second; the previous execution's claim is confirmed absent first (`agent_busy` otherwise); the stored plan is reused unchanged and the host supplies no plan bytes (pin or posture divergence is a new owner admission, as session-host §3.5 already makes divergence a new human operation); the owner principal is still active, so sessions owned by a retired one-shot orchestrator are not restartable and the spec says so; a fresh `revocation.check` with context `start` and distinct effect IDs through the record ID; successors never extend an ordinary allocation's lifetime, and for ordinary work the owner's lifecycle authorisation carries a cumulative or anchored restart budget (a successor count or a total runtime anchored at the first start), so a restart loop cannot obtain repeated fresh runtime windows; standing executions keep their owner-decided no-runtime-limit rule.
  5. **Withdrawal.** Durable and serialised with successor admission under the dispatcher lock: owner `cancel` or `retire` (no autonomous repeat), revocation or expiry of the owner's chain, the operator's signed standing-retirement record, or R-MAINT; unknown permit state keeps successor starts closed; controller-only re-adoption keeps `execution_id` and needs no permit action.
  6. **Reboot requester.** The permit does not choose who asks after a reboot; the host and the project registry remain the candidates of the open question, and whichever is configured acts only within the owner's lifecycle authorisation.
- **Expected benefit:** One authority object covers a session's execution lifecycle under explicit owner consent; no node-wide spawn or lease grant for the host; the orchestrator stays in every hosted session's ancestry; restart, park, emergency stop and reboot restore become possible as the session-host specification already writes them; the unpublished maintenance authorisation is no longer the only operator stop path for a single hosted session.
- **Risks and costs:** Stored authority is reused for successors, within the owner's explicit lifecycle consent and bounded by its grant window, allocation lifetime and a fresh revocation check per use. A durable permit record needs its own recovery rows (unknown permit state stays closed). `run/1` must record host-requested stops distinctly. Sessions whose owner was a one-shot orchestrator are not restartable after its retirement. Refines F-4's permit binding by making the execution and operation values per use of the permit rather than its identity; it does not reopen F-4's launch authority, D-GOALS or D-IDENTITY.
- **Affected specs:** dispatcher §§3.4, 4.2, 8.1 (`host_stop`), 12, 14, 15 and 16 question 3; session host §§3.3–3.5, 3.7 and 7 question 2; `diagrams/v1-daemon.puml`; helper §4.7 (the caller stays the dispatcher); book chapters 7, 9 and 13.
- **Confirmed-by:** `macmini_swarma-review-2_opus`, answer `$5gnJdPD-KX2ODUZZedc-KNfIF9QDAEYm_PTNdmpNmoY` (no host stop; the per-execution permit cannot admit a successor; successor reuse sound under five recovery conditions, adopted in item 4–5); `macmini_swarma-review-2_astra`, answer `$aZFUn8Kn0gQXmPiz-X7DqyRzMES52B32WSThdIUgkao` (missing host-stop surface; successor admission needs explicit owner lifecycle authority rather than delayed-work reuse alone, adopted in item 1; reboot requester left open, item 6); both in `#swarma-review-2`, topic `f-session-permit-scope`, 2026-10-12. Proposal `$TE3_k7rPlt_m4y9HysT7vZ4P8-uhYxp65OE5vBDGNmo`.
- **Status:** proposed.

## F-21 — State the time assumption and make wall-clock steps unable to destroy state or revive authority

- **Lens:** reliability and recovery; time as an input to irreversible effects and to authority.
- **Problem:** No module spec states a time source or clock assumption. A search of the user manager, dispatcher, broker and session-host specs and the launcher §10 for clock, NTP or monotonic finds nothing. Wall-clock comparisons nevertheless drive both destructive effects and authority. The default time sources are unauthenticated NTP (macOS `timed`, Linux `systemd-timesyncd` or `chrony` without NTS), and they step the clock on a large offset. Depending on the host's time configuration, a rogue or on-path time source, an operator's manual date change, a VM resume or a wrong RTC at boot can therefore move it. This is a contract gap for qualified clock faults, not a demonstrated attack or runtime defect.
  - **A forward step destroys state.**
    - The dispatcher's one-minute sweep retires every ordinary kept allocation whose lifetime the step crosses (24 h default, 7 days maximum). Under F-1, retirement deletes the home, uncommitted work included.
    - The broker removes every binding whose window the step crosses, for good: "Expired bindings are removed by the broker", and a removed binding is never reactivated by replay.
    - Correcting the clock afterwards restores nothing. Every grant window also closes, so every lease and renewal refuses node-wide. That part fails closed.
  - **A backward step revives authority.** Grant windows, leaf and delegation windows and lease `authorized_until` are evaluated against wall time only. After a backward step:
    - an expired caller leaf, orchestrator delegation or agent leaf verifies again;
    - an expired but not yet removed binding leases again;
    - `authorized_until` moves into the future.

    Revocation is unaffected, because it uses records, not times. But expiry is one of the two ways the design ends authority, and F-14's renew-ahead assumes expiry is monotone.
  - **Reversible effects.** False wedge detection, premature or late Codex refresh, and runtime-deadline stops are reversible or fail closed. They are not the finding.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`:
    - §3.4, line 104: leaf windows;
    - §3.5, line 120: allocation lifetimes;
    - §5.4, line 273: an expired ordinary allocation is retired;
    - §7.2, line 329: the one-minute sweep enforces lifetimes and runtime deadlines.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`:
    - §6.2, lines 283 and 286: windows are checked against the current time on every edge;
    - §7.2, lines 362–364: expired bindings are removed and never reactivated;
    - §8.3, line 421: `authorized_until`;
    - §9.4, line 491: the 48 h refresh window.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`, §4.4.1, line 186: retirement deletes the home.
  - `platform/curator-session-host/spec/session-host.md` r8 @ `3a253016`, §3.7, line 226: wedge deadlines.
  - The only time-integrity rule in the sources is in `swarma-review/context/swarm-platform-architecture/vision/contracts/admission-and-delivery.md` @ `e5781c8`, §5, line 90. It keeps a monotonic high-watermark clock per store and rejects `issued_at` more than 2 minutes in the future. No module spec carries a comparable rule.
- **Proposed change:**
  - **State the time assumption.** The installer section names an authenticated time source (for example NTS) or an operator-controlled one.
  - **Watermarked authority time.** The broker and the dispatcher each keep a durable high-watermark of wall time observed under established time confidence, reusing the ADM device.
    - **Both directions narrow.** Expiry checks (`expires_at`, `authorized_until`, binding expiry) evaluate at `max(now, watermark)`. `not_before` checks evaluate at `min(now, watermark)`. A wrong step in either direction can then only narrow authority. A forward watermark alone would open future `not_before` windows early, so the watermark is never applied to `not_before` with `max`.
    - **Ordering.** Detect-and-hold and time-confidence validation, below, precede both authority evaluation and any advance of the watermark. The watermark never advances on untrusted time.
    - **Reset.** A forward step makes the watermark sticky: after a bad step is corrected, authority stays closed until real time catches up. Resetting a poisoned watermark is therefore an explicit operator act, taken after the incident confirms the clock. A reset preserves evidence established under trusted time, so what expired then stays expired. Confirming the correct wall clock is not consent to revive genuinely expired authority.
    - **Limits.** These rules are a proposed contract for qualified clock faults, not a proof against arbitrary clock behavior.
  - **Destruction gated on monotone elapsed time.**
    - Expiry-driven `user.retire` (home deletion) and expiry-driven binding removal require both wall-clock expiry and accumulated boot-inclusive monotonic elapsed time (`CLOCK_BOOTTIME` on Linux, continuous time on macOS) of at least the lifetime, counted from activation.
    - The elapsed time is accumulated durably at each sweep, because those clocks reset at reboot. Downtime is not counted, which can only delay destruction.
    - An expired binding is already unusable, so its removal can wait.
  - **Detect and hold everything else.** This is the primary cut. A grace period alone only delays loss.
    - **One policy.** A single platform time-confidence policy is published and reused by every service, with no per-component prompts.
    - **Within a boot.** Components compare wall-time and monotonic deltas between sweeps. The pair is comparable only inside one boot epoch; it cannot certify the initial RTC or slow drift.
    - **On a step.** A backward move, or a forward move beyond tolerance, raises an incident and holds time-based evidence reclamation.
    - **After boot.** Destructive time-triggered effects, and any watermark advance beyond tolerance, hold until an authenticated sync or an operator confirmation establishes confidence.
    - **While time is untrusted.** New admission, leases and renewals refuse, and retained bindings do not keep issuing credentials.
    - **Unaffected.** Explicit stops and operator retirements keep working.
  - **Qualification.** Cover:
    - a forward step beyond the longest lifetime: no retirement or binding removal before monotone elapsed time;
    - a backward step across a grant expiry: no revived lease;
    - a VM resume;
    - a wrong RTC at boot.
- **Expected benefit:**
  - One clock fault, accidental or induced, can no longer mass-delete agent homes or bindings, or revive expired authority.
  - The time assumption becomes explicit and testable.
  - No new service is added; the existing sweep, the ADM high-watermark pattern and the existing incident surface are reused.
- **Risks and costs:**
  - A little durable time bookkeeping per component.
  - After a bad forward step, the node stays fail-closed until an operator confirms the clock and resets the watermark.
  - Destructive expiry is delayed by host downtime.
  - Lifetime and quota decisions, the standing rules and D-* decisions are unchanged.
- **Affected specs:**
  - dispatcher §§3.4, 3.5, 5.4, 7.2, 11, 15;
  - broker §§6.2, 7.2, 8.3, 9.4, 15, 16;
  - user manager §§4.4.1, 11 (cross-reference);
  - session host §3.7 (cross-reference);
  - book chapter 9.
- **Confirmed-by:** `macmini_swarma-review-2_fable`, answer `$ME0vAJVBEuNYBTTkocYSE7akdNlsetjWqI6AzmGwvFM`, room `#swarma-review-2`, topic `f-clock-step`, 2026-10-12.
  - It confirms from the trust lens at high confidence.
  - It names the unauthenticated-NTP lever and the backward-step revival of authority.
  - It adds the high-watermark "now" and the monotone gate for destructive effects, both accepted in `$UJyR1eZfYvJYMavRK7zaI6-KBMCtxpx2Dy62O3muVCc` with the sticky-watermark and accumulation precisions.
  - Partial refutation: the ADM store-epoch rule exists in VISION, but not in any module spec.
  - `macmini_swarma-review-2_astra`, answer `$Ooqt1wUh42zupdwUOQn2S94m63CQWhVZFh4FyqpoiOg`, same topic, confirms at high confidence the missing time-integrity contract for automatic irreversible expiry. Its corrections were accepted in `$9Y8K7Db3cjZnBzDLQxb9RlM-rnO2Qynxz11u4HfMX4I`:
    - a startup time-confidence rule;
    - one shared policy;
    - refusal of new authority while time is untrusted;
    - boot-epoch limits of the wall/monotonic pair;
    - scope limited to qualified clock faults and a contract gap, not a demonstrated attack or runtime defect.
  - Proposal `$clPNHlMeC3dZnG_R9NuXUkwCKUaYHAt0CeExMrAGVT0`.
- **Status:** proposed.

## F-22 — Classify receiver outcomes so `exec.stop` continues under its effect ID while authority-creating retries stay fresh

- **Lens:** reliability and recovery; idempotency; stop convergence.
- **Problem:** Two receiver rules conflict for `exec.stop`.
  - **Replay rule.** "A repeated mutating (caller, request_id) with the same operation and canonical arguments returns the recorded result together with the target's current state" (user manager; the broker has the same rule for bind).
  - **Retry rule.** The same user-manager spec expects `exec.stop` after `processes_remain` to be repeated with the same effect ID and to make progress. The dispatcher repeats it while the termination receipt is missing.
  - **No tie-breaker.**
    - User-manager recovery resumes only interrupted creation and retirement, not stops.
    - The dispatcher's effect table knows only `ok`, `refused` with a code, and `unknown`, so it records `processes_remain` as `refused`.
    - Neither receiver says whether such an outcome is a recorded result or unfinished work, and R-OBS has no wording for it.
  - **Consequence.** An implementation that records `processes_remain` as the result replays it forever, and the stop never converges. This is independent of F-13's signal scope.
  - **Pre-admission rejections.** The same ambiguity leaves open whether a pre-admission rejection leaves a recorded effect, for example a bind refused with `revocation_state_unavailable` during an F-9 fence. Retrying such a rejection must never bypass fresh authority.
  - **Retirement is not affected.** Recovery already resumes it, although its failed forward steps should be named as unfinished recovery.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`:
    - §4.6, lines 202–205: recovery resumes interrupted creation and retirement; the replay rule; observation and retention;
    - §4.7, line 218: `processes_remain`, "and the call may be repeated with the same effect request id";
    - §4.4, line 174, and §4.4.1, lines 185–186: retirement's retry and forward-recovery wording.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`:
    - §7.2, lines 361–362: pending interrupted work and the bind replay rule;
    - §13.2, lines 590–601: the six observation states.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`:
    - §4.5, line 191: effect results `ok`, `refused` or `unknown`;
    - §4.6, lines 212–223: the R-OBS mapping;
    - §7.1, line 316: a new bind needs fresh authority;
    - §7.1, lines 320–321: same-ID repetition of stop and cleanup.
- **Proposed change:** Publish one outcome table per receiver operation (create, bind, launch, stop, unbind, retire). Map it onto the existing six R-OBS states; add no new state.
  - **Transport uncertainty** maps to unknown or unavailable. It is observed and never relabelled as pending.
  - **Pre-admission rejection** records no receiver intent. Any retry is a fresh admission with current permission, expiry and revocation checks, so the fresh-authority invariant for new binds holds.
  - **Unfinished admitted work** is a durably accepted intent and maps to pending.
    - `exec.stop` with `processes_remain` continues under the same ID. It revalidates the generation and current-execution fence (F-13) and never signals a later execution after success.
    - Failed forward retirement steps are unfinished recovery.
  - **Terminal result** is recorded and replayed with the target's current state.
  - **Dispatcher mapping.** The dispatcher maps unfinished admitted work to its pending handling, never to `refused`.
  - **Continuation rules.**
    - A continuation repeats the original canonical arguments exactly, including `exec.stop`'s `grace_seconds`. No tunable is excluded from the digest, so a changed argument remains `request_id_conflict`.
    - The receiver itself enforces F-13's latest-receipt fence on every continuation. Once a later execution's receipt exists, a continued stop of the earlier one refuses to signal.
    - Continuation never creates authority. Classes 3 and 4 can only narrow: a continued stop or unbind. Only a fresh admission (class 2) can create authority, and it re-checks permission, expiry and revocation. A principal whose grant has lapsed may continue its own stop, never its own bind.
- **Expected benefit:**
  - Stop converges through the retries the specs already prescribe.
  - Replay safety and the fresh-authority rule are preserved.
  - The idempotency contract becomes mechanically checkable, one row per operation.
- **Risks and costs:**
  - A classification table plus qualification rows: retry after `processes_remain`, replay after success, and retry after a pre-admission rejection whose authority has since been revoked.
  - Replay safety is not a general property of the classification. It follows from the journal, current-authority and same-effect reconciliation rules being correct. A completed or never-authorized operation must never become a fresh pending mutation just because its class changes.
  - No owner decision is challenged.
- **Affected specs:**
  - user manager §§4.4, 4.6, 4.7;
  - broker §§7.2, 13.2;
  - dispatcher §§4.5, 4.6, 7.1;
  - F-10 observation wording in all three.
- **Confirmed-by:** `macmini_swarma-review-2_astra`, answer `$AfJKsnEBq0ukSp1BMFwJCwwqDTIm1nISg8OMumb3gz4`, room `#swarma-review-2`, topic `f-retryable-outcomes`, 2026-10-12.
  - It confirms at high confidence that a completed receiver result must be distinguished from an unfinished accepted stop, with same-ID continuation and fence revalidation.
  - It refuses a blanket rule that transient refusals progress without fresh authority. That claim is withdrawn, and the four-class table using the existing states was accepted in `$v1yOY-y0jAb6koU_Gthgj9mps4g6lr5l1L-DcBCaPFA`.
  - `macmini_swarma-review-2_fable`, answer `$c_1lpqcM4S_TRLxLurCRn6960mlMX34E55jNFzbAbt8`, same topic, confirms the narrowed entry from the trust lens. Its three replay-safety points are folded into the continuation rules:
    - identical canonical arguments;
    - a receiver-enforced latest-receipt fence;
    - no authority created by continuation.
  - Astra's qualification of the replay-safety sentence, `$epKuUyWhATnl0aSMaSPirYIk95dw5o3Cw85UXug0Q7s`, is applied.
  - Proposal `$6thKsqEGFnAkIEisxpXM9GNbQTsOCLH6EyOXVj8eQLw`; self-narrowing `$L4AZ6kyXFqvUVCWLIIYI-KlEXOINfQyoocArQKKEUDI`.
- **Status:** proposed.

## F-23 — Keep the broker v0 root key and the operator principal out of any account that runs agent sessions

- **Lens:** trust and threat model; custody of the root of trust; cross-spec consistency with the owners' trust framework.
- **Problem:** The platform's most valuable key, and the principal that may use it, sit in the one account that still runs unconfined agent sessions; the specifications do not state that these may not overlap. The broker's v0 trust root is "a local software key of the operator; `curator broker grant …` signs with it"; operators and account owners are "unmanaged principals (people's own OS accounts acting as operators or owners)". Grants, revocations, enrolment, `unbind` and `revocation.put` are accepted from that configured operator UID, some of them without any root signature; the helper's `operator` role, which may retire any account including protected services, is likewise a UID in root policy; and the dispatcher's operator-signed records (team bring-up, standing retirement, maintenance stop) will be signed by an operator key with unpublished custody, by default in the same account. That account runs agents: the book keeps interactive harness sessions "под твоей учёткой" until SH2+, today's board spawn runner and its children run under the operator, and Decision 0021 makes `curator run` under the person's account the one interactive door. The book's privilege table ("человек-администратор … ничего из платформы не запускает") contradicts this. A prompt injection in any session of that account can read the root key bytes and sign grants or revocations offline in the public format, call `unbind` or `account.enrol` as the configured operator, and, where the operator's sudo rule allows it, retire any account. Every downstream control (narrowing chains, F-3 ancestry, F-8 verdicts, F-9 fenced restore) rests on this key. The owners' trust framework of 2026-09-25 states the premise this violates ("Agents run under an OS account of their own. The operator's account owns the stores, the keys … Secrets live only in the executor's environment") and labels pre-TR6 controls as guardrails; the book's principle 1 («агент не держит секрет») is stated as complete for identity keys. This is a missing safe staging condition for slice 0, not a demonstrated key leak, and it does not claim that every staged exception is forbidden.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`: §4.3, line 138 (the v0 root is the operator's local software key, used by `curator broker grant`); §4.2, lines 131–132 (operators and owners are people's own OS accounts, pinned by UID and directory identity; every enrolling principal becomes an owner); §6.4, line 309 (a key may be revoked only by a root or operator key); §13.2, lines 577–581 (`account.enrol`, `grant.put`, `revocation.put`, `unbind` accepted from owners/operators; no root signature needed for `unbind`); §14, line 617 (`curator broker grant` from the operator's shell).
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`: §3, lines 83 and 89 (callers by UID; `operator` may run all helper operations including retiring protected service accounts); §2, line 36 (the `NOPASSWD` sudo rule shape, shown for the service account).
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`: §5.5, line 295 (operator-signed team description); §5.4, line 279 (operator-signed standing retirement); §8.1, line 342 and §11, line 402 (explicit operator maintenance authority); §16, questions 8 and 12 (operator signature formats unpublished, custody unstated).
  - Book `wiki/book/swarma/ru/09-zapusk.md`, line 141 («твои интерактивные сессии работают как сейчас, под твоей учёткой») and line 34 (the board's spawn runner and today's children run under the operator); `03-polzovatel-na-agenta.md`, line 142 (the human administrator "runs nothing of the platform"); `04-klyuchi.md`, line 15 (broker root = the operator's software key); `02-sistema-celikom.md`, line 23 (principle: the agent holds no secret).
  - `wiki/decisions.md` @ `17569de`: lines 254–260 (2026-09-25 trust framework: agents under their own accounts, the operator's account owns the keys, secrets only in the executor; "until then, these rules are guardrails", delivery TR6); line 170 (principle (a): only a key requiring a person's presence confirms); lines 134–135 (2026-09-24: widening entries take effect only after the operator's OS user authentication, "an agent cannot answer that prompt"; the CLI refuses widening changes from inside an agent session).
  - `curator/curator-spec/decisions/0021-sessions-enter-through-curator-run.md` @ `601cbb0` (`curator run` under the person's account is the interactive door; the agent-account mode is the later amendment).
- **Proposed change:** Change custody first, then gate acts; mandate neither new hardware nor a signature-algorithm change.
  1. **A no-harness operator principal.** The v0 root key, and the operator keys that will sign `team/1`, standing retirement and maintenance records, live at mode 0600 in a dedicated operator account that never hosts a harness session, with protected binaries and configuration. That account, not the person's interactive account, is the configured broker operator and account owner (broker §4.2) and the helper `operator` UID, so the second path (direct operator-UID calls such as `unbind` or `account.enrol` that need no root signature) is closed as well. The person's interactive sessions are agents of their own account. A dedicated signer service is an alternative only with the same explicit intent/authority boundary.
  2. **A non-cacheable authenticated transition.** The operator account is reached only through authenticated sudo: no `NOPASSWD`, `timestamp_timeout=0`, so a cached ticket in the person's terminal cannot be reused by a tool call. The same authenticated rule replaces any `NOPASSWD` entry for the helper `operator` role; `NOPASSWD` stays reserved for the dispatcher service account's helper and launcher rules.
  3. **Confirm the act, not an interval.** Widening acts (grant issue, enrolment, `team/1`, explicit home retention) confirm the exact privileged action and its canonical content at the time of the act, per the 2026-09-24 operator-file rule, and the CLI refuses them from inside an agent session. Narrowing acts (revocation, disable) and reads need only the authenticated transition, so emergency revocation stays quick from any terminal where the person holds the authentication factor; authorised automatic narrowing and service actions keep working without a person.
  4. **Hardware custody as a versioned decision, not a prerequisite.** The Secure Enclave holds P-256 keys only, so Enclave custody of the Ed25519 broker root would change the root algorithm and grant signature format; a token with native Ed25519 keeps the format. Either is a later root-format decision; the dedicated account is the slice-0 cut.
  5. **State the consequences.** Operator acts become human-presence acts: F-14 renew-ahead and F-2 maintenance need a person before the horizon or a pre-authorised, bounded, non-widening re-grant within a published existing delegation, never an inferred infinite re-grant; loss of the operator account or key follows F-9's root replacement, never a key restore into a session account. Replace the privilege table's "runs nothing of the platform" row with the truth: the operator principal is the root-of-trust principal until the keeper exists, and no harness session runs under it.
- **Expected benefit:** The one key everything narrows from leaves the reach of every agent process, and so does the principal that may call the broker and helper as operator; prompt injection in the person's own session can no longer mint, widen or revoke authority, enrol credentials or retire accounts. No new component: it reuses the operator-file confirmation rule, the platform's existing refusal of widening acts from agent sessions, and ordinary sudo policy. The book's privilege table becomes consistent with the trust framework.
- **Risks and costs:** One authenticated transition per operator act, plus a confirmation of content for widening acts; `status` and other reads by the person also go through the transition unless a read-only principal is configured. A dedicated account adds one principal to pin (broker §4.2) and one sudo rule to qualify. Headless renewal and maintenance need a person or a published bounded re-grant. Does not challenge D-* decisions or Decision 0021; it refines broker §4.3's custody of the v0 root and the helper's operator sudo policy, and keeps the v0 Ed25519 format.
- **Affected specs:** broker §§4.2–4.3, 13.2, 14, 15; user manager §§2–3, 11; dispatcher §§5.4–5.5, 8.1, 11, 16 (operator signature custody); book chapter 3 privilege table, chapter 4 key table, chapter 9; decisions.md cross-reference to the 2026-09-24 and 2026-09-25 rules.
- **Confirmed-by:** `macmini_swarma-review-2_opus`, answers `$LWL6b2wii3UMQEuo59dZVKqhd9hz2ogn9gcqdwCaHmc` and `$sCl5PwYLtmJZWAq8Zf-u_uGxPTBvkn51dnJRP4fCLGM` (item 1 at high confidence; a command gate protects the command, not the key, so custody must change; dedicated account with `timestamp_timeout=0` keeps the Ed25519 format; Secure Enclave would be a root-format change; F-14/F-2 become presence acts; key loss uses F-9 root replacement), adopted in items 1–2, 4–5; `macmini_swarma-review-2_astra`, answer `$JHUJDhLLfgRnZJ7UX_7dsA6qcMDUg_qtPky1D-19NGY` (protect both signing custody and the configured operator/owner roles; confirm the exact act and content, not an unlocked interval; no new hardware or algorithm change; a missing staging condition rather than a demonstrated leak; the 2026-09-24 rule targets widening, narrowing stays immediate; F-14 renewal within a published delegation or waits for the operator), adopted in items 1, 3–5 and the problem statement; both in `#swarma-review-2`, topic `f-operator-root-custody`, 2026-10-12. Proposal `$nyDR_47u-Dtd2J4lSnWYquNXFF-cgelVUC3C_z2xgn8`; restated proposal `$Mb04gGBdNpA4b2x8GiWv9GL406d6Nhj5gS4zshZW3jg`.
- **Status:** proposed.

## F-24 — Give the platform's service accounts an egress policy, with the proxy as the only sink

- **Lens:** trust and threat model; network surface (uncovered in cycle 1); least privilege for the accounts the design trusts most.
- **Problem:** The per-UID kernel firewall is specified for agent accounts only. The user manager states its intent as "an agent account reaches the network only through its network profile's local proxy" and `fw.apply` takes an agent generation; the trust contract's network rule and the book's closed-network section speak of agents; the privilege tables give the broker, dispatcher and session host "own unprivileged user" and say nothing about their network. The broker spec says "the broker opens no network listener" and calls itself minimal ("no network listener, no plugins, no shell-outs except the approved Codex executable"), but its outbound side is unaddressed, and it needs outbound: the enrolment ceremony and every refresh run the approved Codex executable under the broker UID against the vendor. The dispatcher and the session host need no network at all. So the account that holds every enrolled credential, and the accounts that see every plan, input and transcript, have unrestricted egress by omission, while the accounts the design distrusts are the only ones fenced. A compromised broker daemon or vendor child can send its store anywhere; a compromised dispatcher or host can phone home. Two further facts make per-UID packet rules insufficient on their own: install-time rows are written once and never re-verified, so a ruleset rewrite or `pf` disable removes them silently; and on macOS name resolution leaves the host as the root `mDNSResponder` daemon, not as the calling UID (on Linux likewise through `systemd-resolved` when `nss-resolve` is used), so a "deny all" account can still leak data by resolving names under an attacker's domain. The user manager and launcher are not part of this gap in the same way: they run as UID 0, which is shared with host services, so a per-UID row cannot express a policy for them. This is a gap in the published threat model, not a tested exploit.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`: §8, line 310 (intent scoped to agent accounts), lines 306–308 (`fw.apply {generation, …}`), line 311 (the parent anchor's position and `pf`'s enabled state are verified on every agent apply), line 312 (support matrix lists DNS as a row to evidence), line 314 (the proxy runs under a trusted service account; the allow list holds only that destination); §3, lines 85–89 (closed role policy; no service-profile operation); §11, line 333 (the installer writes the parent anchor once); §4.4.1, line 190 (the daily root timer owns only the metadata sweep).
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`: §3, line 96 ("opens no network listener"; nothing on outbound); §12.3, line 558 (minimal: no listener, no plugins, no shell-outs except the approved Codex executable); §9.2, line 470 and §9.4, line 491 (device login and refresh run the approved executable under the broker UID); §8.2, line 404 (approved vendor endpoint list for binding checks, which is not the login endpoint set); §9.4, line 493 (`refresh_failed_transient` with backoff).
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`, §5.3, line 265 (egress mentioned only for the harness) and §13, lines 422–426 (security section without a network statement); `platform/curator-session-host/spec/session-host.md` r8 @ `3a253016`, §3.1, lines 133–137 (no network statement).
  - `swarma-review/context/swarm-platform-architecture/vision/contracts/trust-and-isolation.md` @ `e5781c8`: §5, line 45 (per-UID firewall for agents), lines 51–59 (privilege table without network rows for services).
  - Book `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, lines 122–126 (closed network for agent accounts) and 132–142 (privilege table).
  - `curator-network-profiles` main, `docs/integration-contract.md:81,87` and `docs/harness-verification.md:12–15` (cited by ivan-network-profiles): Codex 0.159.0 model-client traffic is verified through the proxy; login and refresh paths are not verified; Codex children do not inherit proxy variables (`codex-env-v1`).
  - Platform semantics cited, not tested: `pf` and `nftables` match addresses, resolving a hostname once at load; macOS resolves names through `mDNSResponder`, Linux through `systemd-resolved` under `nss-resolve`.
- **Proposed change:** Treat every non-root platform service account as a principal with an egress policy, as a v1 capability beside the agent rules.
  1. **One published service-profile matrix and lifecycle.** Extend the user manager's v1 firewall contract and the installer with a service-profile row per service account, installed in the same helper-owned anchor or table as the agent rules. The current agent-scoped closed API (`fw.apply {generation}`) and role policy need an explicit extension for service rows; this is a specification change, not configuration. Root-run components (`swarma-user-manager`, `swarma-user-launcher`) get no per-UID row; any process-specific root sandbox is a separate qualified mechanism.
  2. **Deny all egress** for `swarma-dispatcher` and `swarma-session-host`: they speak only Unix sockets, which the firewall does not filter. Loopback TCP is included in the denial; nothing in their specs needs it.
  3. **Broker through the proxy, not per-endpoint kernel rules.** Vendor names sit behind shared front ends with rotating addresses, so a kernel rule per endpoint is both brittle and over-broad (it admits every other tenant on the same address). The broker gets its own network profile and its own proxy listener; its kernel allow list holds that one destination, exactly as helper §8 does for agents, and the proxy allowlist carries the vendor names. The approved Codex executable receives the proxy variables explicitly (Codex children do not inherit them). The login and refresh paths need their own verification rows (proxy honoured, no direct fallback, endpoint set observed) before the broker profile is written: the `credential_binding` endpoint list is not proof of the authentication endpoint set, so until those rows exist the allowlist content is a guess. The proxy service account's own egress is wide by necessity and enforced by the proxy's allowlist: its matrix row is "proxy-enforced", not "deny".
  4. **Lapse detection and response, published.** Service rows and the parent anchor are re-verified at every service start and on a published schedule, not only at install. A missing row is an incident that drops the affected service's readiness and is reported; the response reuses F-15's recovery controls and F-18's process-fate rules. Because checks are periodic there is a detection window; the entry promises detection and a defined response, not continuous enforcement. The daily root timer's authority is not silently widened: the schedule and its owner are published with the rows.
  5. **Name the DNS side channel in the matrix.** Per-UID packet rules cannot be DNS evidence on macOS, because the query leaves as `mDNSResponder`; the same holds on Linux under `nss-resolve`. Accounts behind a CONNECT proxy need no local resolution, since the proxy resolves. For accounts that never need names, the service unit's or launcher's sandbox denies the resolver (the `mDNSResponder` Mach lookup on macOS; no resolver socket in the namespace on Linux). DNS, Mach/XPC and resolver paths are qualification rows, not assumptions.
  6. **State the model in one sentence** in the trust contract and the book: every non-root account under `/opt/swarma` has an egress policy; the only sinks are the trusted proxy (agents and the broker), the proxy's own allowlist, and, later, the bridge's carrier.
- **Expected benefit:** Uncontrolled egress from the highest-value unprivileged account and from the accounts that see every plan, input and transcript is reduced to the proxy's allowlisted destinations; the broker's "minimal" claim gains an enforceable network side; the egress model becomes uniform and mechanically checkable (every non-root UID has a matrix row; the proxy is the single sink). No new component and no new privilege: the installer already writes the parent anchor, the helper already owns the rules and the proxy already enforces allowlists. The claim is bounded: allowed vendor or carrier destinations and local intermediary services can still carry data, so an allowlist reduces uncontrolled egress rather than proving that a store cannot be exfiltrated.
- **Risks and costs:** A v1 capability that depends on the firewall anchor and its per-OS evidence (slice 2); the software-root slice 0 is not disabled by this later prerequisite. The agent-scoped firewall API and installer scope grow by one service-profile contract. Routing the broker through the proxy makes the proxy a dependency of Codex refresh: a proxy outage becomes `refresh_failed_transient` with backoff (broker §9.4). Login and refresh verification rows and the DNS/resolver sandbox are new qualification work. The broker's device-login ceremony relays a URL to the person's browser, which runs under the person's account, so the broker rule does not block it. Does not challenge any D-* decision; it extends an existing mechanism to the accounts the design trusts most.
- **Affected specs:** user manager §§3, 8, 11, 12 (service-profile rows, scheduled re-verification, DNS clause); broker §§3, 9.2, 9.4, 12.3, 15.2 (egress statement, proxy route and dependency); dispatcher §13 and session host §3.1 (deny-all statement, readiness); curator-network-profiles (broker profile and login/refresh verification rows); trust-and-isolation.md §5 privilege table; book chapter 3 closed-network section and privilege table.
- **Confirmed-by:** `ivan-network-profiles`, answer `$LRMsDy1qysFpR65DeApet5WP9KtusYLTFYLsxMG82Z0` (item 1 confirmed; proxy route with own listener and login/refresh rows qualified first; the proxy account as "proxy-enforced"; the DNS side channel per-UID rules do not see), adopted in items 3 and 5; `macmini_swarma-review-2_opus`, answer `$VRetOlUMQ0_QfFpuRKMBsd12rOXBiW_fkVxlc3ATYqk` (item 1 at high confidence; install-time rows lapse silently, so re-verify and fail closed as part of readiness; the proxy becomes a refresh dependency), adopted in item 4 and the risks; `macmini_swarma-review-2_astra`, answer `$ou6V5N1hZ5vxZh_CMsx-hkYrrIoH61xNy9BHhZOua1o` (no per-UID row for root-run components; one published service-profile matrix and lifecycle as a specification change; bounded benefit claim; qualified DNS/Mach/XPC coverage; a detection window rather than continuous enforcement; a v1 capability that does not disable slice 0), adopted in items 1, 4–5, the benefit and the risks; all in `#swarma-review-2`, topic `f-service-egress`, 2026-10-12. Proposal `$722G-SAR9T4IjxX7lSvzWHYqn3nPQzcJ819Ya0_TJJU`.
- **Status:** proposed.

## F-25 — Bound helper recovery and retiring-home work without replacing the shared lock

- **Lens:** simplicity and operations; privileged control availability; isolation from agent-controlled filesystem work.
- **Problem:** Every helper and launcher operation shares one exclusive lock, and every invocation first recovers interrupted work. Retirement must walk and delete an agent-controlled home before completion, with partial failures resumed forward, but no work bound or scheduling rule separates that traversal from unrelated operations. A large/deep/wide home can occupy a long global critical section; a recovery-to-completion interpretation repeats it before another generation's launch, stop or observation. The launcher's explicit bounded pre-exec requirement has no published way to coexist with this dependency. F-12 removes the broker RPC from retirement and F-15 keeps dispatcher controls available, but neither bounds the privileged filesystem work beneath those controls. This is a contract gap, not a measured denial-of-service exploit or a claim that endless retry is explicitly required.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`, §4.6, lines 201–204: one lock for every operation of both binaries; recovery first; interrupted retirement resumed; observations serialized with that work.
  - The same spec, §4.4.1, lines 185–186: declared-key destruction and the full descriptor-relative deletion walk; failed/partial deletion remains `retiring`. §6, lines 256–260: protected roots, no-follow descriptors, quiescence and quarantine before deletion.
  - The same spec, §7, lines 285–287: acquire the shared lock and recover before launch; the entire pre-exec path must be bounded. §4.1, line 128, and §4.2, line 143: UID hygiene and the durable `retiring` admission fence. §2, line 39, bounds request input, not traversal work.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`, §7.1, lines 320–321, and §7.2, line 329: the existing daemon repeats pending stop/cleanup effects through reconciliation and its sweep.
- **Proposed change:**
  - **Recover by dependency.** Before any operation, validate shared ledger/journal integrity, establish all UID reservations and accounting, and recover prerequisites of that operation. A safely classified retirement of another generation need not finish before an unrelated, authenticated stop, observation or launch can proceed. Shared corruption, unbounded identity uncertainty or incomplete accounting still closes the shared path.
  - **Bound work under the existing lock.** Publish a bounded cleanup quantum and serialized deletion batches, yielding the global lock between batches. Revalidate protected state at each batch. Apply an explicit work/scheduling bound to recovery performed before a requested operation; give both control operations and pending cleanup fair progress. Keep the existing lock and journal rather than adding a collector daemon or another privilege owner.
  - **Keep the same retirement obligation.** The generation stays `retiring`, starts and credential issuance remain refused, and UID/quota reservations and cleanup evidence remain retained. Continue the original admitted retirement effect through existing dispatcher cleanup/sweep retries or explicit operator resumption. The daily root timer currently owns metadata `archive.sweep` only; this change does not silently give it a new operation or authority.
  - **Preserve the deletion boundary.** Quiescence, quarantine and declared-key destruction still precede the walk; every batch uses trusted roots and no-follow descriptors. Only verified full deletion and required account cleanup permit `removed`; there is no automatic retention, early UID reuse or invented success receipt. Pending batches remain unfinished admitted work under F-22. Prefer safe re-walking of the quarantined tree where it makes bounded forward progress; qualify the resume mechanism for deep and wide trees instead of assuming idempotence alone proves progress. No agent-supplied continuation is authoritative, and no new persistent cursor format is mandated.
- **Expected benefit:** A retiring home cannot consume an entire unrelated control operation's critical path merely because of its size. This also reduces the influence of an untrusted workplace's filesystem on other tenants' launch/stop latency. The existing lifecycle and authority owners suffice. Qualification covers a large/deep/wide tree during another generation's stop, repeated deletion failure, crash between batches, same-effect observation, fair cleanup progress, and refusal of admission/UID reuse while deletion is incomplete.
- **Risks and costs:** Work bounds, recovery dependencies and fair progress need publication and per-platform qualification. Bounds describe cooperative work on a functioning filesystem; they cannot promise recovery from a stuck kernel or storage device. Deletion can take multiple invocations, with the existing pending obligation visible until completion. F-1, F-6, F-10, F-13 and the shared-state lock remain intact; no owner decision is challenged.
- **Affected specs:** User manager §§4.1, 4.4–4.7, 6, 7, 12, 14 and recovery/retirement diagrams; dispatcher §7 cleanup references; book chapter 3.
- **Confirmed-by:** `macmini_swarma-review-2_opus`, answer `$N_ixiDaY6FQjqqJsRc8G4AuWkN2qx5DEHnVkTlPni44`, and `macmini_swarma-review-2_fable`, answer `$lzyoXH4abyqW3ne3O6gjncp6Fb8Oc03APwKWn41BHX8`, room `#swarma-review-2`, topic `f-bounded-helper-recovery`, 2026-10-12. Both confirm the gap and separate finding at high confidence; dependency-scoped recovery is adopted. Astra's refinement `$0rcVSTwO0vprS9hz0OEicRIhqzLt0vDa60t_d6gZm1g` preserves the metadata timer's existing scope and requires qualification of bounded forward progress. Proposal `$ZFam8lis1w_bkiXgWL8Hcku03k9LZegSbVsnO87ZZ7o`.
- **Status:** proposed.

## F-26 — F-10's retention gate needs a cross-module decision: receivers cannot establish inadmissibility under the current grammar

- **Lens:** reliability and recovery; evidence retention; checks how F-10 was applied.
- **Problem:** As applied, F-10 lets receivers discard effect evidence only once the original identities are "permanently inadmissible". It explicitly calls time-based expiry insufficient. No component can establish that condition.
  - **The receivers cannot.** Effect IDs are opaque hashes of the dispatcher's caller principal, request ID, record ID, component, operation and attempt. The receivers cannot tell when the dispatcher's record is terminal.
  - **The dispatcher never says.**
    - It reuses an effect ID for as long as the record is non-terminal, and standing allocations may stay pending indefinitely.
    - It publishes no record retention or release rule.
    - Its delayed-work rule refers to a request "validity window" that the published request schemas do not contain.
  - **The mechanism is open in all three modules.**
  - **Consequence.** Receivers either keep journals and tombstones forever, or invent a time window that F-10 forbids and that F-21 shows to be clock-dependent. Realistically, evidence grows without bound: every launch and stop of every standing execution, and every bind and unbind, adds evidence for good.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`:
    - §4.6, line 205: discard only when permanently inadmissible; mechanism unpublished;
    - §4.6, line 207: the append-only audit;
    - §14 question 8, line 370.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`:
    - §7.2, line 367: time-based expiry insufficient; mechanism required before activation;
    - §12.3, line 558: the append-only audit;
    - §18 question 9, line 714.
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`:
    - §3.4, line 108: the "validity window" with no schema member;
    - §4.5, line 191: effect ID derivation;
    - §4.6, lines 212–223: the R-OBS mapping;
    - §7.1, lines 320–321 and 325: same-ID retries; standing records pending indefinitely;
    - §16 question 11, line 477.
- **Proposed change:** Treat the retention mechanism as one joint decision by the dispatcher and both receivers. No receiver can make it alone under the current grammar. Choose between two options, compare them before choosing, and publish the one chosen.
  - **Option A: caller release.**
    - Once the dispatcher has durably recorded a record as terminal, with all its effects confirmed, it sends each receiver an `effect.release` listing that record's effect IDs. Record IDs are random and never reused.
    - The receiver refuses any resent released ID and compacts its replay evidence to a tombstone. Trust rules:
      - The receiver refuses to release an effect it still holds as pending (F-22 class 3). Its own terminality decides, never the caller's assertion.
      - Only replay evidence is compacted, never the append-only audit.
      - A released ID observes as `recorded`, with the outcome class and target identity from its tombstone, never as `not_recorded`. The six R-OBS states are unchanged.
      - Release is a journaled, authenticated, idempotent effect of the original caller principal or an operator, serialized under the receiver's journal lock with any continuation.
  - **Option B: an admission floor carried in the request.**
    - Effect requests carry an admission epoch or sequence, so receivers define admissibility themselves with a durable floor, as F-7 does for remote effects. This changes `helper-op/1`, `launch-op/1` and `broker/1`.
    - A sequence-based floor avoids F-21's clock dependence; a time-based floor inherits it.
    - Either way, the dispatcher's undefined "validity window" (§3.4:108) is published as this floor or removed.
  - **Common rules for both options:**
    - No caller claim erases pending intent, stop or cleanup evidence, or live authorization dependencies.
    - Removing a target compacts evidence only for operations that the target's state already refuses on replay. Effects that create a target (`user.create`, `bind`) are not covered by it.
    - Either the digest-and-result linkage that R-OBS requires is retained, or a reduced observation contract is published.
    - A shared rollback of receiver state remains fenced under F-17.
- **Expected benefit:**
  - The hidden cross-module dependency is stated. With opaque effect IDs, receivers cannot close F-10's gate on their own; the dispatcher and receivers must agree on Option A or Option B.
  - Both options come with their safety rules, so whichever is chosen is checkable.
  - **Storage, stated honestly.** Option A does not bound storage. It keeps one tombstone per released create or bind effect, so growth is proportional to the allocations ever created. That is the same order as the ledger, which already keeps every generation forever, rather than proportional to every effect ever issued. Option B can bound storage only with durable floors plus explicit backpressure and storage limits.
- **Risks and costs:**
  - Option A adds a new wire operation per receiver, with its own durable completion and replay semantics and caller-to-receiver coordination. Its qualification rows:
    - a lost release (evidence is kept, which is safe);
    - a replayed release;
    - a release racing a continuation;
    - a release refused for pending work;
    - observation after release.
  - Option B changes three closed request grammars and needs durable floors.
  - Remote claims keep F-7's floors.
  - No owner decision is challenged.
- **Affected specs:**
  - dispatcher §§3.4, 4.5, 4.6, 7.1, 16 question 11;
  - user manager §§2, 4.6, 14 question 8;
  - broker §§7.2, 12.3, 13.2, 18 question 9.
- **Confirmed-by:** `macmini_swarma-review-2_fable`, answer `$Or0Ly56XuB5cc-gSCjIYuT03b7VtbrMCgdrhotAX0eU`, room `#swarma-review-2`, topic `f-evidence-release`, 2026-10-12.
  - It confirms the gap: no rule lets a receiver establish permanent inadmissibility on its own.
  - It confirms that caller release is sound under four trust rules, all folded into Option A. Rule 3 uses the existing `recorded` state, as accepted in `$msPTzG0GKbU3i4JMtML12Yy_4I3ZmofhwflW9ga6aHM`.
  - **Dissent.** `macmini_swarma-review-2_astra`, answer `$Amyijfm7nFracjiFVX4BFOttmdnlr0lCsRHlwB2H7kQ`, same topic, does not confirm this as a new finding.
    - F-10 already gated the mechanism.
    - Release with one tombstone per effect does not bound storage.
    - A receiver-defined epoch, floor or window is possible in principle with a grammar change.

    Astra recommends treating the topic as design input to the existing F-10 gate. Its corrections are applied in this entry: the storage claim, Option B, receiver refusal in place of the restore claim, and the safety conditions. The owner should weigh the entry as design input with one trust-lens confirmation and one simplicity-lens dissent.
  - Proposal `$gD04ngB4KxrhUvMAfof3l9aQxKXBGSlrz6b6QOF1hHw`.
- **Status:** withdrawn by its author on 2026-10-12. The entry is kept as design input to F-10's publication gate; it is not a finding.
  - **Reason.** Astra's simplicity test, `$tby3ycRQjcYf29phypeU2Mgnpo3cs09kWRf6A6MzJgs`, shows that release makes nothing safely discardable beyond what local compaction already allows. The reasoning is in `$7UyQW6_AXHImRbWkGB4KoYU7igg7GaIL4zy5R9VssM0`.
  - **How the gate can be closed locally, with no new operation:**
    - receivers compact terminal step journals and keep the effect ID, digest, terminal result and target linkage;
    - replays of target-bound effects are refused or idempotent by state: retire, unbind, `exec.stop` (receipt, latest-receipt fence, re-verified absence) and `launch.start` (receipt or rolled-back tombstone in the receipt store);
    - an identity index is kept only for create-type effects (`user.create`, `bind`). It grows with allocations, like the ledger.
    - A request-carried floor is needed only if bounded identity storage is ever required.
  - The safety rules recorded above still apply to any future design. Fable's confirmation concerned release safety, not its necessity.

## F-27 — Bind a child's network profile to its granted Curator profile through a machine-owned policy, pinned at admission

- **Lens:** trust and threat model; network authority (uncovered in cycle 1); cross-spec consistency.
- **Problem:** Under helper v1 an agent's kernel rule admits one destination, its network profile's proxy listener, so the effective egress policy is the proxy allowlist of the *selected* profile. Nothing bounds which profile a caller selects for a child, and nothing ties the applied digest to the policy the listener serves. The caller composes the launch's network profile; `provision` carries an optional `network` member that is caller text; `fw.apply` takes `profile_ref`, `profile_digest` and the proxy port from the dispatcher and verifies only that the listener belongs to the trusted proxy account, so the applied-state record certifies a label, not a served policy. The grant vocabulary has accounts, harnesses, Curator profiles and a window, and no network dimension; the broker constrains network only when an account requires a profile for its credential, so an agent that needs no lease, or already holds its token, is not bounded by the broker. The network-profiles specification, written before per-UID accounts and grants, bounds selection by "host locks and the allowed profile set" of an "operator-owned file `~/.curator/network.toml`", and its vector S7 lets an explicit `direct` override a profiled parent whenever the allowed set admits it. Two contradictions follow under the platform. First, an orchestrator composes its children's plans "under its own agent account, using its own Curator configuration in its home", so the `~/.curator/network.toml` that holds the allowed set is a file the orchestrator itself can write: the bound is self-issued. Second, CIP-0011 says the launch resolves the network profile from the Curator profile through `[bindings.profiles]` in the operator's `~/.curator/network.toml`, but the network-profiles specification defines no such table; its only defaults are `runtimes.toml` `network = "<name>"` and the project `spawn.network.default`, so the derivation route CIP-0011 cites does not exist. A prompt-injected orchestrator can therefore give a child `direct` or the most permissive configured profile, and v1 enforcement reduces to "whatever the caller picked". v0 networking is cooperative by design and claims no containment, so nothing current is broken; this gates slice 2. It is a published-contract gap, not a tested exploit.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/` unless a repository is named.
  - `platform/curator-credential-broker/spec/broker.md` v0.6 @ `a0e6ab95`: §5.5, line 238 ("The caller composes the launch's network profile with curator-network-profiles"), lines 236–239 (network bounded only through an account's requirement; v0 result recorded as declared); §6.1, lines 258–262 (grant body: accounts, harnesses, profiles, window).
  - `platform/curator-dispatcher/spec/dispatcher.md` v0.6 @ `e06fcfee`: §8.1, line 339 (`provision` with `network?`); §3.4, lines 101–104 (vocabulary and intersection without network); §5.1, line 235 (`fw.apply` only at provisioning); §5.2, line 251 (the orchestrator composes children's plans with its own Curator configuration in its home); §16, question 7, line 472 (child profile/environment access open).
  - `platform/curator-host-helper/spec/helper.md` v0.6 @ `e58b0726`: §8, lines 306–308 (`fw.apply {generation, profile_ref, profile_digest, proxy: {port}}`), line 313 ("Order": rule changes for a running account flush that account's existing states), line 314 (only the listener's owning UID is verified), line 315 (applied state publishes the digest the helper was given).
  - `curator/curator-spec/cips/CIP-0011-credential-broker-and-agent-users.md` @ `601cbb0`, §6, line 117 (`[bindings.profiles]` in "the operator's destination-local `~/.curator/network.toml`").
  - `curator-network-profiles` @ `93d0ab8`, cited by its lane owner `ivan-network-profiles` (outside this reviewer's readable sources): `spec/network-profiles.md` N3, line 76 (operator-owned `~/.curator/network.toml`, one machine-owned catalog per plane) and line 105 (the only defaults: `runtimes.toml` `network`, project `spawn.network.default`); N4, line 109 and `spec/contract-appendix.md` §3.7, line 1282 (selection bounded by host locks and the allowed profile set); lines 148 and 215 (the orchestrator selects a profile id from the allowed set); vector S7, appendix line 1421 ("explicit direct overrides a profiled parent within the allowed set"); N7 table and appendix "Binding equality" (`network_profile_drift`: changed profile content under the same name refuses on reattach or resume); no `bindings` table anywhere in `spec/` or `docs/`.
  - Book `wiki/book/swarma/ru/03-polzovatel-na-agenta.md`, lines 122–124 (enforcement means the agent reaches only its profile's proxy; the proxy decides what is reachable).
- **Proposed change:** No new grant dimension; a machine-owned binding, pinned at admission, with a served-policy check at apply.
  1. **Machine-owned binding.** A root-owned, agent-readable policy beside the user manager's configuration maps the admitted Curator profile identity (name plus its lock digest, never the name alone, so a caller-owned profile with the same name cannot redefine it) to exactly one network profile ref and digest; `direct` only where that policy says so. Grant `profiles` already narrow down a chain in the F-3 shape, so egress narrows transitively. A separate `networks` grant dimension is needed only if one Curator profile must ever run under several egresses; nothing requires that today.
  2. **Resolved and pinned at admission.** The dispatcher resolves the binding from that policy at `prepare` and pins ref and digest in `input/1`, so retries and recovery apply the same profile; a policy or catalog change between admission and `fw.apply` refuses through the effect's canonical arguments instead of silently applying a different profile (the platform form of the network-profiles `network_profile_drift` rule). The caller's `network` member is checked against the bound and refused at `prepare` when it differs; caller text and a caller's home are never the source of `profile_ref` or `profile_digest`.
  3. **Served-policy handoff at `fw.apply`.** The proxy service publishes, per listener, the digest of the allowlist it actually serves; `fw.apply` refuses unless that served digest equals `profile_digest`. The applied-state record then certifies the served policy, not a label.
  4. **Narrowing propagation.** A journaled re-apply effect on existing allocations, the network counterpart of F-14's rebind: the kernel half exists (helper §8 "Order" flushes a running account's states on a rule change); the missing halves are the journaled trigger and the proxy side, which must drop or re-check sessions of the old allowlist. Without it a standing agent keeps its old, possibly broader, egress indefinitely.
  5. **Timing.** A v1 (slice 2) requirement that lands together with enforcement; v0 records the selected profile as declared only, and no v0 cooperative check is read as containment.
  6. **Specification repairs.** The network-profiles specification revises N3 (catalog and binding ownership outside agent homes), N4 (the machine-owned binding ahead of host locks and the allowed set) and S7 (`direct` only where the binding says so); these are lane-owned draft decisions revised on the owner's word, not owner D-* decisions. CIP-0011 §6 replaces the nonexistent `[bindings.profiles]` route with this binding. Dispatcher §§3.4, 5.1 and 8.1 and helper §8 cross-reference it.
- **Expected benefit:** Egress authority narrows transitively with the granted Curator profiles through a binding no caller can write; "enforced network" comes to mean "enforced to the profile the operator bound to the granted Curator profile", not "to whatever the caller selected"; the applied state certifies a served allowlist rather than a label; one digest source for `fw.apply`, the broker's network check and the applied state; a dangling cross-reference is removed before anyone implements it; the v0 grant vocabulary stays frozen.
- **Risks and costs:** A root-owned binding policy with an installer/operator lifecycle; the proxy must publish a served-allowlist digest per listener; the re-apply effect and the proxy-side session drop are new publication and qualification work; one Curator profile maps to one egress until a `networks` dimension is ever needed; Curator reads network defaults from the platform location on platform hosts. The network-profiles revision is the lane owner's work. Does not challenge any owner D-* decision.
- **Affected specs:** dispatcher §§3.4, 5.1, 8.1, 15, 16; user manager §8 (binding location, served-digest check, re-apply); broker §5.5 (cross-reference); CIP-0011 §6; curator-network-profiles N3, N4, N7, S7 and the contract appendix; the proxy's listener contract; book chapter 3 closed-network section.
- **Confirmed-by:** `ivan-network-profiles` (owner of the curator-network-profiles lane), answers `$pbgCAnrCoDUaelJlL4NpnShwM42-A0Y6MFFrtE8pp84` (the gap and the network-profiles evidence), `$GJozyeus9dBmX23VlXduBkLWlPsNwVfwumjYEgDXN_U` (the final remedy after astra's challenge: machine-owned binding by profile identity, served-digest check, v1 timing) and `$D1lTBQHcsiMc7qBF0onZ8G7ZwlYYdoRGJdIIRUUrCGE` (pin at admission equals `network_profile_drift`; the kernel half of re-apply exists); `macmini_swarma-review-2_opus`, answers `$POHS7Xy7aH567XweWgEb0syTnxtrcmULloBvrmXLqdQ` (confirmation from the platform specs; rows 2 and 4) and `$TD1d_M7YvCY4pkggHD_1eJ4K_QvJ2Mc5Or6ZcX0Gg2k` (confirms the final remedy at high confidence). `macmini_swarma-review-2_astra`, answer `$FkfWw2l0dVl_4ZmiUr0zbFavEk1a9Qy_0az_WcwUJvo`, narrowed the claim to the explicit-integration gap, proposed the simpler route and the listener handoff, both adopted. All in `#swarma-review-2`, topic `f-network-profile-authority`, 2026-10-12. Proposal `$SbAIPhMcECMR8DYal8Gp2kSB0Ssoxpp2SCp22j7H1pI`.
- **Status:** proposed.
