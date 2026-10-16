# T2 — Admit node policy and project metadata-only source state

- **Owner repository:** curator.
- **Normative clauses:** T0 L1/L3/L4/L5; CIP-0010 C2/C3.1/C3.5/C6; login-readiness §§1,1.1,1.2,2,3,4,5; environments §§7.4,12.1–12.2.
- **Attack surface:** source-policy resolution and adoption; reuse the separate readiness engine rather than add another credential probe system.
- **Size:** M, source-policy hooks and carrier integration, not a full status/login rewrite.

## Acceptance

1. Parse user-owned `credential_source.<profile>.claude_code` only from T0's published manager revision; source-policy v1 absence preserves per-home. Reject package/lock/overlay selection and unsupported harness/mode.
2. Apply source → home-store selector → isolation → link. Node requires native home-store selection and no native link; explicit conflicting isolation/locks refuse. Retained CIP-0003 semantics let node override an implicit link-sharing default, never an explicit shared instruction.
3. Source migration is inspect → plan → apply, preserves native credentials and old home evidence, and uses coordinated marker/source identity. Ordinary resolve/repair/status never silently adopts node or marks a historical per-home-keychain strategy as observed login.
4. Project required non-secret source metadata through the published successor. `env resolve`, shell preview and dry run never read secret values or emit an ambient token export. Snapshot inventory remains source/credential-free.
5. Integrate registration metadata with the established reader/row engine: node/native/file/caller, present/absent/unknown as design §4. No agent execution, secret contents, Keychain prompt or network from any status column. Node login refuses; prepare gives enrollment guidance without minting or falling back. Current+present still does not certify executor or vendor authentication.

## Mandatory negatives and positive controls

- ST-01/06: package lock, unsupported store, explicit shared lock, old per-home marker/native credential, changed source mid-operation: intended refusal, no native credential deletion/link/copy or repair migration. Valid explicitly adopted source resolves.
- ST-05: missing versus denied/unsafe/empty/conflicting registration has exact distinct outcomes. A fake nonempty sentinel candidate is present, proving only accessibility; a read-spy confirms zero secret opens/vendor/helper/network calls.
- ST-12: node absent/unknown never invokes home login or setup-token; nearby per-home isolated/absent participant still uses the normal admitted login ceremony.
- ST-09/13: source/token cannot enter snapshot, old fragment, shell export, plan literal or current marker authority; metadata-only successor is accepted.

## Dependencies and paths

T0; T1 metadata API; CIP-0015 store/admission and metadata readiness leaves. Serialize with D14/CIP-0018 work on `internal/config/environments.go`, `cmd/curator/envconfig.go`, `internal/envprofile/managed.go`, marker models, `internal/envfragment` and public CLI entry points. `internal/envprofile/status.go` and `cmd/curator/envstatus.go` consume the shared reader; login/prepare get source-specific guidance hooks only. Read-only resolver and snapshot work must compose on the reviewed integrated head.
