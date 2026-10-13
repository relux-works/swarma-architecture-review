# World-readable ledger, receipts and applied state let any tenant enumerate every account and execution on the host

- **Lens:** trust and threat model (fable); book-versus-spec consistency. User-manager cross-check (astra-02).
- **Status:** proposed (hardening and clarification, not a broken invariant).

## Problem

The user manager publishes three sets of root-owned, world-readable records: the ledger with one record per generation (`generation, username, uid, gid, kind, label, state, created_at, created_by, retired_at`); the start receipts per generation and execution (`execution_id, epoch, pid, start_time, boot_id, session_id`), mode 0644; and the applied-state record per generation (`profile_ref, profile_digest, proxy: {service generation, port}, firewall_generation, applied_at`). World-readable means every agent and workplace account on the host, including an untrusted remote worker's workplace, can read them: which accounts exist, their caller-chosen labels, kinds and creators, when each execution of each tenant started and under which root pid, and each trusted agent's proxy port and network profile. The book says a remote worker "does not see other homes and processes, the board as a whole, the carrier directly, the network outside its profile"; the Linux reference mounts `/proc` with `hidepid=2` for other tenants' processes. The files re-expose the root start identities and history that `hidepid` hides and add labels and network attribution that `/proc` never showed. The specs' "readability is not authority" and "no secrets" are true; the records are metadata. The claim is therefore a hardening and clarification: on a host that admits untrusted work, the host topology and the activity timing of other tenants should be confidential to tenants, and the book's isolation sentence should either be made true for these files or be narrowed to homes and processes.

**Scope, as narrowed by the cross-checks.** The ledger's named readers are services: the broker, the root launcher (which reads the ledger and writes the receipt before the privilege drop, user manager §7 step 2 and step 6), the dispatcher and the session host. The launcher specification's unqualified phrase "the broker/launcher read the helper's root-owned ledger" sits in the section whose first consumer is `curator-run` under the agent account, so whether any agent-side phase reads the ledger is not settled by that text; the consumer and phase clarification is required publication work, and if a child ever needs ledger evidence it gets a scoped own-generation projection, never global enumeration. The denial proposed below applies to the child execution after the privilege drop and leaves the root launcher's ledger and receipt work untouched. Homes are 0700 and the book's sentence can be read as homes and processes only; receipts expose root start identities, not descendants or home contents. Blocking these files is necessary, not sufficient: OS account databases (`dscl`, `getent`) still list usernames, the host's process-visibility row decides what `/proc` or `ps` shows, and that residual is stated, not solved here. No authority bypass or deployed leak is claimed.

## Evidence

- `swarma-user-manager` at `7b59da7` (v0.10, UM7), `spec/helper.md:130` (§4.0 layout): "ledger.json (0644), receipts/ (0644 files), applied-state/ (0644)"; `:230` (§4.5): "The ledger is a root-owned, world-readable file with one record per generation ... It contains no secrets ... Readability is not authority"; `:405` (§7 step 6): the start receipt `lib/user-manager/receipts/<generation>/<execution_id>.json` with pid, start time, boot id and session id, mode 0644; `:468` (§8): the applied-state record is "root-owned, world-readable"; `:423` (§7 R-CEILINGS): the Linux unit's "read-only system" and `/proc` with `hidepid=2`, and the macOS file sandbox, with no deny row for this subtree; `:182` (§4.3): homes 0700.
- `swarma-dispatcher` at `74687e60` (v0.11), `spec/dispatcher.md:551` (§9.1): `/proc` with `hidepid=2` in the Linux reference.
- `curator-agent-launcher` at `f08f566d` (LR6), `SPEC.md:2085-2089`: "The broker/launcher read the helper's root-owned ledger ... (0644 in a root-owned directory)", inside §10.3 (`:2064` onward), whose first consumer is `curator-run` under the agent account; the term "launcher" there is not disambiguated between the root user-launcher and the agent-side executor.
- `wiki` at `87f387d`, `book/swarma/ru/11-udalennoe-rabochee-mesto.md:108`: the remote worker "does not see other homes and processes".
- `swarm-platform-architecture` at `6b3f983`, `trust-and-isolation.md:67`: homes 0700 with no ACL; no statement about platform metadata files.

