# Parked: astra-02, cycle 3

- **Date:** 2026-10-13.
- **Identity:** `macmini_swarma-review-3_astra-02`.
- **Lens:** user manager and privileged launcher; cross-module activation, account lifetime, process absence, policy authority and recovery.
- **PARK:** ivan-curator, `#swarma-review-3`, `rounds`, `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o`.
- **Last round marker:** round 13, `$BOu8rDkZqKCWjWPvVFNQwY0J-FBAyJy5L0vaQia5SIg`.
- **Own finding files:** none. Contributions and corrections were consolidated into peer-owned findings; no duplicate file was created.
- **Work performed:** documentation and source-document review only. No implementation, source-spec edits, builds, tests, runtime qualification, web access or child-agent runs.

## Final source pins

User manager UM7 `7b59da740037865dd42936982e5a069ea05eab53`; dispatcher DP7 `74687e600e04817fa6e7a2e8904a9f7a3c83a1d8`; broker CB7 `df8c7385456e9588392900e000738d419ffee2ec`; session host SH7 `798a321c82a6a3f86532300ad64a6ba04b52f114`; launcher LR6 `f08f566dd378ea27ce23ca0351ec793e95a696b6`; curator-spec `a0154285`; network profiles `359365e`; architecture `6b3f983`; wiki `87f387d`. Transfer context: spm PR #604 r6 (`d65cf7f`) and RWP v2.1. The full UM7 helper delta and affected figures were reread after the final landing notice.

## Peer findings confirmed or refined

All remain subject to the curator's cycle-3 disposition. Event references are in `#swarma-review-3` under the named topic.

| Topic | Contribution and limits |
|---|---|
| `f-workplace-relay-quiescence` | Confirmed that a live workplace-UID relay conflicts with the launcher's zero-account-process precondition, and that export/replacement also needs ingress exclusion. No process-name exception to F-13. Initial confirmation `$rEPd5m2JsEOJmHqfjuPKBiWtCq-opoHnLWIbio5b-fQ`, with final-UM7 recheck `$biHQdv0YQWHidZm4LrA0HGxINv5nnEN_XKjZfPZj2sc`. |
| `f-exec-profile-authority` | Confirmed the trusted selector relation and immutable resolved-policy identity gap, preserving existing admitted-profile/class/host checks. `$elHGpas5gb_rCQtgpkbrQABs3nVnnlD-Yf74Om2qUsc`. Final-file correction `$vCPRgC6H6M1yc0rm6nl5KNtBgiA4AuqZptDADAtRDXA`, verified resolved at `35b5631` in `$Ihx5hYh_harngQk-756KSO0OIPsmAtOVKXyt7UHNu2E`. No existence-only admission or current bypass was confirmed. |
| `f-allstop-dispatcher-path` | Added the receiver fence for already-issued physical starts and preserved direct operator parts in CB7/UM7. `$bpt_pO6UYVVhFhUykVtokD8EE5LFIDFyQe7Vrr_BSm0`; UM7 `$GWlk7YMJB_drjCQjzEc5S3-NtVkP7Xza7wiMUtL1RMU`; SH7 `$rEKRcXh41GTH31mwDq7ggQ3A1RicWIljJqpVbq5zmpg`. Refuted the shared-latch bypass inference in `$ymlti_B-lUoBrmVMgwaXfSCuH7Ie6cPe-9n2odX0UK0`. Final correction `$COoJD9reAkLA_s4eJ11WNgjcBKiqaNecWhsVPRTOjlo` distinguishes containment/stops without D from whole-act completion: D's own journaled part remains unresolved until reconciliation. Verified `c6b49e3` in `$wngjP2qwM8E1QBJBHlvk5_UsOnOtVJ6Uz5FXqLJ1XjU`. |
| `f-book-archive-tree` | Confirmed the retired-home tarball example contradicts F-1 and the chapter's own metadata-only prose. `$jTmPZZ4e3rN4KHcCwS6ofI5Rd61obDOnCzl8SGxMGUY`. Did not invent an export filename or treat unpublished operator retention as the normal path. |
| `f-book-egress-example` | Confirmed the code-host destination conflicts with provider-only agent networking and zero workplace egress. `$gbExWfhRGHc1XYYRAUoTUu7oWkVHK-OjcJkALsm-GkY`. No demonstrated push/exfiltration trace. Peer scribes published both book findings; no competing file from this seat. |
| `f-workspace-result-modes` | Confirmed that a path-to-blob-only base manifest cannot express chmod-only changes or regular-file/symlink mode changes. `$kCWK2xCFT2aOXc3IDzzHTzgNWz74HWgJ9ydLeDW71UU`. Refuted the separate claim that refusal diagnostics already require deterministic traversal: DP7 permits prefix observations before refusal. That item was withdrawn; outcome class and recorded digest remain distinct from diagnostics. |
| `f-restart-stop-authority` | Confirmed stale direct signals/group-only absence and removed ticket/redemption paths, against current dispatcher/helper stop/start and separate fresh-runner native-lock checks. `$s1UIcUbohdV3CCQki1KnV3Ce-gudVFIWS8AvaXRAJes`. Preserved VISION's non-canonical status and the book figure's valid dispatcher-stop and D-RESUME portions; no conforming unsafe restart claimed. |
| `f-ledger-topology-read` | Confirmed declared metadata visibility as a policy clarification/hardening proposal, not an existing total-confidentiality invariant. `$Z465d4vgyQVu07HTdJGalzjeE-fItx4tzYNRqjBKMc4`. Required the unresolved launcher reader/phase audit in `$p_alhc5OJyf4PJAq2pOwT6icO3hSO7-LjyDGfinlR_8`: preserve pre-drop root ledger/receipt work; qualify child, relay and mediated views. Verified the file no longer calls that audit complete. |

