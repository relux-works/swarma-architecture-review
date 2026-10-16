# SNAP-CLOSURE — Verified content closure and relocation

Owner repository: **curator**. Size: **5**. Required in rc.7.

Normative clauses: snapshots §§3, 4 (descriptor channels), 5 (protected source objects), 6 (adapter bounds); environments §§5/7/8.1/10.2; CIP-0014 leaf 2.

Attack surface: accidental credential/state export or semantic loss when moving content away from its live home.

Acceptance criteria:

- Derive the allowlisted closure from verified lock, renderer and marker, not a recursive copy or marker-only authorization. Include complete admitted skill payloads, referenced supports, root context, system prompt and declared MCP, including participating global skills.
- Exclude seeds, credentials/credential links, native config, markers, unknown files and runtime state. Validate selected assets using existing secret/admission checks; secret-bearing selected content refuses rather than silently changing the profile. No credential content is read to perform exclusion.
- Resolve only recorded managed store indirection by verified identity through protected handles. Never recursively follow arbitrary links or credential/foreign-XDG links. Reject reparse/special/unrecorded/escaping objects.
- Rerender generated source-home/store references with qualified snapshot-relative semantics; hash relocated output. Preserve opaque asset bytes. Unsupported absolute-only forms return `environment_materialize_relocation_unsupported`.
- Produce exact per-adapter relative env maps and Muse `root_context` iff selected verified content requires it. `path_prepend` refuses in v1. Opencode materialize refuses `environment_materialize_adapter_unsupported`; Pi receives no synthesized MCP. Backend policy and Codex launch settings remain separate composition inputs.

Mandatory tests with positive controls:

| Positive control | Negative case / required invariant |
| --- | --- |
| Admitted root/support/skill/system/MCP fixture exports completely, preserving executable metadata | Nested credential-shaped state, native seed, auth link, marker internals or unknown surface cannot enter output; credential-read spy remains unused |
| Clean admitted skill exports byte-exactly | Secret-bearing selected asset refuses; no redacted substitute or successful partial export |
| Recorded store link to the verified object exports an independent regular file | Unrecorded/nested escaping link, replaced store object, failed read or special file refuses |
| Qualified relocated referenced form remains functional after source fixture removal | Leftover generated live-home reference or unsupported include semantics refuses; opaque payload is never search/replaced |
| Claude/Codex/Muse/Pi declared supported forms produce their specified descriptors | Opencode, required `path_prepend`, false Muse root omission, invented Muse/Pi MCP or settings/backend fields refuses |

Controls: credential-denylist-only export (M1), failed read treated as optional absence (M4). Production CLI coverage is required in SNAP-CLI; helper tests alone do not establish exported closure.

Dependencies/paths: SNAP-ID interface, SNAP-LOCK capture contract; serialize `internal/envprofile/managed.go` (`assembleHome`, `verifyHome`, `buildFragment`) and `internal/contextmaterialize/{contextmaterialize,referenced,mcp}.go` changes with CIP-0017/18 work. Prefer new `internal/envprofile/materialize_content.go` and relocation files. Existing `assembleHome` includes link/seed behaviors and must not become an unfiltered exporter. Finish v4 root-context/credential projection first so capture freezes the actual supported source fragment.
