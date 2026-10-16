# H-PREP — Authenticated private-resource reservation

Owner repository: **skill-project-management**. Size: **3**.

Normative clauses: hosted §§2/3/6; CIP-0016 leaf 4 preparation half. Attack surface: resource allocation becoming launch authority or permitting cross-board/replay reuse.

Acceptance: authenticate through existing private control transport and normal authoritative-board rules; reserve board/owner/runtime/generation-bound session identity, permitted private directory outside the active workspace, expiry and opaque reservation. Return Codex endpoint/transport/policy and all delivery values needed by composition. No provider, profile resolve, caller preparation command or arbitrary repository socket/binary is executed. Preparation is not authorization. Persist lifecycle metadata privately; cancellation/expiry frees only owned resources without following links. Endpoint reservation's release-before-bind race is explicit and cannot authorize substitution.

| Positive control | Negative / forbidden effect |
| --- | --- |
| Authenticated same-user board request reserves exactly its declared resources without provider calls | Wrong account/board/owner/runtime, malformed bounds, project-selected endpoint or arbitrary preparation command refuses |
| Fresh unexpired reservation is available once for admission | Expired/cancelled generation or another board's reservation cannot be revived/rebound |
| Cancellation removes only own unused allocation | Symlink/ancestor replacement cannot delete native/managed/workspace data; provider start count remains zero |
| Exact reserved endpoint can be handed to composition | Port loss/bind uncertainty never silently selects a replacement endpoint |

Dependencies/paths: H-WIRE and destination requirements from HOST-HOME-SPEC. New preparation handlers/records beside `tools/board-cli/internal/sessionmanager/hosted_*`, control route registration and private-layout allocator. Coordinate durable generation state with H-ADMIT through one fixed interface; serialize shared control/manager/layout files. No raw token/argv/env persistence is introduced.
