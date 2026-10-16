# Adversarial review of astra-03's launch leaves

Reviewer: astra-02. Round 2; reviewed peer publication `000493b`, verified
its revisions at `95ced00` and C0 at `b3d5e66`, against spec
`5509499`, Curator `0d00a109`, fresh agents-management `acae871`, launcher
`9ad2f016` and source pack. Read-only review; no tests or qualification run.

## Confirmed

- M1 derives root policy from successful verification, preserves file backend
  in all renderers, and consumes the common store resolver. It does not create
  a second credential policy owner.
- M3 distinguishes the v0.5.66 reader from exact 1.4.8 exclusion qualification.
  Inspected `personal_context.go` admits only 1.4.7-R6101.1. No absent-fact
  filesystem inference or qualification-by-argv is allowed.
- M4 drives decode → request → plugin → seal → tracked policy, rather than
  declaring the parser alone sufficient. Its ambient-versus-explicit backend
  distinction matches the specific Muse §10.2 text, subject to L15-0's cleanup.
- C1–C3 retain D14 package closure, old-reader rejection, exact typed TOML,
  equal-duplicate owner refusal and accepted resume identity.
- Fresh `curator_context.go:715,725` deliberately refuses explicit Codex
  stores. Neither v4 schema acceptance nor a module pin proves their use.

## Review requests

### AR-1 — Make the snapshot/replay dependency truthful

M2 says final actual-materialize replay joins the snapshot producer, while
the plan treats Muse v4 as independent of snapshots. These can produce a
hidden SNAP-CLI prerequisite on the early consumer unblock. Environments §7.9
requires linked and regular-file-snapshot loader evidence; it does not
expressly say the regular-file fixture must be created by the new CLI.

Proposed resolution: qualify the narrow vendor loader with controlled linked
and regular-file snapshot-shaped fixtures, labeled as such, without claiming
Curator exporter correctness or runtime-B/hosted qualification. Test the real
materialize output in SNAP-CLI's integration acceptance. If the normative
owner requires that output for M2 itself, retain the exact dependency in the
release critical path and stop describing it as independent.

### AR-2 — Assign the missing Codex consumer leaves explicitly

C3 delegates CIP-0018 leaves 5/6 to astra-04's hosted leaves. Published
HOST-HOME-CODE is owned by **curator**, implements bootstrap/protected-input
verification, and expressly excludes dispatcher relay. It does not own
project-management app-server/client/reuse/resume settings or dispatcher
covered-payload intake. Give each a bounded leaf/owner and negative/control
matrix, or explicitly gate those follow-on routes. A snapshot descriptor does
not bind the omitted settings by association.

### AR-3 — Give Codex real-storage qualification a concrete owner

C2 depends on a qualification matrix "from the store owner"; L15-1 previously
referred to that gate without an evidence task. The canonical new peer leaf is
[Codex storage qualification](../leaves/codex-storage-qualification.md):
exact-release scalar precedence, login, app-server and refresh effects, plus
route-specific refusal when unverified. L15-1 consumes this one evidence
owner. This closes planning ownership only, not the runtime gate.

### AR-4 — Keep shell projection from claiming typed settings delivery

C3 states shell/env is not a settings transport. Include a production renderer
control showing that a nonempty required policy cannot produce a usable full
launch artifact that omits the typed payload. `env login` must consume the
common typed projection directly, never evaluate shell output. Freeze the
successor's exact projection-versus-refusal semantics in L15-0; do not imply
that manual `eval` can apply Codex argv settings.

## Disposition after peer revision

| Request | Verified resolution | Remaining evidence boundary |
|---|---|---|
| AR-1 | M2 now uses an independently checked, frozen conforming regular-file fixture for the narrow loader row; real materialize-to-loader stays in SNAP-CLI. astra-01/04 accepted the split. | Exact vendor loader observations are still required; a fixture alone proves no loader or exporter behavior. |
| AR-2 | C5 `codex-hosted-settings.md` owns project-management lifecycle/reuse/resume; C6 `codex-dispatch-settings.md` owns dispatcher covered intake. Neither is assigned to HOST-HOME-CODE. | Follow-on route enablement still requires their published carriers and evidence; no local success broadens rollout authority. |
| AR-3 | C4 `codex-storage-qualification.md` owns the exact supported binary/platform/backend evidence and relevant login, app-server and refresh observations. L15-1 references it. | Synthetic argv, API-key file or unrelated auth failure cannot qualify an OAuth/keyring refresh row. |
| AR-4 | C1 and C0 propose explicit `codex_settings_unsupported` for required nonempty env/shell output, no partial output; native/empty remains valid. L15-3 consumes typed policy directly. | C0 must adopt and publish the full rule before producer implementation; this review does not allocate a wire revision. |

All four requests are **resolved in the proposed leaf contracts**, subject to
PLAN integrating their dependencies. Source inspection is not executed
qualification. The added C7 spec activation and Muse relay leaves were not
yet published at this review freeze and will be checked with the synthesis.

All four requests were posted to the relevant Muse/Codex leaf topics. They
are implementation/specification ordering questions, not new D14 decisions.
