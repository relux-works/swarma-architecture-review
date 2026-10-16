# M6 — Preserve file backend with broker-key child delivery

- **Owner repository:** swarma-dispatcher.
- **Normative clauses:** CIP-0017 implementation leaf 7 and Design §4;
  environments §10.2 broker-key paragraph; D11; broker's own adoption gates.
- **Attack surface:** confusing local shared OAuth files with broker child keys.
- **Size:** S seam after the dispatcher/final-executor route exists.
- **Release cut:** follow-on, never an rc.7 local broker-support claim.

## Acceptance and paired tests

The minting owner retains its OAuth login. The approved final child receives
the minted key only through its separately admitted env/stdin source channel,
and receives the exact managed `TBH_CREDENTIAL_BACKEND=file` constant.
Dispatcher does not copy/link the owner's auth.json or put credential material
in a plan, snapshot, archive, receipt, log or generic env-literal map.
This leaf does not create broker custody/lifetime authority or bypass the
executor's credential-source conflict/qualification checks.

- Valid covered child policy plus a disposable admitted key channel preserves
  file backend and no owner-store link. Wrong/missing backend refuses before
  launch; ambient backend cannot replace the mandatory constant.
- Attempted linked/copied owner OAuth or secret in covered generic payload
  refuses with no child/no credential persistence. Nearby valid source-ref
  metadata relays without material and final injection stays at its owner.
- Missing/unsupported broker capability, source conflict or snapshot/policy
  identity mismatch refuses; a qualified exact route succeeds with unchanged
  nonsecret policy and the admitted secret channel only.
- Plant a backend-only omission or forbidden OAuth link in disposable fixtures;
  the destination test must detect the intended violation. A synthetic key
  proves transport/leakage checks, not subscription billing or token refresh.

## Dependencies and paths

Requires the separate broker/dispatcher/final-executor adoption and qualified
key channel, plus M3/M4 v4 consumers and the route's snapshot/archive contract.
The local Muse v4 producer/replay/pin chain does not wait for this dormant route.

Known contract path: `swarma-dispatcher/spec/dispatcher.md`, referenced from
the supplied broker source. No dispatcher implementation checkout was supplied;
its owner must pin actual admission/child-delivery/test paths before coding.
Receiver backend enforcement remains M4's curator-run path; broker secret
custody remains its own owner. Serialize covered-plan changes with C6 and
the archive relay owner. No runtime completion is asserted here.
