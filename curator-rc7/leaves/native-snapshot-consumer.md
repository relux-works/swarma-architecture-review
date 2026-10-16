# D4-N — Make native curator-run consume an admitted private snapshot

- Owner repository: curator-agent-launcher.
- Normative clauses: managed-home-snapshots §§1,4,6–7; environments §§10.2,10.5; D1, D4, D5; the separately published HOST-HOME-SPEC runtime/verification contract.
- Attack surface: native interactive/exec launch composition and restart content identity.
- Size: 3 for shared composition; split adapter-specific projection work before implementation if it exceeds one review. This is a consumer leaf, not snapshot production or authentication qualification.
- Release cut: a separately qualified route after the additive curator materialize release; mandatory before claiming D4 on native curator-run.

## Acceptance

1. Resolve/admit source content through Curator, allocate a permitted private destination outside the workspace, and obtain Curator's snapshot/runtime receipt before final composition. Do not launch against the live managed home or copy a consumer-maintained inventory.
2. Apply the snapshot descriptor and separately covered machine credential policy/settings through the existing runtime composer. Preserve Muse root_context/exclusions and all four XDG roots; do not mutate HOME or drop policy merely because the descriptor excludes it.
3. Verify the expected original snapshot/runtime identity at the actual start boundary using Curator's published verifier. A matching caller-supplied digest or manifest-only output cannot replace it. Keep content and mutable runtime/policy slots distinct; do not rewrite config to patch authentication or policy.
4. A native restart/resume uses its admitted private home, protected inputs and original identity. Source repair/use/global sync does not change that baseline. Drift does not trigger recapture/relabeling or a new session disguised as resume.
5. Qualify each claimed adapter/form/platform with its separately admitted destination authentication strategy. A source-home login row is not destination authentication. Native per-home, local token and cross-account broker are different rows; unsupported rows refuse before the provider starts.

## Negative tests with positive controls

| Positive control | Negative witness and forbidden result |
|---|---|
| Real direct interactive/exec composition binds a valid private snapshot and current expected receipt | Live managed path, missing/unreadable verifier, altered receipt, extra protected content or lost policy refuses before provider start |
| Source repair changes the source while a running fixture retains its captured context | Resume silently resolves latest profile, rewrites baseline or follows a source link; assert the original content remains unchanged |
| Allowed runtime state changes survive a verified restart | Root/skill/support/MCP/descriptor drift or an overlay shadowing protected content refuses; no whole-home hash workaround |
| Qualified destination credential strategy authenticates through its own gate | Caller present row, copied credential, receiver-style native link or unknown token final hop cannot grant authentication |

Use the actual launcher entrypoint with disposable source/destination fixtures and real filesystem verification. A bounded known-invalid live-home or altered-content plant must fail the intended detector. Native argv changes, tool child behavior and model-visible behavior retain their own qualification evidence.

## Dependencies and paths

SNAP-CLI + HOST-HOME-SPEC + shared HOST-HOME-CODE; v4 launcher integration precedes shared fragment/composition edits. Authentication-dependent end-to-end qualification joins its source/executor leaf; do not create a circular implementation dependency by requiring T3 qualification before the snapshot composer can be built. Likely paths: `cmd/curator-run/main.go`, `internal/fragment`, `internal/composition`, `internal/execution` and new runtime-preparation client/receipt files. Serialize with typed Codex settings and T3 final injection on these paths. This does not activate CIP-0016, archive transport or dispatcher execution.
