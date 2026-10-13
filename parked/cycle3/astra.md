# Parked: core astra, cycle 3

- **Identity:** `macmini_swarma-review-3_astra`.
- **Date:** 2026-10-13.
- **Lens:** simplicity and operations; component and privilege count, contract duplication, cleanup and cut-over.
- **PARK:** ivan-curator decision `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o` in `#swarma-review-3` / `rounds`.
- **Final source pins:** DP7 `74687e60`; UM7 `7b59da74`; CB7 `df8c7385`; SH7 `798a321c`; launcher LR6 `f08f566d`; curator-spec `a0154285`; network `359365e`; trust `6b3f983`; wiki `87f387d`; board transfer PR604 r6 `d65cf7f` and RWP v2.1 context inputs.
- **Scope:** documentation review only. No source implementation, build, test, deployment or runtime qualification was performed.

## Owned finding

[`f-export-cleanup-authority`](../../cycle3/findings/f-export-cleanup-authority.md), proposed and independently confirmed across both machines, is published at signed `284841f`, refined at `be50b37`, and revalidated against the final corpus at signed/verified `83a7ebe2a98432bf1a3cf1d57161f08512adc2b9`.

The mandatory child-UID exporter needs explicit bounded cleanup authority after ordinary work authority expires. Each physical materialize/work/export launch retains distinct execution evidence. Discharge requires the result and every referenced blob to survive home retirement durably, with verified content, bounded custody and explicit release authorization. An archived request does not authorize result retrieval by a retired or revoked requester. Security holds, actual resource limits and unknown evidence remain gates; cleanup authority never becomes worker-repair or general successor authority. Reuse the existing launcher/effect machinery; no new service is required.

The concurrent `f-export-after-expiry` topic was consolidated into this finding. No source landing or confirmation remains pending.

## Peer work completed

- Published core Wonder's manifest-mode finding verbatim at signed `ec76e4d`; appended requested confirmations at `b2352df`.
- Published Wonder's wire/register finding at `b2352df` with approved citation and scope corrections. The convener published its later amendment at `ba7a6e3`; I preserved that landing and restored the omitted confirmation paragraph at signed/verified `f2d3066`. Future Muse publication belongs to scribes astra-10 and astra-20.
- Confirmed or refined workplace ingress/quiescence, interpreted-input qualification, inherited review/web obligations, never-launched ALLSTOP inventory, review-harness surfaces, and bounded export-refusal disposition. Required live work authority for worker repair; rejected automatic discard and unsupported infinite-retry claims.
- Final-file audits corrected unnecessary mandatory service topology in landing transport (`15401e1`) and unsupported existence-only admission language in exec-profile authority (`b2cc732`, `35b5631`, `73d5277`). Resulting files were read and verified; those follow-ups are resolved.
- Independently confirmed the host-credential and mailbox-figure findings from macmini after the cross-host request: `$gNIj04N6rHNbk9nhm9fDjv1IWAs3v-ujHtb1ZXxyLGA` and `$JycH2z3tBjFPlhkaFSxT2ZEffi3D3aYjYskbYUDaUH8`. Current broker/host/keeper checks remain counterevidence to a deployed bypass. Author and scribe received both events.

## Refuted or bounded probes

- Codex network activation: existing auth-only qualification and release gates already supply the claimed boundary; the candidate was withdrawn.
- Handoff `dirty_patch`: standard HOP projections never select it, its apply-only rule is not positive mutation authority, the v1.2 context is same-UID, and no current session-host consumer was found. Astra-05 withdrew the candidate following `$0Lr0ntPAxWru-zKUh1iJugEelbYSyUpsiZOdqYs0ruU`; astra-04 and fable independently agreed. An explicit dormant/same-account scope is optional publication cleanup, not a second transfer route.
- `round` numbering: constant 1 per distinct work execution is coherent with the existing identity tuple and C/C2 lineage. Intermediate-export semantics remain publication input, not another finding.
- No-board ALLSTOP and SH1 cut-over: the explicit goal-free exception and snapshot/swap/health admission barriers preclude the suggested broad failures.

## Open threads and consolidation

- No owned candidate, requested correction or publication remains unfinished.
- The two final cross-host confirmations may still need a scribe's metadata append; their findings and substantive claims were already published.
- The consolidation pass found implementation dependencies, not a basis to discard independent failure cases: cleanup authority versus deterministic refusal; manifest completeness versus base consistency; ALLSTOP delivery/fencing versus unused-generation absence. The naming findings already require one typed owner-linked index design. I changed or deleted no peer finding and obtained no additional merge agreement before PARK.
- Optional HOP draft cleanup stays optional unless a current consumer is demonstrated. It must not be made reachable by adding a projection or permission just to justify the old clause.

## Next examination

1. Freeze the smallest joint contracts and qualification gates before selecting implementation slices; keep decision, draft publication and qualified activation separate.
2. Trace cleanup authority, independent blob custody, quota accounting and explicit operator disposition through crash, expiry, revocation and restore without inventing services or widening authority.
3. Prefer one protected policy relation and one owner-linked architecture index over additional grant dimensions, policy stores or independently maintained status lists.
4. Preserve existing board operation during SH1 extraction; separate extraction compatibility from SH2 authority, transcript and storage guarantees.

Per the PARK handoff, continue with the same identity into track 2. `MISSION-IMPL.md` has been read completely; core astra is the assembler of `impl/PLAN.md`, while Opus owns the Russian translation.
