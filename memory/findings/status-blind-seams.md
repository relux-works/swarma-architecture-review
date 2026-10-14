# Finding: base integrates against spec-stage seams as if they existed

- Lens: rubric and proof (wonder-04). Status: `proposed`.

## Problem

The base's platform claims are accurate in substance (see the mechanical checks), but several
load-bearing seams it integrates against are specification-stage, proposed or unpublished, while
the text leans on them as available platform surface:

- Handoff package and the SH2+ session-host service: spec draft r13 ("no implementation claimed");
  today sessions live in `tb-sessiond` inside the board. The goal-client interface on the host
  socket is unpublished (Swarma book ch. 08, marked open).
- The attestation quadruple (contract version, candidate, policy version, environment) belongs to
  the distributed-protocol layer, whose status is "designed", not implemented.
- Exchange reputation receipts: marked open ("idea for the future").
- Post-deprovision metadata export: schema unpublished and export disabled until published.
- "One writer per store" itself is marked proposed in the book (its input-writer instance is
  decided).
- Status must cite the governing source, not the retelling: e.g. CIP-0002 is marked decided in the
  book but remains Draft/unaccepted in curator-spec (wonder-02, C-8 nuance).

What works today is narrower: the board with `tb-sessiond`, Curator profiles and managed homes,
the model router, network profiles, and Matrix/a2a communication. An MVP that assumes SH2+ seams
builds on a gate that has not passed.

## Evidence

- `verdicts/wonder-04.md` §1 rows C4, C5, C8, C12 and §2 F-b/F-f, with file:line citations to book
  v0.12 and `swarma-session-host/spec/session-host.md`.
- Independent corroboration: wonder-02 C-19/C-6 (same defect, narrower framing).

## Proposed change

Every seam named in the memory RFC carries its governing-source status (works today /
specification / proposed / open / unpublished). The first slice lands only on working seams
(board + git documents + Curator + router + Matrix/a2a) and degrades explicitly — named fallback,
not silent assumption — wherever a format is unpublished.

## Rubric rows affected

R2 (reuse of what exists vs what is promised), R7 (unpublished formats cannot carry conformance),
R8 (slice value must not wait for platform gates).

## Confirmed by

- wonder-02 (five 1), event `$PaySnRZ-cqP2nyHiJztUHVRz4PM15875QGopINjRHts` in topic
  `f-status-blind-seams`.
