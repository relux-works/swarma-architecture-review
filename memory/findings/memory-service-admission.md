# Optional memory still requires an admitted platform service boundary

- Owner: astra-04 (five 2, ivmbp)
- Lens: platform fit and authority boundaries
- Status: proposed
- Confidence: high
- Room: `f-memory-service-admission`
- Candidate: this proposed finding.

## Problem

The base Part 2 §3 places `swarma-memory` under a separate unprivileged service account, and §6 correctly says memory must not block the platform's safety controls or bring-up gates. Those statements do not yet supply the deployment contract for the new service.

In the current module specifications, an account name is not a confinement boundary by itself. At **v1 enforced readiness**, every non-root platform service needs an explicitly admitted egress row and qualification. The allowed Unix-socket reachability set must also be qualified; a client needs authenticated admission and current principal-generation binding. No generic “memory” module exemption exists.

An implementation that installs the new daemon with an unspecified/permissive row, places it under the session-host or broker identity, opens source-owned state files to it, or interprets a source URL as permission to fetch would enlarge authority while claiming merely to add optional retrieval. The opposite error is making the useful documentation experiment wait for all of that infrastructure.

This is a missing deployment-profile contract. It is **not** a claim that the base intentionally grants operational authority or that all platform service requirements are already implemented. The v1 egress prerequisite does not retroactively disable the earlier software-root slice.

## Evidence

1. Base [`SKETCH.ru.md`](../inputs/SKETCH.ru.md), Part 2 §§3,6,8: separate unprivileged service, no raw shared store, optional memory, architecture-document first slice and no platform-gate dependency.
2. `swarma-user-manager` @ `12609a9e05d5013c34416e1a0332fe5c28c4bcd5`, `spec/helper.md:531–547`, §§8–8.1:
   - R-SOCKETS requires reachable sockets to equal the declared platform set.
   - Service rows belong to installer/operator authority; dispatchers cannot alter them.
   - The “Every other non-root platform service” row requires an explicit policy before v1 enforced readiness, with no permissive default.
   - Start-time and scheduled verification, resolver restrictions, incident handling and unpublished encodings remain real gates.
3. `swarma-session-host` @ `255523d43129538b7e7064a0dbfc0b06713bb7e2`, `spec/session-host.md:132–144`, §3.1: an analogous service separates private storage and socket permissions, verifies peer UID/current generation and server identity, and requires verified deny-all egress/resolver restrictions for its enforced profile. Running a harness under a service identity is explicitly not a boundary.
4. `swarma-user-manager` at the same pin, `spec/helper.md:519–527`: task resources are admitted read-only data; the optional web service has a distinct principal, row, socket/grant boundary and activation requirements. A memory source locator cannot silently substitute for such an approved fetch path.

These local sources were read-only, without pulls or execution. They are specification requirements and publication gates, not implementation qualification evidence.

## Proposed change

Define two deployment profiles for the same memory semantics:

- **Documentary M0:** reviewed, explicitly persistable decision records and a read-only CLI/library adapter. No new platform daemon or account, no autonomous source intake, no claim of hostile-agent storage isolation. Exact policy/source versions and data-only output still apply.
- **Protected platform service:** activate only after the relevant owners publish and qualify its own service identity, private store/custody, authenticated generation-bound client/socket contract, explicit egress policy, allowed source-resolution path, resource bounds and readiness/recovery rules. Do not borrow host/broker capabilities or add a direct shared-database lane. For v1 enforced deployment, qualify its service row and resolver/socket restrictions with the existing owners; no invented wire fields are allocated here.

The service may fail its own admission while ordinary platform stop/revocation/recovery remains available. Memory code, adapters, extraction and inference must not become a dependency of those controls. The documentary experiment can measure value before service deployment is chosen.

## Rubric rows affected

- **R2:** reuse existing service-admission and source-owner boundaries instead of a parallel privilege path.
- **R3:** make operational authority separation concrete at the socket, principal and storage boundaries.
- **R7:** name the missing owner contracts and qualification cases rather than imply they already exist.
- **R8:** keep useful document-only M0 independent of later service readiness.

This finding alone does not require reducing the base's R3 score: its authority prohibition is sound; the missing executable seam is primarily R7.

## Proposed conformance cases

| Input/deployment | Required result | Forbidden result |
|---|---|---|
| Memory enabled without its v1 service policy row | No enforced-service readiness | Permissive fallback or readiness claimed from the account name |
| Authorized-looking request from reused/retired UID generation | Refuse under current identity binding | Inherit old memory capabilities |
| `observe`/`verify` contains an arbitrary source URL | Resolve only through an admitted bounded source path, otherwise refuse | New network capability from the locator |
| Missing or slow memory service during operator stop | Existing control owners continue | Stop waits for memory or graph traversal |
| Same-user embedded documentation reader | Report its local/cooperative isolation honestly | Claim that the caller cannot modify its own store |

These are paper acceptance cases for later specification/implementation, not tests executed in this pass.

## Confirmed by

- **astra-05**, memory service-admission review, 2026-10-14: independently checked helper §8.1 and host §3.1; confirmed no permissive default, installer/operator ownership, peer/current-generation boundary and no network authority from a source URL.
- **wonder-03**, memory service-admission review, 2026-10-14: independently confirmed service-row/socket/custody obligations and accepted documentary-first versus separately admitted daemon profiles.

The finding remains `proposed` under the mission's writing protocol; peer confirmation is not an operator adoption or a platform spec amendment.
