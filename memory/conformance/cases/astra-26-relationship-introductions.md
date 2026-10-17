# ASTRA26-05 — relationship status does not create introduction consent

Status: executable regression challenge, not an observed spec defect.
Seat: astra-26. Package: `0.1.0-draft` at `0ef608a`.

## Clauses and two readings

Kernel §§4 and 11.2 separate relationship status and openness to introductions,
with no derivation between them. Package `relationship_status` and
`open_to_introductions` declare `no_derived_consent`; K-SCOPE-1 grants no action
authority. The domain README permits storing enabled-without-adult-opt-in as
attributed data while forbidding a romantic introduction from that record alone.

1. Exact typed records govern each predicate independently; absence stays absent.
2. A convenient profile builder fills a missing openness field from relationship
   status, or converts a stored enabled flag directly into permission to contact.

## Minimal input and outputs

[Complete fixture](astra-26-relationship-introductions.vector.json): a synthetic
subject initially has only `relationship_status = partnered`. A private capture
queries `open_to_introductions`; it must return no items and `currentness=none`.
An empty response asserts neither openness nor a denial of openness.

Next, the issuer explicitly admits a reviewed self-declaration with:

```json
{"adult_opt_in": false, "enabled": true}
```

That valid data admission succeeds. A new-cut query now returns exactly those
two booleans, with self-declaration attribution and no evidence witness. External
effects remain exactly empty: neither the relationship record nor the explicit
flag sends an introduction or discloses contact details.

The positive admission means a blanket refusal of all introduction-related data
cannot pass. The earlier empty capture prevents default inference, including
inferred `enabled=false`; the postcondition prevents automatic external effects.
No real person, contact detail or sensitive corpus is used.

## Evidence and recommendation

Both domain documents exist but are absent from every supplied semantic vector
in `0.1.0-draft`. This case exercises their intended separation using the existing
closed grammar. Shape, canonical domain equality, references, normalization and
forbidden predicates pass the package checker functions.

The first astra-22 adapter at `0216fbb` explicitly reports **unsupported** because
the frozen core transaction mapping does not support `admit`. The full local
result is in seat `.temp/r7-astra-26/owned-cases-astra22-01.json`; unsupported is
not a pass. Recommend preserving the existing source/package distinction and
retaining this as an evaluator regression, without adding an introduction action
to the kernel.
