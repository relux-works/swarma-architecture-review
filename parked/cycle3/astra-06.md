# astra-06 — cycle 3 parked

- **Identity:** `macmini_swarma-review-3_astra-06`.
- **Lens:** network; R-NET-TOOL, R-RANGE-DENY, N15/N16, proxies, DNS and egress evidence.
- **Park decision:** ivan-curator, 2026-10-13, `#swarma-review-3` / `rounds`, `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o`.
- **Disposition:** cycle 3 review work is parked. The same decision directs this seat to read `MISSION-IMPL.md` and continue into track 2 under its current identity after this note is committed and acknowledged.

## Owned finding

[`f-proxy-budget-incarnation`](../../cycle3/findings/f-proxy-budget-incarnation.md) remains **proposed**, pending the curator's acceptance/numbering. It was published signed at `e010041051bca9b3400b795f8089adfc9c460e30`, with adversarial evidence added at signed `b1effe733578f979a3e329930da11991063aaeeb`.

N15's identity/day cap and the candidate RWP service's process-local counters have different lifetimes. A replacement service can pass valid policy attestation while losing the same identity's already-consumed allowance. The finding is an adoption/qualification mismatch, not a demonstrated deployed bypass. It preserves the existing activation gates and proposes no new daemon, wire member or per-byte fsync requirement. Calendar-day and rolling-24-hour limits are explicitly distinguished.

Independent confirmations:

- Opus, recovery/time lens: `$K2FCuWyEpI5LDMYXZ-VExVJaRadk0ww6xJaBDTfGoXw`.
- Sol-01, scenario lens: `$w00vhCvG9JTgsrxD71r-pTKq0Epf0BUGRMuaXRIL8Zw`.
- Astra-16, adversarial network lens on the other host: `$Re1zxUwlw7RB4e9YulPd8Xvhhf1WbA5OwsaWM11v_xM`.

The record includes the N16 adaptation-list omission, P4/P6 qualification distinction, same-identity E-rebind/re-apply case, conservative unknown-consumption handling and existing R-TIME application. The original topic is `$6XLGLTWoJuXU4DQvNsGNKoJXKNC-qHGgdjAEdZwMzd4`.

## Peer findings reviewed

- `f-connect-origin-boundary`: confirmed authority/address confinement does not establish the opaque tunnel's application origin; no live provider/CDN fronting tuple claimed. `$YGJn9pi1GPD4TWaTqoCXX0olIXhIHCD56hDUefOBglQ`.
- `f-dial-guard-transition-ranges`: confirmed the three missing whole-prefix exclusions; deployment-dependent reachability preserved. `$eHNtv7BlVKTqKV8C-FA5jTakOFVfq-JRTCqzufjBkdo`.
- `f-verify-network-phase`: confirmed the board recipe/qualification needs N16's fetch-without-candidate-code then offline-execution boundary. `$iyPVUdylNQe0QVrVlG3yBkVmqvImYBnwokY69A6VdjU`.
- `f-watch-freeze-lifecycle`: confirmed only the revised lifecycle/version/outcome scope, preserving existing effects and linked narrowing records. `$XbK20tZ56e1Oy0I_KteG4bLdNogMZDNlYoUn-ASxRfI`. Added kernel-state plus generation-proxy-session containment, live CONNECT qualification, independent stop progress and honest unknown containment: `$l3oxr_i_qLBenW1YpItz3RRu0Wn-pRKLzHmKN-9zSWE`.
- `f-landing-egress-principal`: confirmed the missing concrete transport boundary, retaining existing board/infrastructure logical owners and deployment choices; no mandatory new daemon or widening of agent egress. `$433CiuGGPfCNzFm4oKx0sYFYUT4KlVbj2EfelmFrh60`.
- `f-alert-egress-owner`: partial confirmation of owner/route/version/delivery publication; refuted inevitable silence and a mandatory new outbound service. Existing later broker recipients and inbound-initiated response/subscription paths remain counterevidence. `$wv20WZQkXVeh5kAu10XL18s-6HprJ7DPuFUnZ4zsPEU`.
- `f-book-egress-example`: confirmed destination-policy drift, without inferring repository write authority or a no-exfiltration guarantee. `$t5p2hXR3lvn1JvjVKerBplgXVx68nY7zt436VshV0bY`.
- `f-book-web-boundary`: final-pin cross-host confirmation of default-off/operator-opt-in and separate search-key custody; provider-credential enrollment is a different statement. `$g1SgaHPzp_UpF1_sAlRIbzeyNuUxo5B-J-V8Ng_aVCA`.
- `f-donor-provisioner-register`: final-pin cross-host confirmation of the missing supersession and B activation gate in the trust summary; no replacement donor API invented. `$4vCjzdzNIeHPZGnQXL2zcJArT79L7qiEBichxnHSFyw`.

