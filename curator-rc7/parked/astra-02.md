# astra-02 — parked after completed collective review

Date: 2026-10-16. Identity: `ivmbp_curator-rc7_orch-astra-02`.
Convener `ivmbp_curator_orch` issued PARK in `rounds`, event
`$gEYZR8rhEkJFEWRBsXfmU770rvlfWj0hSlSsIC3mnfc`, after all five exact-plan
acceptances and two unchanged rounds. This file records completion of the
architecture/planning mission, not delivery of the future implementation.

## Final position

- [PLAN](../PLAN.md): **12/12**, accepted content at `32cf0f2`, unchanged
  through `d36c7ed`; blob `f355619747d51fea46966ddbeed70e0560b83e36`.
- [Setup-token design](../designs/setup-token-local-source.md): **11/12**;
  E8 remains 1 because deliberate enrollment/migration still requires operator
  effort. The authority, containment and real-route gates are accepted.
- [Final verdict](../verdicts/astra-02.md) contains the rubric evidence and
  principal risks. No new operator-only decision is requested.

## Open threads

**None at artifact-review level.** All addressed requests are answered.
The following confirmed findings are resolved in the proposed contracts:

- Config/status versus Codex carrier ownership and Muse/status cross-document
  reconciliation are assigned to L15-0/C0.
- Full status and materialize share one pure verifier boundary, with independent
  real CLI no-execution controls; no hidden vendor version probe is admitted.
- Prepare bypasses first-install activation through an explicit internal seam
  and reuses PreserveLock instead of silently migrating an existing identity.
- [Adversarial astra-03 review](../findings/astra-02-review-astra-03.md)
  closes the M2 fixture/product-integration split, Codex hosted/relay owners,
  real-storage qualification, typed-login/env-shell rule and C7/M6 follow-ons.
- CIP-0015 consumer guidance and later broker integration have separate
  L15-5/6a/6b owners. All four peers accepted those leaves and PLAN maps them.

## Remaining implementation gates

These remain assigned delivery work, not unresolved collective objections:

1. Publish complete config/status/Codex/source carriers and reconcile the
   exact Muse diagnostic, ambient-backend and no-agent-status rules.
2. Implement and qualify actual metadata readers, trusted login and no-activation
   preparation, including failure state, cancellation, concurrency and negative
   controls. Unknown remains honest and OpenCode remains in aggregate results.
3. Obtain exact Muse loader and Codex backend/login/app-server/refresh evidence;
   retain C7's required-consumer activation gate and route-specific refusals.
4. Adopt and qualify T0–T4 on the real same-user headless final-executor route.
   Source presence or a direct-only test cannot close spawned authentication.
5. Keep broker source/operator/observer publication separate from the local
   source; no readiness request enrolls, leases or widens authority. Runtime B
   retains its already-published operator-confirmation gate after a concrete
   protected mechanism is reviewable.

## Persisted delivery evidence

Core L15-0..4: `b4d55ab`; prepare/peer-review refinements: `c1cab0f`;
shared verifier and launch follow-ups: `288eccc`; L15-5/6a/6b: `82b669b`;
exact-plan acceptance: `29dccd6`. These publications were signed and verified
with Git status `G`. The final parking change is published by a signed commit
and identified in the room acknowledgment.

Read-only documentation validation found all 53 leaves mapped and all 74
then-existing Markdown file targets valid. Known missing-file and omitted-M1
controls failed for the intended reasons; anchors were not checked. Seat logs
are `.temp/doc-check-02.log` and `.temp/doc-check-03.log`. No product build,
vendor/broker operation or runtime qualification was performed by this seat.
