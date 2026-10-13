# astra-13 — cycle 3 parked

- Seat: `ivmbp_swarma-review-3_astra-13`, adversarial pass on astra-03's credential-broker lens.
- PARK authority: ivan-curator, event `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o`, 2026-10-13. The same event directs immediate handoff to track 2.
- State: all directed review questions answered; no owned finding, unconfirmed candidate awaiting publication, or failed send remains. Documentation review only; no builds, tests, credential-store access or source-repository edits.

## Reviewed baseline

The final lens pass used broker CB7 `df8c7385`, dispatcher DP7 `74687e60`, user manager UM7 `7b59da74`, session host SH7 `798a321c`, launcher LR6 `f08f566d`, curator-spec `a0154285`, network profiles `359365e`, wiki `87f387d1109fb41213394a8d794dfbbbaefacba6`, and architecture/TRU `6b3f9831f9c928cd316e2d1886a0e1c89465af20`. Earlier confirmations were corrected when SH7 and UM7 superseded their evidence.

## Contributions and disposition

- **Host credential-boundary propagation:** independently confirmed wonder-11's [f-host-credential-lookup](../../cycle3/findings/f-host-credential-lookup.md), event `$_gF2jt79x-IzeupHYLnFGFdeXWbcRLItvhEuGG6Hq7g`. Peer-published the exact reviewed attachment at signed commit `3c0bb84175721786f4bfc3b1971fccd195994f9c`; wonder-11 retains ownership. Stale SPA host/supervisor lookup arrows conflict with agent-side `curator-run` consumption in CB7/SH7. This is guidance drift, not demonstrated credential leakage.
- **Donor egress principals:** confirmed [f-donor-egress-principals](../../cycle3/findings/f-donor-egress-principals.md), events `$TirGgn0_UT0JxSvIu6f0yKflkl7cBXCFhN0hc-62svo` and `$YPYcLbtzqhmg5Y0v8afXnM62g4aZhNhhzFJtrS_UulQ`. A bridge UID restricted to SSH/join cannot also provide provider egress. The selected Codex app-server loopback control route needs its own exact authorization. Neither issue justifies a generic loopback exception or broader credential exposure.
- **Muse C7 propagation:** confirmed [f-book-muse-c7](../../cycle3/findings/f-book-muse-c7.md), event `$ggc1KpVHeZjHiaBL1AgZqK4CuXDP5xs2-ZUBVMciHzw`. Research priority is decided; channel qualification, lifetime, billing and fallback publication remain open. Do not turn the documentation correction into a claim that Muse subscription leasing is admitted.
- **Trusted-circle scope:** final correction `$l2B8fbtydn7b_z66sF6V0_BCQ8OgUG3y9_YoTDbjiSQ` supersedes the earlier literal class-mismatch confirmation. SH7 and UM7 now carry the exception. The peer finding is narrowed to predicate clarity; class membership alone does not grant reviewer, donor, host-loop or broker authority.
- **ALLSTOP composition:** supplied counterevidence and scope corrections in `$DS9MpFD3q808869gznaUyO4tnTbInJa4HLslL10vh7I` and `$otwLmBs6yW9X03iqfnyxeafzX4c-H2t9434OTAdLw7g`. CB7 has a direct operator-to-broker freeze path and distinct retained gates. Containment progress with the dispatcher absent is not whole-act completion without every required service record.

## Withdrawn or refuted leads

- **Own `f-codex-network-activation`: withdrawn**, event `$scSKgBCZfGQ1IFmCzzeKfukf7kz-Ct8bcMzsakm76Y4`. Native exec probe results do not establish the external-token app-server behavior. N7, the static UID-range deny, CB7 qualification refusal and credential-only refresh requirements already gate activation. No finding file was created.
- **Muse minted-key end:** a separate admission defect was not established; CB7 already leaves all twelve qualification rows open and refuses an unqualified channel. Mandatory remint on holder retirement would add a policy choice, not merely implement an existing guarantee. Refutation `$6rnXm3I4Zy9bhabrXlUGecCsLfs9cILhiUrVDZcKiD0`; owner withdrew the candidate.
- **Client report poisoning:** CB7 §§8.5 and 11 scope `event.report` to the reporting lease; account state changes require owner action or the auth owner's own refresh outcome. No shared-account revocation exploit established. The absence of a surviving env-exec reporter is an explicitly open process-model issue.

## Open qualification work and next checks

These are future implementation gates, not new cycle-3 findings:

1. Qualify exact Codex build, external-token entrypoint and credential-only refresh path under the intended network fence; preserve one refresh writer and fail closed after an ambiguous outcome.
2. Keep Muse subscription disabled until its proposed minting-owner/channel contract and every required qualification row are resolved. Preserve the distinction between broker authority expiry and provider key validity.
3. Before donor admission, publish and qualify provider, refresh and app-server control routes with exact principals, peers and lifetimes.
4. In cut-over and emergency-stop runbooks, distinguish durable containment, process absence, export obligations, service-local reconciliation and explicit recovery authority. Clearing one hold must not clear another.
5. Propagate the accepted host/runner credential boundary and C7 status before operators use the affected diagrams as implementation instructions.

No review request remains open for this seat. Track 2 handoff: operations and cut-over, with astra-03 holding the section pen; retain these credential and recovery constraints while reviewing its implementation sequence.
