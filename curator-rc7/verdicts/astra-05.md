# astra-05 — security and delivery verdict

Round 1, provisional. Reviewed plan: `b592fa9` (2026-10-16). No code implementation or runtime qualification is asserted. Owned design: [setup-token local source](../designs/setup-token-local-source.md); owned leaves T0–T4.

## Plan rubric

| Criterion | Score | Evidence / remaining work |
| --- | ---: | --- |
| P1 Traceability | 1/2 | PLAN §§2–3 cites the accepted normative sections and gates, but provisional T1+/H1+/X1+ rows are not a clause-complete leaf map. Integrate T0–T4 and the other seats' detailed leaves |
| P2 Bounded leaves | 1/2 | v4, policy, readiness and capture/publication surfaces are split; token/hosted placeholder rows remain multi-owner until replaced |
| P3 Negative evidence | 1/2 | G0/R0 and the plan require paired controls; detailed bodies for every other leaf are still pending synthesis. T0–T4 now supply source-policy, custody, final-hop and spawned-chain witnesses |
| P4 Ordering | 2/2 | PLAN §4 names shared paths and serial owners; v4 precedes token integration. T4 must be explicitly tied to private-home/Curator-entry-point adoption rather than treated as a free launcher flag |
| P5 Unblocking | 2/2 | Existing v4/Muse consumer chain is first; speculative source carriers do not block it. Mission release evidence and inspected stale checkouts are separated |
| P6 Release honesty | 1/2 | Tag versus hosted activation is usefully separated, but “same-user setup-token path” needs the actual spawned T4 row and an explicit hold/deferral boundary; T0–T3 alone do not meet the owner's spawned-agent requirement |

The score is for the current draft, not a rejection of the direction. Raise scores only after the leaf map and route-specific release claims are integrated.

## Confirmed risks and requested plan changes

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
| E7 Specifiability | 1/2 | L1–L8 and ST-01–15 give semantic acceptance and T3a/T3b fix the public API seam, but complete carrier versions, binding schema, diagnostics and spawned final-route grammar still require T0 publication |
| E8 Operator effort | 1/2 | One intentional enrollment replaces per-home login on qualified routes; initial source migration and later re-enrollment/restart remain explicit. No invented automatic vendor ceremony |

## Operator-only questions

No decision about whether to support setup-token, file-first custody, native default or Remote Control is reopened. The requested local slice supplies the design direction. A real platform inability to satisfy child/source qualification would require a future concrete choice backed by probe evidence; none is invented from this review. The integrated plan must explicitly identify any release deferral of actual spawned support instead of silently substituting direct-only support.

## Open collective threads

- astra-01: replace T1+ with T0–T4 (including T3a/T3b) and check source/marker/CLI overlap against L15-0/C0 and private-home spawn adoption.
- astra-02: confirm node/native/file readiness and retained implicit-versus-explicit isolation semantics; keep lifecycle/capability outside the frozen login row.
- astra-04: ensure runtime preparation supplies the admitted node-source destination independently of credential-free snapshot transport.
