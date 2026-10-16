# L15-2 — Report caller-session login presence without credential reads

- Owner repository: **curator**.
- Normative clauses: login-readiness §§1–1.2, 5–7 and all corresponding
  semantic rows in `conformance/login-readiness-v1/README.md`; environments
  §§7.4, 7.9, 12; D7.
- Attack surface: false readiness and secret/process side effects from status.
- Size: 5; platform reader qualification is separately evidenced, never
  inferred from fixtures. Baseline curator `0d00a109`, spec `5509499`.

## Acceptance

Every participating profile × environment has independent `current` and
`login: present|absent|unknown`, with the closed `login_detail` metadata and
`session: caller`. A protected accessible nonempty candidate is present;
successful no-entry lookup is absent; failures, unsafe ownership/modes,
unexpected types/links, ambiguous source/backend, empty file and unqualified
metadata readers are unknown with the exact applicable row reason.

Only the expected verified shared link may lead to native credential metadata.
Detached passthrough remains non-current independently of login. Missing home
proves absence only for an exclusively home-local source with a protected,
readable parent. No JSON parsing or token/expiry/scope/inference assertion.

Full `env status`, not just its new helper, performs no agent invocation,
credential-content open, secret-producing helper, network operation, lease,
prompt or store unlock. Current code calls `detectRelease` through both
`adapterStates` and `verifyHome`/`checkToolRelease`; remove these status-path
effects under L15-0's reconciled version-reporting contract.

Claude macOS metadata uses a separately qualified bounded/nonprompting caller
capability probe. Hash the **exact exported** `CLAUDE_CONFIG_DIR` string, not
realpath, with the specified service/account convention. A qualified fallback
session checks only its file; do not try a second store to obtain present.
Unqualified capability or identity stays unknown. Transport labels (ssh,
desktop) are guidance, not a capability oracle. Codex keyring/auto and Windows
backends stay unknown unless their own metadata reader is qualified.

Managed Muse reads effective file metadata under L15-1. Pi uses its declared
file path. OpenCode is unknown/ambient, not an invented home-local login.
Explicitly adopted external-source metadata readers do not enroll, invoke
helpers or obtain leases; source conflicts are unknown without fallback.

Ordinary complete status exits 0. `env status --check [--json]` exits 0 only
when all existing currency checks pass **and every participating login is
present**; otherwise 1, with all available rows. Operational inability to
produce the matrix is nonzero. No cached readiness in markers/locks/plans;
caller presence never authorizes a snapshot or remote destination.

## Negative tests and positive controls

| Named requirement / negative | Positive control |
|---|---|
| Metadata-only: tripwire agent (including `--version`), secret reader, network and helper see zero calls | Full status with a synthetic nonempty private file emits present |
| Denial, timeout, locked store, directory, unsafe owner/mode, wrong symlink or unavailable parent becomes absent | Successful missing candidate lookup emits absent |
| Zero-length file becomes present; malformed nonempty bytes are parsed for validity | Empty is unknown; arbitrary nonempty synthetic bytes are presence-only present |
| Another session's Keychain item satisfies a fallback session; canonicalized path changes identity | Qualified session selects exactly one store and exact exported-path identity |
| Current+unknown passes check, ambient OpenCode omitted, or non-current+present passes | All current/present passes; plain status still renders with exit 0 |
| Status repairs a detached link or caches presence in a marker | Current verified shared link is inspected without any mutation |
| Node/source conflict is counted as home login or broker timeout triggers local fallback | Adopted unambiguous external metadata reports its selected source only |

Instrument production entrypoints, not self-contained row constructors.
Mutate the harness with one known forbidden content-open or agent execution
and demonstrate the expected tripwire failure; include neighboring valid
controls. Report every declared vector, mutation witness and exact source pin.
Fixtures do not qualify real Keychain API behavior or vendor refresh.

## Dependencies, paths, release cut

L15-0 allocates the status carrier and resolves the version-probe seam;
L15-1 supplies source/store/isolation identity. Likely paths:
`internal/envprofile/status.go`, a focused new metadata reader module,
`internal/envprofile/managed.go` status verification seam,
`cmd/curator/{env,envstatus}.go`, tests and status documentation. Serialize
status/managed edits with snapshot/Muse work; implement the reader module
independently first. Required for rc.7. A backend lacking qualification ships
honest unknown and cannot claim successful native login preparation there.
