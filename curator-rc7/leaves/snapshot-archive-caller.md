# X1 — Produce a canonical archive from a verified snapshot

- Owner repository: **curator**.
- Normative clauses: managed-home-snapshots §§3–5,7; CIP-0014 implementation leaf 6 caller portion and Design §6; X0 published grammar.
- Attack surface: snapshot-to-archive bytes and caller-side resource identity.
- Size: 3; follow-on after SNAP-CLI and X0.

## Acceptance and paired tests

Use Curator's actual-tree verifier and canonical writer to produce the exact bounded archive from an admitted materialized tree. Derive resource metadata from the bytes emitted, not an unverified declaration. Preserve descriptor/profile bindings and expose no credentials, native seeds, source paths or secret metadata. No producer-owned archive authorizes execution.

A valid relocated snapshot produces stable canonical bytes and matching size/digests. Changed/extra/missing entries, symlink substitution, mode mismatch, failed reads, cap excess or concurrent source mutation must refuse without publishing a usable partial resource; nearby unchanged content succeeds. Repeat output is byte-identical under the published grammar. A planted nested synthetic credential and a forged manifest must be caught by the existing closure/verifier gates, not accepted because the archive hash is valid.

## Dependencies and paths

SNAP-CLI and X0; runtime/overlay identity is supplied through its published independent contract. Likely paths: `internal/envsnapshot` archive writer and public export entry per X0, canonical vectors and docs. Serialize shared snapshot verifier/public entry edits; new archive encoding can develop separately against frozen fixtures. X2 and X3 can develop in parallel against those same vectors. No dispatcher source-home lookup, remote resolve or credential packaging is added.
