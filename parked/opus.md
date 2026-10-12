# Parked: macmini_swarma-review-2_opus

- **Date:** 2026-10-12.
- **Identity:** `macmini_swarma-review-2_opus` (Claude Opus 5.5).
- **Lens:** reliability and recovery: failure, crash and recovery paths; reconciliation; unknown versus absent; idempotency; fences and epochs; durability ordering; maintenance and restore.
- **PARK:** decision by ivan-curator in `#swarma-review-2`, topic `rounds`, event `$zTT0jikPpXgzoLY2F1oawRrPL4sUCDzzccdlq7bsqpI`. The register was F-12 … F-28, with F-26 withdrawn, at `72c6236`. My last round markers are round 9 `$2MJ_3FPjCfLur_Rk9-ARvK0NBRoKFT_9XLWWyx5328Q` and round 10 `$w8S7eis2uG0c6ecFiM_m6vXEDjIhaTQ-3aRFi03-DJ0`. No analysis was started after PARK.
- **Sources read at the cycle-2 pins:**
  - book v0.8 (wiki `17569de`);
  - user manager 0.6 `e58b0726`;
  - dispatcher 0.6 `e06fcfee` (with v0.5 `5d0476d` for history);
  - broker 0.6 `a0e6ab95`;
  - session host r8 `3a253016`;
  - agent launcher `22973272` §10;
  - curator-spec `601cbb09` (CIP-0009, CIP-0011);
  - platform architecture contracts (`e5781c8`);
  - `wiki/decisions.md`;
  - a2a `docs/protocol.md`;
  - installed sshd, git and launchd manual pages for platform semantics.

  This was a documentation review. No source was changed and nothing was built, run or measured.

## Own entries

| Entry | Subject | Confirmed by | Limits and weak spots |
|---|---|---|---|
| F-13 | `exec.stop` signals the receipt session but verifies all account processes since the receipt, so escaped descendants make stop, cleanup and capacity release non-convergent. Fix: one termination scope shared with retirement; current-execution fence; persistence denial. | astra, fable | Persistence-denial mechanisms (cron, at, launchd user domain) are per-OS qualification rows, not claims. Unkillable processes stay honestly unknown. Relies on one execution per generation. |
| F-14 | Standing and kept allocations have finite credential authority but no renewal path. Fix: journaled rebind; renewer already in the chain; never widens; expired versus revoked; honest scope. | astra, fable | Rebind interrupts running leases unless a qualified handoff is published. With F-23, renewal is a human-presence act. |
| F-17 | User-manager and dispatcher state loss or restore: identity resurrection, non-repeating generations that only move forward, ledger store epoch, shared restore fence, reverse inventory. | astra, fable | Reader epochs help only while reader evidence survives outside the restored domain. An undeclared, internally consistent whole-machine rollback is undetectable locally, the same limit as F-9. |
| F-18 | Per-class process fate and containment table, plus a fence against writers from a replaced daemon instance. A per-execution unit is recommended, not mandated. | astra, fable | The specs publish no unit configuration. systemd, launchd and sudo behavior is cited from documentation, not measured. Resource ceilings are a separate future capability. |
| F-21 | Time assumption: watermarked authority time (max for expiry, min for `not_before`); destruction gated on accumulated monotonic time; detect-and-hold; startup time confidence. | fable, astra | A proposed contract for qualified clock faults, not a proof. A poisoned watermark needs an operator reset that preserves trusted expiry evidence. |
| F-22 | Receiver outcome classes on the existing six R-OBS states. `exec.stop` continues under its effect ID with the latest-receipt fence; pre-admission rejections retry as fresh admissions; continuation never creates authority. | astra, fable | Replay safety follows from journal, authority and reconciliation correctness, not from classification. Retirement non-convergence was withdrawn because recovery-first covers it. |
| F-26 | **Withdrawn** by me (`b627be6`) after astra's simplicity test. Caller release makes nothing discardable beyond local compaction. Kept as design input to F-10's gate: compact terminal step journals; state-based refusal for target-bound replays; an identity index only for create/bind, which grows like the ledger; a request-carried floor only if bounded identity storage is ever required. | fable (release safety); astra dissent | A withdrawn note, not a finding. |
| F-28 | No service-wide state-transition lock across a synchronous call to another platform service. Ownership locks exempt; effect fixed at intent but no authorization cache; epoch-bound calls; revalidation of late results; per-record in-flight serialization; acyclic wait/lock graph. | fable, astra | The concrete wait/lock graph, the cancellation linearization point and bounded in-flight concurrency are publication and qualification work. |

## Peer entries I validated

| Entry | My contribution |
|---|---|
| F-12 | Unmatched broker authority, global-lock coupling, and stalls during the F-9 fence. |
| F-15 | Per-record quarantine refinement; confinement of receiver-assigned identities. |
| F-16 | git `safe.directory` evidence; hooks and `core.fsmonitor` as cross-account code execution. |
| F-19 | Contradiction: the `nologin`/`false` shell blocks sshd ForceCommand. Cleanup proof only at execution granularity. |
| F-20 | Five recovery rows for successor starts. |
| F-23 | A command gate does not protect key custody. A dedicated no-harness operator account keeps the Ed25519 format; the Secure Enclave is P-256 only. |
| F-24 | Scheduled re-verification of install-time rows; fail-closed start as part of readiness. |
| F-25 | Launcher "recover first" contradicts F-6's bounded pre-exec path. Dependency-scoped recovery. |
| F-27 | Platform-spec evidence; pin the bounded profile in `input/1`; journaled re-apply of a narrowed catalog to existing (standing) allocations. |

## Open threads at parking

- None of my own. No candidate of mine awaits confirmation, no question addressed to me is unanswered, and no append is pending.
- All entries are `proposed`. Peer confirmation is not operator adoption.
- The amendments to F-13, F-14, F-17, F-21, F-22 and F-28 that folded in late confirmations are signed and on main.

## What I would examine next

1. **Publication follow-ups for F-28:** the concrete wait/lock graph per service, the cancellation linearization point and bounded in-flight concurrency.
2. **Dispatcher request freshness.** §3.4:108 cites a request "validity window" that §8.1 does not publish. Dedupe rests on unbounded `request_id` retention, so an old signed request is re-admissible after state loss (F-17). A validity window and an identity floor solve different problems.
3. **Restart after daemon loss or reboot in the supervisor backend.** It has no restart path for standing executions; F-20 covers SH2+ only. Decide whether operator restart is the intended v0 behavior and say so.
4. **Claim `epoch`.** It is written, passed to the launcher and stored in the receipt, but nothing increments or validates it. Remove it or specify its fence.
5. **Defaults versus standing teams.** Two concurrent executions per caller conflict with a standing team owned by the operator principal, and a capacity claim's `expires_at` has no value for standing executions.
6. **Partial rollback detection.** Use cross-component high-water marks, such as the broker revocation sequence returned by `revocation.check`, to detect undeclared rollback. This complements F-9 and F-17; it does not replace them.
7. **Qualification evidence for F-13, F-18, F-21 and F-24 per OS:**
   - macOS updates restoring `/etc/pf.conf`;
   - launchd process-group cleanup after `setsid`;
   - sudo `use_pty` (a process-group leader cannot `setsid`);
   - cgroup delegation;
   - NTS availability.
8. **Fable's lower-confidence note:** declared-key destruction before deletion may be vestigial once the generation is `retiring`.

Resume only on the operator's instruction. Start from the operator's dispositions of F-12 … F-28 and from any new spec revisions, not by re-reading this cycle's topics.
