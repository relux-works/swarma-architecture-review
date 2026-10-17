# Review 3 against the contract

Input: `memory/inputs/REVIEW-3.ru.md` (operator-supplied, 2026-10-17). It reviewed book chapter v0.3 only. Every point is now answered in `designs/kernel.md` v0.2; this note maps them. Status: proposed, pending executable vectors.

| Review point | Kernel v0.2 answer | Vector |
| --- | --- | --- |
| §2 Snapshot is immutable, its applicability is not | §6.4 frozen views: history bound to a cut; "knowledge moved on" vs "use or disclosure revoked"; the next delivery or effect owner refuses or rebuilds; caches never extend permission | P12 |
| §2 Editorial: "no automatic seed" vs "snapshot stays" | §10: first slice is explicit tool pull only; the snapshot is a later adapter mechanism whose channel D-001 fixes | — (text); book fixed in v0.4 |
| §3 Declared evidence is not complete lineage | §7.1: lineage comes from the integration's controlled inputs; `lineage: unknown` inherits the most restrictive supplied constraints and is not publishable; first publishing path is structured fields only | P13 |
| §3 Assessment of permission is not permission | §7.2: a `declassification` assessment is evidence of the owner's decision, rechecked before each disclosure; a model's "safe" is `semantic_review`; each owner lifts only its own constraint | P05 |
| §4 Three conflicts | §5.4 table: `version_conflict` (write), `ambiguous_current` (projection), evidence conflict (both witnesses); never mapped onto each other | P14, P10, S28, S02 |
| §4 Exclusion from own projection ≠ revising another's record | §9.3: exclusion is a projection-rule choice; local erasure by policy | P15 |
| §5 Linking several profiles | §9.4 subject handles (already in v0.1); P09 now names the shared-global-id case | P09 |
| §7 Portability needs the full normalized input tuple | §1: corpus, schema and rule versions, perspective, authorized projection, cut, logical budget | all |

The review's process advice is adopted: no further kernel widening before the first execution; the next work is the R7 package and independent implementations.
