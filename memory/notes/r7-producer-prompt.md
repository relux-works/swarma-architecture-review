You are the producer of the R7 specification package for "bounded evidence memory", working in a disposable copy of a private design repository. The memory lane orchestrator (a Claude session) reviews your output and lands it; you do not commit, push, publish or message anyone.

## Hard rules

- Read and write only inside this directory. Write only under `memory/spec/`. Do not modify any other file.
- No network access is needed; do not install packages. Use only the Python 3 standard library for any script (the `jsonschema` package is NOT installed).
- Do not start background processes, servers or other agents.
- English only. The kernel part of the package must contain no Swarma, Curator, board, dispatcher, session-host, a2a or other platform terms, no agent seat names, no local paths, no private links: it may become public (decision D-002/D-007).

## Read first (in this order)

1. `memory/DECISIONS.md`: owner decisions D-001…D-008. Binding.
2. `memory/designs/kernel.md`: the consolidated kernel contract. Your primary normative source.
3. `memory/designs/bounded-support-semantics-astra-03.md`: the semantic companion. Its §§3–6 and vectors S01–S27 stay normative unless kernel.md amends them.
4. `memory/designs/bounded-evidence.md`: stores/authority, APIs, and its 17 boundary vectors (table "First-slice acceptance vectors").
5. `memory/notes/review-1-gaps.md` and `memory/notes/usecase-profiles-gaps.md`: why the amendments exist.

## Goal

Turn the contract into one canonical, closed, machine-checkable package, so that an independent implementer who reads ONLY `memory/spec/` can build an evaluator that produces exactly the expected outputs. Ambiguity is the enemy: wherever the sources leave a choice open, make the narrowest choice consistent with them, and record it.

## Deliverables (all under `memory/spec/`)

```
memory/spec/
  README.md                 package map, version (0.1.0-draft), conformance rules, how to run the checks
  kernel/
    semantics.md            normative kernel semantics, closed and self-contained (RFC 2119 words), derived from kernel.md + companion; no platform terms
    schemas/                JSON Schema 2020-12, closed (additionalProperties: false everywhere)
      envelope.schema.json
      assertion.schema.json  source.schema.json  justification.schema.json
      assessment.schema.json revision.schema.json
      domain-schema.schema.json      meta-schema that every domain schema document must satisfy (types, equality, cardinality, incompatibility rules, statement kind, freshness default, disclosure defaults)
      projection-rule.schema.json    the three rule families
      query.schema.json  view.schema.json (incl. the extended per-polarity result)  receipt.schema.json  refusal.schema.json (closed error/refusal codes)
      vector.schema.json             format of a conformance vector
    vectors/
      semantic/   one JSON file per vector: S01–S33 and P01–P11
      deployment/ boundary vectors from bounded-evidence.md, renumbered B01–B17, that test a protected deployment rather than semantics; mark any of them that are actually semantic and put those in semantic/ instead, with a note
  domains/
    decisions/        domain schema documents for the architecture-decision pilot (decision, rule, assumption) + a small fixture corpus for the archive-home → delete-home case
    profiles-synthetic/ domain schema documents for interest, competence, location, availability, intent, account_link, relationship_status, open_to_introductions; synthetic data only, no real people
  adapters/
    swarma.md         the Swarma adapter contract (this file MAY use platform terms): how identities, policy scopes, representation references and source owners bind to the kernel; the data-only delivery of D-001; what the adapter must never do. It is destined for the platform architecture repository.
  checks/
    validate.py       stdlib-only checker: parses every JSON file, checks that schemas are closed, that every vector validates against vector.schema.json structurally (implement the needed subset of JSON Schema yourself: type, required, properties, additionalProperties, enum, const, items, $ref within the package, oneOf), that every vector id in the coverage table exists exactly once, and that domain schema documents satisfy domain-schema.schema.json. Exit non-zero on any failure.
  AMBIGUITIES.md      every place where the sources were ambiguous, contradictory or silent; for each: the choice you made, why, and which vector pins it. Also list choices you could NOT make and that need the owner.
  COVERAGE.md         table: vector id → normative clause(s) in semantics.md → source clause (kernel.md §, companion §, design table row)
```

## Vector format requirements

Each vector is closed and executable in principle: `id`, `title`, `profile` (`semantic` or `deployment`), `clauses` (ids of normative clauses in semantics.md), `initial_state` (a complete snapshot: records with full envelopes, domain schemas referenced, policy facts as plain data), `operations` (ordered admit/revise/declassify/erase/… calls with exact inputs), `query` (exact), `expected` (exact output or typed refusal, including every per-polarity field), `forbidden` (outcomes that must not occur, stated as checkable predicates), and `normalization` (which fields are random/fresh and how they are compared, per the companion's S13/S24/S27 rule). Use opaque ids like `rec:a1`, `subj:h1`. Expected outputs must be derived by hand from semantics.md; do not invent behaviour that semantics.md does not state — if you need it, add the clause to semantics.md and cite it.

## Quality bar

- Every clause in semantics.md has a stable id (e.g. `K-ENV-3`) and is referenced by at least one vector, or is listed in COVERAGE.md as "not vector-tested" with a reason.
- No clause contradicts DECISIONS.md. Where kernel.md and the companion disagree, kernel.md wins; note it in AMBIGUITIES.md.
- Run `python3 memory/spec/checks/validate.py` until it exits 0, and include its final output at the end of your last message.

## Final message

Summarize: files written (count by directory), the number of normative clauses and vectors, the validate.py result, the top five ambiguities you resolved and every open question for the owner.
