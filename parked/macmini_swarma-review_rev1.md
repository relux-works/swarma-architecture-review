# Parked: macmini_swarma-review_rev1

Date: 2026-10-12. Role: rev1, trust and threat model. Review basis: signed main `78c1bf43954944022a180ccb565936f6320f6ed5`, containing F-1 through F-11.

PARK was issued by `ivan-curator` at 2026-10-12T07:44:19Z in `#swarma-review`, topic `rounds`, decision `$EB6OzWXmhe2CPevdsra59AzLdOCV0XXzznaJEQfDJUk`. New analysis stopped on that decision. Resume only on the operator's word.

Read the complete sixteen-chapter Russian book first, then the relevant helper, dispatcher, broker, session-host, launcher, Curator CIP and trust/admission contracts. Sources were read-only; work produced review documentation and room messages.

Own confirmed entries in [FINDINGS.md](../FINDINGS.md):

- **F-3**, signed `415b66e`: requester-signed orchestrator delegation preserves ancestor revocation. Topics: `f-orchestrator-delegation`. Weak spot: requester participation, generation-bound registration/proof-of-possession and the pre-key exception still need a published bootstrap; existing depth/chain limits bound recursion. This is a constructibility/revocation counterexample, not a tested exploit or a new authority graph.
- **F-6**, signed `ee08f60`: one launcher descriptor lifecycle for trusted handles and bounded staging. Topics: `f-launch-descriptor-lifetime`, `f-launch-plan-staging`. Weak spot: literal close-all ordering may be shorthand in an eventual implementation; no implementation or kernel capacity was tested. The internal-handle lifetime and maximum-payload staging mechanism must be jointly published/qualified. Late rev3 confirmations: `$sMGCsByt7OrJHL3exdtKOLOhOc2qONx6clpr4eHAazg`, `$u_hNRRlaW87ufCbm7zZbvRKZ9pQuMhlxGPAXhHzgVxo`; rev5: `$L43xwTC-W-VkzAo3auM3rMkC94UVRWTHaiEKjgmTS5Q`, `$Lbb0WNj4FqAkyolYRIDjR3VG3O_zIAtvi7Hb9OA90g4`.
- **F-9**, signed `7221f05`: fence local broker restoration until acknowledged revocation history is recovered. Topic: `f-local-revocation-restore`. Weak spot: a declared fenced restore procedure is the initial recommendation; an undeclared whole-machine rollback cannot detect itself using an in-snapshot sequence. All-lost-history recovery requires unavailable authorization or explicit old-root invalidation/fresh reauthorization. Late rev3 confirmation: `$O0Kmr_lArWzwybCcGEEZmZFGAN1h2_X4RJpKaTMl8m8`. Preserve the distinct scope of F-8, the current-state view.

The original peer confirmations and source citations are in the entries; additional confirmations remain in their Matrix topics. F-3 also received rev5 confirmation `$6y0QLBKcZleFZ3Vvy241_v0Ng4vFC4mMD6maXrvTRNk`.

No own candidate or addressed request remains open. Independently confirmed peer findings on archive export, standing maintenance, single launch authority, daemon-first transport, remote replay floors, local revocation views and refresh-child ownership. Audited the signed F-10/F-11 landing: completed helper replay stays intact, and confirmed child absence does not authorize retry of an unknown external token rotation. All findings remain **proposed**, for operator disposition.

If resumed, start from the operator's dispositions rather than rereading or duplicating the eleven entries. Next useful checks:

- Publish and qualify F-3 bootstrap/delegation and revocation mutants; preserve standing identity/account separation.
- Qualify the actual F-6 descriptor success/failure lifetimes, maximum payload and launch/stop/retire races, including bounded privileged cleanup.
- Select F-8 current-state evidence and F-9 fenced recovery together; prove witness failure-domain and acknowledgement ordering, or use explicit authorization-root replacement.
- Revisit egress/proxy/firewall and agent-side runner assurance only against concrete platform qualification/evidence. These were not exhaustively reviewed here; no additional high-confidence finding is claimed.

Keep the accepted limits: root is trusted, and a harness may read/copy an already leased token; local revocation cannot erase it. Caller keys, software authorization roots and keeper identities are distinct phases. Explicitly unpublished gates and older superseded VISION wording are not fresh discoveries.
