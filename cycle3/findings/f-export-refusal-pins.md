# Give a deterministic export refusal a disposition path, so a worker-controlled tree cannot pin its round until an operator act

- **Lens:** reliability and recovery: export obligations, idempotency, unknown versus absent, abuse resistance (operator presence).
- **Problem:** R-TRANSFER makes export precede retirement, and home deletion waits for a recorded export or an operator waiver. The approved exporter refuses the whole export on tree properties the worker controls: a special file, any `.git` component however spelled, a case-fold or Unicode-normalisation collision, a gitlink, a root escape, or any exceeded file-count, per-file, total or binary cap.
  - Wave 5b makes the consequence explicit: "Recording a refusal does not discharge the export cleanup obligation." The only release is the export-obligation waiver, now classified as a widening operator act: authentication plus exact-content confirmation, once per act.
  - A retry cannot converge. The tree is quiesced, so a re-run of the pinned exporter yields the same refusal.
  - The round's account, home, UID reservation and live-allocation quota therefore stay held until an operator acts. Execution capacity is released after confirmed absence.
  - No path continues the work. Remote rework re-materializes only from a new candidate C and removes the old round "only after its export is recorded". A refusal produces no C. The board draft has a rework edge only for *import* refusals.
  - **Impact, narrowed by peers:**
    - A hostile remote worker pins its own workplace: there is no next round.
    - It can also force one phone-confirmed widening act per refused round, which is a lever on operator presence rather than node capacity.
    - Honest workers hit the same pin through ordinary accidents: names differing only by case, which Linux allows, or a generated file over the cap. For local trusted children this holds the caller's allocation quota (4 by default) until the operator acts.
    - A retained workplace still counts against the per-node live-allocation quota (16 by default; standing allocations keep live-allocation and concurrency quotas), even after its execution slot is released.
    - No multi-placement attack by one donor, and no permanent execution-slot retention, is claimed.
  - One forbidden or over-cap entry can coexist with valuable valid edits, so a refusal does not prove the work is worthless. Retention is a deliberate safety trade-off. What is missing is any disposition other than a per-incident widening waiver.

  This is a lifecycle gap in a draft contract, not an implementation defect.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher` at `74687e600e04817fa6e7a2e8904a9f7a3c83a1d8` (v0.11, wave 5b):
    - `spec/dispatcher.md` §5.2 step 3, line 324: whole-export refusal classes and the export-before-retirement obligation, "never silently dropped".
    - §5.2.1, line 345: `outcome` is `recorded` or `refused`; "Recording a refusal does not discharge the export cleanup obligation." Lines 361–362 and 366: the refusal reports one `reason_class` and one `offending_path`.
    - §3.2, line 114: the export-obligation waiver is a widening act with exact-content confirmation.
    - §5.4, line 394, and §7.1, line 441: the obligation survives expiry, failure, direct retirement and restore.
    - §3.5, lines 158–159: per-caller and per-node live-allocation quotas.
    - §9, line 539: capacity claims are released after confirmed absence.
  - The same repository, `diagrams/workspace-transfer.puml`:
    - lines 51–54: refused result → "retain export obligation; deletion blocked unless operator waiver";
    - line 60: only the valid change-set branch discharges;
    - line 75: "remove old round only after recorded export".
  - `platform/curator-host-helper` at `3da62ad45d02efb34784a935ca5a17bf3b42ba35` (helper text unchanged from `ae540c59`), `spec/helper.md`:
    - §4.4 step 3, line 202: ordinary retirement exports before `retiring`, with no launcher bypass; failed, partial or unknown evidence cannot discharge the obligation.
    - §7, line 443: exporter refusal classes and the obligation.
    - §3, line 108: unattended widening cannot be inferred from an old confirmation.
  - `curator/curator-spec` at `a0154285`, `cips/CIP-0009-donor-side-deployment-and-bridge.md` D5a step 7, line 196: the old round is removed only after its export is recorded.
  - spm PR #604 r6 (`d65cf7f`), copy at `swarma-review/context/inputs/worker-code-transfer.spm-pr604.md` §3, diagram lines 435–441: a rework edge exists for import hard refusals only. There is no export-refusal edge.
- **Proposed change:**
  1. **Keep four outcomes distinct.**
     - Recorded export: discharges the obligation.
     - Deterministic policy refusal: the draft's `refused`; retains the obligation pending a disposition.
     - Interrupted or unknown export (exporter crash, OOM, I/O error, deadline before a verdict): `pending`/`unknown` under the same effect with identical canonical arguments, retained by design.
     - Authorized discard.

     Two runs over the same quiesced tree that disagree are `contradictory`. Reuse the export effect identity and distinct execution evidence from `f-export-cleanup-authority`. Pin the exporter digest and cap values in the plan digest, and stop the walk at the first cap excess so a hostile tree cannot make export unbounded.
  2. **Bounded repair (no owner decision needed).**
     - The original caller may reopen a refused round's workspace for a bounded number of fix-up turns. The workspace is not re-materialized, so valid work survives. The refusal evidence goes only to the caller and the worker.
     - Fence, account-wide absence and export then repeat. A repaired export is a new, complete export, never a partial result turned into success.
     - Repair is forward work, not cleanup. It needs valid current work authority and a separately admitted continuation. It never inherits cleanup-only authority after expiry, and never lifts R-ALLSTOP, restore or other security holds.
     - The refused result and its export effect stay immutable terminal evidence. Each repair turn and each re-export gets its own linked execution and effect identity, so a changed tree is never replayed under an already-terminal export.
     - Each repair is a new fenced round on the same workspace under the same rules. Account-wide absence is confirmed before each export. The workplace write fence and the SSH ingress fence of `f-workplace-relay-quiescence` stay closed from quiescence through export, and reopen only for the repair turn.
     - The repair budget is fixed in the admitted plan and counted per round. When it is spent, the obligation stays retained and the per-act waiver is the only exit. Nothing is discarded automatically.
     - The worker learns only the refusal class and offending path(s), as a letter or task snapshot, never a partial change set. DP7 reports one `offending_path`. Listing offending entries up to a published bound is an optional schema extension that would let one repair turn converge.
     - This publishes the currently missing "continue the same workspace after round end" step.
  3. **Disposition of refusals that persist after repair: an explicit owner choice.**
     - (a) **Per-incident widening waiver**, as today. The file then records the operator-presence lever plainly as an accepted cost.
     - (b) **Standing operator disposition** per admission class or host: one content-confirmed, revocable operator record, "discard after a recorded deterministic refusal". The platform then applies it automatically, journals the refusal and the applied disposition, and reports both to the original caller.
       - DP7 classifies the waiver as widening, and helper §3 forbids inferring unattended widening from an old confirmation. Option (b) therefore **needs an owner decision**: it pre-authorises a widening act. It is not claimed to fit the existing pre-authorised narrowing grammar.
       - Automatic discard without such a record, or a release by the caller alone, would **challenge R-TRANSFER (2026-10-13)** and is not proposed.
     - Trusted-class allocations default to retain-and-repair.
  4. **Board flow.** Add an export-refusal edge to the board draft: no C; a repair round, or the next round on the last admitted base after the disposition.
- **Expected benefit:**
  - Honest workers recover from accidental refusals without the operator and without losing valid edits.
  - Hostile repeated refusals have a stated cost, (a), or a one-time policy, (b).
  - Export outcomes are mechanically distinct and replay-safe: unknown never becomes discharged, and refused never becomes success.
  - The remote rework loop has a defined continuation.
- **Risks and costs:**
  - Repair adds a same-workspace continuation and a bounded repair count to the round contract.
  - Listing offending entries carries worker-controlled path strings, but only to the caller and the worker. It is not retirement metadata, so F-1's closed metadata schema is unaffected.
  - Option (b) needs an owner decision and its own record format.
  - Pinned caps make cap changes take effect only for newly admitted rounds.
  - Residual: a hostile worker can spend the whole repair budget and still end at the operator act. With (a), the per-round operator cost is bounded, not removed. After expiry or revocation, a refused round can only be waived unless the owner designs a pre-authorised repair.
  - No change to unknown-versus-absent handling, whole-export refusal semantics or retention of partial or unknown exports.
- **Affected specs:**
  - dispatcher §§3.2, 5.2, 5.2.1, 5.4, 7.1, 15, 16 question 22 and `diagrams/workspace-transfer.puml`;
  - user manager §§4.4, 7, 12, 14 question 15;
  - CIP-0009 D5a steps 4 and 7;
  - session host §3.1 (round boundary), cross-reference;
  - spm PR #604 §3 flow and diagram;
  - book chapter 11 code-path section.
- **Confirmed-by:** Matrix room `#swarma-review-3`, topic `f-export-refusal-pins`, 2026-10-13:
  - `macmini_swarma-review-3_astra` (simplicity/operations), `$PvqpTOHk7qCeDWhZS8FeyLMMp4_cjNQZDDDRNCjjOvE`: confirms the operational retention consequence. It corrects the claim that deletion loses nothing transferable, requires automatic deletion or a caller waiver to be labelled a challenge to R-TRANSFER, and keeps partial and unknown retention. All adopted.
  - `ivmbp_swarma-review-3_astra-19` (abuse controls), `$Ny39KoFe6Y5YCOnFsVANusVnrmiMFL3kRDPToJw4KPI`: confirms the allocation pin from the figure's refusal branch and finds no refusal/rework edge. It keeps deterministic refusals distinct from I/O, OOM and unknown outcomes, and limits the impact to live allocation, UID and home. Adopted.
  - `ivmbp_swarma-review-3_astra-15` (R-TRANSFER), `$4V0eoCqrtm2bndAUG_AkfjmYLcvVYaStLRwanyxJdL4`: confirms the liveness and abuse trace. It refutes harmless automatic deletion and proposes a standing disposal policy or bounded repair with four distinct outcomes. Adopted.
  - `macmini_swarma-review-3_fable` (trust/threat model), `$3PH4hfVA-hSicDh7K4HuuM0yebPz_7KI6_l5359fkk8`: confirms. It narrows who is pinned (the hostile worker's own workplace; the operator-presence lever) and notes that accidental refusals are a usability cost. It proposes the standing operator disposition, adopted as option (b), marked as needing an owner decision because DP7 classifies the waiver as widening.
  - DP7 rechecks, after the revised scope:
    - `ivmbp_swarma-review-3_astra-11` (dispatcher), `$nl26m2aohn8r3LAPoRc4Y4NY27bDofBHMVSmOxM44uY`: the refusal branch at 74687e6 still retains the obligation. Automatic refusal-as-discharge would change R-TRANSFER policy.
    - `ivmbp_swarma-review-3_astra-15`, `$iPgsnZk04KFk7bdUcamn0-E5R1OhPW7D_n4DYOGCQWc`: §5.2.1:345 is explicit. A retained standing workplace consumes per-node allocation capacity. A standing disposal policy is an explicit owner choice. Adopted.
    - `macmini_swarma-review-3_astra`, `$SsgqTO6O2HqjnxxKdeM32AG5MnyvTjDkD9jTBqZtl3c`: the revised scope is sound, provided repair needs current work authority and a separately admitted continuation, and each repair attempt keeps its own linked identity. Adopted.
  - Repair conditions:
    - Core astra `$jnz7HHnTum7RT7QM9cYEvDcLnsVH819bUML35urdQ0c` and fable `$FSdi6bteNi6f3trnJErYV-t2k2jtanpYFxtUdu0KyJA` agree that a standing discard policy is a new owner decision. Fable gives four trust conditions for bounded repair.
    - astra-11 `$NF8TgtoJXQSRXsoxGbBN5dYKOzGxRy7sI39YAZ6afiw` and core astra `$NIaADAY8eakcWzQ6A1ssPI_Q4FiBxv66eIslPTySVLw` refute repair as cleanup continuation: repair runs the worker, so it is forward work needing current authority. Fable accepts this in `$xugOcXWdEFyy08f7zibiG_1Z1u1x1B6jAfSb_1o3Xrc`.
    - The remaining conditions (fenced same-workspace round, plan-bounded per-round budget, class and path only) are adopted above.
  - Proposal `$vc7Ie_X8ANWJBL1F5LoJQl53zBXFE26UYLtQG01UiZs`; review request `$RGmGgkoCjCjzQpUL-DCUwmBBuhwlBdJoGwR_4vP12Oo`; revised scope `$SvuheVv1VzWhXIEADzqrUyEVNSHbcbhkm_AHAHGtaHg`.
- **Status:** proposed. Revalidated against dispatcher wave 5b `74687e6` and user-manager head `3da62ad` on 2026-10-13. DP7 made the retention explicit (§5.2.1 line 345) and classified the waiver as widening (§3.2 line 114). The confirmations were given against `19a75e63`, and the problem is unchanged. UM7 remains pending.
