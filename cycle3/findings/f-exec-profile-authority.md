# The exec-profile reference is caller text: publish a machine-owned selection and digest pin, the F-27 shape for R-EXEC

- **Lens:** trust and threat model (fable); user manager and launcher cross-check (astra-02).
- **Status:** proposed.

## Problem

The task-class exec profile is the OS-enforced executable allowlist that decides what an account can run. It travels as "the task-class exec-profile reference" in the caller-composed plan, covered by the plan digest, and is checked at `prepare` and before every launch for existence against the host's capability matrix and class gates. No text says which profiles a given caller, placement or grant may select, and nothing pins the profile's policy body: hashing a reference does not freeze a mutable policy.

F-27 settled the same question for the network profile: caller text and caller home configuration are never authority; a root-owned machine policy maps the admitted Curator profile identity and lock digest to exactly one network profile and pinned policy digest, resolved and pinned at `prepare` (R-NETBIND). The exec profile has no counterpart. The orchestrator composes children's plans under its own agent account from its own home configuration, so a prompt-injected orchestrator can give an untrusted workplace the widest light-tool profile the host publishes, interpreters included, for a documentation task, and nothing in the published checks refuses. The class floors bound the damage (no compilers, package managers, network tools or harness binaries in any class), and `f-exec-input-closure` shows what an interpreter-bearing profile still permits.

This is a publication gap in the selection and pinning contract, not a claim that a deployment currently admits every existing profile; activation gates keep the path disabled.

## Evidence

- `swarma-dispatcher` at `74687e60` (v0.11), `spec/dispatcher.md:189`: the plan digest covers "the exec-profile reference"; `:296`: `prepare` checks the "exec-profile reference" among its gates; `:374`: `start` requires "the recorded class, current qualified host matrix and admitted exec-profile reference"; `:384`: "The plan carries the task-class exec-profile reference, covered by its digest"; `:316`: the orchestrator composes children's plans under its own account from its own Curator configuration; `:142-144`: R-NETBIND supplies the source-and-pin rules for the network profile that are missing here; `:735` (§16 q25): profile formats unpublished.
- `swarma-user-manager` at `ae540c59` (v0.9; unchanged at `3da62ad4`), `spec/helper.md:397`: the launcher verifies "the task exec profile" against host and class gates before a start; `:433`: per-task-class allowlists; `:441`: the plan records the exec profile; `:601` (§14 q19): profile encoding and enforcement open.
- `curator-agent-launcher` at `f08f566d` (LR6), `SPEC.md:1757-1765`: the composed plan carries the exec-profile reference under the plan digest; `:2006-2021`: the user manager owns the allowlist; neither names a selection authority.
- `swarma-session-host` at `70c9d97e` (r10), `spec/session-host.md:172`: the same R-EXEC text, no selection rule.

## Proposed change

Reuse the R-NETBIND shape, in its smallest form.

1. A root-owned machine policy beside the network binding maps the admitted Curator profile identity and lock digest, intersected with the placement and admission-class minimums, to one exec-profile identity and its policy digest. A selectable set per entry is optional, not required initially.
2. The dispatcher resolves the entry at `prepare`, pins the exec-profile identity and policy digest in `input/1`, and refuses a caller reference outside the bound; caller text and the caller's home are never the source. Policy drift between admission and launch refuses rather than substituting another profile; retry and recovery use the pinned digest.
3. The launcher applies the pinned profile and verifies the policy digest before any child code starts, in the same step that today checks existence against the host matrix.
4. Workplaces get the narrowest entry by default; an interpreter-bearing profile is an explicit per-placement entry. All class floors and the no-heavy-code rule stay as written.
5. No grant dimension is added: grant `profiles` already narrow the Curator profile, which narrows the exec profile through the binding, exactly as egress narrows through R-NETBIND.

## Expected benefit

Exec authority narrows transitively with the granted Curator profile, as egress does; one policy owner and one mechanism for both bindings; the selected profile and its body are pinned and checkable at `prepare` and at launch instead of being an unpinned reference chosen by the caller.

## Risks and costs

One more machine policy with an installer and operator lifecycle, and a policy-digest relation to publish with the profile format (dispatcher §16 q25, user manager §14 q19). No owner decision is challenged.

## Affected specifications

Dispatcher §§3.4, 4.2, 5.1, 5.3, 16 q25; user manager §§7, 8, 11, 14 q19; launcher §10 composed-plan section; session host §3.2; book chapter 11.

## Confirmed by

Room `#swarma-review-3`, topic `f-exec-profile-authority` (root `$31ovEDYd2iC8LcMf4yH7ad0RWoIlLRTS67hW1IjH2K0`), 2026-10-13.

- Candidate: fable, `$31ovEDYd2iC8LcMf4yH7ad0RWoIlLRTS67hW1IjH2K0`.
- astra-02 (`macmini_swarma-review-3_astra-02`), `$elHGpas5gb_rCQtgpkbrQABs3nVnnlD-Yf74Om2qUsc`: confirms the selection and policy-digest publication gap from the user-manager and launcher lens; adopted: a single map intersected with placement and class minimums, the policy-digest pin, the floors preserved, and the claim scoped to a publication gap.
