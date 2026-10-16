# astra-04 position — snapshots and hosted launches

Status: **round 2 provisional**. PLAN reviewed at `2c7d3a1` (retained at `64b4ae7`); snapshot leaf proposals at signed `64b4ae7`. No implementation/build/provider qualification was performed.

Position: ship the complete additive CIP-0014 materialize surface in the Curator rc.7 cut, including actual-tree verifier and real production-entry evidence. Keep first CIP-0016 activation separate until its published wire, Curator runtime-preparation/verification seam, credentials, Codex policy and all three runtime rows qualify. Do not equate either release with complete D4 migration of native or headless-spawn routes.

| Plan rubric | Score | Evidence and remaining change |
| --- | ---: | --- |
| P1 Traceability | 1 | Own SNAP-* / HOST-HOME-* leaves cite exact sections; PLAN still has H1+/X1+ and provisional seat IDs. Native/spawn D4 obligations were added after my challenge; detailed bounded acceptance still needed |
| P2 Bounded leaves | 1 | Snapshot work now separates codec/verifier, lock, closure, publication, CLI and runtime seam. H1+ still groups preparation/admission and three runtime adapters |
| P3 Negative evidence | 1 | Snapshot leaves pair each forbidden outcome with positive controls and M1–M6 instrument checks. Placeholder consumer/hosted/archive rows still lack complete leaf-level tests |
| P4 Ordering | 1 | Shared-path serialization is explicit. Replace provisional S1→S2→S3 with safe parallel codec/lock/destination development followed by closure/CLI integration; retain final shared-path integration order |
| P5 Unblocking | 2 | v4/Muse consumer handoff and qualification are first; snapshot/runtime/archive work does not delay their implementation. Fresh v0.5.66 source proves shape support is distinct from 1.4.8 qualification |
| P6 Release honesty | 2 | PLAN separates additive Curator tag from all-three-runtime hosted activation, preserves runtime-B and wire gates, and now explicitly leaves D4 route obligations open |

Top risks:

1. Reusing `beginOperationValidated` recovers journals; reusing managedPath permits ancestor link resolution. Both are weaker contracts than materialize requires. See [confirmed helper finding](../findings/snapshot-helper-boundaries.md).
2. Pure snapshots exclude runtime seeds/credentials; hosted needs a complete initial private home plus a protected-input resume verifier. Publish that seam rather than moving copying/auth linkage into the receiver. See [hosted seam](../findings/hosted-home-seam.md) and [HOST-HOME-SPEC](../leaves/hosted-home-contract.md).
3. A full-home initial hash breaks legitimate resume writes; refreshing the baseline blesses changed instructions. Initial materialization, immutable content and native state must remain distinct.
4. Source-home login presence is not destination authentication, especially for Claude's config-dir-bound native login. Setup-token can solve a separately qualified same-user route, but direct-only support does not deliver spawned authentication.
5. Current legacy hosted Claude provenance uses a managed home; current legacy Codex prepares config/auth itself. These are migration inputs, not proof of CIP-0016 exact-plan/snapshot behavior. Factory registration and v4 shape acceptance cannot qualify runtime behavior.

Setup-token design reviewed at `2c7d3a1`, sections 1–9 and ST-01–14:

| Elegance rubric | Score | Evidence / limit |
| --- | ---: | --- |
| E1 New concepts | 2 | Reuses CIP-0010 node, source_ref, binding and injection capability; local ordering carve-out is explicit |
| E2 Reuse | 2 | Reuses machine source/store ordering, frozen readiness row and existing source migration; no generic broker is added |
| E3 Secrets | 2 | Final-child-only material, no snapshots/plan/ax transport, protected custody and child/reload qualification; no passing runtime evidence claimed |
| E6 Honest failure | 2 | Missing/conflict/unknown/revoked/expired/unsupported routes refuse; presence is not validity or injection support |
| E7 Specifiability | 1 | L1–L8 and paired vectors are concrete, but hosted §6 caller-secret/daemon-non-resolution rule needs explicit reconciliation or a stated unsupported route; concrete carriers remain T0 publication |
| E8 Operator effort | 2 | One deliberate enrollment replaces per-home login on qualified paths; preserves native state and does not silently migrate |

Only operator decisions retained: runtime-B interpretation of D6; unresolved hosted successor/backend/policy/credential choices only when that route is activated; explicit local CIP-0010 ordering carve-out/route acceptance. D2, D11, D14 and whether setup-token is wanted are already decided. Archive encoding/caps can wait for its separate wave and must not block the additive Curator snapshot command.

Evidence: [pin ledger](../findings/astra-04-evidence.md). Final scoring awaits astra-01 synthesis and the next adversarial round; parked status has not been declared.
