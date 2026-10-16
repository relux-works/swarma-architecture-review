# D4-S — Give each headless task-board spawn its own Curator snapshot

- Owner repository: skill-project-management.
- Normative clauses: managed-home-snapshots §§1,4,6; environments §10.5; local-hosted-launches §1 (spawn is separate); D1, D2, D4, D5; HOST-HOME-SPEC runtime/verification contract.
- Attack surface: per-run home/provenance handoff and retry/resume identity.
- Size: 3 after the entrypoint/runtime contract exists. Separate from source-specific token T4 and primary-session hosted execution.
- Release cut: follow-on consumer of released materialize; mandatory for a task-board spawn D4 claim and prerequisite to the full token-spawn outcome.

## Acceptance

1. The public spawn entry requests Curator-owned private content/runtime preparation and hands the admitted process to the approved curator-run executor. Preserve board admission, task/run identity, input/policy/resource bounds and recovery guarantees. Publish the exact handoff first; do not invent a wrapper around frozen wire.
2. Remove only the corresponding interim home-copy/inventory logic after equivalent producer/verifier capability is available. A profile/fragment digest alone cannot stand in for snapshot bytes. No board-created auth links, native-config copy or marker-layout inspection.
3. Persist the original non-secret content/runtime receipt and expected identity per run. A retry or resume uses that baseline and Curator-defined protected-input verification; it cannot switch to the current live profile or bless a newly copied tree after drift.
4. Keep mutable run state, policy, goals, inputs and credentials outside the content snapshot. Preserve cancellation and unknown-liveness handling. Failure before admitted start launches no provider; retries must not double-start a previously admitted live attempt.
5. Unsupported materialize/runtime/verifier or final-executor capabilities refuse clearly. Preserve valid existing per-home semantics only on explicitly documented legacy paths; never claim the new D4 guarantee for them. Token source uptake remains T4's separate implementation and qualification.

## Negative tests with positive controls

| Positive control | Negative witness and forbidden result |
|---|---|
| Public headless spawn receives a private verified snapshot and metadata-only process handoff | Live managed home, second content inventory, absent receipt or unknown required downstream capability refuses before child start |
| Source changes do not alter a running run's context; legitimate runtime state survives resume | Changed/extra protected content, baseline replacement or new current-profile selection on resume refuses |
| Cancelled preparation cleans only its own reservation/resources | Cancellation/retry cannot delete source/native data or start a duplicate live process; unknown liveness never counts as absent |
| Independently admitted destination authentication works | Caller presence, snapshot archive, native auth link or token in plan env/resources cannot confer authority |

Exercise actual spawn/retry/resume entrypoints, including a controlled provider process and preserved neighbouring valid per-home cases. A known substituted receipt/content witness must fail the intended check. T4 adds the real Claude token-specific end-to-end chain; these filesystem/process controls do not claim vendor authentication.

## Dependencies and paths

SNAP-CLI, HOST-HOME-SPEC/CODE, the published same-user curator-run final entry, and compatible agents-management module. Share entrypoint publication with T0/T3 when the first supported chain is the local Claude node route; implement source-independent home/provenance handling first, then join T3/T4 for final qualification. Likely paths: `tools/board-cli/internal/spawn/{spawn,launch_plan,launch_composition,curator_fragment}.go`, retry/runtime adapters, module pin/vendor and provenance fixtures. Serialize with T4; do not place this under the all-three-runtime primary-hosted activation dependency.
