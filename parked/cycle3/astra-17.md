# astra-17 — cycle 3 parked

- **Seat:** `ivmbp_swarma-review-3_astra-17`; adversarial pass on astra-07's remote-worker lens: CIP-0008/0009/0010, donor variants, bridge, join and retirement.
- **Parked:** 2026-10-13, following ivan-curator's PARK event `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o` in `#swarma-review-3` / `rounds`.
- **Last round:** 14, marker `$_wNDOYrd5j0FEsjOataBkVKV3AZtwYv9Rm1l-f1_wdk`. No new owned finding in the final rounds. No unconfirmed owned candidate or unanswered directed candidate request remains.
- **Scope:** documentation and pinned-source reads only. No builds, tests, rendering, source-repository writes, task-board writes or agent spawns.

## Owned findings

Both files remain **proposed**, pending convener consolidation and owner disposition. Their independent mini-host astra-07 confirmations are included in signed commit `461ab7c`.

1. [Publish a coherent donor network-owner and control-transport table](../../cycle3/findings/f-donor-egress-principals.md). The donor bridge's SSH/join-only egress conflicts with allowing the provider proxy under that UID; token refresh and the qualified Codex loopback control transport also need explicit principal/route assignments. Confirmed by astra-13, astra-16 and astra-07. The pending B provisioner gate limits activation but does not reconcile the written restrictions. Keep provider inference, refresh, native control, and separately admitted web authority distinct.
2. [Reconcile donor P-256 identities with the common envelope signature contract](../../cycle3/findings/f-donor-signature-algorithm.md). The supported A/C Secure Enclave signing key is P-256, while the common envelope grammar and verifier describe Ed25519. Mandatory donor-authored final envelopes need a compatible published suite; project re-signing and an optional generic signature do not resolve the conflict. Confirmed by astra-18 and astra-07, with additional topic confirmation from astra-20. Preserve donor custody and the owner-decided A/C key choice.

## Peer review and consolidation

- Confirmed workplace-relay quiescence: a persistent workplace-UID relay conflicts with account-wide process absence before physical starts and export. Existing SSH ingress and cleanup obligations must remain part of the resolution; do not weaken absence to an execution process group.
- Confirmed donor-provisioner register drift, donor-web book custody/admission drift, and N15 transition-address exclusions. Final UM7 repaired the helper-side web sibling; it was withdrawn and has no finding file to merge with the book finding.
- Challenged automatic authority inferred from the trusted-circle class exception. Final module texts align; the remaining finding must preserve explicit role/grant checks and distinguish owner policy choices from current contradictions.
- Confirmed the C7 priority propagation issue while preserving proposed channel choice and open Muse qualification. The temporary peer-publication race was reconciled without a duplicate push; convener publications own that file.
- Partially confirmed metadata visibility. Managed-generation/start records are not a complete host account/process inventory; macOS path policy remains unpublished, and no total metadata secrecy invariant was established. Consumer phases, own-generation projections and mediated reads remain qualification work. Fable narrowed the published finding accordingly.
- Independently confirmed the retirement and variant semantic deltas in the stale book CIP copies at `$giGziJz_O52sP4bQK1NaC766-PB_rxmIkNMosQg00D8`. Did not claim renderer evidence or that copying current upstream resolves independent upstream defects.
- Added ivmbp confirmation of the book env-executor lifetime finding at `$A3eCpTuBWtlFMj1tSJMp3QfKFrKSdNmeb6beL6GSk-g`: X3 uses a replaced executor as a later reporter; X1 only needs the narrower fresh-invocation/holder clarification. OPEN reauthentication and vendor-token lifetime limits remain.
- The narrow consolidation pass found export-after-expiry and restart-stop-scope already folded into their owners. Book one-shot export, imported CIP copying, exporter admission and refusal disposition require distinct repairs. No additional merge proposed and no finding file deleted.

## Closed probes and open design inputs

- **Cross-UID donor runtime:** not a confirmed defect. The pending B provisioner can install a narrowly authorized service-manager boundary; the documents do not forbid one. Publish caller identity, fixed target UID/service, immutable launch inputs and descendant-stop scope before qualification. Do not borrow project-helper authority.
- **Retired certificate / reused account name:** no conforming bypass established. CIP-0009 D7 already stops renewal, KRL-revokes outstanding certificates and closes established sessions before release. A direct operator helper retirement waives export, not SSH cleanup. Require negative reuse/race cases in the eventual admission/lifecycle contract.
- **Late old-round tools after rework:** a publication/qualification input, not a new finding merely because round/write-fence fields are unpublished. The current-execution and round fence must prevent replay against a freshly materialized candidate C before admission opens.
- **Posture assertions:** the specified supervisor assertion is not kernel attestation; the donor-owner threat limit is explicit. No stronger guarantee was inferred.

## What to examine next

1. Publish and check the donor principal/route table for inference, refresh and exact qualified control transport, including variant C sandbox rules and B's future provisioner.
2. Trace donor signing-suite negotiation from enrollment through canonical bytes to final-envelope admission, retaining replay and donor-authorship properties.
3. Qualify the complete remote join → first export → exact-C review → rework → retire flow under lost/duplicate replies, interrupted export, fresh account generations and late frames. sol-13 owns the scenario walk; coverage and existing negative controls were handed over at `$nwl_95RRxYZUk1rXOPNqWIjAVJe72m5gFkwaDNM-Jd0`.
4. Carry the confirmed relay quiescence and cleanup-export findings into that flow without treating unpublished formats, draft diagrams or proposed hardening as implemented guarantees.

## Evidence baseline

Final reads used curator-spec `a0154285`, user manager `7b59da74`, dispatcher `74687e60`, launcher `f08f566d`, credential broker `df8c7385`, session host `798a321c`, network profiles `359365e`, platform architecture `6b3f983`, wiki `87f387d`, worker-code-transfer `d65cf7f9`, and worker-jail protocol `0635a513b783`. Source mirrors were read-only. The final consolidation read used review `dc14ab7`; the clone was fast-forwarded again before this note.

The convener's PARK message also announces implementation-planning track 2 and `MISSION-IMPL.md`. This note closes the cycle-3 review and preserves the handoff; it records no implementation, deployment or source-change approval.
