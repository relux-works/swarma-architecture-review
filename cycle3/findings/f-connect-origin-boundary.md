# Distinguish CONNECT authority confinement from provider-only application origins

- **Lens:** adversarial network review; trust and assurance; N15/N16.
- **Problem:** N15 describes trusted-agent egress as model-provider endpoints only and says a client-side fetch reaches nothing because only those endpoints are listed. N16 likewise says an opaque registry tunnel guarantees which hosts are reached. The specified mechanism verifies the CONNECT authority and the resolved peer address, then relays opaque bytes without TLS interception. It does not bind the inner TLS or application origin. The named candidate implementation, RWP v2.1, explicitly excludes domain fronting through a shared frontend from its guarantee; the adopting network contract omits that limitation. The existing warning that allowed destinations can carry data does not describe the distinct possibility of another application origin behind the allowed destination. This is a specification and qualification gap, not evidence that any currently qualified provider/CDN tuple permits fronting.
- **Evidence:**
  - `curator-network-profiles-dev` at `359365e03cda729408aa8f9f2a05ae93ac481463`, `spec/network-profiles.md`:
    - N15 item 11, line 211: agent profiles admit CONNECT only, without TLS interception.
    - N15 item 12, lines 213 and 224: provider-only endpoints and the absolute client-side-fetch claim.
    - N16 item 3, line 242: the opaque registry tunnel's stated host guarantee.
    - N16 item 6, lines 245–249: RWP v2.1 egress is the candidate implementation, including its dial guard.
  - `worker-jail` at `0635a513b783c59a69215373740470bffc9a44b7`, `docs/protocol.md`:
    - Section 5, line 134: generic modes explicitly do not contain domain fronting to another site behind an allowed CDN host; tunnel methods, paths and headers are outside enforcement.
    - Section 7, line 190: after authority checks and guarded dial, CONNECT splices bytes and cannot inspect the tunnel content.
  - `swarm-platform-architecture` at `6b3f9831f9c928cd316e2d1886a0e1c89465af20`, `vision/contracts/trust-and-isolation.md`, lines 47, 49 and 82: the service-egress rationale recognizes shared frontends, while the trusted-agent rows still state provider-only endpoints.
- **Proposed change:**
  1. State the achieved boundary precisely: admitted CONNECT authority, checked address and port, dial guard and caps. Do not infer application-origin confinement from that evidence.
  2. Carry RWP's domain-fronting and allowed-destination residuals into N15/N16 and the corresponding trust-contract and book claims. Replace the absolute client-side-fetch statement with the narrower authority-based refusal guarantee.
  3. Before making a stronger provider-only application-origin claim, require explicit evidence and assumptions for the qualified tuple, including alternate TLS/application routing on shared frontends and the effect of provider topology changes. A successful ordinary provider call is insufficient evidence.
  4. Preserve the no-interception decision. If a stronger boundary against a compromised client is required, leave it gated on a separately reviewed enforcement design and any necessary owner decision; do not silently add interception or claim a launch flag closes this gap.
- **Expected benefit:** Admission and threat assessments can distinguish the network boundary actually enforced from application behavior it does not observe. Reuse of RWP preserves its published limitations as well as its mechanisms.
- **Risks and costs:** Documentation and qualification work; stronger assurances may remain unavailable for some tuples. No live provider exploit is asserted and no test was run in this docs-only cycle. This finding does not challenge the owner's no-interception decision or choose a new proxy architecture.
- **Affected specs:** network profiles N15/N16 and their qualification/served-policy contracts; platform trust and isolation contract; user-manager references to provider-only egress; book chapters 3 and 11 where equivalent claims appear.
- **Confirmed-by:** `ivmbp_swarma-review-3_astra-18` (trust lens), answer `$E0al5ETZpEDC80fyMYqledO6jogj5X9LZzc7M870huY`, independently confirms the assurance/qualification gap and the narrower repair. Room `#swarma-review-3`, topic `f-connect-origin-boundary`, 2026-10-13. Proposal `$4LsVeEoMUdkTACGt1nMJiRl6_nUHKXQ-pqVtb8NbQIU`; confirmation request `$nbtsquE9jtbhWEd1rErAGpqit2BN5_DQH8BeHOwZQvc`.
- **Status:** proposed.
