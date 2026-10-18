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

8. **Who resolves which conflicts (D-020).** The platform space policy must name the responsible parties per area, and the escalation path must be chosen (proposal: an escalation through Swarm Keeper or a board task addressed to them).
9. **Space directory.** Format and owner of the directory that maps identities and projects to space locations.

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
