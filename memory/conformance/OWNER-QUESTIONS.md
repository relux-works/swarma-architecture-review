# R7 owner questions

Sole writer: astra-27 (judge). Linked ledger: [LEDGER.md](LEDGER.md).
Status: one unresolved owner question, established in round 30.

## R7-055 — does canonical receipt order cross deciding issuers?

Status: **owner-needed**. Decision owner: Ivan. No decision recorded.
This question does not reopen D-001–D-008 or the verified same-issuer fixes.

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
outside conformance denominators. Other correction and coverage work continues.

Independent bounded source readings are room events
`$YNf8wCxcmJu1oe0g_LiaYDwSu9lMdip9uJBEw1xD-6A` (editor) and
`$89Vv7j9FUXKndbTqR13jqHRMVccAO1Byx5MHH1ygOyg` (attribution adversary).
Judge evidence: `.temp/astra{22,23}-judge-round30-issuer-first.json` and
`.temp/judge-round30-issuer-analysis.md` in the astra-27 seat.

Owner topic: `q-authority-issuer`, root
`$xI3um-5-5mtAfRLub6enUIlkEPrUbVS41wk0hCp6-4Y`;
owner-needed routing event `$Ju7IuqWDcWw6JB87jbG-0K3yC4TWQ2WszJTNwNLZQHs`.
