# HOST-HOME-SPEC — Publish runtime preparation and verification ownership

Owner repository: **curator-spec**, with joint acceptance by curator-agent-launcher and skill-project-management. Size: **3**. Begin during rc.7 planning; required before any hosted activation, but pure materialize does not wait on it.

Normative clauses to complete: snapshots §§3/4/6/7; local-hosted-launches §§1, 3–5, 7, 8 questions 3/4; CIP-0014 leaves 3/4; CIP-0016 curator leaf 2. This is a **new seam publication**, not an API already frozen by Accepted status.

Attack surface: presenting a credential-free immutable content export as a complete writable, authenticated runtime home, or treating a profile observation as session attestation.

Publish one precise contract with the following acceptance criteria:

- Keep pure `materialize` output unchanged: snapshot schema v1 cannot acquire auth links, config seeds, backend settings or a private extension. Define a separate Curator-owned runtime initialization operation/projection and receipt binding to snapshot, adapter, profile, generation and admitted credential strategy.
- Separate immutable content inventory from permitted runtime-owned state and non-secret bootstrap/config. For Codex, identify who creates any initial config bytes without copying ambient native config/MCP. Receiver policy/trust lives beside the home and cannot rewrite config or shadow protected content.
- Publish a consumer-callable verification surface and its closed inputs/results/refusals. Fresh admission verifies actual initial materialization; attach/restart verifies persisted original receipt plus Curator-defined protected inputs. Runtime state is not compared to its prelaunch digest. `manifest-only` cannot implement either verification operation.
- Verification must bind caller-provided expected identity from the admitted plan, not accept a self-minted receipt as authority. Specify actual-start recheck and residual same-user TOCTOU honestly. Missing verifier/capability keeps activation shut.
- Define the Curator-owned local credential strategy/exception separately from export, including snapshot relocation. Source-home `login: present` does not prove a new Claude config-dir can authenticate. Shared file links or separately prepared login cannot be invented by the receiver. Setup-token source admission, injection and secret persistence remain with their owning contract.
- Publish how snapshot descriptor paths and separate backend/Codex settings become one sealed hosted plan. Snapshot v1 intentionally excludes those policy fields; no consumer silently drops them or resolves them again at exec.
- Retain runtime B's explicit operator-confirmation gate and per-adapter start/login/model-turn/native-resume qualification. Same-user local lifecycle evidence does not prove cross-account protected projection.

Mandatory specification counterexamples with positive controls:

| Positive control | Negative example that must be rejected |
| --- | --- |
| Exact original content with declared mutable state changes verifies on resume | Whole-home initial hash rejects legitimate state, or verifier exempts arbitrary new content/overlays |
| Published runtime initialization receipt binds one content snapshot and credential strategy | Receiver adds auth link, copies native config, promotes source-home login status, or rewrites baseline after provider writes |
| Plan covers relative-path binding, policy and backend/settings transport | Descriptor-only plan drops selected file backend or profile settings; undeclared policy shadows root/MCP/skills |
| Freshly verified admitted generation can start | `manifest-only` or matching self-supplied digest substitutes for actual-tree admission; missing expected binding still launches |

Paths: `protocol/managed-home-snapshots.md`, `protocol/local-hosted-launches.md`, new successor/receipt schemas and separate conformance vectors; coordinate CIP-0010 local source and CIP-0015 status/store publication. Do not edit frozen snapshot or fragment schemas in place. Wire spelling/versions and the runtime-B interpretation need recorded owning decisions; recommendations are not silently approved by this leaf.

Release cut: rc.7 can truthfully ship the additive snapshot command/verifier and v4 producer while this seam remains gated. It cannot claim the complete CIP-0016 path, complete D4 adoption, or all-three-runtime hosted qualification. If release acceptance requires hosted launches, HOST-HOME-CODE and the entire jointly qualified hosted matrix become blockers; do not release a Claude-only substitute.
