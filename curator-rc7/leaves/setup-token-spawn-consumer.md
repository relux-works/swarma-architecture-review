# T4 — Adopt the qualified token executor in a real same-user spawn

- **Owner repository:** skill-project-management (first local headless task-board spawn consumer); agents-management carrier changes, if required by T0, are a separate prerequisite PR in that owner repository.
- **Normative clauses:** T0 L5–L8; CIP-0010 C3.3/C3.4/C3.6; D1/D2/D4; Decision 0021; credential-free snapshots §6 and independently published runtime-preparation contract.
- **Attack surface:** the actual spawned process chain, including retries and persisted launch records.
- **Size:** M after the existing Curator-entry-point/private-home adoption seam is published. No broker or interactive hosted activation in this leaf.

## Acceptance

1. Freeze the headless spawn route through T3b's approved curator-run final executor before coding; retain original plan/resource digest, private-home and input/policy contracts. The board transports required metadata only and does not implement its own credential store reader or home inventory.
2. In observed project-management `ad68902`, `tools/board-cli/internal/spawn/spawn.go:1109` directly builds `exec.Command(plan.Binary, plan.Argv...)` and assigns `plan.Env`; the fresh read-only `ab63db823` supplied by the convener retains this at lines 1180–1181. The adopted route must prove the actual final hop, not merely add token bytes to this plan/environment before its persistence. Existing launch provenance/resource records stay secret-free.
3. Same-user fresh launch and retry/resume each re-admit the current local binding; status from the parent does not authorize the child. No token travels in task resources, launch arguments, fragments, journal, result or snapshot. Unknown/expired/revoked/missing source refuses without native fallback.
4. Test one real headless Claude spawned chain through the public task-board entry point and qualified T3b route. Current ax tracked flow and sessionmanager interactive PTY remain unavailable for node mode until separately adopted and qualified; do not represent this narrower row as those routes. CIP-0016 §§4/6's exact-process and caller-secret/daemon-no-lookup rules are unchanged; this leaf does not replace the hosted provider with an unannounced wrapper or inject within tb-sessiond.
5. Record package/release pins and activation tuple; consumer enablement depends on capability evidence for this chain. If the T0 route or private-home preparation is not published, mark the leaf gated and keep the owner-requested spawned support explicitly unfinished.

## Mandatory negatives and positive controls

ST-07–13: old downstream consumer, dropped required extension, token env literal, source substitution, another UID, stale queued retry after revoke and unqualified interactive handoff must fail at the intended boundary without starting Claude, reading credentials in the board or persisting a secret. The valid same-UID headless chain reaches Claude with the source and no token in board/child-tool artifacts. A direct-only mock cannot pass the spawned-chain gate. Preserve neighboring valid per-home spawns.

## Dependencies and paths

T0/T2/T3a/T3b; existing v4 pin handoff; Curator entry-point and private-home spawn adoption identified by the main plan. Serialize `tools/board-cli/internal/spawn/{spawn,launch_plan,launch_composition}.go` and pinned `tools/board-cli/go.mod` with existing spawn migration. Separate interactive follow-up touches `internal/sessionmanager/claude_host.go` (observed direct exec at line 700); it is intentionally not bundled here. The final release cut must name T4 if it claims the owner's requested spawned-agent setup-token support.
