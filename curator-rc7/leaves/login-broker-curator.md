# L15-6a — Route broker-source observation and operator enrollment

- Owner repository: **curator**.
- Normative clauses: CIP-0015 implementation leaf 8, Design §5;
  login-readiness §§1.1, 2–4, 7; CIP-0011 authority boundary; broker spec
  §§3.1, 5.4, 13.2, 14 and publication gate §18.15 at `ec7fb3d`.
- Attack surface: source-readiness or login routing granting operator or
  secret access to an ordinary caller.
- Size: 2. Broker-source follow-on; neither the base rc.7 tag nor the local
  T0–T4 setup-token slice depends on it.

## Acceptance and publication dependency

Implement only after broker source adoption and its operator/observer entry
contracts are published and qualified. Broker §18.15 leaves their exact
entrypoint/wire/admission mechanisms open; this leaf allocates none. Curator
uses those boundaries, never direct owner-UID impersonation, an ambient sudo
fallback, a guessed CLI wrapper or new broker fields. The missing contract is
an explicit activation blocker, not permission to build an alternate channel.

Resolve the selected broker source before home-store/isolation decisions;
non-native home-store overrides remain inapplicable. Use only the adopted
bounded nonprompting local metadata observation to derive the frozen row:
source broker, caller scope, established external backend or unknown. Filter
broker-wide metadata to the admitted row; no account identity, grant, binding,
source reference or lease material enters status. Qualified observable source
presence does not promise the next lease. Unreachable, unauthorized, partial
or unqualified observation stays unknown; do not infer absent from refusal.

Full status/prepare performs no enrollment, lease/renewal, network probe,
secret access, prompt or home fallback. If the required metadata cannot be
obtained within that boundary, return unknown. `env login` under broker source
may route only an explicitly admitted human operator ceremony; an agent or
unauthorized caller refuses with operator guidance before any mutation or
material access. Reuse broker-owned enrollment/custody and the published
`curator broker` provider surface; never run vendor login inside an agent
home, collect tokens through the home-login wrapper or record its transcript.
Report-only/headless prepare provides guidance without starting that ceremony.

## Paired tests and controls

- Qualified metadata-only source observation produces the exact sanitized
  row; timeout, denied/partial read or missing observer publication gives
  unknown with zero lease/renew/enroll/provider calls. A planted timeout to
  local-login fallback must fail the full production-entry test.
- Explicit authenticated, content-confirmed human ceremony enters the
  broker's existing approved path. Agent-session, observer or unauthorized
  caller cannot enter it even with a claimed operator UID or valid profile.
  Assert no mutation, authority widening or material delivery on refusal.
- Broker source plus native store retains source policy; file/keychain or
  competing inherited credentials refuses without changing home/source state.
- Sanitized success/error reports preserve uncertainty; synthetic credential
  or account-identity fields in the broker reply never leak through the closed
  readiness row. Valid safe fields remain observable, preventing blanket
  refusal from passing. No fixture claims real operator/observer qualification.

## Dependencies and paths

L15-0/1/2/3/4 plus separately published broker/source/operator/observer
contracts; [L15-6b](login-broker-dispatcher.md) owns dispatcher integration.
No existing broker-source implementation was established in curator
`0d00a109`; proposed paths are the source adapter in `internal/envprofile`,
status/login/prepare routing and the adopted broker provider frontend. Pin
actual provider API paths when that upstream surface exists. Serialize shared
status/source/CLI paths with T2 and L15-2/3; broker custody/leases remain owned
by swarma-credential-broker, outside this integration leaf.
