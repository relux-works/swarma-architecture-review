# X0 — Publish the cross-service snapshot archive contract

- Owner repository: **curator-spec**, with separately reviewed matching amendments in curator-agent-launcher `SPEC.md` §10 and swarma-dispatcher `R-TRANSFER`. Publication is coordinated; each repository owns its commit.
- Normative clauses: managed-home-snapshots §7; CIP-0014 implementation leaf 5 and Design §6; D6. The CIP tar subset/caps remain proposals until this leaf publishes exact values.
- Attack surface: archive grammar and independently admitted plan/resource binding.
- Size: 3 for the normative allocation; matching repository publications are small required handoffs, not code implementation.
- Cut: follow-on publication; never a prerequisite for pure materialize.

## Acceptance and paired vectors

Freeze exact header, padding, end bytes, canonical paths/order/modes, size/count/depth caps, required-understanding wire members, protected expected identity, resource intake and cross-service refusal mappings. Bind archive length/digest, manifest/descriptor digests, profile/adapter pin, runtime/overlay identity and bounds to an independently admitted immutable plan. No generic extractor tolerance or self-minted digest authority.

Valid canonical bytes and a genuinely admitted matching plan form the positive controls. Reject alternate encodings, traversal/aliases, links, duplicate/special entries, trailing/truncated data and cap excess. Separately reject identical bytes with missing admission, wrong profile/adapter or a stale/mismatched protected expected digest. A known-invalid carrier must fail the exact grammar/authority checker; an unrelated setup failure is not a control.

## Dependencies, paths and handoff

Frozen snapshot metadata/descriptor contract; coordinate HOST-HOME-SPEC runtime projection without reopening content inventory. Paths: snapshot transport protocol and schemas/conformance in curator-spec, launcher `SPEC.md` §10, dispatcher transfer contract and capability references. Serialize shared launcher spec publication with hosted and token amendments. X1/X2/X3 consume the same immutable fixtures; none may choose its own archive spelling or limits. Runtime B confirmation and platform protection are separate activation gates, not implied by wire publication.
