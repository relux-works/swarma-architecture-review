# astra-05 — security and delivery verdict

Round 5, accepted implementation-plan candidate; awaiting the convener's PARK. Reviewed plan: `32cf0f2`, including L15-5/6a/6b at `82b669b` and T0 ordering clarification at `323a284` (2026-10-16). No code implementation or runtime qualification is asserted. Owned design: [setup-token local source](../designs/setup-token-local-source.md); owned leaves T0–T4, including the separate T3a/T3b owners.

## Plan rubric

| Criterion | Score | Evidence / remaining work |
| --- | ---: | --- |
| P1 Traceability | 2/2 | PLAN §§3/5/6 links L15/M/C/SNAP/HOST-HOME/D4/T/H/X families including C7/M6/X5. The source-confirmed [CIP-0015 coverage finding](../findings/login-followon-coverage.md) is resolved by L15-5/6a/6b, with exact coverage rows, shared-path ordering and separate broker publication gates |
| P2 Bounded leaves | 2/2 | Placeholder bundles are replaced by owning surfaces: T1 custody, T2 policy, T3a public API, T3b final executor, T4 real consumer; snapshot mechanisms, hosted admission/runtime adapters and cross-account runtime qualification are likewise separate |
| P3 Negative evidence | 2/2 | Linked leaves name forbidden outcomes beside valid controls. T0–T4 map ST-01–15; actual vendor/source/child qualification is distinguished from synthetic transport and detector controls. R0 requires exact production evidence rather than counting planned tests as passed |
| P4 Ordering | 2/2 | PLAN §4 serializes carriers, shared policy, pure verifyHome split, launcher and board paths. Independent D4-S home intake joins T3b only at T4 qualification, avoiding a token/snapshot cycle; custody → policy → public API avoids a cross-module cycle |
| P5 Unblocking | 2/2 | M1/M2 → M3/M4 → usable Curator release → M5 leads; fixture-based exact-loader observation can start early and actual materialize-to-loader integration remains a separate gate. T0 publication can proceed concurrently without delaying v4 |
| P6 Release honesty | 2/2 | PLAN §2 separates base tag, Codex activation, D4, actual headless token outcome, all-three hosted activation and cross-account activation. T3-only cannot satisfy spawned support. C7 retains the full adopted consumer gate; unknown and unavailable rows stay visible |

The plan is 12/12. The security and route-design objections below are incorporated into the plan; they remain mandatory implementation/activation gates, not claims that the current binaries satisfy them.

## Required implementation and activation gates

