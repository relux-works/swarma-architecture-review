# M5 — Unblock task-board consumption with the qualified v4 pair

- **Owner repository:** skill-project-management.
- **Normative clauses:** CIP-0017 leaf 6; environments §10.2 managed Muse
  compatibility; §7.9 producer/consumer release gate.
- **Attack surface:** dependency upgrade and real spawn-policy propagation.
- **Size:** S; preserve existing consumer behavior outside the v4 seam.

## Acceptance and paired tests

Pin the actual qualified agents-management release and regenerate the existing
vendor tree after a compatible Curator release emits v4. The mission says the
pin currently waits for that release. Fresh supplied source `ab63db823` pins
v0.5.65; the originally named stale checkout is not the upgrade base. Record
actual source/tag/digest and Curator compatibility at implementation time.

Drive the real managed Muse spawn path with root/no-root v4 fixtures and both
admitted launch forms. Assert policy survives the task-board request and
builder. Wrong revision, malformed fact, dropped backend, required exclusion
on unsupported form/build, and contradictory explicit override refuse before
spawn. Valid neighboring cases succeed. A deliberately dropped fact in the
real request mapping must make the contract test fail.

The host must not duplicate Curator's home-layout inventory or create a
temporary path/header workaround. If this path relocates the XDG home, it
must use admitted materialization or stay refused; a pin bump alone does not
claim hosted snapshot/runtime qualification.

## Dependencies and paths

Release after M1/M2/M3 and the compatible launcher path where used. This small
pin leaf does not wait for unrelated setup-token or general Codex settings.
Conversely it does not close the separate hosted snapshot/config integration.

Paths: `tools/board-cli/go.mod`, `go.sum`, vendored agents-management;
real request composition under `tools/board-cli/internal/spawn/curator_fragment.go`,
`internal/spawnruntime/curator_fragment.go` and, where used,
`internal/sessionmanager/curator_identity.go`. Serialize shared vendor/host
edits with astra-04's hosted adapter owner. Verify the implementation base
because adjacent infra-exit changes are still landing.
