# C6 — Relay covered Codex settings unchanged across dispatch

- **Owner repository:** swarma-dispatcher.
- **Normative clauses:** profile-codex-settings §§3,6–7; CIP-0018 leaf 6;
  environments §10.2; D6; separate archive/executor activation contracts.
- **Attack surface:** dropping, rewriting or substituting required policy
  between covered caller intent and destination execution.
- **Size:** S for the settings seam once the dispatcher route exists.
- **Release cut:** follow-on route, disabled until its own publication and
  implementation gates pass. It is not part of Curator snapshot bootstrap.

## Acceptance

The caller's published plan covers the exact typed settings plus accepted
fragment and snapshot identity. Dispatcher verifies the covered request and
relays the admitted payload unchanged. It never resolves profiles, inspects
Curator homes, selects a backend or reconstructs settings from an archive.
Destination `curator-run` validates and consumes the same payload before
execution. The snapshot descriptor/archive alone cannot carry this authority.

Unknown carrier/version, missing required settings, selection disagreement,
digest mismatch and unsupported destination capability refuse before child
start. No downgrade or local/native fallback. Direct or local-hosted support
does not establish cross-account delivery, authentication or broker support.

## Paired negative tests and controls

- Canonical covered request reaches the destination with unchanged typed
  settings and effective override. Change one value or remove the member
  without recomputing authority: refuse before child start.
- A correctly signed but semantically contradictory selection/payload or
  unsupported destination tuple refuses; adjacent valid native/explicit-file
  requests follow their admitted route.
- Changing snapshot identity while retaining settings, or settings while
  retaining snapshot identity, cannot reuse a previous admission.
- A relay stub that drops only the optional-looking settings member is a
  bounded control plant; the end-to-end receiver test must fail for the
  intended missing-required-policy reason, not a transport timeout.
- Dispatcher has no home access and cannot substitute a re-resolved local
  profile. Positive relay needs only covered transport data and destination
  capability, not source home paths.

Observe no privileged start/child effect on refusal; retain permitted refusal
telemetry. Use synthetic payloads and disposable execution fixtures only.

## Dependencies and path-evidence limit

Depends on the separately published dispatcher/archive/final-exec contracts,
C2/C3 supported consumer and the matching destination qualification. Full
archive/runtime-B/broker implementation is outside this bounded settings seam.
Until that route ships, advertise it unavailable rather than making C6 a
fictitiously green prerequisite for local-only capability.

The supplied sources do not include a dispatcher implementation checkout.
`swarma-credential-broker/spec/broker.md` references its contract at
`swarma-dispatcher/spec/dispatcher.md`; that is the known contract path, not
evidence its runtime exists. Before implementation, the owning dispatcher
task must pin its actual source and name the exact admission/relay/test paths.
No invented source-file path or completed-code claim is part of this plan.
Serialize the contract path and covered-plan schema inventory with the
separate archive owner; C3 owns the receiver changes in curator-agent-launcher.
