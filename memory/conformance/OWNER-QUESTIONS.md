# R7 owner questions

Sole writer: astra-27 (judge). Linked ledger: [LEDGER.md](LEDGER.md).
Current status: no owner decision is outstanding. D-009 is received; R7-055 conformance closure awaits 0.2.6 dual verification.

## R7-055 — does canonical receipt order cross deciding issuers?

Status: **decision received; conformance verification pending**.
Decision owner: Ivan; approved 2026-10-17, recorded as [D-009](../DECISIONS.md)
and [kernel v0.3 §5.3](../designs/kernel.md) at `2c3100d`.

D-009 selects issuer-local order: keep only predecessor edges between events
whose protected policy authority-event issuer is H, then take nonempty
transitive closure. Assertion-free intermediate events count. One all-H path
suffices; no contraction over foreign events is permitted, and foreign branches
cannot cancel an all-H path. The same relation governs currentness and strict
replacement succession. Mixed graphs remain admissible; absence of order gives
ambiguous currentness and existing write refusals, with no new error code.
Changes confined to foreign graph parts cannot change H's order.

The original mixed-chain witness therefore requires ambiguous d1/d3; its all-H1
control requires current d3. Closure will be recorded only after the 0.2.6 exact
vectors and both evaluators pass independent verification. The original input
and first outputs remain unchanged. Package `77b951e` and its nine new vectors
are independently verified; source first is 66/66, while package first `1be6026`
has the preserved S34/S39 failures. Package alignment and dual verification
remain pending. Reopening event:
`$7qVXDb4qnZcORPIQr_qJeUzKFAj9Md3ZRI_VLpdOSKk`.

### Historical question and evidence at the first PARK

The text below records the unresolved choice at the 2026-10-17 06:33Z PARK.
Its requests and hold were superseded by D-009; they are retained as history.
This question did not reopen D-001–D-008 or the verified same-issuer fixes.

Evidence: [ASTRA24-12](cases/astra-24-authority-issuer.md), original native
[input](cases/astra-24-authority-issuer.input.json) and
[first outputs](cases/astra-24-authority-issuer.first.json) at signed `4424598`.
Input SHA-256: `8224829a810a97c79fef81cb18f0d650b59ffc84a3262bdef09b1ea900c521b3`.
Judge independently reproduced both validated states and complete outputs;
durable records, runtime and policy remain unchanged.

Two H1 decisions cite endpoint receipts r1 and r3. The declared canonical graph
is r1 ← r2 ← r3, with no assertion at r2. Changing only the middle event/source
attribution from H1 to H2 separates the readers:

| Input or interpretation | Required/observed view |
| --- | --- |
| All three events belong to H1 | Both readers select current d3; d1 historical |
| H2 middle, issuer-local paths | Source selects ambiguous d1/d3; no history |
| H2 middle, global canonical paths | Package selects current d3; d1 historical |

Kernel §5.3 requires the deciding authority's own ordered record. Kernel §5.1
and D-008 preserve issuer-specific revision authority; D-004 requires the deciding
authority's receipt. None defines what a predecessor edge to another issuer
attests. The package's A07 chose a predecessor-DAG encoding, while K-REV-3 leaves
intermediate issuer scope implicit. H1's r3 may endorse H2's ordering claim, or
may cite a foreign causal reference that supplies no H1 order. Both candidate
decisions remain H1; the foreign-write prohibition alone does not decide this.

**Decision needed:** for H1 currentness and strict replacement succession, must
every event on the qualifying canonical predecessor path have H1 as its policy
authority-event issuer, or does an explicit H1 edge adopt a foreign canonical
predecessor's transitive ordering?

- **Issuer-local paths — recommended:** foreign events remain valid data but do
  not establish H1 order. The separating input is ambiguous. An all-H1 direct or
  transitive bypass still orders the endpoints with the foreign branch present.
  This avoids implicit cross-authority ordering; an H1 order must be stated in
  H1's own subgraph.
- **Global canonical endorsement:** an H1 edge may incorporate the foreign
  predecessor's ordering. The separating input is current d3. This supports a
  shared or cross-authority register, but the endorsement meaning and scope must
  be explicit for both projections and write admission.

Rejecting every mixed-issuer edge as invalid state is a separate integrity
choice, not a consequence of selecting issuer-local paths. If that is intended,
the owner must also settle the admitted-state constraint and operation refusal
mapping. The current package accepts both inputs; no new rejection is assumed.

Use the protected policy authority-event issuer for this decision, not the source
carrier, submitter, catalog or representation identity. No exact vector oracle,
new transfer/delegation mechanism, package change or evaluator bug is authorized
until an attributed owner decision resolves the question. The native pair stays
outside conformance denominators. All classified implementation/specification
corrections and semantic vector coverage are complete at PARK.

Independent bounded source readings are room events
`$YNf8wCxcmJu1oe0g_LiaYDwSu9lMdip9uJBEw1xD-6A` (editor) and
`$89Vv7j9FUXKndbTqR13jqHRMVccAO1Byx5MHH1ygOyg` (attribution adversary).
Judge evidence: `.temp/astra{22,23}-judge-round30-issuer-first.json` and
`.temp/judge-round30-issuer-analysis.md` in the astra-27 seat.

Owner topic: `q-authority-issuer`, root
`$xI3um-5-5mtAfRLub6enUIlkEPrUbVS41wk0hCp6-4Y`;
owner-needed routing event `$Ju7IuqWDcWw6JB87jbG-0K3yC4TWQ2WszJTNwNLZQHs`.

Round 31: convener event `$wrLtxOryOvNuOttDN4ofHbvs0INg6jS0hLEpgMJ58wk`
holds the question for Ivan while he is asleep. This is routing/hold evidence,
not an owner decision. Both readings and the undetermined oracle remain intact.

PARK event `$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg` explicitly retains
this hold for Ivan with no oracle. Parking does not resolve or withdraw the
question. An attributed owner decision is the required input for any later
mapping and corresponding positive/negative regression work.
