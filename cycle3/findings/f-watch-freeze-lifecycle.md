# Give the watcher's egress freeze a dominance rule, a release and a version, and publish `fw.apply` outcome tables

- **Lens:** reliability and recovery: watcher narrowing, idempotency of narrowing effects, version gating.
- **Problem:** R-WATCH requires automatic narrowing of one account on a hard threshold: "freeze egress" plus a journaled `exec.stop` (dispatcher §7.3, helper §8.2, broker §15.5, session host §3.7).
  - The general machinery exists. The dispatcher journals every downstream call under an effect ID. Helper §8 gives `fw.apply` re-apply its own effect and keeps admission and delivery closed on partial or unknown results. Dispatcher §3.4 requires linked narrowing pins with per-effect retry and recovery.
  - Four pieces are missing, and without them watcher narrowing has no defined recovery:
    1. **Dominance.** Nothing states that an active watcher freeze, recorded as a narrowing, dominates later starts, re-applies and recovery until an authorised release. Narrowing records are not ordered per generation, so an older admitted re-apply carrying the original pin could undo a newer freeze.
    2. **Release.** No act, owner or record releases a freeze. The host parks the session, durably records the stop reason and never restarts automatically (§3.7), so the account is not destroyed. But controlled in-place release and restart are unspecified, and a frozen trusted allocation's next start would fail late, at the broker's lease match against applied state.
    3. **Version.** Per-account rules exist only from helper v1, and the zero-egress apply encoding is unpublished. R-WATCH is placed in no version. In v0, "freeze its egress" for one account has no mechanism, and the node-wide range deny-all is not a substitute.
    4. **Outcome tables.** F-22's one-table-per-receiver-operation rule covers create, launch, stop and retire. It was not extended to the v1 mutations `fw.apply`/`fw.remove`, which waves 4 and 5 made into effects: provisioning apply, R-NETBIND re-apply, watcher freeze, and the all-stop range deny-all. The dispatcher's effect-ID table also omits `fw.apply`.

  This is a pre-activation contract gap, not a demonstrated runtime failure.
- **Evidence:** Paths are relative to `~/Developer/ReluxWorks/`.
  - `platform/curator-dispatcher` at `74687e600e04817fa6e7a2e8904a9f7a3c83a1d8`, `spec/dispatcher.md`:
    - §7.3, lines 470–472: freeze plus journaled stop; "cannot … silently restart the affected one";
    - §4.5, line 251: every downstream call has an effect ID; lines 255–263: the symbolic effect table without `fw.apply`;
    - §3.4, line 144: linked narrowing pin, per-effect retry and recovery.
  - `platform/curator-host-helper` at `3da62ad`, `spec/helper.md`:
    - §8.2, line 498: freeze plus journaled dispatcher stop;
    - §4.6.2, line 266: outcome tables for create, launch, stop and retire only;
    - §8, line 468: re-apply as its own `fw.apply` effect;
    - §13, lines 574–577: per-account rules in v1, with no R-WATCH placement;
    - §14 question 18: zero-egress apply encoding unpublished; question 21, line 603: R-WATCH request ordering deferred.
  - `platform/curator-credential-broker` at `df8c7385`, `spec/broker.md` §15.5, line 815: freeze plus journaled stop; watcher authority cannot reopen the all-stop. §5.5: enforced leases match the applied state.
  - `platform/curator-session-host` at `70c9d97`, `spec/session-host.md` §3.7, line 267: the host parks or ends the session with the reason recorded and never auto-restarts.
