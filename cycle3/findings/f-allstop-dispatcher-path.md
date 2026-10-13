# Deliver R-ALLSTOP to every service without the dispatcher, contain before stopping, and fence in-flight launches

- **Lens:** reliability and recovery: emergency-stop delivery, containment order, fences, all-stop recovery.
- **Problem:** R-ALLSTOP is one manual node-wide narrowing act with separately journaled parts: hold, process stops, range deny-all, broker freeze, and host delivery closure. The published specs give it no complete delivery or ordering contract that works without a healthy dispatcher.
  1. **The dispatcher is the published coordinator.** It initiates the hold and the per-generation stops, and its `activation.puml` routes the whole act through it (operator → dispatcher → user manager, broker, host). The host figure did the same at `70c9d97`; SH7 withdrew that and selects no coordinator, so the host figure is no longer relay evidence. An absent daemon refuses, and even the recovery and control surface needs exclusive state ownership, a compatible schema and journal replay. A crash-looping dispatcher, unreadable or restored state, or a mid-swap R-MAINT window therefore leaves no complete one-act path.
     - Partial manual capabilities do exist. The user manager's `operator` role may run all helper operations, including the range deny-all, through a password-authenticated terminal path. But they are not the one act: the phone-to-helper transition is unpublished, `exec.stop` is allowed to the dispatcher only, and no receipt-free, non-retiring stop exists (see `f-allstop-unstarted-generation`).
     - The case of a distrusted (compromised) dispatcher is not claimed here; it needs its own threat analysis.
     - The broker part no longer depends on the dispatcher: CB7 delivers the freeze directly. UM `components.puml` :96–101 also draws direct Operator→Firewall (range deny), Operator→Broker and Operator→Host edges, alongside Operator→Dispatcher hold and Dispatcher→Stop. Direct delivery therefore already exists in the corpus. The inconsistency is DP7's relay and serial order against those figures, plus the missing joint ordering and receiver fence. The dependency stands for the hold, the per-generation stops, and the range deny-all and host closure as DP7 routes them.
  2. **The delivery paths disagree.**
     - Broker wave 5b states that the node-wide freeze is "an operator act straight to the broker".
     - Session host wave 5b (SH7) removed the dispatcher relay from its figure and now says "No coordination topology or coordinator is selected or implied".
     - The dispatcher's §6 text and `activation.puml` still relay every part through the dispatcher.
     - Three modules therefore describe three delivery models (direct, unselected, relayed) for one act.
  3. **No prompt-issue order.** The only published sequence issues the broker freeze and host delivery closure *after* a serial per-generation stop loop (TERM, grace, KILL, quiet period; `processes_remain` continues). The host figure disclaims crash order, and the broker leaves cross-service ordering unpublished. The cheapest node-wide cuts can therefore be read as waiting behind N stops. Once the broker receives its part, its final-delivery interlock already refuses queued or late material.
  4. **In-flight launches are not fenced.** Under R-LOCK the dispatcher issues receiver calls outside its state lock. A `launch.start` (worker, materializer or exporter) issued before the hold can execute after an earlier absence scan. The range deny-all does not stop a zero-egress local start. No receiver-side all-stop fence exists at the launcher.
  5. **Recovery scope is unpublished.** R-ALLSTOP is absent from the session-permit withdrawal list. The existing guards (an explicit stop stays stopped; only the fence holder may restart; stale completions never reopen) prevent an automatic restart, so no bypass is claimed. But the stopped set, and which sessions restart by whose act after the content-confirmed recovery, are not specified.

  This is a design-contract gap in an unpublished operator act, not a deployed failure.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher` at `74687e600e04817fa6e7a2e8904a9f7a3c83a1d8` (v0.11):
    - `spec/dispatcher.md` §6, line 433: the dispatcher sets the hold and journals a stop for every agent/workplace execution/generation through `exec.stop`; the other parts are separate journaled service effects.
    - §8.3, line 513: an absent daemon refuses, with no fallback; control availability needs exclusive ownership, schema compatibility and replay.
    - §11, lines 574–575: readiness and the installed emergency stop.
    - §9, line 542: the host-wide `hold` gate is read fail-closed.
    - §4.1, line 183: calls are issued outside the lock with in-flight markers.
    - `diagrams/activation.puml`, lines 44–56: O→D; hold; range deny-all; stop loop at 48–53; broker freeze at 54; host closure at 56.
  - `platform/curator-session-host` at `70c9d97`, `spec/session-host.md`:
    - §3.5, line 242;
    - §3.3, line 194: the permit withdrawal list, which omits R-ALLSTOP;
    - §3.4, line 213: an explicit stop stays stopped; only the fence holder restarts;
    - §7 question 16, line 355: recovery ordering is unpublished.
    - `diagrams/node-emergency-stop.puml`, lines 21–28: Control→Dispatcher, then Dispatcher→Manager, Broker and Host. Line 23 disclaims crash order.
    - At SH7 `798a321c`, the same text is at §3.5 line 246, §3.3 line 198, §3.4 line 217 and §7 question 16 line 360. The figure now draws each service acting on its own part and states at line 25 that no coordinator is selected or implied. The prose still has the dispatcher set the hold and the user manager journal-stop every generation.
  - `platform/curator-host-helper` at `3da62ad`, `spec/helper.md`:
    - §2, line 49: authenticated terminal helper path; the phone-to-helper transition is unpublished;
    - §3, line 102: the operator may run all helper operations, including the range deny-all;
    - §4.7, line 323: `exec.stop` is allowed to the dispatcher;
    - §7 step 2, line 397: zero processes and no unresolved claim under the generation lock before a start;
    - §8.3, line 502.
  - `platform/curator-credential-broker` at `df8c7385`, `spec/broker.md`:
    - revision note, line 10: "the node-wide broker freeze is an operator act straight to the broker";
    - §15.5, lines 805–813: journaled freeze, final-delivery interlock, explicit recovery; cross-service ordering unpublished.
    - `diagrams/revoke-and-unbind.puml`, lines 105–110: draws both O→D (the act) and O→B (the direct freeze).
  - `platform/curator-host-helper` at `3da62ad`, `diagrams/components.puml`, line 92: routes R-ALLSTOP Operator→Dispatcher.
  - Figure count (wonder-01): three of the four modules' figures draw two delivery topologies, and one drawn issue order delays the freeze and closure behind N stops. SH7's figure publishes no topology.
- **Proposed change:**
  1. **Fan-out, not relay.**
     - The operator command delivers one signed act (one act ID, one set of canonical bytes) directly to each service's existing operator intake. Each service verifies it and journals its part idempotently under the act ID, without waiting for another service.
     - The command reports per-service results and retries undeliverable parts, reporting them as unknown meanwhile.
     - The hold is set at act admission, concurrently with the fan-out, and never waits behind the service calls.
     - Publication guidance, not a confirmed defect: clearing one closure condition affects only that condition, and admission still requires every independent gate. The all-stop closure clears only by its explicit recovery act. The contract already states this conjunction: DP7 :519 lists maintenance, restore, hold and time separately; :433 and :575 require explicit recovery; CB7 :801 and :813 keep the freeze independent of restore. Only the encoding is unpublished: the dispatcher defines `hold` by its read semantics alone (§9 :542). No separate store or wire object per reason is mandated, and today's infrastructure HOLD practice is not evidence of the platform encoding.
  2. **Contain before stopping.** Issue the broker freeze, the host delivery closure and the range deny-all promptly and independently. Then run the process stops with bounded parallelism. Hold-last applies only to recovery.
  3. **Receiver-enforced launch fence.**
     - On receiving the act, the user manager persists a root-owned all-stop mark.
     - The launcher refuses every physical start under the generation lock while the mark is set. This includes approved workspace executors and calls already in flight from the dispatcher.
     - The mark is set before any generation is scanned for absence.
     - The same mark closes generation creation and activation (`user.create`, `fw.apply` activation), or the inventory records an authoritative closed-create frontier. Otherwise a `user.create` issued before the hold can complete after the inventory, and its new generation would be missing from "every generation" absence.
  4. **Stops without the dispatcher.**
     - State initiator and receiver duties: the dispatcher initiates E-stops when available; the user manager is the receiver that journals termination.
     - When the dispatcher is unavailable, the operator's helper path initiates generation-scoped stops under the act. Today that is the terminal path; the phone path follows once the transition is published.
     - Reconcile helper §4.7 (dispatcher-only `exec.stop`) with §3 (operator all operations). Use the receipt-free path of `f-allstop-unstarted-generation` for never-launched generations.
     - The dispatcher later reconciles stops it did not initiate: an operator-stopped outcome, claims released only on confirmed absence, no relaunch.
  5. **Recovery scope.** The content-confirmed recovery act names the stopped set and the per-session restart scope, keeping every existing barrier. Durable permit suspension, as R-MAINT withdraws authority, is one way to express it.
  6. **Align the specs.** Dispatcher §6, §11 and `activation.puml`; host §3.5 and `node-emergency-stop.puml`; helper §§3, 4.7, 8.3; broker §15.5 (already direct).
- **Expected benefit:**
  - The emergency stop completes when the dispatcher is absent, unready or mid-swap.
  - Credentials and delivery are cut without waiting for process stops.
  - No in-flight start lands after an absence scan.
  - Recovery says what comes back and by whose act.
  - The broker's direct delivery becomes the rule rather than an exception.
- **Risks and costs:**
  - Each service verifies the operator act itself.
  - The narrow phone-to-helper transition needs publication and qualification.
  - The launcher reads one more root-owned mark under its lock.
  - The dispatcher reconciles operator-initiated stops.
  - Qualification rows: dispatcher absent, crash-looping or mid-swap during the act; a launch in flight at hold; a never-launched generation; a part undeliverable and later retried; recovery with partial parts.
  - No owner decision is challenged: R-ALLSTOP stays one manual narrowing act with explicit recovery.
- **Affected specs:**
  - dispatcher §§4.1, 6, 7.1, 9, 11, 15, 16 question 28 and `diagrams/activation.puml`;
  - user manager §§2, 3, 4.7, 7, 8.3, 12, 14 questions 17 and 22;
  - broker §15.5, §18.17;
  - session host §§3.3–3.5, 7 question 16 and `diagrams/node-emergency-stop.puml`;
  - book chapters on the operator path and recovery.
- **Confirmed-by:** Matrix room `#swarma-review-3`, topic `f-allstop-dispatcher-path`, 2026-10-13:
  - `ivmbp_swarma-review-3_astra-11` (dispatcher, adversarial), `$_t63Q9J-X7JwYBePfUIBU-nGCFWQa3P_CAK0ZiMVqZg`: confirms the narrow dispatcher dependency and the containment-order gap. It corrects "stops nothing" (the operator's partial helper capabilities), places the hold at act admission, treats the two journals as initiator/receiver, and finds no demonstrated silent restart. All adopted.
  - `macmini_swarma-review-3_astra-02` (user manager/launcher), `$bpt_pO6UYVVhFhUykVtokD8EE5LFIDFyQe7Vrr_BSm0`: cites CB7's direct broker delivery as a cross-spec inconsistency, and adds the receiver-enforced fence for in-flight launches. Adopted as items 2 and 3.
  - `ivmbp_swarma-review-3_astra-14` (session host, adversarial), `$K9ZOM-CmBCSmrwwWkhBjz2R0y4ASMCk6FhWCMxdQwJc`: confirms dispatcher availability and prompt fan-out. It refutes silent restart and the two-owner reading, and notes that a compromised dispatcher needs separate threat analysis. Adopted.
  - `ivmbp_swarma-review-3_astra-19` (abuse controls, adversarial), `$6BxQcpv3Xpde-lX_h4MVS9x3USHx2VReKb43snv6dOA`: partial confirmation. No published dispatcher-independent delivery or receipt contract; the stop owner is inconsistent between host §3.5 and dispatcher §6; the ordering is ambiguous with an unsafe sequential reading. It narrows the failure claim and the recovery subclaim. Adopted.
  - `macmini_swarma-review-3_astra-04` (session host, first pass), `$za30C5nspqyw2Cc6ffm4ZPPogR2CT2Jvj8EB_l22M1M`: confirms the contradictory delivery ownership (CB7 `revoke-and-unbind.puml` O→B direct versus DP `activation.puml` :48–56) and the missing prompt independent fencing. The hold must close immediately. Receiver-side launch and ingress exclusion must cover already-issued starts before absence is final. It rejects the silent-revival and two-owner readings. Consistent with the narrowed scope.
  - `macmini_swarma-review-3_astra-01` (dispatcher, first pass), `$vq1HKgFSnK63YelQ5kOKwnuG-5CY2faZZDZXEXrkDdk`: confirms that DP7 `activation.puml` :44–56 routes O→D→H/B/SH and issues the broker and host cuts after the stop loop. Dispatcher :183/:390 provide no root-side fence before the absence scan. It adds the closed-create frontier (item 3) and asks that old both-figures and whole-freeze evidence not be kept. Both applied.
  - `ivmbp_swarma-review-3_astra-13` (broker, adversarial), `$DS9MpFD3q808869gznaUyO4tnTbInJa4HLslL10vh7I`: the SH7 correction, as applied; CB7's direct O→B path stands.
  - Latch amendment refuted as a defect, kept as guidance. `macmini_swarma-review-3_astra-01` `$U_giGyuuzZDOr3yH965MYEcCfb8xjL2xNt8_aRjif3g`, `macmini_swarma-review-3_astra-02` `$ymlti_B-lUoBrmVMgwaXfSCuH7Ie6cPe-9n2odX0UK0`, `ivmbp_swarma-review-3_astra-19` `$-GMCqyHFozs907WPcH7Foxv-qV49qtM3G8SSV1DK9ss`, `ivmbp_swarma-review-3_astra-13` `$otwLmBs6yW9X03iqfnyxeafzX4c-H2t9434OTAdLw7g`, `ivmbp_swarma-review-3_astra-11` `$MKpNDzRiaItD8RTf8THzGTTr9kmrg_zulW8gXE8I9FY` and `macmini_swarma-review-3_astra-03` `$WtAHsEwi_WvUCrHcY_AODhFbxRFe1dlAB2EkHUP2HAk` show that conjunctive, reason-specific clearance is already the contract. Applied.
  - `macmini_swarma-review-3_wonder-01` (spec versus figures), `$T7d9SGx8xBTPBS8pDF0Ra7G86fnvZiGRljKxDVnO8mc`: confirms the narrowed delivery contradiction at figure level and adds the CB7 and UM figure evidence above. Seconds the receiver-side fence. Refutes silent revival and two stop owners.
  - `macmini_swarma-review-3_sol-01` (scenario: phone and standing restart), `$5JBQvC7sN3kXyomttBP6K2PUKrgV2ydEV4ViMeES0Yo`: confirms the narrowed DP7/CB7 discrepancy. A delayed pre-hold E-launch needs receiver-side exclusion, because helper :397/:401/:402 can still start it. Completion must resolve pending launcher intent and keep the fence through the inventory frontier; an empty scan alone is insufficient. Consistent with item 3.
  - `macmini_swarma-review-3_astra-09` (abuse controls, first pass), `$S_P-butdChv2rLGa1gjmUkF7WfbBspnVq2VpXabyHT8`: confirms only the narrowed delivery, ordering and receiver-fence scope. It refutes shared-latch and silent-revival claims as current permissions; receiver exclusion must cover pre-issued launch, create and ingress. Consistent with the file.
  - `macmini_swarma-review-3_sol-01`, UM7 recheck `$Id6ohwAZorTqBSgTiRgSWXg_PoNGToX9FUw0WvsiZUg`: helper §8.3 :514 keeps the all-generation journaled scope. UM7 `components.puml` :96–99 draws Operator→Dispatcher together with direct Operator→Firewall/Broker/Host parts, a mixed topology beside the DP7 relay.
  - UM7 rechecks: `macmini_swarma-review-3_astra-01` `$XoHgfBNyB9E_C0ikkzEss7k4ZTEHsSZWko9St9Lonmk` (the DP7 relay and serial loop and the closed-create frontier survive; the latch stays guidance) and `macmini_swarma-review-3_astra-09` `$7bMjSglwW6TAsJjClEtBCIjsjVQNhjMzLJ7CVZ2PyoE` (direct operator edges in UM `components.puml` :96–101; avoid claiming every part depends on the dispatcher). Applied.
  - SH7 rechecks: `macmini_swarma-review-3_astra-04` `$AUv_fKEGW04UHtJglMWZmlrjbkSnqQMLAxHygbMfDc8`, `ivmbp_swarma-review-3_astra-11` `$K1RycZzyTh2HaVT6tkGgtyKxYpmh3IeZbFQmvfe1Jd4` and `macmini_swarma-review-3_astra-02` `$rEKRcXh41GTH31mwDq7ggQ3A1RicWIljJqpVbq5zmpg`. All three withdraw the old host-figure relay as evidence; SH7 selects no topology and publishes no delivery or issue order. The narrow DP7 relay versus CB7 direct-freeze inconsistency, the prompt-issue requirement and the receiver-side launch and ingress fence remain. Applied.
  - Proposal `$NrsF2Fas4w-yXlWgMDSQr04nulVUV1g43YfnyFxwmbI`; review request `$JGZWlsp-sZvsrFUAvRQhmG0cl99vHExWsAPTslkNzp4`.
- **Status:** proposed. Checked against dispatcher `74687e6`, user manager `3da62ad`, broker `df8c738` and session host `70c9d97` on 2026-10-13.
  - **UM7 recheck (user manager `7b59da74`, 2026-10-13):** substance unchanged; the corpus is final. The helper lines moved: §2 :49→:53; §3 :102→:106; §4.7 :323→:327; §7 step 2 :397→:401 (receipt :401→:405, drop :402→:406); §8.3 :502→:512; `diagrams/components.puml` R-ALLSTOP Operator→Dispatcher :92→:96.
  - Rechecked against SH7 `798a321c` the same day. SH7 removes the host figure's dispatcher relay but selects no coordinator, so the remedy is unchanged. The fan-out in item 1 would be the selection SH7 leaves open.
  - Distinct from `f-allstop-unstarted-generation`, which exists with a healthy dispatcher, and from `f-workplace-relay-quiescence`, whose ingress fence also applies during the all-stop.
