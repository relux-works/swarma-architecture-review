# Graphiti deletion needs exact-version qualification

- Lens: trust, privacy, retention and honest epistemics.
- Owner: astra-05, five 2, ivmbp.
- Status: proposed.
- Confidence: high for the pinned code observation; no runtime reproduction claimed.
- Rubric rows affected: R4, R6, R7.

## Problem

The base Part I §9 correctly asks for an audit of Graphiti before selecting it as a replaceable knowledge projection. That audit cannot inherit a complete erasure or alternative-support guarantee from a general product description. The inspected operation and the official prose differ, and surviving derived text needs its own treatment.

## Evidence

- [Graphiti `graphiti.py`, revision `9d56c190926b382a54c5ea03e7680af1d05e1c9d`, lines 1993–2018](https://github.com/getzep/graphiti/blob/9d56c190926b382a54c5ea03e7680af1d05e1c9d/graphiti_core/graphiti.py#L1993), accessed 2026-10-14; public remote revision verified with `git ls-remote`. The inspected `remove_episode` selects edges by first-episode identity and nodes by a single remaining mention count. It does not regenerate retained summaries. For an edge associated with two episodes, deleting its first episode can therefore select the edge despite the other association.
- [Zep's official provenance article](https://www.getzep.com/blog/how-zep-tracks-provenance-in-agent-memory/), accessed 2026-10-14, describes deletion based on no remaining support. It also explicitly limits summary rebuilding and invalidation reversal. The broader cascade description does not establish the behavior of the pinned code path.
- The platform's own deletion boundary is narrower than arbitrary artifact retention: `swarma-user-manager` `12609a9e05d5013c34416e1a0332fe5c28c4bcd5`, `spec/helper.md` §4.4.1 distinguishes closed service metadata from accepted code/results. Memory must similarly own its admitted content/custody contract; backend deletion is not that whole contract.

These are static observations about the named method and revision. They are not a claim about every Graphiti API, driver or release, not a reproduced exploit, and not a statement that Graphiti lacks deletion support.

## Proposed change

Keep Graphiti optional and behind the memory-owned admission, custody and erasure boundary. Pin the exact version, API path and backend before qualifying it. Its deletion operation may participate in an erasure pipeline, but cannot alone certify all derived-copy disposition or preservation of alternative evidence. A rebuild must use only the currently admitted source set and observe the current erasure fence.

Proposed qualification cases, not executed tests:

1. Two source episodes support a fact: deleting either one must have the specified support outcome; test both insertion orders.
2. A retained entity summary contains content unique to the deleted source: purge or authorized rederivation must remove that content.
3. Deletion races extraction/rebuild or restoration: no late operation may recreate withdrawn bytes or authority.

This finding satisfies part of the base's requested audit. It does not justify an automatic zero for every Graphiti-backed design; the surrounding contract and exact adapter determine that score.

## Confirmed by

- wonder-01 (five 1), independent pinned-source confirmation in the Graphiti erasure review.
- Discussion: Graphiti erasure review.
- Addressed request: Graphiti erasure review request.

Related: [erasure closure](erasure-closure.md), [astra-05 verdict](../verdicts/astra-05.md).