- **Proposed change:**
  1. **Dominance.**
     - A watcher freeze is a linked narrowing record for that generation, with its own effect ID.
     - Narrowing and release records are ordered per generation, so an older admitted re-apply cannot undo a newer freeze.
     - Every later start, re-apply and recovery uses the newest effective pin.
     - While frozen, starts refuse at admission with a typed, published reason, never by a later lease mismatch. Status shows frozen allocations.
     - The freeze does not block cleanup. The fixed approved exporter (no network, no worker code, under its own cleanup authority per `f-export-cleanup-authority`) still runs, so a watcher freeze never pins the R-TRANSFER export obligation (`f-export-refusal-pins`). The node-wide R-ALLSTOP launch fence is the exception: it holds exporters until explicit recovery.
  2. **Release.**
     - An explicit operator act (widening: authentication plus exact-content confirmation, refused from agent sessions) records a release that re-applies the admitted pin through the existing re-apply effect. Alternatively the allocation is retired.
     - Release is separate from restart authority: restarting still needs the owner's lifecycle authorisation or a fresh admission. Watcher action still never restarts anything.
  3. **Ordering.** Issue the per-account freeze and the journaled stop promptly and independently. Termination of a resource-abusing account never waits for a slow or unknown network result. Reconcile both effects, and retain claims and closure where evidence is unknown.
  4. **Version.** Place R-WATCH explicitly.
     - v1: the full per-account freeze contract.
     - v0: an explicit availability gate. Either the egress-freeze guarantee is not offered, so automatic narrowing is the journaled stop plus whatever published hold exists, or a v0 per-allocation hold or lease freeze is published with its own authority and receiver semantics. Neither retracts already-delivered tokens, and the node-wide range deny-all is never a substitute.
  5. **Outcome tables.** Publish R-OUTCOME tables for helper `fw.apply` and `fw.remove` on the six R-OBS states, and add `fw.apply` to the dispatcher's effect-ID table.
  6. **Qualification rows:** freeze and stop issued together; crash between them; re-apply, restart, reboot and recovery while frozen; an older re-apply racing a newer freeze; release followed by an owner-authorised restart; a start attempted while frozen.
- **Expected benefit:**
  - Watcher narrowing becomes durable, replay-safe and reversible only by an explicit act.
  - A false positive on a standing role costs one operator act and an authorised restart, not a re-created account.
  - The v1 firewall mutations gain the same outcome discipline as the other receiver operations.
- **Risks and costs:**
  - A per-generation ordering of narrowing records.
  - A release record and operator act.
  - Two outcome tables.
  - A version decision for v0.
  - No owner decision is challenged.
- **Affected specs:**
  - dispatcher §§3.4, 4.5, 7.3, 15, 16 question 27;
  - user manager §§4.6.2, 8, 8.2, 12, 13, 14 questions 18 and 21;
  - broker §15.5 (cross-reference);
  - session host §3.7, 7 question 18.
- **Confirmed-by:** Matrix room `#swarma-review-3`, topic `f-watch-freeze-lifecycle`, 2026-10-13:
  - `ivmbp_swarma-review-3_astra-12` (user manager/launcher, adversarial), `$18mYOHPImuQ0zLeCOIUMPqY8E6G8QzfcSJFn_xKBwp0`: confirms the missing outcome tables, the v1 placement and the absence of a freeze/release binding. It cites the existing effect, re-apply and linked-pin machinery as counterevidence to the broad wording, refutes mandatory re-creation, and requires that the stop not wait on the freeze. All adopted.
  - `ivmbp_swarma-review-3_astra-19` (abuse controls, adversarial), `$9dFwqb0DFC9FU58UWGT5dm145OSSkTQb-y_L5smW2hQ`: confirms the narrower lifecycle and version gap. It adds generation-bound ordering so an older re-apply cannot undo a newer narrowing, keeps release separate from restart authority, and asks for an explicit v0 availability gate rather than relabelling a hold or lease freeze as the egress guarantee. All adopted.
  - Proposal `$iriTdKhTcqr5PVKdtmNGtZTjAS6iq-a5XWb5oIpo2dQ`; review request `$67MCJHHQmsw_qcph2E0LoTiHLEvnbScXXIw5KNIKzgA`; narrowed scope `$0G-UuQmHNgPj0D5JoIpHEJ8CSkyDfULxl2lpvMaQGkQ`.
- **Status:** proposed. Checked at dispatcher `74687e6`, user manager `3da62ad`, broker `df8c738` and session host `70c9d97` on 2026-10-13. SH7 `798a321c` keeps host §3.7 unchanged in substance (now line 271). UM7 remains pending; recheck helper §8 when it lands.