## Withdrawn, superseded and closed probes

- **Helper web custody:** the earlier `f-helper-web-custody` probe was fixed by UM7, including default-off/operator opt-in and separate web custody. Final confirmation `$AIufSJonhqeqHzRNgCZI0guWYkXgSC1RKgEUJ3bi75A`. The book sibling is a separate propagation finding.
- **Provisioning activation order:** my initial confirmation `$Q8rDAALQVy5zK6NSuJqLecYXZxEIUF-ri_YMN1fgTgY` is superseded. Astra-10 showed that create-owned initial enforcement followed by a redundant same-pin apply is not forbidden. I withdrew the intrinsic ordering claim in `$8P44zyWJMZYXt_7NxrIdYe16qHDapafL3a7x_ewNb_I` and recommended withdrawal as a distinct finding in `$VE_vt6KB0SToHAQWpem_g66Zdm15MQiLXzyeilJKcVo`. Verified `b69ad96` moved it to `cycle3/withdrawn/f-provision-activation-order.md`. The remaining pin/generation/listener handoff is existing R-NETBIND publication work, not a new confirmed defect.
- **Fresh park note under a closed fence:** partial review `$izjwKOeQgfNx4esZIQlYT9hq-pGlJWi_90he9EsMxbA`; no separate finding. SH7 promises a bounded attempt and marked snapshot fallback, not a fresh turn from every healthy idle agent. Existing `park <note>` data can be passive evidence. If a typed note turn is selected later, keep ordinary input closed, bind the control effect to operation/execution/epoch, reconcile ambiguous control without automatic replay, and repeat tool/external-effect drain afterward.
- **Old SSH certificate after label reuse/direct retirement:** declined as a new bypass in `$SKAKUjOcknBTzWAe6nKGlfJxAM8McL1KMlGUgDpMn8E`. CIP-0009 already requires certificate revocation/renewal stop and connection closure before project retirement; the broker-outage exception does not waive SSH cleanup. Keep name reuse and in-flight connections as qualification cases.

## Consolidation and open threads

No unanswered directed question, unconfirmed owned candidate, pending publication or source recheck remains for this seat.

The consolidation pass found independent acceptance cases in the execution-policy/input/discovery cluster; ALLSTOP delivery/unused-generation/workplace-ingress cluster; and cleanup-authority/export-refusal pair. An editorial grouping is possible, but fixing one case must not be recorded as satisfying the others. Host credential lookup and the book's exec-replaced reporter are also distinct. Cross-host coverage exists in newer topic replies even where a file's confirmation list has not yet caught up; avoid duplicate confirmation requests based only on those lists. Curator/owner consolidation remains their decision.

## Next examination and track-2 handoff

1. Freeze the helper/dispatcher launch and recovery boundary before implementation: immutable intake, generation exclusion, distinct physical execution evidence, observations, rollback and resource bounds.
2. Publish and qualify workplace ingress/start/quiesce ownership and the ALLSTOP receiver frontier, including unused generations and pre-issued create/start calls.
3. Complete R-NETBIND's initial pin/generation/listener handoff, without inferring a prepared state from `pending` or reintroducing the withdrawn ordering finding.
4. Resolve exec-policy authority/body pinning, interpreted-input qualification and candidate discovery as separate required boundaries.
5. Publish bounded cleanup authority, complete-content durability and refusal disposition while preserving independent security holds and explicit data-loss consent.
6. Set reader/phase and per-host evidence requirements before tightening metadata visibility; do not claim a completed reader audit or universal topology secrecy.

The PARK decision directs immediate continuation into track 2. `MISSION-IMPL.md` was read completely at review `b498936`; astra-02 is a reviewer on lens 2, dependency graph and contract freezing, with astra-10 holding the pen. Cycle-3 work is parked; subsequent discussion belongs only in `#swarma-impl-plan`.
