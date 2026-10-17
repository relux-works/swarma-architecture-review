# ASTRA25-03: independent support does not preserve tainted derivative bytes

Status: source-contract regression case; package not yet landed.
Owner: astra-25. Source baseline: `4d4ef45`; kernel v0.2.

## Clauses

Kernel §7.1 and P08; companion §6 and S12/S20; bounded-evidence design,
"Retention and derived information"; incorporated erasure-closure finding.
Content/custody lineage is distinct from the epistemic justification graph.

## Minimal separating input

```text
C: retained assertion with independent, currently allowed sufficient witness B
A: restricted source supplying a synthetic identifying detail
D: cached summary of C containing that detail, content lineage [A, C]
There is no justification edge A -> C or A -> D.
Custody: primary D payload, derived search entry I, cached frozen view F.
Operation: authorized erasure of A and its controlled content derivatives.
Primary D and I purge receipts exist; F's controlled sink is unreachable.
```

F is a previously generated historical artifact, not an independently owned
recipient outside the declared custody boundary. No new authority to delete
external journals is assumed. Historical disclosure rights do not authorize new
delivery of erased content.

## Two readings and outputs

| Observation | Erasure follows support invalidation only | Erasure follows content and custody lineage |
| --- | --- | --- |
| C support after erasure | present via B | present via B |
| D/I/F containing A-derived detail | may remain because C stays supported | fenced; purge/rebuild obligations remain |
| Erasure completion with missing F receipt | success | incomplete / purge-pending |
| Historical F re-delivery | allowed as immutable history | refused while content is erased/fenced |

The first reading also fails if D and I are actually deleted but it declares
complete erasure without accounting for the unreachable cached-view sink.

## Recommendation and controls

Use content/custody closure. The proposition can remain supported through B;
that says nothing about retaining A-derived bytes. Never create C- from erasure.
F's historical identity may survive in an admitted nonsensitive receipt; its
immutable historical nature is not a promise to retain or replay deleted bytes.

Positive control: all registered sinks reconcile and return valid purge receipts,
then completion within the named controlled boundary is possible. Rebuild a new
summary from C/B only, with a new identity and permitted lineage; no A detail may
return. Negative neighbor: a stale extractor tries to recommit old D after the
erasure fence; it must be refused or actually rederive from allowed inputs.

## Evidence and limits

No purge, service, backup or remote sink is operated in this audit. This is a
state-machine and representation requirement, not deployment qualification.
Package-format vectors should keep witness semantics separate from custody
completion and expose any unsupported deployment operation explicitly.
