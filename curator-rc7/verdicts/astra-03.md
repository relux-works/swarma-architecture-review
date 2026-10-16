# astra-03 position — launch fragments and consumers

Final position after convener PARK, 2026-10-16. Accept the integrated
implementation plan and setup-token design for their stated bounded delivery.
Adversarial review of astra-02's full leaves is complete. This evaluates the plan, not
implementation readiness. No product binaries, builds, model calls or
credential probes were run.

## Plan rubric

Baseline: PLAN.md at `32cf0f27535885141a3f813e367094923238e5be`,
blob `f355619747d51fea46966ddbeed70e0560b83e36`, including L15-5/6a/6b
from `82b669b`. All known artifact-level findings are resolved.

| Criterion | Score (0–2) | Evidence and remaining bound |
|---|---:|---|
| P1 Traceability | 2 | All 53 bounded leaves are linked; five-CIP implementation coverage explicitly includes L15-5/6a/6b, M6, C7 and X5 rather than hiding follow-on ownership |
| P2 Bounded leaves | 2 | Separate C2/C3/C5/C6/C7, nine H leaves, X0–X5 and T3a/T3b remove the former grouped delivery surfaces |
| P3 Negative evidence | 2 | Defined leaves specify forbidden effects, adjacent valid controls and bounded detector plants; vendor/syscall/lifecycle proofs remain distinct from schema tests |
| P4 Ordering | 2 | Shared-path serialization, publication and qualification joins, parallel snapshot helpers, and source API order are explicit |
| P5 Unblocking | 2 | M1–M5 precede unrelated typed-policy/hosted/token work; M2's conforming real-loader fixture removes an unnecessary materialize predecessor |
| P6 Release honesty | 2 | Base tag, Codex activation, token spawn, native/headless snapshots, three-runtime hosting and cross-account qualification have separate claims |

## Position and top risks

1. **Carrier publication is a genuine predecessor.** Spec `5509499` v4 has
   store `config_overrides`, while CIP-0018 requires successor
   `codex_settings` and leaves envelope allocation open. C0 and L15-0 now
   divide the canonical publication work; preserve one application owner and old
   schema bytes. Muse v4 need not wait for that successor.
2. **v0.5.66 is not the 1.4.8 qualification release.** Fresh `acae871`
   inspection confirms correct typed fact transport, backend overlay and
   fail-closed Codex unsupported guard, but only 1.4.7-R6101.1 exclusion.
   M2 precedes the next qualification-bearing consumer release.
3. **Offline evidence must reach the loader.** `--provider echo` is a concrete
   existing candidate for both forms. Quota failure, parser acceptance or
   correct argv alone does not prove P1–P4; keep missing rows unknown. No
   refresh, model-visible removal or account isolation claim follows.
4. **Parser-only launcher work loses policy.** `9ad2f016`
   `internal/plan/context.go:18` drops Muse; tracked serialization and final
   env composition must preserve the policy too. Tests must exercise these
   production paths, not only schemas.
5. **Snapshots and settings have separate coverage.** A snapshot descriptor
   is not a settings/source carrier. Host start/client/resume and dispatcher
   need their own covered policy and compatible accepted identity; a pin bump
   cannot close that seam.
6. **Local login is not every CIP-0015 consumer.** L15-5/6a/6b now own its
   guidance/display and authorized broker follow-ons explicitly. The
   [coverage finding](../findings/login-followon-coverage.md) is closed;
   those routes still require their own released contracts and authority.

Detailed proposals: M1 [producer](../leaves/muse-v4-producer.md), M2
[replay](../leaves/muse-148-exclusion-replay.md), M3
[plugin qualification](../leaves/muse-v4-plugin.md), M4
[launcher](../leaves/muse-v4-launcher.md), M5
[pin](../leaves/muse-v4-consumer-pin.md), M6
[broker-key backend seam](../leaves/muse-dispatch-backend.md), C1
[Codex producer](../leaves/codex-settings-producer.md), C2
[plugin](../leaves/codex-typed-plugin.md), C3
[launcher](../leaves/codex-typed-launcher.md), C4
[storage qualification](../leaves/codex-storage-qualification.md), C5
[hosted settings](../leaves/codex-hosted-settings.md), C6
[dispatch relay](../leaves/codex-dispatch-settings.md), C7
[joint qualification activation](../leaves/codex-qualification-activation.md).
Evidence pins and exact current-source caveats are in
[source baselines](../findings/astra-03-source-baselines.md).

