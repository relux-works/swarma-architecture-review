# Memory: open questions and risks

Living list for the agent-memory design. Each item says why it is open, what is known, and what a decision needs. Owner decisions are in `DECISIONS.md`; proposals are in `notes/`.

## External and non-persistent agents

1. **Memory of agents from outside.** In the first version they are ephemeral and have no own memory (D-021). The design direction is decided (D-022); its platform-compatible form awaits the owner's confirmation.
2. **Returning agent, same memory.** Proving sameness is solved by the platform: re-registration proves possession of the pinned key (later: keys current in its identity cell). Getting earlier memory back is then a grant decision by policy or the operator; which rule applies is open.
3. **Where an external agent's memory belongs.** Knowledge created while working on our project is about our project; the leaning is that it belongs to the project space, not to the agent. Portability of that memory to the agent's owner is then a disclosure decision by the project owner.
4. **Signing by external agents.** The platform answer: it signs with its own key in the donor-side bridge, never through model tools, and only protocol objects. Open: carry its memory records inside the signed result export (no new protocol object, no mid-task writes, already compliant with decision 57 «no blind signing») or add a bridge message type for memory records, which must carry the full canonical record for the bridge to check.

## Persistent agents

5. **Where the agent space is hosted.** Decided for now (D-026): a git repository on the owner's remote, a working clone in the home. Open: what happens to the space when its agent is revoked.
6. **Residual secret risk of memory that outlives the home.** Homes are deleted because an agent can hide a token in their content; the same risk applies to memory records. Mitigations: schema-typed, length-limited fields, no blobs or arbitrary files, a secret scan at write and export. None proves absence of secrets. The owner leans to managing this for trusted agents (D-021); explicit acceptance is still open.
7. **Temporary keys (D-017, D-024).** The owner registers the key (D-024). A key kept in the home can be read through prompt injection and is lost when the home is deleted. Open: how a lost key is replaced without breaking the agent's history.

## Shared memory

8. **Who resolves which conflicts (D-020).** The platform space policy must name the responsible parties per area, and the escalation path must be chosen (proposal: an escalation through Swarm Keeper or a board task addressed to them). **Decided for v1 by the panel (D-029, 2026-10-21).**
9. **Space directory.** Format and owner of the directory that maps identities and projects to space locations. **Decided by the panel (D-028, 2026-10-21).**

## Carried over from the design

10. Which source classes must stay presentable, and for how long.
11. Real source classes, retention and custody boundaries.
12. Production resource limits and the restore mechanism of the protected service.
13. Coarse availability information that may be disclosed in advance.
14. Qualification of the protected deployment.
15. When the kernel becomes a standalone open release.

## Found while implementing the Go kernel (2026-10-18)

16. **Retention-admission reference without a registry (K-REC-1, K-API-2, vector S30).** An excerpt names `retention_admission` = `retention:grounds` v1, but the closed snapshot holds no such record and no registry. The kernel treats the exact reference as trusted adapter evidence and checks current retain rights separately. The spec should say whether that is intended or add the registry. The interpretation is documented in the public repo's `docs/write-admission.md`.
17. **Team perspective grants (K-ENV-1, vector S10).** The grant model has issuer, principal and space but no team selector. The kernel requires the issuer's explicit admit grant in the space and infers no membership from the team principal. The spec should state that or add a team selector.
18. **Version label.** The package README says draft 0.2.7; `semantics.md` and the schema URNs still say 0.2.6. Bump the URNs in a package release, or label 0.2.7 as a text-only revision.
19. **Vector gaps found by review (stage 1).** Three defects in the Go kernel passed every package vector before the reviewer caught them. Each one deserves a new semantic vector in the next package release:
    - a release assessment that is withdrawn after declassification must stop authorizing reads and prepared delivery (K-REC-2, K-REV-2, K-PUB-1);
    - reads must honour per-record fences and erasure states supplied in the initial state, including for current source resolution (K-ERASE-1);
    - handle-slot declarations that over- or under-cover the expected report must be a harness error (K-VEC-2).

## Found in stage 2–3 (2026-10-18)

20. **Where the trusted kernel configuration comes from outside tests.** A git space opens with an independently trusted kernel template: domain registry, grants, intake reviews, lineage facts, evaluation policy and bounds. Signed records never manufacture these. For the CLI (stage 3) the provisional choice is twofold:
    - the binary ships a built-in agent-memory profile that carries only non-authority configuration;
    - every write and read authority is derived from the owner-signed space policy, and no local config may widen it.
    Open: whether an owner should be able to distribute a signed profile per space, and how intake reviews and lineage facts reach a reader in a real deployment.
21. **Signed write transactions in commit metadata (stage 2).** The closed record wire carries no admission operation or receipt. The git adapter therefore adds a fourth signed purpose, a write transaction in the commit metadata. It binds the space, the first parent, the source tree and the policy digest. The independent review judged it justified. The architecture (§6.1, §6.3) should name it, or the record wire should carry the operation in a future package release.
22. **Repository layout for Curator packaging (stage 4).** The Curator go-v1 driver requires a build root other than `.`, holding its own `go.mod`. It also forbids declaring the enclosing root module (curator-spec core §4.2.3). The orchestrator therefore moved the Go module to `go/`, which serves as both build root and module root. `spec/` stays at the repository root, and the CLI embeds a byte-identical copy of the schemas under `go/`, guarded by a test. The skill root is the repository root. The alternative was a Curator protocol change that admits a root module; that belongs to the Curator lane.
23. **Session-excerpt sources are not visible to readers (stage 3 gate, scenario 11).** The normative closed view (`spec/kernel/schemas/view.schema.json`) carries `source_refs`, which are ids and versions, but no source payload. Source records are never selected as read items. A reader therefore sees that a decision cites a session source but cannot see the locator (runtime, session, message, digest) or the excerpt, although architecture §7.2 and §8 promise exactly that. Closing the gap needs a package release: either a disclosure-filtered source payload in the view, or a source-read operation with its own non-interference vectors. Implementation-side workarounds were rejected because they would compute disclosure outside the kernel. **Interim for v1 (orchestrator, reversible):** the gate asserts the source reference only, and `docs/cli.md` lists the limitation. The source-visibility gate task of 2026-10-19 is blocked on this decision. **Decided by the panel (D-027, 2026-10-21): a source table in the view, package 0.3.0-draft.**

## Left to the owner by the panel (2026-10-21)

These come from the owner card in `notes/panel-261021/SYNTHESIS.md`. Each one has a panel default that stays in force until Ivan decides otherwise.

24. **A real second owner.** Admitting another owner's agents means a manual exchange of genesis pins and agent keys. Their agents become named read-only readers, and identifiers are owner-qualified until the owner registry exists. Stage 5 is gated with simulated owners only.
25. **Can one opposing review stop dependent work?** The panel default is D-020 taken literally: an attributed opposing review of a supported decision is an evidence conflict. The alternative is to let only human, test or formal evidence stop work. Measure the effect in stage 7.
26. **Precedence between platform and project decisions.** The panel default is no precedence: each space's resolvers decide. A binding rule would be governance, not memory logic.
27. **Excerpt visibility.** Every reader of a shared space sees its retained excerpts and session ids. This follows from git, and D-027 makes it explicit.
