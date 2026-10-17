# First working version: architecture draft (for owner decisions)

Status: draft by the memory lane, 2026-10-18, answering Ivan's direction in session: move to a first working version, not a pilot; memory is autonomous (agents write it themselves, no approval gate); both agent-own and platform memory; shared platform memory with a second owner's agents; Go; one new repository; part of the Swarma platform architecture. Nothing here is decided until recorded in `DECISIONS.md`.

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
