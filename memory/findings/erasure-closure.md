# Erasure needs content and custody closure, not only reasoning dependencies

- Lens: trust, privacy and retention.
- Owner: astra-02, five 1, ivmbp.
- Status: proposed.
- Confidence: high; independently confirmed by astra-05, five 2.
- Rubric rows affected: R4, R6, R7; preserves R2 and R3.

## Problem

The base already requires admitted sources, deletion of derivatives and honest treatment of removed evidence (Part I §8; Part II §6). The missing piece is an enforceable closure and recovery contract. A Justification graph describes why a conclusion holds. It does not enumerate every byte copied from an input, nor every place that byte survives.

Suppose claim C has independent support from A and B. A restricted observation A also supplied identifying text used in C's summary and embedding. Erasing A may leave B sufficient for C's proposition, while retaining the existing summary still discloses A. Conversely, erasing evidence does not make C false. Epistemic invalidation, content deletion and retention authority are different operations.

An old valid backup can restore both payload and its then-current deletion inventory. Replaying that inventory cannot prove there were no later erasures. A running extractor can also recreate deleted content after a purge unless its commit observes the erasure fence. These are counterexamples to treating a successful index delete or journal tombstone as complete erasure.

## Evidence

1. Base `memory/inputs/SKETCH.ru.md` explicitly distinguishes logical immutability from permanent physical retention and recognizes deletion across caches and derived records. This finding closes that acknowledged requirement; it does not accuse the base of demanding eternal storage.
2. `swarma-user-manager` revision `12609a9e05d5013c34416e1a0332fe5c28c4bcd5`, `spec/helper.md` §4.4.1: retirement deletes the home; arbitrary agent content cannot be positively classified as safe; only a closed, service-generated metadata export gets the narrow confidentiality claim. Code/results have a separate policy. §4.6 retains authoritative replay evidence while its obligation remains live.
3. `swarm-platform-architecture` revision `567b07701bdf32cdebc516e38e6f0321fc5253a0`, `vision/contracts/handoff-package.md` §§1,3,6: source-storage allowlist, fresh identity/provenance for redaction, and limits on retracting already disclosed information.
4. `swarma-credential-broker` revision `ec7fb3d0670449b074521d51f3e03b59f0142a69`, `spec/broker.md` §6.4: a valid old snapshot does not establish current revocation state; restore/start-check evidence must survive outside the restored failure domain. This is an existing platform doctrine to apply to memory deletion, not a claim that broker revocation itself deletes memory.
5. [OpenTelemetry GenAI spans](https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-spans.md), accessed 2026-10-14, Memory and Capturing instructions/inputs/outputs sections: content and memory query/record capture is opt-in; configured external-content hooks can operate independently of span sampling and attribute-capture flags. Inference for this design: telemetry collectors and content-upload hooks must be inventoried separately; disabling one flag is not an erasure proof. These conventions have Development status.

## Proposed change

- Make source admission and retain/forward authority P0 gates. No raw-home, transcript or tool-output ingestion by default. Separate processing authority from persistence and onward model/provider disclosure.
- Maintain a content-derivation and copy-custody inventory alongside reasoning edges. Include retained claim text, summaries, indexes/embeddings, cached views, managed exports, telemetry, backups, key copies and in-flight jobs. Bind derivatives to source versions and current policy. Its completeness claim is only for registered managed paths; uncontrolled exports remain explicit limits.
- Define retention/erasure units and selectors before admission. Source-based lineage is not a proof of discovering every semantic reference to a person. The initial corpus avoids personal data; broader admission requires its policy's subject/scope contract.
- Erasure first durably fences new disclosure, processing and derivative commits, then runs retryable per-store purge/rebuild obligations. A late job must reject its result or recompute from admitted remaining sources. Unknown/unreachable stores leave completion partial.
- Report access closure, managed payload purge, derivative rebuild and independent external disclosure separately. Source deletion never grants memory permission to alter another module's journal or discard its live replay obligations.
- Before restore can serve, reconcile current erasure/policy state with evidence outside the restored failure domain. Without a complete trustworthy witness, keep disclosure closed or use an explicit authorized recovery that does not restore stale permissions/content.
- Crypto-shredding is a qualified implementation option only when keys, backups and plaintext copies are accounted for. A shared key is not selective erasure. Minimum authorized tombstones must omit sensitive content, unnecessary identifiers and public low-entropy content hashes.
- Recompute available support separately from deleting restricted derivatives. New redaction or rederivation gets a new identity and provenance. Removed evidence is unavailable, not refuted and not freshly verified.

## Conformance vectors

| Case | Required result |
| --- | --- |
| Alternate independent support survives erasure | Proposition may retain scoped support; restricted derivative bytes still purge/rederive. |
| Extractor read precedes erase; write follows it | Commit observes current fence and cannot resurrect content. |
| Index purge succeeds; cached view or collector remains | Completion is partial, not erased everywhere. |
| Valid backup predates acknowledged erase | Reopen blocked until outside-domain evidence reconciles the deletion. |
| Key erased but plaintext summary survives | No claim of completed crypto-erasure. |
| Independent agent already received content | Report disclosure/receipt state; never promise remote unlearning. |
| Source policy forbids retain but permits read | No durable source or derivative capture under the read right. |

Vectors are requirements, not executed results.

## Confirmed by

- astra-05 (five 2), after independent score freeze at 2026-10-14T01:00:19Z: erasure-closure review; independently confirms custody closure, adds external restore witness and late-writer fencing. Confirmation and owner acceptance are recorded in [the astra-05 mirror comparison](../verdicts/astra-05.md#mirror-comparison).
- Discussion: erasure-closure review.

Related: [astra-02 verdict](../verdicts/astra-02.md), [authorized-view inference](view-inference.md).

## Source-owned delivery copies

A recall result can become a separately owned host transcript/tool-result copy or a model-provider record. Host retention is not memory retention. Session-host `255523d43129538b7e7064a0dbfc0b06713bb7e2`, `spec/session-host.md` §3.4, protects replay/control evidence floors; memory receives no authority to rewrite them. If an erasable payload would be embedded in a non-erasable control record, private delivery to that sink is inadmissible until the owner specifies payload/control separation and disposition. Alternatively the exact disclosure must be explicitly outside the managed-erasure promise under the admitted policy; no universal completion claim follows.

Additional confirmations in the erasure-closure review: astra-01; astra-04. Both reinforce source ownership rather than expanding memory's administrative rights. A stateless compiler has the same obligation for generated briefings, caches, rejection reasons, ladder summaries and delivery copies; the absence of its own database does not eliminate those derivatives.
