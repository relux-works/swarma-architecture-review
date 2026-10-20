# Panel brief: three open questions in the swarma-memory design

You are one member of an independent panel. Several other models get the same brief and the same material, and none of you sees the others' answers. The orchestrator compares the answers and turns the points where you converge into design decisions. A concrete, well-argued answer is worth more than a survey of options.

## The owner's request (verbatim, Russian)

«Так, по поводу memory design, пускай запустит коллектив режим, там могут быть AstroMax, пускай будет несколько AstroMax, можно несколько Opus 5.5 Max, можно, если есть еще ресурс Muse Wonder X-High, можно еще кого-то, ну, обозначить им вопрос, обозначить им наш дизайн памяти, отдать им прям книгу с этим дизайн памяти, передать им эти вопросы и пусть поищет подходящее решение на конкретно эти вопросы.»

In short: give the panel the full memory design and these questions, and let each panelist find a fitting solution.

## Material (all in this directory; read only here)

Read these in full before you answer:

1. `book/01-pamyat-agentov.md`: the book chapter that describes the memory system as a whole, in Russian. This is "the book" the owner means.
2. `design/DECISIONS.md`: the owner's decisions D-001…D-026. They are decided design. Do not reopen one unless you show it is defective, and say so explicitly if your proposal needs one changed.
3. `design/OPEN-QUESTIONS.md`: every open question. Yours are 8, 9 and 23. Items 20–22 are provisional implementation choices you may rely on or criticise.
4. `repo/docs/architecture.md`: the architecture of the first working version (v1). Stages 1–4 are implemented. Stage 5 (platform space: directory, promotion, sharing with a second owner) and stage 6 (escalation) wait on your questions.
5. `repo/spec/`: the normative package (closed JSON schemas, `kernel/semantics.md`, executable semantic vectors). Any change to kernel behaviour or to the view is a package release with new vectors.

Use as needed:

- `repo/docs/*.md`: the implemented contracts (`git-spaces.md`, `signing-policy.md`, `read-evaluation.md`, `disclosure-erasure.md`, `write-admission.md`, `cli.md`), plus `repo/UNRESOLVED_QUESTIONS.md`.
- `repo/go/`: the implementation, for when you need to check what really exists.
- `design/SYNTHESIS.md`, `design/designs/`, `design/findings/`: the design history and the collective findings behind the kernel.
- `platform-book/`: the Swarma platform book, in Russian. It covers identities, keys, grants (`06-granty.md`), the board (`13-doska.md`), keepers, orchestrators and the bridge. Use it for what the platform already offers for escalation and ownership.

## The three questions

### Q1 (OPEN-QUESTIONS 23). Session-excerpt sources are not visible to readers

The normative view carries `source_refs` (ids and versions) but no source payload, and source records are never read items. A reader sees that a decision cites a session source, but not the locator (runtime, session, message, digest) or the excerpt. Architecture §7.2 and §8 promise exactly that. The fix has to come from the package; computing disclosure outside the kernel was rejected.

**Wanted:** the exact contract change. Choose between a disclosure-filtered source payload in the view, a separate source-read operation, or something better. Give:
- the schema shape;
- how disclosure and availability states (available, unavailable, withheld) apply;
- what a reader without the right sees;
- the new vectors, including non-interference and negative cases.

### Q2 (OPEN-QUESTIONS 9). The space directory: format and owner

The platform space holds a directory that maps identities and projects to space locations and access (architecture §5.4, D-018). An agent finds another agent's or project's memory through it. Sharing a space with another owner means granting git read access and adding a directory entry.

**Wanted:**
- the entry format;
- who writes and signs entries, and who owns the directory;
- how a reader verifies an entry;
- whether an entry is a kernel record kind or an adapter-level signed object;
- what the directory is authoritative for and what it is not. Access truth today lives in each space's owner-signed policy and in git access;
- what happens to stale and revoked entries;
- how the stage-5 gate is met: two owners' agents read each other's shared spaces.

### Q3 (OPEN-QUESTIONS 8, D-020). Who resolves which conflicts, and the escalation path

D-020 and architecture §10 give the rule. When the current work depends on a decision that is `ambiguous_current` or in evidence conflict, the dependent step stops. The agent or its orchestrator escalates to the resolvers named in the space policy for that area. Memory itself never escalates or wakes anyone. The resolvers record a superseding decision.

**Wanted:**
- how the space policy names resolvers per area: the area selector and the fields;
- the default resolver when none is named;
- resolver authority in terms of the existing grants and revision authority;
- conflicts across two readable spaces, or between decisions by different owners;
- the concrete escalation path. The proposals are a Swarm Keeper escalation and a board task addressed to the resolvers. Say what exists today and what v1 should use;
- the escalation packet the CLI or skill produces;
- how the stage-6 gate is met: a conflicting decision stops a dependent step and reaches its resolvers.

## Constraints

- **v1 storage:** git spaces only. There is no memory server and no protected service. Every record is signed by its submitter, and every reader verifies (D-019). Authority comes only from the owner-signed space policy (provisional trusted kernel profile: OPEN-QUESTIONS 20).
- **v1 keys:** temporary per-agent keys, registered by the owner in the policy (D-017, D-024). The platform key holder does not exist yet.
- **External agents** have no memory of their own in v1 (D-021).
- **The kernel** is deterministic and closed. Disclosure, erasure and non-interference are kernel properties with vectors. Do not move them into adapters.
- **Escalation stays outside memory.** Memory never wakes a session, changes a task or escalates by itself (D-020).
- **Proportionality.** Prefer the smallest change that meets the stage gates and keeps the target design reachable. Say what is v1 and what is later.

## Answer format

Write your answer in English, in Markdown, as your final message. Keep it under about 4,000 words. For each of Q1, Q2 and Q3, give:

1. **Recommendation:** concrete shapes, fields, who signs, and the flows.
2. **Why:** the reasoning, with references to sections, decisions and files.
3. **Trade-offs and rejected alternatives.**
4. **Changes needed:** package, architecture, decisions and implementation, each marked v1 or later.
5. **Tests and vectors:** positive, negative and non-interference, with the gate check.
6. **Risks**, and your confidence (high, medium or low).

End with a short section, **For the owner**: only the points that need a product or ownership decision from the owner and that you cannot settle from the material. Say why each one needs the owner.

## Rules

- Do not modify, create or delete files. Do not run network commands. Do not read outside this directory.
- Do not invent platform components. If you rely on something, cite where it is described. If it is missing, say so.
