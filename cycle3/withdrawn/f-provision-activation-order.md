# Withdrawn: initial v1 provisioning activation-order candidate

**Status: withdrawn as a distinct finding. Do not number or merge into FINDINGS.md.** Retain the initial-handoff scenario below as qualification input for accepted F-27 / R-NETBIND publication work.

Owner: `macmini_swarma-review-3_astra-01`. Final source pins: dispatcher DP7 `74687e600e04817fa6e7a2e8904a9f7a3c83a1d8`, user manager UM7 `7b59da740037865dd42936982e5a069ea05eab53`, network profiles `359365e03cda729408aa8f9f2a05ae93ac481463`.

## Why the finding was withdrawn

The original reading treated the `fw.apply` drawn after `user.create` in dispatcher §5.1:298 and `diagrams/dispatch-lifecycle.puml:53–66` as the first enforcement. Under that assumption, helper `user.create` returning `active` (§4.3:177–179) conflicted with its requirement that verified initial enforcement and activation commit together (§8:466–467; `provision-retire-recovery.puml:115–128`). Four seats initially confirmed that reading, and the candidate was published at `d2dc527`, with an evidence amendment at `8c432db`.

Astra-10 supplied a valid counterexample: creation performs initial enforcement before returning active, then the dispatcher performs a redundant same-pin apply. DP7 never explicitly says its later call is the first enforcement, and helper §8:472 permits existing-allocation re-apply. No current clause excludes this interpretation. The original intrinsic opposite-order claim was therefore too categorical and was withdrawn in `1ff2461`.

The remaining initial policy/generation/listener handoff is unpublished, but its known owners and required invariant are already selected: dispatcher prepare owns the immutable pin, the helper owns enforcement before activation, and N15 owns the generation-bound listener contract. Dispatcher §3.4:144 / §16:729 and helper §14:606 explicitly retain the input-pin, listener attestation, lifetime and related transport/recovery publication work. After removing the first-apply assumption, the review established no additional violated invariant or conflicting mandatory path beyond those gates. The missing concrete connection is useful publication work, not a distinct confirmed architecture defect.

Static range denial precedes account creation, physical starts recheck current network gates, and the dispatcher remains provisioning until its effects complete. No runtime bypass, deadlock, unfiltered launch or completed implementation was demonstrated.

## Retained publication and qualification scenario

Before activating the v1 path, the selected protocol should demonstrate:

- How the admitted immutable Curator/network pin reaches initial enforcement, and how the helper-assigned fresh generation reaches its own listener before active is committed. The caller must not preselect a generation or infer proxy-provisioning authority from a permission to query listener evidence.
- How initial enforcement evidence and effect identities link to creation. A post-create same-pin apply may remain if explicitly identified; its removal is not required for correctness.
- That an interrupted creation rolls back under the current helper contract. Receiver `pending` maps to dispatcher `unknown` (§4.6:271/:278); it is not an implicit successful prepared-generation result. A new prepared state or API is neither required nor inferred.
- That proxy I/O remains outside the shared state lock, with generation, pin, listener and fence revalidation before commit; failed or unknown evidence cannot activate the account.
- Crash/rollback behavior around generation assignment, listener preparation, applied-state publication, active commit and caller acknowledgement, without duplicate allocation or substitution of a changed policy.

These checks complete existing publication gates. They do not weaken activation, require a new service, mandate a prepared state, or reopen F-27/F-28.

## Disposition evidence

Room `#swarma-review-3`, topic `f-provision-activation-order`, 2026-10-13:

- Candidate `$6NroDcAxayr6JWDhBcrwmU5deJtoxQ3Ta1JjiwYoj3A`; initial review request `$9a9jN3bCsffbHXzrp7_1rgAejo2_XUZUTILXbmfSLH0`.
- Initial confirmations, superseded for the stronger claim: astra-11 `$1wrAIOWJERC3o_CowCP5XYe5nzVYPAKBOMkcsRCH2Lc`; astra-06 `$3kVDJl3J6P6gBn-r3zq0ckJJpUcTZALeBLUKMPwNP0U`; sol-02 `$9U8QDBP5D9btyWVfSp7OuxSiF4b-sEq9OQuvDkEaWCo`; astra-02 `$Q8rDAALQVy5zK6NSuJqLecYXZxEIUF-ri_YMN1fgTgY`. They must not be counted as support for retaining a distinct opposite-order defect.
- Astra-10 counterexample `$NLYOkK_dcpyVdLOUHDljwuE0RZ-oK3aKwCg26AwLmuM`; author acceptance `$CBbvi093Go3xbrGl8FhyOHSI-mLs6VOmL0-CKIIVdr8`; narrower-disposition recheck `$zkaqgVUYmaLirGpW_Maef-z-g2NlgWVlNE0aY7XuHdg`.
- Astra-02 superseding review `$8P44zyWJMZYXt_7NxrIdYe16qHDapafL3a7x_ewNb_I` and explicit withdrawal recommendation `$VE_vt6KB0SToHAQWpem_g66Zdm15MQiLXzyeilJKcVo`.
- Astra-11 withdrawal of the stronger confirmation and classification as existing publication work: `$GEnZmbzWvN9di727L_P2ISv4nCDUEzSPZ0CrgqStjC0`.
- Astra-10 recommendation to withdraw the distinct finding: `$oyx1NA2xdRqtqcCOxQg6ks06u-C1qQ2ttMcnltnaPAw`.
- Sol-02 superseding review `$FJYJJGGYLs5eC8A6QiouXkbph-zdGEOT7GAJYkb9J04` and explicit withdrawal recommendation `$OP0JAechk_hA2hzzd5TNslet8FjRSbEqCA346RSwwIY`.
- Astra-06 superseding review `$YQzK3LgoBEDr1kdKlzWAUjRh5JWAjaKuJ1t6Ju8RT_E`: explicitly withdraws the initial first-enforcement assumption and recommends keeping the remaining scenario solely in existing R-NETBIND publication work. All four initial confirmations are now superseded by their authors' later reviews.

The author accepts this disposition and moved the record out of `cycle3/findings/`. The prior proposal and corrections remain in signed Git history; this note is the current conclusion.
