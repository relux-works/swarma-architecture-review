# CIP-0015 follow-on coverage is not the local login implementation

Reviewer: astra-03, round 4, 2026-10-16. Source: curator-spec `5509499`,
`cips/CIP-0015-login-readiness-and-profile-preparation.md` implementation
leaves 7–8; `protocol/login-readiness.md` §§1.1,3.
Plan reviewed: `6186899`, with seat leaves through `75dc718`.

**Confirmed traceability gap in that synthesis, not an rc.7 broker blocker.**
The plan maps all of CIP-0015 to L15-0..4/C4/T2. Those leaves own local
publication, source/store policy, metadata, login and prepare. They do not
name the two further implementation owners in CIP-0015:

1. Leaf 7: skill-project-management preparation guidance and sanitized
   present/absent/unknown display, retaining source and caller-session scope.
   M5 only owns the Muse module/pin path; D4-S owns snapshot lifecycle. Neither
   declares this readiness/guidance consumer or its required no-inspection
   and no-automatic-login tests.
2. Leaf 8: Curator plus dispatcher broker-source enrollment routing and
   lease-source metadata readiness through existing authority. L15-2 correctly
   refuses to acquire leases and L15-3 gives external-source guidance, but
   neither supplies a separately adopted authorized broker ceremony bridge.
   M6 owns Muse key/backend delivery, not enrollment/readiness authority.

These can remain explicit bounded follow-ons after the base release and the
broker's independent adoption. The correction must not enable a broker route,
read credentials, introduce new broker wire or make local rc.7 wait for broker
implementation. If the implementation plan intentionally excludes them,
state that exact exclusion and preserve accountable follow-on ownership rather
than claiming the whole CIP is covered by local leaves.

## Required acceptance bounds for the eventual owners

- Guidance/display consumes the published status contract with no home or
  credential inspection. Current+present and valid guidance are positive
  controls; unknown/absent, incomplete rows, stale revision and non-caller
  scope must not become present or trigger automatic login, prepare or source
  mutation. Sanitized outcomes preserve source/session meaning.
- Authorized operator enrollment dispatches only through the separately
  adopted broker authority; unauthorized agent/unavailable capability refuses
  without local login or widened authority. Readiness performs no enrollment,
  lease acquisition or secret retrieval. Unreachable/denied metadata remains
  unknown beside an admitted metadata-only positive control.
- Separate repository changes and real production entry tests; pin actual
  dispatcher implementation paths at owner intake because no checkout was
  supplied. A synthetic relay test is not broker authorization qualification.

No new operator decision is required to preserve this accounting. Existing
source/custody choices and all broker adoption gates remain unchanged.

## Resolution

Accepted astra-02's signed `82b669b`: [L15-5](../leaves/login-consumer-guidance.md),
[L15-6a](../leaves/login-broker-curator.md) and
[L15-6b](../leaves/login-broker-dispatcher.md). Their concrete contracts retain
the paired controls above, separate repository owners and broker §18.15's
operator/observer publication gate. They invent no wire or broker authority.

PLAN `32cf0f2` maps all three in its canonical table, follow-on release cut,
shared-path serialization and exact CIP-0015 implementation coverage. The
finding is closed at the planning level. This neither implements those leaves
nor qualifies a broker path. Base rc.7 and local T0–T4 retain independent cuts.
