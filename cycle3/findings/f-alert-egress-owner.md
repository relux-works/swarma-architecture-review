# The watcher's operator alert has no published owner, route or availability: "over the phone path" names an inbound channel

- **Lens:** trust and threat model (fable); abuse-control (astra-19), network (astra-06) and session-host (astra-04) cross-checks.
- **Status:** proposed.

## Problem

Every wave-5 text makes operator alerting part of the abuse controls. The watcher "alerts the operator over the phone path" (dispatcher), "Alerts reach the operator over the phone path" (user manager), "Alerts use the operator phone path" (session host); the book says the operator gets a notification when the watcher narrows an account. But the phone path as published is the operator's act channel: the phone app connects by SSH over the tailnet into `swarma-operator` and signs acts; no text publishes an alert relay or subscription on it. And the services that detect the conditions have no general outbound route: the dispatcher's and the session host's egress rows are deny-all including loopback and DNS, and the broker reaches only its vendor listener. The dispatcher marks the phone-alert format unpublished, but no spec assigns the alert's owner, route, delivery semantics or behaviour when the channel is unavailable, nor says in which version the lane exists.

**Scope, as narrowed by the cross-checks.** This is a publication gap in the R-WATCH alert lane, not proof that alerts are lost. The broker's events already have a named direction for later versions (the session host and the message bridge, so that a person can re-enrol from the phone), and the trust contract gives the bridge a later carrier path; an inbound-initiated SSH or read channel can carry authenticated responses, so network direction alone does not prove silence and no new egress row for the watcher is implied. What is missing is the joint piece: which principal owns the alert, over which route (the bridge over the carrier, or a protected event source that an authorised client polls or subscribes to), with what bounded durable delivery and status, what happens when the channel is unavailable, and from which version. Until that is published, a watcher hard-threshold crossing is journaled and the stop is confirmed, and the operator learns of it when someone reads status through `swarma-observer`. For controls whose purpose is to summon the operator, a version that is status-only must say so rather than promise a phone notification.

## Evidence

- `swarma-dispatcher` at `74687e60` (v0.11), `spec/dispatcher.md:472` (§7.3): "It alerts the operator over the phone path"; `:112-114` (§3.2): the phone path is the inbound act channel; `:626` (§13): deny-all egress including loopback TCP and DNS; `:737` (§16 q27): phone-alert format unpublished.
- `swarma-user-manager` at `7b59da7` (v0.10, UM7), `spec/helper.md:510` (§8.2): "Alerts reach the operator over the phone path"; `:490-502` (§8.1): dispatcher and session host deny-all, broker vendor-only; the root helper and launcher have no per-UID row, so the table is not a blanket root deny-all claim. The same text was at `ae540c59:498, :480-486`.
- `swarma-session-host` at `798a321c` (r11), `spec/session-host.md:271` (§3.7): "Alerts use the operator phone path"; `:140` (§3.1): deny-all, Unix-socket platform calls only; `:362` (§7 q18): phone-alert and reason-delivery formats unpublished.
- `swarma-credential-broker` at `df8c7385` (v0.10), `spec/broker.md:600-605` (§11): events on `status` and the audit log now; "Later versions deliver them to the session host and the message bridge, so that a session is parked and a person is asked to re-enrol from their phone"; `:873` (§17): labelled later.
- `swarm-platform-architecture` at `6b3f983`, `trust-and-isolation.md:78`: the bridge's egress is "later to its carrier".
- `wiki` at `87f387d`, `book/swarma/ru/11-udalennoe-rabochee-mesto.md:137`: the operator receives a notification when the watcher narrows an account.

## Proposed change

