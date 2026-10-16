# Adversarial review of astra-02's login/store leaves

Reviewer: astra-03. Round 2, 2026-10-16.
Reviewed five leaves introduced by signed `b4d55ab` as present at `000493b`.
Normative baseline: curator-spec `5509499`; code baseline curator `0d00a109`.
This is a review of proposed acceptance contracts, not executed test evidence.

**Verdict: accept the detailed decomposition for synthesis.** No confirmed
correctness defect in these five leaf contracts. Their explicit pending
publication/qualification gates must survive the synthesized plan.

| Attack | Normative/source evidence | Observed leaf response |
|---|---|---|
| Add store/readiness to an old closed envelope; use module projection as full validator | login-readiness §§1,2,7; profile-codex-settings §7 | L15-0 requires complete successors and old-envelope rejection |
| Introduce two Codex application owners or put store in a package | profile-codex-settings §§1,3–5; v4 schema | L15-0 single-payload successor recommendation; L15-1 machine-only policy |
| Treat generic native Muse as Keychain instead of the later file amendment | environments §§7.4,10.2 vs login-readiness §§2,2.1 | L15-0 explicitly reconciles native mapping, diagnostic and ambient/explicit distinction |
| Invoke agent --version during supposedly metadata-only full status | status.go:1140 adapterStates; managed.go:1957/2386 verifyHome/checkToolRelease | L15-2 names both existing call paths and requires production entry tripwires |
| Convert denied/unsafe/empty candidate to absence or validity | login-readiness §§1,1.1; environments §8.4.1 | L15-2 keeps unknown reasons, arbitrary nonempty bytes as presence only, no content parse |
| Count another session's Claude Keychain item, normalize its hash path, or try both stores | login-readiness §1.1 exact exported path and session scope | L15-2 explicitly prohibits each fallback/inference |
| Link stale Codex file under native keyring/auto; isolated keyring treated as private | profile-codex-settings §5 matrix | L15-1 requires compatible sharing and separately prepared isolated file; pending qualification retained |
| Login writes through shared link or captures the vendor transcript | login-readiness §3 | L15-3 refuses shared even if present, attaches terminal I/O, preserves vendor writes on failure |
| Env login repairs/installs or source conflict is stripped to manufacture success | login-readiness §3 | L15-3 requires current trusted home and deliberate home-owned source; no fallback or repair |
| Prepare drops inconvenient participants or mutates under detected headless mode | login-readiness §§1.2,4 | L15-4 includes OpenCode/unknown and enforces explicit or detected report-only behavior |
| Cancellation starts more ceremonies; TOCTOU redirects login to changed selection | login-readiness §4 | L15-3/L15-4 revalidate and release mutation locks before browser wait; cancellation and retry controls |

## Integration notes, not new operator decisions

- Specific Muse backend semantics are the later CIP-0017 amendment. Publish
  the reconciled diagnostic and ambient/explicit decision table once; do not
  leave each implementation to choose which text wins.
- Native metadata qualification is separate from the row formatter. Present
  node metadata does not prove a final executor can inject setup-token; no
  login-readiness result authorizes snapshot/destination authentication.
- Exact Codex runtime qualification needs a durable owned matrix, now proposed
  as [C4](../leaves/codex-storage-qualification.md). L15-1 correctly declares
  that gate; the new leaf makes its execution and evidence concrete.
- environments §8.2 says Muse root_context needs no new marker member.
  I corrected my M1 dependency to avoid accidentally serializing Muse behind
  the unrelated Codex successor marker.
- Shared `managed.go`, registry, status and CLI integration remains serialized.
  Independent metadata/probe/coordinator modules can proceed in parallel.

No new human-only question is established. D14 and the metadata-only choice
are fixed; the plan must implement their consequences, not reopen them.

## Round 3 corroboration: prepare reuse traps

Confirmed astra-02's subsequent `f-prepare-first-install` finding directly:
`internal/envprofile/envprofile.go:911` skips activation for `Use=false` only
when machine-current is already nonempty; `:919` otherwise calls `useLocked`.
`reinstallActivation` likewise returns true for empty current. Therefore
prepare needs an explicit non-activating installation seam. Installing then
restoring a pointer is not equivalent: native surface writes already occurred.
Preserve the adjacent control that ordinary first `profile install` still
activates as environments §9.1 requires.

`internal/envprofile/managed.go:2599–2607` already refuses identity migration
under `PreserveLock`. Prepare must retain that selected-lock contract or report
explicit required migration; unconstrained repair cannot silently upgrade the
installed identity. L15-4's added first-machine and old-lock controls are
necessary refinements, not new product choices.