## Refutations and corrections

- `f-enforcement-restart-lifecycle`: supported withdrawal of the broad stale-applied-state claim. Existing helper service-start checks and listener/service-generation lifetime gates already rule out treating stale policy evidence as valid. `$mDRhBKgZ-kZNo-iBz_GtA15749UawkYhhYGz2LYPuu8`.
- `f-helper-web-custody`: final UM7 `7b59da74` repaired the helper paragraph; its withdrawal as landed is correct. The separate book paragraph remains stale.
- `f-provision-activation-order`: **my original confirmation was withdrawn**. I inferred that DP7's post-create `fw.apply` was the first enforcement, which the text does not establish. Helper-owned initial enforcement followed by same-pin re-apply is a valid counterexample. Superseding review `$YQzK3LgoBEDr1kdKlzWAUjRh5JWAjaKuJ1t6Ju8RT_E` recommends retaining the initial pin/generation/listener handoff only as existing R-NETBIND publication work. The author moved the candidate to `cycle3/withdrawn/f-provision-activation-order.md` at `b69ad96` and included my superseding review at `0b7dd96`. Do not count the earlier `$3kVDJl3J6P6gBn-r3zq0ckJJpUcTZALeBLUKMPwNP0U` as a current confirmation.

## Consolidation and open threads

No unconfirmed owned candidate or unanswered directed question remains. The late cross-host confirmations for the web-book and donor-provisioner files were sent to their owner before PARK; the owner may append those event references to the existing files.

The network consolidation pass at review `dc14ab7` found no justified duplicate among CONNECT-origin assurance, dial-range classification, quota continuity, runner phase isolation, watcher freeze lifecycle, operator notification and repository/runner transport. They can share implementation and qualification work, but their failure cases and acceptance evidence differ. Book destination repair should use the CONNECT finding's precise assurance wording. Daily-budget persistence must not be confused with the watcher's generation/boot-bound raw telemetry baselines. No merge, deletion or extra finding was proposed by this seat.

The withdrawn provisioning case remains useful as an initial-creation acceptance scenario: demonstrate immutable pin flow, helper-assigned generation and correct listener before active, coherent rollback/observation and unlocked proxy I/O. It adds no new prepared state or root orchestration authority.

## Source pins and next examination

Final affected corpus checked:

- wiki `87f387d1109fb41213394a8d794dfbbbaefacba6`;
- network profiles `359365e03cda729408aa8f9f2a05ae93ac481463`;
- user manager UM7 `7b59da740037865dd42936982e5a069ea05eab53`;
- dispatcher DP7 `74687e600e04817fa6e7a2e8904a9f7a3c83a1d8`;
- session host SH7 `798a321c82a6a3f86532300ad64a6ba04b52f114`;
- credential broker CB7 `df8c7385`;
- Curator CIPs `a01542857678108a77d5e1b1f051989b00384f1d` (read via `git show`, since the worktree lagged);
- launcher LR6 `f08f566d`;
- trust architecture `6b3f9831f9c928cd316e2d1886a0e1c89465af20`;
- RWP `0635a513b783c59a69215373740470bffc9a44b7`, supplied protocol copy;
- board import PR #604 r6 `d65cf7f9529d726b5e17e4654ac11b34c14765d4`, supplied input copy.

Next useful work is the implementation-plan dependency order: one shared versioned dial guard and conformance set; accurately bounded CONNECT claims; identity/window budget recovery; generation-bound listener evidence; freeze/release ordering; N16 phase transition; and the existing owners' notification and repository/runner transport choices. `MISSION-IMPL.md` will determine the next track's scope and deliverables.

This was a documentation-only review. No source repository was edited, and no build, test or live network probe was run. Own Markdown changes passed whitespace checks; both published finding commits were signed and their signatures verified.
