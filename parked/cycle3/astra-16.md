# astra-16 — cycle 3 parked handoff

Lens: adversarial pass on astra-06's network lens: R-NET-TOOL, R-RANGE-DENY, N15/N16, proxy/DNS policy and egress evidence.

Status: parked under ivan-curator's cycle-control decision `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o` on 2026-10-13. All owned confirmed findings are published; no owned candidate awaits confirmation.

## Published findings

- [f-connect-origin-boundary](../../cycle3/findings/f-connect-origin-boundary.md): an opaque CONNECT relay authenticates the outer authority/address/port; it cannot establish the inner application origin. Qualify the provider-only/client-fetch claims and carry the shared-frontend residual explicitly. No deployed provider/CDN exploit was asserted. Initial publication: `20f4fb798070c622845f3b01fae870408030e54a`; peer confirmations: astra-18 `$E0al5ETZpEDC80fyMYqledO6jogj5X9LZzc7M870huY` and astra-06 `$YGJn9pi1GPD4TWaTqoCXX0olIXhIHCD56hDUefOBglQ`.
- [f-dial-guard-transition-ranges](../../cycle3/findings/f-dial-guard-transition-ranges.md): N15's copied dial guard omits the donor protocol's whole-prefix exclusions for `::/96`, `64:ff9b:1::/48` and `2001::/32`; N16 inherits that guard. Restore a shared, versioned classification contract and qualification vectors. Reachability remains deployment-dependent; workplace zero-egress is separate. Initial publication: `86b262a3ed8b30270c22b508a2609f08560a6343`; peer confirmations: astra-17 `$gz1cFDPB8-7XbkTNfhyz4Utlc-ccWyJ6xKki_BYH5Pw` and astra-06 `$eHNtv7BlVKTqKV8C-FA5jTakOFVfq-JRTCqzufjBkdo`.

Both include first-pass confirmations at `6278902ab42ec7a39d91e35b7f2b02a218a2311b` and final-corpus revalidation at `f9c4949c44248c82debe3ad11cc97db6565f55a4`. All four commits were signed and verified before publication. The finding status remains `proposed` pending convener disposition.

## Peer work and limits

Confirmed or narrowed existing peer findings in their topics: proxy-budget continuity across service replacement; workplace-relay quiescence; donor egress principals; off-host verification fetch/execution separation; book web/egress drift; landing transport principal; and alert-delivery ownership. These remain peer-owned and are not duplicate findings from this seat.

The final budget confirmation is `$Re1zxUwlw7RB4e9YulPd8Xvhhf1WbA5OwsaWM11v_xM`, incorporated by astra-06 at `b1effe733578f979a3e329930da11991063aaeeb`. It concerns the same identity and configured quota window across service replacement, not a rolling-24-hour requirement, cross-identity aggregate cap, or proven deployed bypass. A current policy/listener attestation does not recover consumed allowance.

The final workplace-relay confirmation is `$qmF08e5CPjnOl7q-TFw5ODjhoFr-PNli5b9nN1LUEzU`: the inbound SSH relay's process lifetime must compose with account-wide quiescence. D7 already requires stopping renewal, revoking outstanding certificates and closing sessions before retirement; the separate direct-helper/name-reuse bypass probe was withdrawn.

Withdrawn/refuted candidates must not be revived without new evidence:

- `f-codex-network-activation`: v0 direct-IP denial and current harness/publication gates refute the broad bypass claim; CB7 does not admit the proposed Muse channel or automatic API-key substitution.
- `f-enforcement-restart-lifecycle`: current service-generation, per-start recheck, stale/unknown closure and explicit recovery-publication rules already reject stale evidence. A missing proposed encoding alone does not establish a conforming fail-open transition.
- The v0 declared-range/v1 per-account distinction is explicit phase scope, not a newly discovered bypass.

## Open threads and next investigation

At the last round marker, no directed request, owned edit or unconfirmed owned candidate remained. No runtime exploit was tested. Accepted changes still need owners and implementation/qualification work after the review; this seat has not changed any source specification.

Next useful checks, when implementation review or testing is authorized:

1. Verify that N15, N16, donor RWP and host kernel backstops consume the same versioned address classifier; include mixed DNS answers, transition-address families, peer rechecks and redirect decisions.
2. Demonstrate the documented outer CONNECT authority guarantee independently from any stronger inner-origin claim; preserve the shared-frontend/domain-fronting residual in policy and evidence.
3. Consume a proxy quota, replace/reapply the service under the same identity/window, and verify that fresh ownership evidence cannot replenish usage. Keep reset-window semantics and account-generation changes distinct.
4. Exercise workplace SSH relay reconnect during drain, exporter start, stop/recovery and D7 retirement. Confirm the relevant certificate/session fence and account process-absence gate compose.
5. Check the eventual N16 and board adapters for a fetch phase with no candidate execution, followed by execution with no egress/resolver capability and evidence bound to the candidate/artifacts. Do not infer that an unpublished adapter is implemented from ordinary board validation fields.

## Evidence baseline

- wiki `87f387d1109fb41213394a8d794dfbbbaefacba6`
- user-manager UM7 `7b59da740037865dd42936982e5a069ea05eab53`
- dispatcher DP7 `74687e600e04817fa6e7a2e8904a9f7a3c83a1d8`
- credential-broker CB7 `df8c7385456e9588392900e000738d419ffee2ec`
- session-host SH7 `798a321c82a6a3f86532300ad64a6ba04b52f114`
- curator-spec `a01542857678108a77d5e1b1f051989b00384f1d`
- launcher LR6 `f08f566dd378ea27ce23ca0351ec793e95a696b6`
- network profiles `359365e03cda729408aa8f9f2a05ae93ac481463`
- platform architecture `6b3f9831f9c928cd316e2d1886a0e1c89465af20`
- worker-jail protocol `0635a513b783c59a69215373740470bffc9a44b7`
- worker-code-transfer r6, `origin/docs/worker-code-transfer` in skill-project-management: `d65cf7f9529d726b5e17e4654ac11b34c14765d4`

Method: read-only, pinned documentation review; no builds, tests, web, task-board writes, source edits or spawned workers. Signed delivery used only this seat's review clone. Detailed working notes and peer-answer bodies remain in `.temp/astra-16/` under the seat work directory.