## Proposed change

1. Deny agent and workplace executions read access to `lib/user-manager/` (ledger, receipts, applied state) through the per-execution mechanism the host already selects: a file rule in the Linux per-execution unit beside its "read-only system" row, and a file rule in the macOS sandbox profile (R-CEILINGS/R-EXEC), applied after the privilege drop so the root launcher's ledger read and receipt write are unaffected. The files stay world-readable for the service accounts, so no mode or group change is needed, which the no-supplementary-groups rule would complicate. Before the row is written, publish the reader and phase list (root launcher, broker, dispatcher, session host; any agent-side phase named explicitly or excluded), and give any child that needs ledger evidence a scoped own-generation projection. Qualify the workplace relay stub (which reads no files) and every service-mediated read path separately from the job unit.
2. State in user manager §4.5 and §8 that readability serves platform services and `swarma-observer`, and add a qualification row beside R-SOCKETS/R-SHARED: a test UID under the agent and workplace unit cannot list or read the ledger, receipts or applied-state directories, while the broker, launcher, dispatcher, session host and observer can; direct-reader epoch and fence checks (R-GEN) are unaffected.
3. Either way, make the book's sentence precise: homes and processes are hidden; platform metadata files are hidden only once the row above is in place; account names remain visible through the OS account database.
4. Labels: the ledger's `label` plays no part in authorisation (broker §6.3), so nothing changes for authority; the denial makes their content invisible to tenants.

## Expected benefit

Cross-tenant enumeration and timing of other tenants' executions through platform files is closed for untrusted placements at the cost of one file rule in a mechanism the host already requires; the service read path is untouched, and the book's isolation statement becomes accurate.

## Risks and costs

One file-deny row per platform, a qualification row and a consumer audit of ledger readers (done above for the published readers; to be repeated when the keeper or a web-tool service becomes a reader). The OS account database residual remains. No owner decision is challenged.

## Affected specifications

User manager §§4.0, 4.5, 7 (R-CEILINGS rows), 8, 12; dispatcher §9.1; session host §3.1 (ledger as a service reader); launcher §10.3; book chapter 3 layout and privilege table, chapter 11.

## Confirmed by

Room `#swarma-review-3`, topic `f-ledger-topology-read` (root `$bQGTP3zrM3wr_ESXrQhEeOymEQ_62Jkoa3qX-oCLvIo`), 2026-10-13.

- Candidate: fable, `$bQGTP3zrM3wr_ESXrQhEeOymEQ_62Jkoa3qX-oCLvIo`.
- astra-02 (`macmini_swarma-review-3_astra-02`), `$Z465d4vgyQVu07HTdJGalzjeE-fItx4tzYNRqjBKMc4`: confirms the declared metadata exposure (no cited row denies the reads); limits adopted: hardening and clarification rather than a broken invariant, receipts expose root identities only, a consumer audit of ledger readers before denying the directory (done: LR6 names the broker and launcher), qualify the workplace relay and service-mediated reads, and the OS account database residual.
- astra-09 (`macmini_swarma-review-3_astra-09`), `$_WVT898Kdk_cJSS05TNAQ4-E3N_4Yj0eS04V4z5fVek`: first-pass abuse-control confirmation of the declared cross-account metadata exposure, not of a stronger confidentiality invariant or of one-row sufficiency; adopted: the per-host process-visibility row and OS account databases keep the denial from hiding all accounts and processes, preserve service epoch and restore checks, and qualify any own-generation projection and relay or file-tool paths.
- astra-02, second answer `$p_alhc5OJyf4PJAq2pOwT6icO3hSO7-LjyDGfinlR_8`: the LR6 "broker/launcher" wording does not by itself exclude an agent-side reader, so the consumer and phase clarification stays required publication work and the denial must preserve the root launcher's pre-drop ledger and receipt work. Applied in the scope paragraph and item 1.
