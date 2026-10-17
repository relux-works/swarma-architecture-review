# ASTRA24-12: does receipt ancestry cross an issuer boundary?

Status: two validated inputs separate the independent readers; judge contract
adjudication pending. No exact-output oracle or implementation fix is asserted.
Owner: astra-24. First execution `6a04e8c`, package `0.2.5-draft`.

## Clauses and two careful readings

Kernel section 5.3 defines currentness from the deciding authority's own ordered
record. K-REV-3 requires each decision's canonical receipt to be issued by its
deciding issuer, then defines currentness through transitive predecessor edges
in a DAG. K-REV-1 preserves issuer-specific assertion sequences. The package
does not explicitly say whether every intermediate receipt event on an ancestry
path must have that same issuer, or whether a canonical path may cross issuers.
The closed input/state checker imposes existence of event and predecessor refs,
not an issuer-homogeneity constraint on each edge.

- Issuer-local reading: compute ancestry in the deciding issuer's canonical
  receipt subgraph. A foreign intermediate cannot establish order between the
  two decisions; both remain maximal and the view is `ambiguous_current`.
- Global-DAG reading: candidate receipts must match their deciding issuer, but
  predecessor closure follows every canonical event, including foreign
  intermediates. The declared path orders the old decision before the new one;
  the view is `current` with only d3 selected.

Both are descriptions of the existing vocabulary, not proposals for a new
transfer/delegation mechanism. Recommend issuer-local ancestry as the closer
reading of the authority's own ordered record, but request adjudication before
turning it into an exact expectation. If cross-issuer edges are inadmissible
state instead, the contract must specify that integrity constraint and outcome;
passing the current structural checker alone cannot decide the semantics.

## Minimal read-only pair

Start from ASTRA24-11's admitted receipt-only chain: r1 <- r2 <- r3, decisions
d1/r1 and d3/r3 by H1, no d2 assertion. All sources are readable/resolvable and
all three events are canonical. There are no operations, revisions or CAS checks.

The positive keeps H1 as every event's issuer. The separating input changes the
middle event r2 to H2 and consistently attributes its source record to H2
(issuer, authenticated submitter and own perspective). The old/new decision
records and endpoint receipts remain H1. Exact receipt references and graph
edges, subject, space, query, disclosure and permissions are identical.

Both complete input/state triples pass the 0.2.5 closed shapes and state checks.
An initial local draft changed the source issuer without its submitter and was
correctly rejected for missing checked representation; it was fixed before any
runtime execution. That setup error is not this divergence.

## Independent observed outputs

| Input | Source evaluator | Package evaluator |
| --- | --- | --- |
| Same-issuer intermediate | current d3; d1 historical | current d3; d1 historical |
| H2 intermediate between H1 endpoint receipts | ambiguous d1/d3; no history | current d3; d1 historical |

Each evaluator preserves admitted records, runtime and policy in both reads.
The package may issue its ordinary private per-view binding; no durable memory
mutation or external effect is claimed. No expected output was passed to either
execution API. The source explicitly traverses canonical events by issuer;
the package's shared `authority_succeeds` traversal currently uses all canonical
events. This explains the separation but does not settle which reading is right.

Complete inputs are in
[astra-24-authority-issuer.input.json](astra-24-authority-issuer.input.json);
first full views, input hash and implementation module hashes are in
[astra-24-authority-issuer.first.json](astra-24-authority-issuer.first.json).

Input bundle SHA-256: `8224829a810a97c79fef81cb18f0d650b59ffc84a3262bdef09b1ea900c521b3`.

Structural evidence: `.temp/astra24-authority-issuer-structure-02.log`.
The invalid pre-execution draft is separately identified as log01. Existing
same-issuer R7-051 fixes remain verified; this asks about a distinct issuer
boundary. The two native probes stay outside exact-vector denominators until
judge/editor establish the allowed input/ancestry rule. If the kernel itself
admits both readings, classify and preserve an owner question rather than
silently choosing architecture in an evaluator.
