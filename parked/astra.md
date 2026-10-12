# Astra — cycle 2 parked

- Date: 2026-10-12.
- Identity: `macmini_swarma-review-2_astra`.
- Lens: simplicity, operations, component ownership and recovery cost.
- PARK authority: `ivan-curator`, room `#swarma-review-2`, topic `rounds`, decision `$zTT0jikPpXgzoLY2F1oawRrPL4sUCDzzccdlq7bsqpI`.
- Reviewed findings head: `72c6236`. The register has 16 proposed cycle-2 findings, F-12 through F-28 except withdrawn F-26. Cycle-1 F-1 through F-11 remained the accepted baseline.
- Last completed round: 11. Rounds 10 and 11 had no new confirmed finding after F-28. No own candidate or incoming question remains unanswered.
- This is a resumable park. No source specification was edited and no build or test was run; the work was document review.

## Own findings

All are in [FINDINGS.md](../FINDINGS.md), peer-confirmed with Matrix evidence and published by signed commits.

| Finding | Change proposed | Commit |
| --- | --- | --- |
| F-12 | Keep privileged retirement local; leave broker unbind and its pending obligation with the existing dispatcher/operator owner. | `a64df81` |
| F-15 | Keep recovery controls reachable and confine unresolved records only when identity/accounting uncertainty is demonstrably bounded. | `bc262e7` |
| F-16 | Give every agent UID private writable Git administration; qualify any authorized immutable object sharing and source/result handoff. | `bc262e7` |
| F-25 | Scope helper recovery by dependency and batch retiring-home work under the existing lock, retaining all fences and cleanup obligations. | `0334ed2` |

F-25 was renumbered after F-24 service egress landed concurrently. The final push preserved F-24 unchanged and appended only F-25.

## Cross-review outcomes to preserve

The confirmation scopes and evidence live in the findings and their room topics. Material refinements included:

- F-13/F-22: account-wide stop must fence the current execution; same-effect continuation must never signal a later successor. Pending accepted work is distinct from pre-admission refusal and transport uncertainty.
- F-14/F-20: finite credential authority requires an explicit renewal path. A signed one-start request is not recurring consent; successor admission requires owner-signed lifecycle authority, per-start fences and ordinary-work restart bounds. Reboot requester remains open.
- F-17/F-18: restored ledger consumers close before stale bytes become visible; evidence inside a restored failure domain cannot prove its own freshness. Publish actual process fate and replaced-instance writer fencing without promising universal survival or resource containment.
- F-19/F-24/F-27: service-owned workplace evidence, explicit cleanup blast radius, enforced egress at workplace activation, no per-UID rule for shared UID 0, and qualified service-network behavior. Prefer the protected Curator-profile identity/digest mapping over a new network grant dimension. Canonical policy proofs must match the actual listener and its lifetime.
- F-21: time confidence precedes authority evaluation and destructive expiry. Backward steps can revive expired authority; forward steps can open future not-before windows. Clock recovery must preserve trusted expiry evidence.
- F-23: protect both root-key custody and configured operator/owner roles. A CLI prompt alone protects neither copied key bytes nor unsigned privileged-UID calls.
- F-28: release service-wide transition locks around dependency calls while retaining ownership locks, immutable effect inputs, cancellation/epoch fences, conservative claims and bounded concurrency. Late results never resurrect work; stored verdicts are not continuing authorization. Final wording checked at `72c6236`.

## Open threads and next examination

There is no open review question requiring an immediate answer. The following are future publication or qualification work, not new confirmed findings:

1. Follow the owner's disposition of cycle-2 proposals before changing module specifications. For the four own entries, check the concrete ownership, operation-availability, workspace-materialization and bounded-cleanup contracts against the stated invariants.
2. F-10 retention remains gated publication work. F-26 was withdrawn at `b627be6` after the local-compaction comparison: an extra release operation adds no demonstrated benefit over retaining the required identity/digest/result/current-target evidence. Do not reinstate it as an accepted optimization. A future bounded identity index needs an explicit floor/backpressure design; it does not replace time-bounded request authorization.
3. Qualify the F-15/F-25/F-28 interaction: one unresolved record, one large or failing retirement, and one stalled receiver while unrelated status and authorized stop remain usable. Recheck cancellation, stale completion and daemon replacement at every unlocked boundary.
4. Examine other content-dependent privileged work, such as UID hygiene scans, against the bounded-work contract. No separate finding was claimed for this.
5. For F-16, establish the safe source/result handoff and the access/lifetime of any shared immutable Git objects; preserve private administration, fresh configuration and the admitted base.
6. For F-27, verify canonical digest semantics and listener reload/port-reuse ordering, plus narrowing of existing standing allocations. Network-owner evidence still leaves Codex login/refresh proxy behavior and per-OS firewall/DNS/loopback coverage unqualified; these were not tested in this review.

Resume from this clone and the latest `rounds` topic. Read intervening decisions and changed source revisions before reopening any candidate. Continue using the same a2a identity; do not duplicate the withdrawn F-26 or cycle-1 findings.
