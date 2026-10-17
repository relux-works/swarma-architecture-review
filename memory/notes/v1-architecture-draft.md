# First working version: architecture draft (for owner decisions)

Status: draft by the memory lane, 2026-10-18, answering Ivan's direction in session: move to a first working version, not a pilot; memory is autonomous (agents write it themselves, no approval gate); both agent-own and platform memory; shared platform memory with a second owner's agents; Go; one new repository; part of the Swarma platform architecture. Nothing here is decided until recorded in `DECISIONS.md`. Decided so far: D-011 (autonomous writing), D-012 (autonomy does not require the protected service), D-013 (spaces as git repositories), D-014 (Go, one repository).

## What the design already supports

- **Several memories.** `space` is a policy scope; issuer, subject and perspective are separate envelope fields; projection rules choose issuers and perspectives. An agent-own space, a project space and a platform space are three spaces with different policies, all on one kernel.
- **Autonomous writers.** Admission classes (`self_declaration`, `imported_publication`, `machine_observation`, `semantic_inference`) are kernel; the acceptance path per class is policy. Epistemic safety does not depend on review: agent records are attributed to their issuer and perspective, cannot replace another issuer's sequence, cannot mint an adopted decision without the deciding authority's receipt, and reach agents only as data.
- **Several owners.** Issuer-local order (D-009) orders each owner's decisions by that owner's own events; disagreements between owners are evidence conflicts and stay visible.

## Where the design falls short of the new direction

1. **The write gate.** D-004 makes human review the steady write gate for the documentary register. That conflicts with autonomous memory.
2. **Who enforces admission in a multi-writer git store.** The documentary profile assumed one reviewed publication path. With many agents pushing, something trusted must enforce schema validity, authenticated issuer, representation, revision authority and compare-and-set.
3. **Physical layout of spaces.** Not specified.
4. **Multi-owner decision authority.** A shared platform space needs a rule for which owner decides what; issuer-local order only orders one owner's decisions.
5. **"Personal memory" is ambiguous.** The design excluded personal and sensitive data about people. An agent's own working knowledge is a different thing and is admissible when non-sensitive.
6. **D-006 coupling.** D-006 ties autonomous writers to the protected service. That holds only if git cannot carry trust for autonomous writers; with signatures and verification on read it can, for non-sensitive spaces.

## Proposed architecture

