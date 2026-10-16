# astra-03 position — launch fragments and consumers

Round 3 position, 2026-10-16. Provisional pending final seat-leaf synthesis.
Adversarial review of astra-02's full leaves is complete. This evaluates the plan, not
implementation readiness. No product binaries, builds, model calls or
credential probes were run.

## Plan rubric

Baseline: PLAN.md first synthesis at `7fde72b` / review repository `2c7d3a1`.

| Criterion | Score (0–2) | Evidence and remaining bound |
|---|---:|---|
| P1 Traceability | 1 | PLAN table names clauses; detailed leaf closure and five-CIP coverage still pending |
| P2 Bounded leaves | 1 | Muse, policy, snapshot and runtime splits are sound; grouped C3/H1+/X1+ still need their detailed single-owner leaves |
| P3 Negative evidence | 1 | G0/R0 and submitted Muse/Codex leaves pair refusals with controls; complete plan mapping pending |
| P4 Ordering | 2 | Shared-path serialization and qualification/publication predecessors are explicit |
| P5 Unblocking | 2 | Independent Muse v4 path precedes unrelated Codex/hosted/token work; M2 can investigate offline echo immediately |
| P6 Release honesty | 2 | Conditional activation, three-runtime hosted gate and route-specific D4 limits are explicit |

## Position and top risks

1. **Carrier publication is a genuine predecessor.** Spec `5509499` v4 has
   store `config_overrides`, while CIP-0018 requires successor
   `codex_settings` and leaves envelope allocation open. Support astra-02's
   canonical publication leaf; preserve one typed application owner and old
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

## Operator-only questions

None established by this review yet. Missing runtime qualification is work,
not an invitation to relax the contract. If no safe no-model replay can
observe a required row, the convener must record the remaining release gate
and timing honestly; a private fallback or silent downgrade is unacceptable.
