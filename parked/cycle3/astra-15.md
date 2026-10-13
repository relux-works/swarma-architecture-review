# astra-15 — cycle 3 parked

- Identity: `ivmbp_swarma-review-3_astra-15`.
- Lens: adversarial R-TRANSFER, paired with astra-05.
- Park authority: ivan-curator, rounds event
  `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o`, 2026-10-13.
- Review-only work: no source changes, builds, tests, board writes or spawns.

## Published finding

[f-rework-inherited-flags](../../cycle3/findings/f-rework-inherited-flags.md)
is published through signed commit
`34692e1b1c726c579c48caad6b8fe2bd5df8def6`. It covers inherited sensitive-hunk
and unresolved web-provenance obligations when unaccepted C1 becomes C2's
materialization base. A fresh exact-C verdict does not itself define the
complete acknowledgement set. Keep a separate trusted integration baseline,
recompute the final obligation set, and obtain fresh candidate-bound
acknowledgements without falsifying the current run's capability class.

Independent confirmations from astra-18, core astra and astra-05, including
the web-provenance refinement, are cited in the finding. Final DP7, UM7,
SH7 and LR6 rechecks left its substance unchanged.

## Peer review and consolidation

Confirmed or narrowed the published cleanup-authority, refusal-disposition,
relay-quiescence, mode-aware manifest, base-binding, review-harness,
verification-network-phase and landing-principal findings. The bounded
scope and relevant event identifiers are recorded in their files/topics.
In particular:

- Cleanup consent is not expired worker/repair authority. Complete result
  and blob durability, not merely their digests, precedes home deletion.
- Refusal retains the export obligation, not execution capacity after
  confirmed absence. Standing discard policy is an owner choice. Permission
  denial requires qualification of the actual reader and admitted worker
  tools; infrastructure denial remains distinct.
- Existing exact-B invariants already forbid mismatched base material.
  Missing mechanical cross-checks are pre-publication work, not a conforming
  bypass or proof that an exporter-reported edit came from the worker.
- Review consumption stays inert. Acceptance is not admission of candidate
  control surfaces. Exact-C review and independent harness H remain separate.
- Different refusal diagnostics do not establish contradictory terminal
  results; diagnostic determinism was withdrawn as a current defect.
- Final trusted-circle clauses agree. Consumer-predicate clarification is
  distinct from an automatic capability upgrade or an adopted class rewrite.

The consolidation pass at review `dc14ab7` proposed no further merge:
cleanup authority versus refusal disposition, manifest modes versus base
binding, inherited obligations versus inert review, and CIP-copy refresh
versus book-owned one-shot cleanup each retain independent acceptance
criteria. `f-export-after-expiry` is already folded into cleanup authority.
Round-10 report: `$EVHYvXO5NVWvrSzqKdPo0sc9VcDeQtE5H5cVHAeHkDU`.
Cross-host confirmations can be in later topic replies rather than the
published attachment; machine-ID searches alone are not a coverage audit.

## Open threads and next examination

No unanswered directed request, unconfirmed owned candidate, or unpublished
confirmed finding remains. Astra-05 withdrew the handoff dirty-patch
candidate after closed-projection and same-account counterevidence; no
duplicate finding was opened.

Sol-14's late-result walk remains qualification input, not a new finding
or an extension of N16. Authentic J1(C1) may be retained historically but
must neither satisfy nor regress C2's gate. The receipt-to-current-state
adapter remains unpublished. Existing CR tree/source/input binding is not
an exact-commit substitute. My reply
`$cm16pqFpZjYGAY_MytFsSbhX8lrlDJ4flgfBa62rZVQ` adds equal-tree/different-OID,
late success/red, crash recovery and current-request mutation checks,
preserving at most one infrastructure retry and no retry of test failure.

Next, turn the confirmed transfer requirements into ordered publication
and qualification gates: immutable mode-aware B representations; fenced
export with cleanup authority and durable content; explicit refusal/repair
disposition; independent import; inert exact-C review with inherited
obligations; H-pinned verification with fetch-only egress and offline
execution; and exact signed-C landing. Keep owner choices visible, including
standing refusal disposition and transport topology, rather than selecting
them by implication. No executable qualification has been run in this cycle.

The convener requests immediate continuation into implementation-strategy
track 2 under `MISSION-IMPL.md`, keeping this identity. This note closes
cycle 3 only.

## Evidence pins

- Board draft r6: `skill-project-management`
  `d65cf7f9529d726b5e17e4654ac11b34c14765d4`,
  `references/worker-code-transfer.md`; the late-result check also read
  `.specs/validation-binding.md` at that exact revision.
- Dispatcher DP7: `74687e600e04817fa6e7a2e8904a9f7a3c83a1d8`.
- User manager UM7: `7b59da740037865dd42936982e5a069ea05eab53`.
- Session host SH7: `798a321c`; launcher LR6: `f08f566d`.
- Curator spec: `a0154285`; network profiles: `359365e`.
- Trust architecture: `6b3f983`; wiki: `87f387d`.
- RWP v2.1: `worker-jail` at `0635a513b783`, `docs/protocol.md`.

Task-local detailed research and reply payloads remain in
`.temp/astra-15/`; they were not included in shared commits.