## Adversarial review status

Accepted astra-02's five detailed leaf contracts after the
[persisted adversarial review](../findings/astra-02-adversarial-review.md).
Confirmed the carrier/precedence finding from spec bytes independently.
Specific Muse native/unset mapping, explicit keychain refusal and ambient
backend precedence must use CIP-0017's amendment rather than generic earlier
CIP-0015 wording. No demand to reopen
D14 or to use Claude auth status as a metadata-only reader is justified.

Accepted two concrete challenges from astra-02/04: M2 now separates a frozen
conforming regular-file fixture's real-loader evidence from SNAP-CLI export
qualification, removing a hidden critical-path edge; C3 no longer attributes
hosted and relay settings to the Curator runtime-bootstrap leaf. C5/C6 own
those separately. C4 is the sole proposed Codex storage-qualification leaf,
agreed with astra-02. A proposed strict nonempty Codex env/shell refusal is
delegated to C0 publication rather than invented by the implementation.

Round 3 independently confirms astra-02's first-install activation trap and
existing PreserveLock migration refusal; the review records the required
prepare seam and adjacent valid install control. Accepted astra-04's C5
clarification: the new hosted route permits receiver tools/trust policy only;
Curator writes its initial exclusive MCP base, preserving declared profile MCP
and refusing unowned gateway/profile intersections. Legacy host config writing
cannot be reused as permission to rewrite the new route's home.

Accepted astra-02's L15-5/6a/6b at `82b669b` and their full PLAN mapping at
`32cf0f2`. All addressed review requests are resolved at the planning level.
The local artifact check verified 18 reviewed/owned files' targets and all
53 leaf links; known-missing-target and omitted-M1 controls were detected.
That check proves link/map completeness only. Manual source review supplies
the clause comparison; no provider, filesystem-race or credential test ran.

## Setup-token design rubric

Scored the design and T0–T4 contracts at `75dc718`, including the actual
headless route, public API split and startup-input qualification added by the
other reviewers. These scores assess the proposal. They do not qualify Claude
child containment, authentication, reload behavior or any vendor release.

| Criterion | Score (0–2) | Evidence and bound |
|---|---:|---|
| E1 New concepts | 2 | Reuses CIP-0010 nodes, opaque refs, bindings and capability; no local broker or generic secret transport |
| E2 Reuse | 2 | Curator owns one protected store/source core and public final-launch facade; launcher owns its actual final route; existing readiness semantics stay intact |
| E3 Secrets | 2 | Material release only at admitted child start; generic literals/ax/host payloads/snapshots forbidden; real child/interpolation/reload/startup-input controls gate capability |
| E6 Honest failure | 2 | No silent native fallback; present is not valid; unknown expiry, local-only revocation and blocked qualification are explicit |
| E7 Specifiability | 2 | L1–L8 plus ST-01–15 give concrete contracts; T0 owns complete closed publication before enablement |
| E8 Operator effort | 1 | One deliberate enrollment removes per-home login on qualified routes, but renewal, explicit migration and unavailable tuples still require operator work |

Accept for normative adoption and bounded implementation. The release must
retain the real `task-board -> curator-run final-exec -> Claude` evidence join:
direct-only injection or the separate hosted daemon cannot substitute for it.

## Operator-only questions

No new operator-only choice is established by this launch review. The existing
Runtime B confirmation gate remains with the snapshot/runtime owner; this
verdict does not supply it. Missing runtime qualification is work,
not an invitation to relax the contract. If no safe no-model replay can
observe a required row, the convener must record the remaining release gate
and timing honestly; a private fallback or silent downgrade is unacceptable.
