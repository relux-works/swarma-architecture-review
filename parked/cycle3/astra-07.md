# astra-07 — cycle 3 parked

- **Identity:** `macmini_swarma-review-3_astra-07`.
- **Lens:** remote worker: CIP-0008/0009/0010, donor variants, bridge, join and retire.
- **PARK:** ivan-curator, 2026-10-13T03:11:52Z, event `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o` in `#swarma-review-3`, topic `rounds`. The same decision directs immediate continuation into implementation-planning track 2.
- **Disposition:** no new finding file owned by this seat and no unpublished confirmed candidate. Independent confirmations and counterevidence were contributed to existing topics. All directed candidate questions were answered. Cycle-3 findings remain proposed pending curator/owner disposition; confirmation is not implementation.

## Independent confirmations

| Finding | Contribution and bounds |
|---|---|
| [`f-donor-egress-principals`](../../cycle3/findings/f-donor-egress-principals.md) | CIP-0009 D1/D2 gives the bridge UID SSH/join-only egress while also assigning it the provider proxy; CIP-0010 credential refresh and the CIP-0008 loopback app-server pair need explicit principal/route ownership. Publish a principal/route table, not blanket loopback permission. Variant B remains qualification-gated; no deployed exploit claimed. Confirmation `$eFU_l-x9mOHknN2zg2WbHr9sTqi_1SOdzyxtMR7peyA`; publication `461ab7c`. |
| [`f-donor-signature-algorithm`](../../cycle3/findings/f-donor-signature-algorithm.md) | CIP-0009 D4 requires Secure Enclave P-256 `K_sig` for A/C, whereas ADM/TRU admit Ed25519 and D5 preserves the final signed envelope. The optional generic data signature does not repair final-envelope verification. Keep SSH and operator-phone keys separate; publish and qualify the suite without silent fallback. Confirmation `$ZAsDGeVrU4GlhsDeOXSj6pRcwWXuXHRVqF0X4eM7LRQ`; publication `461ab7c`. |
| [`f-workplace-relay-quiescence`](../../cycle3/findings/f-workplace-relay-quiescence.md) | Rechecked against final UM7. A persistent workplace-UID relay conflicts with zero-process first-launch admission, account-wide stop and export quietness; stopping it also loses the channel and reconnect can recreate the process. This affects ordinary job/export/replacement flows. CIP-0009 D7 already requires renewal stop, KRL revocation and established-session closure during retirement: do not assert a compliant stale-certificate retirement bypass. Confirmations `$aCgIZ1peQTWh1V2YUjydQy19SDo1lxlzmakLcs3wGvw` and `$-2GKBoA-gBUURsp7Y_KgTVCXJWEzGSdjUZKX4sfBvyI`; final owner update `5e2acad9c2b65551b1a25e64f9e58a7dfdb591be`. |
| [`f-book-one-shot-export`](../../cycle3/findings/f-book-one-shot-export.md) | Generic one-shot book paths omit the conditional workspace-export or explicit operator-waiver obligation before deletion, although DP7 expressly retains it. Preserve early execution-capacity release after proven absence, non-workspace one-shots and pre-work compensation. Documentation propagation, not a compliant-runtime bypass. Confirmation `$bOHa-P2Z1dOpO2UvgFTBj8jEe_Ft4r03FVytLyoTdwo`; publication `dc36690`. |
| [`f-donor-provisioner-register`](../../cycle3/findings/f-donor-provisioner-register.md) | Added operator-host confirmation: TRU still suggests donor verbs on a root helper, whereas final UM7 and CIP-0008 reserve a separately named, unpublished donor provisioner. Preserve TRU's proposed status and the gated B variant. This does not revive the closed cross-UID-supervisor probe. `$sK7p4uHD7EOxgvSxbdhdg3XDgbZHkN2df9cyZ2_VUdI`. |
| [`f-book-web-boundary`](../../cycle3/findings/f-book-web-boundary.md) | Added operator-host confirmation of the missing default-off/operator-per-identity opt-in and variant-specific web-key custody in the book. Provider credential custody is a distinct, still-correct bridge responsibility. Preserve snapshot/spec-precedence limits. `$PctyploTJ4KykNtMtjRJ_PwLZaaKlrTRqjk8KfhG7yU`. |

## Book and consolidation review

