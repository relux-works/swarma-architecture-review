# L15-0 — Publish the containing login/store contracts

- Owner repository: **curator-spec**.
- Normative clauses: `protocol/login-readiness.md` §§1, 1.2, 2, 2.1, 5–7;
  `protocol/profile-codex-settings.md` §§3–7; `protocol/environments.md`
  §§7.4, 7.9, 10.2, 12–12.2. Owner decisions D7, D8, D14.
- Attack surface: accepting new policy or readiness members under an old,
  closed wire identity, or resolving contradictory cross-document rules.
- Size: 3; publication before consumer/producer activation, not runtime qualification.
- Evidence baseline: curator-spec `5509499`; curator `0d00a109`.

## Required output and acceptance

1. Allocate and publish the full successor **manager-config** and **status**
   carrier contracts, with closed schemas and positive/negative carrier vectors.
   The frozen `credential-store-config-v1` subtree and `login-row-v1` row are
   inputs, not validators for their enclosing documents. Existing config
   versions 1–3 and closed status contracts retain their prior meaning.
   Do not invent a carrier number in implementation ahead of this publication.
2. Coordinate with the Codex/v4 owner on a single delivery encoding. Published
   v4 has `credential_store.config_overrides`; CIP-0018 requires a successor
   `codex_settings` member and prohibits two policy owners. Do not widen v4 or
   emit two independently authoritative settings blocks. A successor allocation
   must settle the old-reader/consumer transition. Recommended coordinated
   allocation: retain `credential_store.selection` as agreement metadata,
   use `codex_settings` as the sole typed argv payload and forbid legacy
   `config_overrides` in that successor. Preserve existing v4 unchanged.
3. State the managed-Muse exception explicitly: configured absent/native/file
   resolves to effective **file**, without rewriting the configured selector.
   The generic native-preservation table is not a second Muse admission rule.
4. Reconcile these specific seams before freezing expected verdicts:
   - Muse explicit keychain: environments §7.4 names
     `environment_credential_unsupported`, while login-readiness §5 names
     `environment_credential_store_unsupported` for unsupported explicit maps.
   - Muse ambient backend: environments §10.2 makes the mandatory file literal
     override ambient backend state and refuses an incompatible explicit plan;
     login-readiness §2.1 generically refuses inherited backend conflicts.
     Keep credential-source conflicts separate from this backend-literal rule.
   - Status process boundary: login-readiness §1.1 prohibits invoking an agent
     executable; environments §7.9 still prescribes best-effort `--version`.
     Recommended amendment: adopting readiness status executes no agent binary;
     unknown detected version is honest. Any later diagnostic is explicit.
5. Preserve the exact CLI surface: `env login <env-id> [--profile <name>]` and
   `profile prepare <source-or-name> [--non-interactive]`. Preparation uses
   install's explicit source grammar and default naming, not implicit update or
   activation. Document native-store versus effective-store reporting separately.
6. Announce strict `status --check`/prepare aggregation, including participating
   OpenCode's currently unavoidable unknown row. This changes check semantics,
   not launch authorization. No credential bytes, digests or account identities
   become status fields.

## Negative tests and positive controls

| Forbidden outcome / negative vector | Positive control |
|---|---|
| New store member inserted into old manager-config accepted; login fields silently added to an old closed status shape | Existing old document remains accepted unchanged; complete allocated successor accepted |
| Standalone row/subtree validator accepts a malformed containing document | Full carrier validates both enclosing fields and the imported member contract |
| `codex_settings` appended to v4, or required policy silently dropped for an old consumer | Existing valid v4 and the separately published successor each validate under their own reader |
| Package/overlay/system lock selects store or account; nonempty package Codex setting admitted | Empty or absent package `codex_settings` is valid; machine selector is the sole store authority |
| Ambient backend and explicit operator override treated as the same source; error taxonomy varies by entrypoint | One published Muse decision table consumed by resolve, login and all launch paths |
| A status version-probe exception accidentally allows `auth status` | Full status has zero agent execution; a separate future diagnostic has no implicit call site |

The spec validator must detect a bounded known-invalid carrier/control plant;
report the intended failure rather than an unrelated parser/setup failure.
These checks prove grammar and published decisions only, not runtime safety.

## Dependencies, paths, release cut

No runtime prerequisite. Share one schema-allocation owner with the
manifest/lock/marker and launch-carrier work; serialize edits to
`protocol/environments.md`, `cli/curator.md`, schema indexes and conformance
indexes. Touch `protocol/login-readiness.md`, affected full schema files,
login conformance carriers, release notes and the coordinated Codex seam.

This is an **rc.7 prerequisite** for the affected emissions. Accepted CIPs do
not waive the explicit publication gates. It need not block internal reader
development or the already specified Muse v4 work where no seam is exercised.
