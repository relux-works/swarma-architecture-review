# Authorization covers inference status and provenance, not only source text

- Lens: trust, privacy, poisoning and epistemic honesty.
- Owner: astra-02, five 1, ivmbp.
- Status: proposed.
- Confidence: high; independently confirmed by astra-05, five 2.
- Rubric rows affected: R4, R6, R7; preserves R3.

## Problem

The base's `recall` returns status, conflicts, dependencies, evidence and a proof reference; `explain` and `changes` disclose additional structure. Namespace filtering is insufficient if these outputs were computed from globally visible evidence before inaccessible links are removed.

Counterexample: the public corpus contains support for C. Add one private refutation without changing any public records. If the public caller now sees `conflicted`, a new conflict count, a changed rank, a proof node or a different change cursor, private information has crossed the boundary. Returning C as globally supported while concealing its basis is also misleading. Public proposition text does not make its provenance public.

The base's separate read/use/retain/forward rights and KnowledgeView concept support the correction, but do not yet specify this output semantics.

## Evidence

1. Base `memory/inputs/SKETCH.ru.md`, Part I §§6,8 and Part II §§4,6: structured recall, independent data rights, no memory-to-instruction promotion and current authorization at the action boundary.
2. `swarm-platform-architecture` revision `567b07701bdf32cdebc516e38e6f0321fc5253a0`, `vision/contracts/handoff-package.md` §§1,3–5: per-recipient projection, per-item provenance, reference-resolution authorization and reauthorization at seed time.
3. `swarma-credential-broker` revision `ec7fb3d0670449b074521d51f3e03b59f0142a69`, `spec/broker.md` §§4.1–4.2,6.4: identity is not caller-supplied and historical authorization is not current authorization.
4. [W3C PROV-AQ §6](https://www.w3.org/TR/prov-aq/#security-considerations), accessed 2026-10-14: provenance can expose sensitive derivations and behavior even when the resource itself is public; privacy controls and auditing apply to provenance. §4.2 also distinguishes existence-sensitive errors. This supports the threat, not a complete implementation of information-flow security.

## Proposed change

- Bind each view to authenticated recipient, task purpose, source/claim revisions or watermarks, effective policy revision and as-of semantics.
- Evaluate support and refutation over evidence eligible for that view. Preserve separate positive/negative witnesses and evaluation completeness; bounded or interrupted computation cannot turn an unseen polarity into an established absence. A result is supported-within-view, never globally unconflicted merely because a source is hidden.
- Apply the same boundary to `recall`, `explain`, `verify` reports, `changes`, relationship traversal, counts, ranking, pagination/cursors, errors, cache keys and notification contents. Shared ranking statistics must not introduce a forbidden cross-space dependence. Content locators, digests and source-author identities are protected outputs too.
- If an owner deliberately permits publishing a conclusion while withholding its basis, create an explicitly declassified derivative or attestation with its own provenance and rights. A global support bit cannot act as an implicit declassification mechanism.
- Reauthorize every new disclosure, including cached views and handoff/reference resolution. An immutable view records what was issued; it is not perpetual access. Do not promise revocation of information already in a recipient's context.
- Unknown/denied/erased evidence are distinct internal states. Reveal the distinction only when the caller is allowed to know it; otherwise use an indistinguishable response contract. Do not expose hidden object counts in an explanatory error.
- Maintain memory as labeled data through summaries, compaction and restore. Existing Curator approval remains necessary for a proposed instruction/skill; source authenticity and allowed visibility do not grant authority.

## Conformance vectors and honest limits

Construct two managed stores with identical authorized records and allowed policy outputs but different inaccessible records. For the same recipient/purpose/query, compare visible response semantics: claims, statuses, proofs, provenance, counts, rank, cursor, errors and advisory notifications. They must match unless the difference is itself explicitly authorized. A secret refutation is the minimum counterexample.

Also test authorization withdrawal between cache issuance and reuse; direct `explain` with a guessed hidden ID; a hidden source author on a public proposition; an interrupted negative-evidence search; and a declassified attestation whose raw source remains inaccessible.

This is a specified functional non-disclosure property, not a claim of universal covert-channel elimination. Shared-resource timing and availability require an explicit deployment threat model and qualification. A finite test suite cannot prove that a model will never infer a private fact from legitimately released information. Scores must not overstate those limits.

## Confirmed by

- astra-05 (`ivmbp_swarma-memory_astra-05`, five 2), after independent score freeze: event `$xsPoJ7ySbI_0Q7ev0saFa7mvwPPaHpRljhmg-1oH3J4` in `f-view-inference`; independently confirms status leakage and requires rank/count/cursor equivalence and scoped completeness. Owner acceptance: `$xzASIoBf7TlGzWYhc-15wyPLFO1eqNc9i1yfWmmPuuQ`.
- Topic root: `$AskgYFX-NOEGGAeOKav2Kwp2ZUg_TqrlGkyedbXDNOg`.

Related: [astra-02 verdict](../verdicts/astra-02.md), [erasure closure](erasure-closure.md).
