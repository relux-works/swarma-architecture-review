# Align the book's reboot requester with the unresolved host contract

- **Lens:** End-to-end reboot scenario; book/spec consistency.
- **Status:** proposed.
- **Problem:** The reboot walk names a sole automatic requester in chapter 7, while the standing-team scenario, the book's open-item list and the host contract leave that choice unresolved. A reader could treat registry-only recovery ownership as settled before the corresponding decision and activation contract exist.
- **Evidence:**
  - `wiki@87f387d`, `book/swarma/ru/07-host-sessiy.md:87`: after reboot, recovery is requested by the project registry, described as the sole automatic requester; the assertion has no open-status marker.
  - The same revision, `book/swarma/ru/13-scenarii.md:9`: who requests standing-session starts after reboot is not yet named by the specification, explicitly marked open.
  - The same revision, `book/swarma/ru/14-gde-my.md:101`: who starts team sessions after reboot remains an open item.
  - `swarma-session-host@798a321c` (SH7), `spec/session-host.md:344`: the reboot requester, host or project registry, remains unresolved; either eventual requester is limited by the owner's session lifecycle authorisation. Publication and qualification still gate backend activation.
  - `wiki@87f387d`, `decisions.md:533`: the stable-team decision requires idempotent bring-up after reboot but does not select its automatic requester.
- **Proposed change:** Mark chapter 7's reboot requester as unresolved and align that paragraph with chapters 13/14 and the host contract. State that any eventual requester must remain within the owner's admitted session lifecycle authorisation. This finding selects no requester, changes no R-SESSION authority and adds no wire member.
- **Expected benefit:** The end-to-end reboot account consistently distinguishes settled lifecycle authority from the remaining requester decision.
- **Risks and costs:** One paragraph correction; preserve process-absence, permit, successor and fresh-authority gates. This is documentation status drift, not evidence of automatic restart, duplicate execution or a deployed recovery defect. No owner decision is challenged.
- **Affected specs:** `wiki/book/swarma/ru/07-host-sessiy.md`; cross-check against chapters 13/14 and `swarma-session-host/spec/session-host.md` question 2.
- **Confirmed-by:**
  - `ivmbp_swarma-review-3_wonder-12` (book/spec consistency lens), event `$gRkZWI34xXahFw0TNXJ2YghQVxt4xTYvVsy932MY4hs`, room `#swarma-review-3`, topic `f-book-reboot-requester`, 2026-10-13. Independently verified all three initial cites at wiki 87f387d / SH7 798a321c, added chapter 14's open item, found no later registry-only owner decision, and confirmed the narrow repair.
- **Discussion:** Candidate `$3mYqxOyGsEhVu30W1f9pEPcW3vqsqP-UHUsuWgc1cqg`; confirmation request `$UQVEHaAdvRLS5YuIdpXQRjOkOuu4hYiVjgOYFS6uTIo`.
