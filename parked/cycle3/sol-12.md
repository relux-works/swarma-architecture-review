# sol-12: cycle 3 parked

Identity: `ivmbp_swarma-review-3_sol-12` on ivmbp. Lens: end-to-end scenarios, concentrating on credential lease and revocation after coordination with the other scenario seats.

PARK: ivan-curator's event `$vw0OI2CLh_T3kUEAHCIQ6nyjwrdqqDcBz3KqiZvsn0o`, 2026-10-13. No owned candidate remains unconfirmed or unpublished.

## Delivered

- `cycle3/findings/f-book-env-report-client.md`, signed commits `13ab17a220e54736510d12b9dd7d41488a83a53a` and `633beb1a666d9cfbc92a3dd7953f9ac974c8bb50`, published on main. X3 replaces the env executor, explicitly leaves no broker client after exec, then reuses E for the Claude-inclusive authentication-error callback and common `event.report` arrow. CB7 expressly excludes that surviving env client and leaves the env reporter unspecified. Branch by holder lifetime; preserve the external-token holder and the open env reporting/reauthentication workflow. No host credential consumer, automatic restart, new authority or demonstrated runtime failure is inferred.
- X1 is a weaker adjacent clarification in the same finding: label a later lease request as a fresh admitted executor invocation, and renewal as a surviving external-token holder. Its refusal rule, no-Claude-renewal note and delivered-token lifetime limitation remain correct.
- Original confirmations: mini astra-03 `$-bzszpTzA_3pzsx-vWlbGtmunmsbUzJwhuQRvoXzpF0` and mini wonder-01 `$LRzv2nsoKqTgn1ir1ECFp4ZJmHvNVuGknSpdYI1BVu4`. Astra-03's narrowed X1 confirmation is `$WCkp4r8NgtVxJwqCgrXmjHGQ-oYbmP6xlpQuEynTzcc`. The published record cites these events.
- Additional independent confirmations, retained in the room: ivmbp sol-11 `$fbIk8Dx9BjAuLlS6Yh6ERAZhKA510_1wiwzEzP5MCaw`; mini wonder-02 `$Ew1JfOoyLKM5W7jmIdAC2jvwAwHGxflPh4pquBebBaU`; ivmbp astra-17 `$A3eCpTuBWtlFMj1tSJMp3QfKFrKSdNmeb6beL6GSk-g`; ivmbp astra-19 `$tmahexBZJldoGRVUyJ0gOf61VwJai1JoFwmoG6hDJF0`. All preserve the bounded X3 defect and weaker X1 interpretation. No additional finding or count follows from these confirmations.
- Latest publication receipt: `$RFKZ0i5JVetYVcichEzF9BBiWAecs7I3HqfzDsmr5As`; finding topic root: `$LvwIjBHxyo9sFMmRPXfaE04N2_5ravejlsroPZ_u1FI`.

## Completed scenario walk

Final-corpus pins: wiki `87f387d1109fb41213394a8d794dfbbbaefacba6`; CB7 `df8c7385`; DP7 `74687e60`; UM7 `7b59da740037865dd42936982e5a069ea05eab53`; SH7 `798a321c`; LR6 `f08f566`; CIP `a0154285`; trust contract `6b3f983`.

1. Plan composition and protected lookup: agent-side executor obtains material after the UID transition. The board runner and session host are not broker consumers. Caller and leaf delegation chains remain independently checked (CB7:126/134/405-406).
2. Bind and initial lease: a fresh connection under the active bound generation passes lease checks and final state-lock rechecks after asynchronous refresh. A prior dispatcher verdict is not a credential grant (CB7:451-459).
3. Delivery and renewal: env exec removes the executor broker client; external-token delivery retains its executor/private app-server holder. Renewal timeout does not permit a late response or native fallback (CB7:507/511/513/535-538).
4. Revocation: durable recording precedes acknowledgement and denies future lease/renew. Already-delivered material retains vendor validity; this is an explicit limitation (CB7:351/356/515).
5. E-rebind: old binding, leases and connections are removed before publishing the fresh binding. An old lease cannot renew through the new binding. Live handoff remains gated and explicit park/restart does not bypass independent session-successor consent (CB7:407-415/481/504; SH7:188-202).
6. Broker replacement and restore: the old refresh writer and the vendor rotation outcome must both be resolved; absence alone is insufficient. Restore stays fenced until acknowledged revocation history is recovered (CB7:353-354/544-548).
7. Retirement: ordinary retirement unbinds first. Direct operator retirement during broker outage may leave durable cleanup, but a retired or reused generation cannot lease (CB7:421-427).

No additional module-level contradiction was established. Existing publication, cleanup and qualification gaps retain their existing owners. Only source/document reads, scoped diff review and signature/publication checks were performed. No build, test, renderer, web, spawn, task-board write or credential-store inspection occurred.

## Coordination, consolidation and next examination

- sol-01 covered standing-team/restart and phone/ALLSTOP; sol-11 covered one-shot/export/reboot; sol-13 completed the remote-worker walk. I took the unclaimed credential lifecycle after their replies, rather than duplicating those walks.
- Mini sol-03 completed the complementary late/lost lease and E-rebind response cut across stop, replacement and restore, with no new contradiction: `$FMPODCDkY80KWOKPfdi97ZyIqyjmKbDqaRSWlgzSFb0`. Sol-14's asynchronous verification-result/board-testing/exact-C landing cut is separate; my coordination answer is `$x3l833hoIqhENtjSsmSkfqlcqgUhJvRWPH86cl_mBMc`.
- Consolidation conclusion `$2qhHda-IPiYEBlh2a-dKUBF-YkM2uUGcuGgz2Dj_KGA`: this finding, `f-book-one-shot-export` and `f-host-credential-lookup` require distinct corrections even where they share figures. Coordinate the edits; retain their independent acceptance criteria. Their records already have cross-host confirmations. No merge proposed.
- The withdrawn `f-muse-minted-key-end` and `f-codex-network-activation` threads remain qualification inputs, not revived findings. Explicit exact-release/auth-only/containment, token-lifetime and rotation gates already prevent the alleged blanket activation paths.
- Next authorized document pass: verify X3's conditional holder-lifetime repair and X1's fresh-invocation label after publication; check that env reporting remains explicitly open until an actual authorized reporter is specified; preserve delayed-refresh, rebind, revocation-history and restore counterbounds when qualification documents arrive.

The delivered finding remains `proposed`; the review seat does not implement or accept it. Local research and tool evidence remain under `.temp/sol-12/`, principally `review-notes.md` and signature/publication logs.

## Session boundary

The PARK event also relays immediate track 2 in another room. This session's direct brief permits posts only in `#swarma-review-3` plus the single lobby join notice and explicitly requires ending after the parking note and ack. Track 2 requires a direct scope update; it was not entered from the peer-relayed owner statement. Cycle-3 parking is complete.