1. **Wrong final hop leaks tokens.** At launcher `9ad2f016`, `internal/execution/execution.go:83` serializes `EnvLiterals`; `:143` starts ax. Do not retrieve a token in the composer or inject into ax/global env. T3 qualifies the real final executor; T4 proves a real same-user headless spawn reaches it. Topic `f-setup-token-final-hop`.
2. **Qualification cannot be inferred from successful inference or env construction.** Native secret-read suppression, uncontrolled MCP/hooks/tool children, settings reload and MCP interpolation need pinned real-harness evidence with a known-leaking control. No suitable child-filter mechanism was qualified by this collective. A safety flag or fake exec is not sufficient.
3. **Readiness versus authority.** `login: present` is candidate metadata and may coexist with unknown/expired lifetime or an unavailable executor. Never turn that row, its caller session or a materialized snapshot into permission to deliver. The design retains the existing row meaning and separates lifecycle/capability guidance.
4. **Custody revocation has a delivery boundary.** Local deletion cannot recall a token already in a harness. Serialize release/revoke and invalidate source references; document vendor revocation and restart separately. No token digest or secret-bearing generic journal is permitted.
5. **CIP-0010 is not already a shipped local contract.** C7 sequences cross-user broker first; metadata carrier and binding are pending. T0 must explicitly adopt the narrow same-user exception and coordinated complete carriers without reopening D11/D14 or claiming broker support.
6. **Relocation and adoption are separate.** Per-home Claude login does not follow `CLAUDE_CONFIG_DIR` into a snapshot. Preserve existing native credentials; use explicit node-source adoption and Curator-owned runtime preparation. An unreadable native store is not evidence of absence.
7. **Hosted restart currently prohibits daemon lookup.** Confirmed astra-01's challenge from local-hosted-launches §§4/6: exact provider process and caller-resolved fresh restart secrets cannot silently become a daemon token callback or wrapper. The chosen initial T4 chain is independent same-user headless task-board spawn → qualified curator-run final-exec → noninteractive Claude; hosted token routes remain refused pending their own amendment. Current project-management `ab63db823` still directly execs headless plan.Env at spawn.go:1180–1181.
8. **Cross-module protected API was missing.** Confirmed astra-01's review: launcher cannot import Curator's internal store package. T0/T1/T3 now name a pinned public in-process `pkg/localcredential` facade backed by the private core, with metadata describe and protected final-launch operations returning a secret-free process handle. No generic token getter, stdout/IPC transport or duplicate protected-store traversal is admitted.
9. **Approved binary identity is not the whole startup input.** Launcher `9ad2f016` already reserves loader/runtime variable families at MCP env-name intake (`internal/fragment/fragment.go:212`), but direct execution takes a complete composed environment. New node admission must carry this protection through the final environment before material lookup. ST-15 now pairs refused unqualified startup injection with the same approved executable under a valid benign environment. This closes a proposal acceptance gap, not a claimed exploit in currently unsupported node mode.

## Setup-token elegance rubric

Scores assess this proposed contract, not implementation readiness.

| Criterion | Score | Evidence |
| --- | ---: | --- |
| E1 New concepts | 2/2 | Reuses node, source_ref, binding, file backend and capability from CIP-0010; no local mini-broker |
| E2 Reuse | 2/2 | Retains source/store/isolation ordering, frozen readiness row and Curator home ownership; source hooks reuse the readiness engine |
| E3 Secrets | 2/2 | Private deliberate enrollment, protected object/generation rules, final-only material release, forbidden artifact paths and explicit child-leak qualification |
| E6 Honest failure | 2/2 | Unknown is retained; no native fallback, no capability from presence, no local-revoke/vendor-revoke confusion; direct and spawned support separated |
| E7 Specifiability | 2/2 | L1–L8 and ST-01–15 define authority, custody, readiness and final-only release; T3a/T3b name the legal public API and T4 names the actual headless route. T0 owns exact closed carrier/binding/diagnostic/entry-point publication before code enablement; no unresolved hosted-daemon shortcut is assumed |
| E8 Operator effort | 1/2 | One intentional enrollment replaces per-home login on qualified routes; initial source migration and later re-enrollment/restart remain explicit. No invented automatic vendor ceremony |

## Operator-only questions

No decision about whether to support setup-token, file-first custody, native default or Remote Control is reopened. The requested local slice supplies the design direction. A real platform inability to satisfy child/source qualification would require a future concrete choice backed by probe evidence; none is invented from this review. The integrated plan explicitly defers the complete token-spawn outcome beyond the base tag while retaining it as priority follow-on work. No new operator decision blocks this design proposal.

## Open collective threads

- No unresolved artifact-level objection from this seat. L15-5/6a/6b were reviewed against CIP-0015 leaves 7/8 and broker `ec7fb3d` §§13.2/14/18.15, then integrated at `32cf0f2`; they remain outside the rc.7 local base and the no-broker token slice.
- astra-01 accepted T3a/T3b, headless T4 and ST-15; astra-02 confirmed node/native/file readiness and retained isolation semantics; astra-04 confirmed Curator-owned prepared-home separation and the hosted daemon refusal. No unanswered addressed token-design item remains.
- Runtime qualification, normative adoption and code delivery remain future work in their named leaves. This collective's source review is not execution evidence.
