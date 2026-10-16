# T3a — Publish Curator's protected in-process final-launch API

- **Owner repository:** curator.
- **Normative clauses:** T0 L5–L8 and public API contract; CIP-0010 C3.4/C6 protected read order; D1 home/source ownership.
- **Attack surface:** moving from metadata-only preparation to secret-bearing child start in one trusted final-executor process.
- **Size:** M; follows the store and source-policy leaves, separate from the launcher consumer.

## Acceptance

1. Extend T1's public `pkg/localcredential` facade with T0's typed final-launch operation. Keep the store implementation private and reuse T2's source/home admission. No generic get-secret API, CLI stdout, secret IPC or returned populated environment/command object.
2. Independently check the protected local binding, source generation, effective policy, approved executable/endpoint and conflicts before material access. Construct the child environment from admitted inputs and reject unqualified startup/loader code injection from every layer; a clean executable digest does not authorize injected startup code. A caller's `authorized=true`, capability string, metadata row or plan digest is insufficient.
3. Keep the binding/revoke check and material release serialized; build private child environment and start exactly the approved Claude process. Return only a secret-free process handle supporting the required wait/signal/lifecycle operations. Preserve qualified terminal/process-group/cancellation semantics through the frozen API; do not import another repository's internal process package or create a module dependency cycle.
4. A failed start closes secret FDs, releases the node lock, discards buffers and leaves registrations coherent. Neither success nor error exposes a token or environment dump. Document memory-zeroization and already-released-token limits honestly.

## Mandatory negatives and positive controls

ST-03/07/08/09/11/15: injected path replacement, mismatched binding/executable, competing source, revoked generation, unqualified startup env and launch failure must produce intended refusal/no forbidden process or leak. Matching protected synthetic child with admitted benign environment starts and returns only lifecycle data. The public API dependency test is compiled from an external module, proving consumers do not import Curator's `internal` package; it is not vendor qualification. Preserve signal/terminal/cancellation controls when the process-start boundary changes. Real Claude qualification belongs to T3b.

## Dependencies and paths

T0 → T1 metadata/custody → T2 policy → T3a → T3b → T4. This ordering removes the T1/T2 cycle that would result from implementing full source-aware launch in the initial custody leaf. `pkg/localcredential`, private `internal/envcredential`, existing source/home admission adapters, module API documentation and external-consumer fixtures. Serialize with T1 on that public facade and with T2 on its source hooks; no simultaneous edits under an assumed cross-repository import exemption.