1. **Publish the alert lane as a joint item of R-WATCH:** the owning principal, the route, bounded durable delivery with a status record, retry and unavailable-channel behaviour, and the version from which it exists. Two designs fit the existing boundaries: the bridge delivers typed events over the carrier to the owner's ordinary client (the phone app subscribes like any client), or a protected local event source serves an authorised polling or subscribing client. Neither gives the watcher, the dispatcher or the host a new egress row.
2. **Separate notification authority from operator mutation authority:** an alert never carries or implies an operator act; the inbound act channel and any outbound or read channel are distinct authorities even if one transport carries both.
3. **Alert content and rate:** typed events with a closed per-class schema and no agent-controlled strings (the broker's event rule), journaled with the triggering effect ID, bounded in rate so an alert storm cannot exhaust operator attention or service storage.
4. **Containment stays independent of notification:** alert delivery failure never delays or undoes the journaled per-account narrowing and stop.
5. **Honest versions:** a version without the lane states that watcher and broker conditions are status-only and that the observer read is the operator's detection path; it does not say "over the phone path".
6. **Qualification:** a watcher threshold crossing yields one journaled alert that reaches the published route within the published bound, or a recorded delivery failure; no alert uses TCP from a deny-all account; no alert originates in an agent account.

## Expected benefit

The abuse controls get the detection channel they assume, with an owner and failure semantics; the operator's attention cannot be exhausted by alert storms; no new egress.

## Risks and costs

The bridge or a read-side event source becomes a dependency of alerting, with a schema and subscription to publish. No owner decision is challenged.

## Affected specifications

Dispatcher §7.3, §13, §16 q27; user manager §8.2; session host §3.7, §7 q18; broker §11, §17; trust contract §5 bridge row; book chapters 11 and 13.

## Confirmed by

Room `#swarma-review-3`, topic `f-alert-egress-owner` (root `$e34rO-gD462QhsZAgvtCDRfDa2HQAg7ZuHm2EV7p41E`), 2026-10-13.

- Candidate: fable, `$e34rO-gD462QhsZAgvtCDRfDa2HQAg7ZuHm2EV7p41E`; narrowing accepted in `$62F87EISjeFe-Q1S5niFV4B51chms7q7o9KaUO1F9Uc`.
- astra-19 (`ivmbp_swarma-review-3_astra-19`), `$SFzwfHI1esFDGGuXWvCcUzphvRFbyLnM9SyCZ_H6Cs0`: partial confirmation of the missing alert-delivery owner contract; adopted: broker events have a named later recipient, the SSH channel is not technically one-way, no prohibition on reuse, status-only must be declared, alert failure never delays narrowing.
- astra-06 (`macmini_swarma-review-3_astra-06`), `$wv20WZQkXVeh5kAu10XL18s-6HprJ7DPuFUnZ4zsPEU`: partial confirmation of the channel-selection gap; adopted: broker events are not evidence of an unassigned route, observer- or phone-initiated delivery is a valid design, distinguish owner, delivery semantics and activation timing from the unpublished format, no new egress row inferred.
- astra-04 (`macmini_swarma-review-3_astra-04`), `$gePSl87ItGc0hKsYJvmeXmjEiwNtQ6SJN0TX5wEB_Ok`: partial confirmation of the joint publication gap; adopted: the root helper and launcher have no per-UID row, no mandatory bridge topology, notification data never acquires act authority, delivery failure must not block narrowing or consume unbounded storage.
- astra-16 (`ivmbp_swarma-review-3_astra-16`), `$IgJq9yx0_5Rwr0Jl_gBxi3cV0S8tkvWL5W4lstQDn60`: confirms the narrowed owner/route/availability publication gap (SH7 :271 versus :362; N15 :194 and helper :484-486 are not a notification capability); independently refutes the broader universal-silence reading; adopted as recorded.
- astra-14 (`ivmbp_swarma-review-3_astra-14`), `$E0ecxv4p-Tw1gNRTLwgMo_4YoyxvmKVu5InNS07UQrM`: session-host confirmation of the missing joint publication contract at 860043d; adopted: the host's deny-all row stays in its v1 scope (no slice-0 containment claim), and a status-only stage is an explicit version boundary, never represented as the promised automatic alert.
