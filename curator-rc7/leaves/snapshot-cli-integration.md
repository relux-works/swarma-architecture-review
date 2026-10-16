# SNAP-CLI — Materialize command and production-entry proof

Owner repository: **curator**. Size: **3**. Required in rc.7, after SNAP-ID / SNAP-LOCK / SNAP-CLOSURE / SNAP-PUBLISH.

Normative clauses: snapshots §§1–6; environments §§8.1/9.2/10.1/10.5/13; CIP-0014 compatibility step 1 and implementation leaf 2. Section 7 archive/runtime gates stay explicitly unimplemented.

Attack surface: orchestration and public CLI behavior bypassing otherwise correct helpers.

Acceptance criteria:

- Expose exactly `env materialize <env-id> [--profile name] --into dir [--format json]` or `--manifest-only --format json`. Detect both/neither destinations, bare manifest-only and unsupported formats before selection/lock/write.
- Run the same locked selection, relocation and hashing in both forms. With unchanged source fragment/inputs, emit identical canonical manifest bytes; manifest-only publishes no destination. No success output precedes final verification/publication.
- Preserve published diagnostics and source/target state on refusal; never repair, provision, recover, login or launch as a convenience. Document explicit repair/preparation followed by a new invocation.
- Ship the actual-tree verifier together with export and byte conformance; distinguish its internal implementation from the later consumer-facing hosted API. Do not advertise snapshot runtime, hosted support, archive interoperability or source-home-independent manifest hashes.
- Update CLI/API docs, README tool entry and capability/release notes with supported forms/platform evidence and explicit unsupported Opencode/runtime/archive bounds.

Mandatory tests with positive controls:

| Positive control | Negative case / required invariant |
| --- | --- |
| Public CLI exports a stable valid fixture and manifest-only matches it | Illegal flag combinations invoke zero selection/lock/publication operations; no success manifest |
| Known current input succeeds with a fresh permitted destination | Stale/unprovisioned, lock timeout, pending recovery, unreadable marker/store/credential metadata, bad destination and drift return specified errors without repair or fallback |
| Independent output survives repair/use/global sync of source fixtures | Runtime/live-home reference remains absent; changed generation cannot overwrite an existing snapshot |
| Qualified adapter and platform uses the real path | Helper-only passing evidence, unsupported adapter/form or skipped platform cannot be reported as production support |

Run the seven materialize production-entry property groups named in CIP-0014 (content, destination, generation, source, portable identity, idempotence, plus CLI syntax/output) and their applicable bounded M1–M6 controls. Record real versions, commit and exit codes. These tests are planned, not executed in this read-only collective.

Paths/serialization: `cmd/curator/env.go`, new `cmd/curator/env_materialize.go` and entry tests, `internal/envprofile` orchestrator, `docs/environment-config.md`, README/CLI reference. Shared `env.go`/docs changes serialize behind CIP-0015 CLI/store and v4 emitter edits; pure snapshot packages can develop in parallel. Ordinary native curator-run and headless task-board spawn migration remain explicit D4 follow-up leaves, not covered by this command's existence.