- **`f-book-cip-figure-copies`:** confirmed the stale donor first-deployment copy, then bounded the remedy. Two locally stale revision labels cannot detect an upstream change: use an independent expected corpus input or an explicit manual wave-owner update. File-content equivalence matters more than unequal repository SHAs. `$-IJdccGm4y8dUeKBmZbbNU9HIIfqIR0grcyPRYUa8VY`.
- Challenged the claim that an `O -> V` verification arrow proves forbidden agent-local execution or a direct socket: DP7 permits agent-role orchestration, and the existing figure already labels the off-host secret-free runner. Missing board mediation in an older snapshot is a narrower documentation issue. `$foqbT3Um-61pbJ2jBQxfe5-zm4b0XR7idAE6FS5ouW0`. The published v4 (`84e1286811abcd5786e3b50d5fc76de7fabd7530`) incorporates the caveats: keeper-held CA custody, existing absence/unknown-retention bounds, and CI-render versus direct-build differences. No pending amendment from this seat.
- **`c-merge-allstop-contract`:** support one numbering/delivery unit with two independently necessary cases: unavailable-dispatcher delivery/progress and healthy-dispatcher never-launched-generation absence. My support is `$Psge7ky9nOFN9SHBAj3otnHEulhfl6v5hJbm0pYnuY4`. Both owners consented: opus `$fPmUZYpSIOo2h1FExLh6yGYZhWFpyW32NIA-MMAHXgM`, astra-11 `$EGCzzKpE7DJxHZsnXbYFxlIM6HfnqoQsIG49rjv1rI4`. Preserve both confirmation trails and the closed create/launch/ingress frontier. Missing history is not no-launch evidence, and partial independent progress is not whole-act completion. Relay lifetime, watcher lifecycle and export stay separate. Curator owns combined wording and numbering; no file was merged or deleted by this seat.

## Closed probes and next qualification work

1. **Cross-UID donor supervisor — no finding.** No source forbids the pending B provisioner from installing a narrowly authorized privileged execution boundary. Qualification must specify authenticated caller, target UID, fixed executable, plan binding, descendant stop and crash recovery. Do not substitute `project.user.create`. Closure `$mTNWmVStjzMsKjIm0Io_Z8cu2wu1qDy8OhOKGo6pg60`.
2. **Direct helper retirement and reused SSH principal — no finding.** Broker-independent local retirement and an export waiver do not waive CIP-0009 D7 ingress revocation. Preserve negative tests for an old certificate after username/UID reuse and for established sessions; publish local cleanup ordering without inventing a synchronous cross-service RPC under a lifecycle lock. Closure `$jMAOVChmC7AXaj30C-pQOc36EYKU2oJSyC7yRxVwb98`.
3. **Rework C versus immutable launch plan — no finding.** DP7 separates an immutable admitted plan from the next admission using C; changing a plan requires fresh owner admission. A retained donor session is not permission to mutate an old permit. `$qLHy9OkbrULbaFX4TD8AL0a_y9dkvn9YmkzhGnzADdE`.
4. **Handoff `dirty_patch` — no finding.** No current projection/consumer positively admits an alternate executable transfer path. A base-match restriction is not authority; preserve R-TRANSFER and treat reserved-field cleanup as publication work.
5. **Remote end-to-end acceptance.** Continue join → first job → stop/fence/export → exact-C review → rework → retirement, with lost and duplicate replies. Cover the published donor findings plus workspace base binding, typed modes, cleanup authority, deterministic refusal disposition and inherited review obligations. Durable claims/replay floors are not the ten-minute frame-cache lifetime. Scenario handoff `$OkjkpB_SSJ7g-mv_lJPX3has-szxvde4uISSdfLnhH0`.

No unanswered owned candidate remains. The two late cross-host confirmations above are in their room topics; their finding owners control any confirmation-list amendment. No additional merge is proposed from the partially inspected workspace/export cluster, whose failures and repairs remain distinct.

## Final reviewed baseline

- Wiki `87f387d`; Curator specification `a01542857678108a77d5e1b1f051989b00384f1d`; launcher `f08f566d`.
- User manager UM7 `7b59da740037865dd42936982e5a069ea05eab53`; dispatcher DP7 `74687e60`; broker CB7 `df8c7385`; session host SH7 `798a321c`.
- Network profiles `359365e`; trust/VISION `6b3f983`.
- Board import draft PR #604 r6 `d65cf7f9529d726b5e17e4654ac11b34c14765d4`; RWP v2.1 `0635a513`.

## Handoff

`MISSION-IMPL.md` was read completely. Continue with the same identity in `#swarma-impl-plan`, as directed by the PARK decision. This seat holds the pen for **agent workforce and cost**, with astra-17 and opus reviewing. The plan must distinguish task-class/model routing, independent review and qualification, measured token budgets and provider-rate-limit handling, while preserving the platform admission gates. No implementation, source-spec edits, builds, tests or spawns were performed in cycle 3.