- **Repository** `swarma-memory` in Go: `kernel/` (a Go module implementing package 0.2.7), `cmd/memory/` (the CLI), `skill/` (`SKILL.md` and the Curator install manifest for the CLI), `conformance/` (a runner over the package vectors; the Go kernel must pass the 66 semantic vectors, becoming a third independent implementation). Splitting into separate modules later is cheap.
- **Spaces as git repositories.** One repository per space, each carrying a policy file: owners, writer grants, admitted classes, sensitivity ceiling, retention, decision authorities. Kinds: agent space (in the agent's home, which Curator owns), project space, platform space (shared remote). An agent reads and writes several spaces under its rights.
- **Write path, no approval.** `memory add|revise` validates locally (schemas, authority, compare-and-set against the fetched head), signs the commit with the agent's key (later the identity-cell key from the owner registry, D-010) and pushes. A non-fast-forward push means fetch, re-check compare-and-set per sequence, retry. A human writes with the same CLI under their own identity, or asks an agent.
- **Read path, verify on read.** `memory recall|explain|changes` fetches the readable spaces, verifies every record (signature to identity, schema, the space policy's admission rules, revision authority), evaluates with the kernel and returns data. Records that fail verification are reported and ignored. Trust comes from signatures and policy, not from repository write access. Readers remember the last heads they saw, so a history rewrite is detected.
- **Concurrent sequences.** Two agents extending one sequence from the same version produce a fork in git history. The kernel already rejects the second write; a fork that arrives through a race is projected as `version_conflict` for the later writer and needs a deterministic rule (proposed: the earlier commit in the space's first-parent history wins; the other version is reported as a rejected write).
- **Shared platform space with a second owner.** Every record is attributed to its owner's identity. The space policy names decision authorities per domain (one owner, the other, or joint). A joint decision needs receipts from both. Disagreement between owners is an evidence conflict, never auto-resolved.
- **Safety without review.** Git history cannot be erased, so every git space stays non-sensitive. An automatic secret and personal-data scan runs on `add`: it is a filter, not proof. The agent space lives in the agent's home and is deleted with it on retirement unless records were derived into a project space with lineage. Sensitive data, guaranteed erasure or admission enforced before the write (instead of on read) is what brings in the protected service later.

## Decisions this needs

1. Autonomous writing with no approval gate replaces D-004 for all spaces; humans write through the same path.
2. Spaces: agent, project, platform; one git repository per space with a policy file.
3. Verify on read with signed commits as the v1 trust model; the protected service remains for sensitive data and enforce-before-write.
4. Shared platform space: decision authorities per domain in the space policy; joint decisions need both receipts.
5. Agent space lifecycle: deleted with the home on retirement unless derived into a project space.
6. Go, one repository `swarma-memory` (kernel, CLI, skill), installed through Curator.

## Second round (2026-10-18): agent memory, keys, sync, federation

### Facts from the Swarma book (swarma-docs `orch/editorial-opus` at a84a74f)

- Chapter «Пользователь ОС и сеть агента»: at retirement the home is deleted; **there is no home archiving, and the operator cannot preserve a home in the first version**. Code and results leave through git and task acceptance; acceptance does not prove they contain no secrets either.
- Chapter «Ключи и ключник»: the agent holds no private identity key. The key holder signs bytes for the connecting agent (`sign(bytes)`), choosing the key by kernel peer UID plus an active account generation. Identity is a derivation path `purpose'/product'/project'/agent'`, stable across account re-creation and machine moves. The owner's published root lets anyone verify a key's origin offline. In Swarm Chain each identity has a cell with current keys, a hash of the next keys and the owner root as parent. The key holder is designed but has no module or contract yet; a temporary exception applies until then.
- Chapter «Идентичность агента»: the history of an agent's work belongs to its stable identity and is meant to be portable.

### Agent memory as its own class

A new class, **agent memory**: the agent's own working knowledge (observations, choices it made in its work, hypotheses, lessons), not personal data about people. It lives in the agent space (owner, issuer and perspective = the agent). Non-sensitive ceiling as for every git space.

### Agent space bound to identity, not to the home

Because homes are deleted and never archived, an agent space must not live only in the home. Proposal: the agent space is a git repository addressed by the agent's identity, with a remote under the owner; the home holds only a working clone. Then:

- retirement deletes the clone; the memory remains with the identity;
- a persistent agent that returns under the same identity path gets the same memory, on any machine;
- moving to another owner or team: the space travels as a signed export or a repository transfer; receivers verify record signatures against the identity's attestation chain;
- revoked identity: the space is sealed with a final record and kept or deleted by the owner's policy;
- one-off workers write straight into the project space and have no space of their own.

This treats memory like code and results: a work artifact that leaves the home through git, with the same residual secret risk the book already accepts for code. Mitigations: schema-typed, length-limited fields, no blobs or arbitrary files, a secret scan at write and at export. The residual risk needs explicit owner acceptance.

### Signatures

- Every record carries the submitter's signature over its canonical bytes (package K-JSON-2), made through the key holder's `sign(bytes)`. Record signatures make records verifiable outside git (export, transfer, later anchoring); commit signatures remain for transport and history.
- Readers verify against the public key attested by the owner root, or later the identity cell (D-010).
- Gap: the key holder does not exist yet, and today all ivmbp agents sign with one shared key, so per-agent attribution is impossible. Proposal: temporary per-agent Ed25519 keys registered in the space policy (like the caller key exception), migrated to the key holder when it exists.

### Promotion to platform memory and session decisions

- An agent promotes a record by writing a record in the platform space that cites its agent-space record as source, with lineage; the original stays in the agent space. The issuer stays the agent; owner-level "platform decided" still needs an owner receipt.
- "Decided in session S": the evidence is the agent's own signed record naming the session; once the session host exports admitted journal positions, the record cites the exact journal position.

### Sync protocol

The engine provides primitives; the skill tells the agent when to use them.

- `memory sync`: fetch every readable space, verify new records, advance a per-space cursor (the last verified head).
- Start of task: `sync`, then `recall` for the task topic. Before a write: `sync` (compare-and-set sees the current head), then write and push; a non-fast-forward means retry. At checkpoints and before finishing: `changes --since <cursor>`. End of task: write what was learned, `sync`.
- A space directory (in the platform space) maps identities and projects to space remotes and access, so an agent can find another agent's memory.
- Optional later: an authorized client posts change notices through the bridge; memory itself wakes no one.

### Federation and projections

There is no central store. Memory is a set of spaces; a view is computed over the spaces the caller may read, with issuer and perspective filters. Sharing an agent space with a second owner means granting git read access and listing it in the directory; that owner's agents add it as a readable space and query it.

### Owner authority in a shared space (simplified)

This matters only for records of the kind "the platform adopted X". Default for v1: each owner's decisions stand as that owner's; a platform view shows both, and a disagreement shows as an evidence conflict. A per-area authority rule in the platform space policy is added only if that becomes a problem.
