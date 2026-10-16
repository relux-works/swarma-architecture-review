# HOST-HOME-CODE — Curator-owned runtime bootstrap and resume verification

Owner repository: **curator**. Size: **5**, split again if platform projections need independent implementations. Conditional follow-up after HOST-HOME-SPEC; mandatory before hosted activation.

Normative clauses: local-hosted-launches §§3 (materialization receipt and actual-start boundary), 4 (Curator/receiver writers and credentials), 5 (protected inputs and original provenance), 7; snapshots §6 runtime boundaries plus the newly published HOST-HOME-SPEC contract.

Attack surface: mutable runtime state, credential strategy and protected profile content crossing ownership boundaries.

Acceptance criteria:

- Implement only the published Curator runtime initialization/verification surface. The pure content manifest remains unchanged; separately attest permitted initialization and bind exact snapshot/descriptor identity.
- Populate the complete admitted initial private runtime layout through Curator, outside the active workspace, without receiver profile-file lists, seed selection or native auth reconnection. Selected backend and login source remain consistent with machine policy.
- Implement distinct fresh-start and resume checks: full initial materialization first; original receipt plus protected inputs on restart. State changes legitimately made by the runtime cannot become new original-content evidence.
- Preserve snapshot bytes after source repair/switch/global sync. Qualify protection against writable-ancestor replacement for any claim of sealed runtime content. Unsupported combinations refuse; chmod alone is insufficient.
- Expose no provider-ready capability based on helper success or login metadata. Coordinate actual runtime qualification with hosted launcher/receiver leaves; all Claude/Codex/Muse rows are required for first public CIP-0016 support.

Mandatory tests with positive controls:

| Positive control | Negative case / invariant |
| --- | --- |
| Valid private home and receipt initialize/start with separate credentials | Receiver-style injected auth link/native config/unknown overlay or wrong generation refuses |
| Source changes leave admitted content usable; allowed runtime state changes survive restart | Root/support/skill/MCP/descriptor drift, missing or unreadable baseline, extra protected input or shadowing overlay refuses without baseline rewrite |
| Declared credential strategy works after home relocation in qualified session/platform | Native source-home login alone cannot prove relocated readiness; unavailable/conflicting source never silently falls back |
| Actual supported tool can start, perform admitted work and resume with immutable content | Tool attempt to rewrite protected content or replace its ancestor refuses that combination |

Paths: new Curator runtime/verification files next to `internal/envsnapshot` and `internal/envprofile`, public CLI/API entry files per published spelling, integration fixtures/docs. Serialize auth/store/init changes with CIP-0015 and setup-token implementation, and bootstrap changes with SNAP-CLI. Depends on snapshot completion and HOST-HOME-SPEC, plus runtime-B confirmation where that projection is chosen. Archive encoding, dispatcher relay and cross-account executor remain later CIP-0014 leaves 5/6, not inferred from local success.
