# Attributed mirrors do not prove their asserted source-ledger events

- **Owner / lens:** astra-06, five 2; semantics and formal core, crossing into source authority.
- **Status:** proposed.
- **Confidence:** high, based on exact code and two independent direct-read confirmations. This is a memory-ingestion requirement, not a claim that the board violates its documented guarantee.
- **Discussion:** mirror-origin review.

## Problem

The base correctly separates provenance from truth and proposes importing confirmed platform outcomes as observations. A generic "board event verified" classification is nevertheless too broad. Some board activity is an authoritative event for a board-owned transition; other activity is a **derived report** about a different owner's control-plane ledger. Authenticating the board record or its submitter establishes the report, not necessarily the reported event.

Concrete counterexample: a write-capable principal submits a remote `record_ledger_event` mirror describing a run, CR or workspace ledger event. The board-server sees the same principal and handler as for a legitimate runtime-relayed mirror. It preserves attribution and accepts the remote plane, while explicitly not proving runtime origin. A memory adapter that turns that row into "the ledger transition occurred" has invented assurance that its source does not provide.

This remains a problem when the copy's digest is verified, the view is signed, or an extractor is deterministic. Those checks authenticate a report's bytes, envelope or processing, not the asserted source transition.

## Primary evidence

Read-only local repository `skill-project-management`, commit `ad68902f74ae55b1cd0445fef58390b42feea3dc`:

1. `pkg/board/query/activity_ledger.go:53–85`, `authorizeLedgerMirror`: the `STATED BOUND` comment says the remote API cannot distinguish runtime-relayed and hand-composed mirrors. `ActivitySourceRemoteAPI` returns `nil`; local entrypoints have a separate gate. The comment explicitly limits the remote guarantee to attribution.
2. `docs/activity-mutation-coverage.md`, **Authoring authority**: source-ledger ownership and remote mirror limits are documented. Board-domain mutation activity and control-plane mirrors must not be treated as equivalent evidence classes.
3. The cited files were checked against `git show HEAD:<path>`; `git diff --stat HEAD -- <these paths>` was empty. No code was executed or modified.

Base evidence: `memory/inputs/SKETCH.ru.md` lines 95–97, 124–130, 191–203 and 529–547. It already supplies the correct general principle; the missing piece is a source-specific admission/assurance mapping, not a new authority architecture.

## Proposed change

For every adapter, define which exact propositions each source record can establish and with what native assurance. Keep at least these distinctions observable:

- An authenticated principal submitted content X.
- The board committed its own domain transition Y.
- Another owner committed the ledger transition Z reported by X.

The first proposition cannot be promoted to the third without resolving an exact authoritative source record or checking an attestation bound to that subject, revision and issuing authority. If resolution is unavailable, retain an attributed report with `origin_unchecked`/equivalent proposed vocabulary. Never silently treat it as a failed or nonexistent ledger event either.

Memory's proposal receipt and envelope signature must preserve these limits. A source binding to the mirror supports a `source_says` assertion; a world/domain assertion needs its own admitted support. This also applies to agent-written summaries, copied acceptance text and room messages.

No new board field, ledger API or cryptographic scheme is allocated by this finding. If canonical resolution is not available in a deployment, importing that stronger fact remains unavailable. The documentation-only pilot can use documentary assertions with honest limits.

## Conformance cases

| Input | Expected result | Forbidden result |
|---|---|---|
| Hand-composed remote mirror, authenticated submitter | Attributed report; purported ledger origin unchecked | Verified source transition from attribution alone |
| Same mirror, source resolver unavailable | Report retained at its original assurance; source gap explicit | Treat unavailable as nonexistent or verified |
| Exact authoritative ledger record resolves | Separately supported domain-event assertion with exact source binding | Transfer assurance to a different run/candidate/version |
| Memory signs or summarizes the mirror | Original provenance and assurance preserved | Signature or summary upgrades origin |

## Rubric impact

R2: preserve the actual domain owner. R6: distinguish a report from the proposition reported. R7: make adapter conformance falsifiable. R3 is a secondary protection if a consumer might use a falsely promoted completion/acceptance claim; memory still must not become acceptance authority. This finding does not independently force any base row to zero.

## Confirmed by

- **astra-03**, five 1, direct code read in the mirror-origin review. Confirms the remote API branch, attribution-only assurance and authoritative-resolution/exact-subject-attestation requirement; explicitly distinguishes this from a claimed board prevention guarantee.
- **astra-01**, five 1, independent code and documentation read in the mirror-origin review. Confirms `activity_ledger.go:53–85` and `docs/activity-mutation-coverage.md`, and requests astra-06 own this finding without duplication.

## Recommendation link

See [astra-06 verdict](../verdicts/astra-06.md), V15, and the source-authority table in [bounded evidence memory](../designs/bounded-evidence.md). The candidate already incorporates the remedy; the finding records why it is required.
