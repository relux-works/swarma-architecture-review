# Parked: macmini_swarma-review-3_opus

- **Date:** 2026-10-13.
- **Identity:** `macmini_swarma-review-3_opus` (Claude Opus 5.5 at max; the requested `claude-opus-5-6` is not served).
- **Lens:** reliability and recovery: crash and recovery, unknown versus absent, idempotency, fences, export obligations, watcher narrowing, all-stop recovery.
- **PARK:** decision by ivan-curator in `#swarma-review-3`, topic `rounds`, event `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o` (03:11:52Z).
- **Final source pins:**
  - dispatcher `74687e60` (v0.11, DP7), including `schemas/workspace-result-1.schema.json` and the figures;
  - user manager `7b59da74` (UM7);
  - broker `df8c7385` (CB7);
  - session host `798a321c` (SH7);
  - launcher `f08f566d` (LR6);
  - curator-spec `a0154285`;
  - network profiles `359365e`;
  - trust contract `6b3f983`;
  - spm PR #604 r6 (`d65cf7f`) and RWP v2.1 from the context inputs;
  - wiki `87f387d` (`decisions.md`, book chapters 11 and 14).

  Docs-only: nothing was built, run or measured.

## Own findings (all `proposed`, signed on main, revalidated at the final corpus)

| File | Subject | Confirmed by | Limits |
|---|---|---|---|
| `f-export-refusal-pins` | A deterministic whole-export refusal never discharges the R-TRANSFER obligation; only a per-incident widening waiver releases the round. Fix: four distinct outcomes; bounded repair under current work authority; an owner choice between per-incident waiver and a standing disposition; a permission-denial disposition; a board export-refusal edge. | astra, astra-19, astra-15, fable, astra-05, astra-11, wonder | Automatic discard or caller release would challenge R-TRANSFER and is not proposed. A standing disposition needs an owner decision (DP7 classifies the waiver as widening). Determinism covers only the outcome class and the recorded digest. Infinite retry is not claimed. |
| `f-allstop-dispatcher-path` | The R-ALLSTOP delivery models disagree: DP7 relay, CB7 direct freeze, UM mixed topology, SH7 unselected. The drawn order issues stops before freeze and closure. No receiver-side fence covers pre-issued launches and creates. Recovery scope for stopped sessions is unpublished. Fix: fan-out; contain first, with stops not waiting on acknowledgements; a launcher, create and ingress fence; initiator and receiver duties; recovery scope. | astra-11, astra-02, astra-14, astra-19, astra-04, astra-01, astra-13, wonder-01, astra-09, sol-01, astra-03 | Containment and stops proceed without the dispatcher, but the dispatcher's own part, and whole-act completion, need it. The shared-latch bypass was refuted and kept as guidance. Silent restart and two-owner readings were refuted. The compromised-dispatcher case is not claimed. |
| `f-watch-freeze-lifecycle` | The watcher's egress freeze lacks dominance over later re-applies, a release, a version placement and `fw.apply` outcome tables. Fix: per-generation ordered narrowing records; an operator release separate from restart; independent freeze and stop; proxy-session scope; a v0 availability gate; collection-time telemetry provenance; the exporter not blocked by a freeze. | astra-12, astra-19, astra-06, astra-09, astra-01, astra-11 | The effect, linked-pin and re-apply machinery already exist. Re-creation is not mandatory. Generation attribution is existing intent (UM `components.puml` :89). |
| `f-base-binding` | Archive, plan manifest and commit B are never mechanically cross-checked, so a mismatch yields misattributed deltas in C (reverts, deletes, adds). Fix: verify the archive against the manifest at materialization; recompute the manifest from repository B at import, never from the orchestrator's plan. | wonder, wonder-03, astra-05, fable, astra-15 | Existing exact-B integrity rules make a mismatch invalid; this is a pre-publication verification gap. It does not prove worker authorship or remove the compromised-exporter residual. |

**Consolidation:** astra-01 proposed merging `f-allstop-dispatcher-path` and `f-allstop-unstarted-generation` into one R-ALLSTOP finding with separate delivery and inventory cases (`c-merge-allstop-contract`). I support it, deferring to astra-11's preference; separate F numbers with cross-references are equally sound.

## Withdrawn or declined

- **`f-enforcement-restart-lifecycle`** (applied state versus reboot and proxy restart): withdrawn. astra-16, astra-12, astra-06 and sol-11 showed that the per-start network gate, start-time re-verification and the service-generation binding close the stale-record trace. The residue is design input to helper §14 q12/q14 and dispatcher §3.4: boot reconstruction order, current-boot validity, the proxy-restart re-apply trigger.
- **The all-stop shared-latch amendment:** refuted as a defect by six seats; kept as guidance.
- **Not raised:**
  - the watcher auto-restart probe (host §3.7 parks without restart);
  - Muse minting ambiguity (already open qualification);
  - materialization folded into `curator-run` (would split the local and remote paths);
  - test-UID reservation (inside helper q18);
  - the `round` field (design input per astra-05 and astra).

## Peer findings I confirmed or refined

| Topic | Contribution |
|---|---|
| `f-export-cleanup-authority` (astra) | A distinct execution identity per transfer launch; cleanup capacity not competing with forward work; blob durability before discharge (accepted, `be50b37`). |
| `f-envelope-intent-replay` (astra-14) | Module receivers compare full canonical arguments, opposite to ADM's body-only rule; the `control.*` successor case. |
| `f-host-output-accounting` (astra-04) | Dispatcher log bounds are lost at the SH2 switch; the §9 disk gate omits the host store; a hard reserve for stop, park and fence-close journaling. |
| `f-workspace-result-modes` (wonder) | Confirmed item 1 from the recovery side; the determinism narrowing applied to my own file. |
| `f-proxy-budget-incarnation` (astra-06) | Process-lifetime counters; a forward clock step resets the daily window early (F-21). |
| `f-unknown-data-replay` (astra-08) | Confirmed the Z18 drift. Liveness refinement: with the once-only replay removed, an undecidable delivery keeps a session fenced indefinitely; a resolution path must be published. |

## Open threads at parking

- None of mine awaits confirmation.
- The consolidation decision above lies with the curator and astra-11.

## What I would examine next

1. **F-17 × R-TRANSFER.** Export obligations and the admitted plan live only in dispatcher records. After dispatcher state loss, reverse-inventory orphans do not show which homes hold unexported work, and a re-adopted orphan cannot be exported without the original plan (base, manifest, caps). Options: a helper-side obligation marker, and re-adoption from the caller's originally signed request.
2. **Standing-team restart after recovery events** (all-stop, maintenance, reboot): requester and consent. This joins the open reboot-requester question and `f-session-authority-renewal`'s acceptance cases.
3. **Remote-round end with in-flight tool calls.** The order of write fence, in-flight drain and account-wide stop, so a killed job's partial write is not exported as the worker's result.
4. **Resolution of permanently undecidable deliveries** under SH7 (see the `f-unknown-data-replay` refinement): authority and evidence semantics, with no timeout-derived success.
5. **Harness self-written state versus R-STANDING digest checks** on restart. Speculative; needs harness evidence.
6. **Per-OS qualification evidence** for the new rows: deny-ACL readability, listing versus search directories, launcher fence timing, proxy counter persistence.

Resume only on the operator's instruction, starting from the owner's dispositions of cycle 3.
