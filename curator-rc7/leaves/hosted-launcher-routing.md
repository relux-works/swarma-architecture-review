# H-LAUNCHER — Local hosted preparation and exact handoff

Owner repository: **curator-agent-launcher**. Size: **5**.

Normative clauses: hosted §§2/3/4/6/7; CIP-0016 leaf 7. Attack surface: selecting/transporting a hosted route silently changing execution or authority.

Acceptance: preserve host precedence/locks, repeated-selector errors and legacy ax conflict. Native selection contacts zero receivers. Explicit --hosted with absent backend selects local-task-board with stable future meaning; backend choice alone does not enable hosting. Unimplemented dispatcher selection refuses. Existing operator defaults require explicit local migration; machine hosted defaults remain gated on upgrade-without-hangup. ax conflict precedes defaults gate.

Run knowable terminal/piped-stdin/network refusals before preparation/contact; attached payload stdin refuses after composition before handoff. Use authoritative-board private receiver client and authenticated control transport, never repository socket/binary discovery. Request preparation, call Curator materialize/runtime preparation in its reserved permitted home, call H-FORMS, compose complete environment and seal once. The receiver client transports/attaches but never recomposes. Fresh restart secrets follow the published caller-side policy; no daemon secret lookup or unsupported node-mode injection.

Tests/control pairs through production `curator-run`: native success with receiver-contact spy zero; explicit hosted valid successor reaches handoff. Missing/unreachable receiver, wrong runtime/capability/version, dispatcher unavailable and failed materialize return exact refusal with zero native fallback. Terminal/stdin/network failures leave no reservation; cancellation after preparation cleans only owned resources. Decode real private plan stdin/fd3/fd4; grandchildren must not inherit control descriptors. Valid framed status works; complete malformed remains poisoned after later truncation, clean truncation is unavailable, bare child exit supplies no typed status. Exact final env is compared under a poisoned parent/receiver environment, including removed as well as changed fields.

Dependencies/paths: H-WIRE, H-PREP/H-ADMIT, HOST-HOME-CODE, H-FORMS plus route-qualified receiver capabilities. `cmd/curator-run/main.go`, CLI/config selection, `internal/hosted/{payload,transport,status,resume}.go`, composition/fragment/plan bindings and registry. Serialize after v4/settings/source changes; dormant integration may land before all runtime proofs, but production capability stays gated by H-RELEASE.
