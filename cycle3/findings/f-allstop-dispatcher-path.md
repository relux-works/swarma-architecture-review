# Deliver R-ALLSTOP to every service without the dispatcher, contain before stopping, and fence in-flight launches

- **Lens:** reliability and recovery: emergency-stop delivery, containment order, fences, all-stop recovery.
- **Problem:** R-ALLSTOP is one manual node-wide narrowing act with separately journaled parts: hold, process stops, range deny-all, broker freeze, and host delivery closure. The published specs give it no complete delivery or ordering contract that works without a healthy dispatcher.
  1. **The dispatcher is the published coordinator.** It initiates the hold and the per-generation stops, and both figures route the whole act through it (operator → dispatcher → user manager, broker, host). An absent daemon refuses, and even the recovery and control surface needs exclusive state ownership, a compatible schema and journal replay. A crash-looping dispatcher, unreadable or restored state, or a mid-swap R-MAINT window therefore leaves no complete one-act path.
     - Partial manual capabilities do exist. The user manager's `operator` role may run all helper operations, including the range deny-all, through a password-authenticated terminal path. But they are not the one act: the phone-to-helper transition is unpublished, `exec.stop` is allowed to the dispatcher only, and no receipt-free, non-retiring stop exists (see `f-allstop-unstarted-generation`).
     - The case of a distrusted (compromised) dispatcher is not claimed here; it needs its own threat analysis.
  2. **The delivery paths disagree.** Broker wave 5b states that the node-wide freeze is "an operator act straight to the broker". The dispatcher and host figures still route the freeze through the dispatcher.
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
  - `platform/curator-host-helper` at `3da62ad`, `spec/helper.md`:
    - §2, line 49: authenticated terminal helper path; the phone-to-helper transition is unpublished;
    - §3, line 102: the operator may run all helper operations, including the range deny-all;
    - §4.7, line 323: `exec.stop` is allowed to the dispatcher;
    - §7 step 2, line 397: zero processes and no unresolved claim under the generation lock before a start;
    - §8.3, line 502.
  - `platform/curator-credential-broker` at `df8c7385`, `spec/broker.md`:
    - revision note, line 10: "the node-wide broker freeze is an operator act straight to the broker";
    - §15.5, lines 805–813: journaled freeze, final-delivery interlock, explicit recovery; cross-service ordering unpublished.
- **Proposed change:**
  1. **Fan-out, not relay.**
     - The operator command delivers one signed act (one act ID, one set of canonical bytes) directly to each service's existing operator intake. Each service verifies it and journals its part idempotently under the act ID, without waiting for another service.
     - The command reports per-service results and retries undeliverable parts, reporting them as unknown meanwhile.
     - The hold is set at act admission, concurrently with the fan-out, through the host-wide fail-closed `hold` gate. It never waits behind the service calls.
  2. **Contain before stopping.** Issue the broker freeze, the host delivery closure and the range deny-all promptly and independently. Then run the process stops with bounded parallelism. Hold-last applies only to recovery.
  3. **Receiver-enforced launch fence.**
     - On receiving the act, the user manager persists a root-owned all-stop mark.
     - The launcher refuses every physical start under the generation lock while the mark is set. This includes approved workspace executors and calls already in flight from the dispatcher.
     - The mark is set before any generation is scanned for absence.
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
  - Proposal `$NrsF2Fas4w-yXlWgMDSQr04nulVUV1g43YfnyFxwmbI`; review request `$JGZWlsp-sZvsrFUAvRQhmG0cl99vHExWsAPTslkNzp4`.
- **Status:** proposed. Checked against dispatcher `74687e6`, user manager `3da62ad`, broker `df8c738` and session host `70c9d97` on 2026-10-13. SH7 and UM7 remain pending; recheck host §3.5 and helper §8.3 when they land. Distinct from `f-allstop-unstarted-generation`, which exists with a healthy dispatcher, and from `f-workplace-relay-quiescence`, whose ingress fence also applies during the all-stop.
