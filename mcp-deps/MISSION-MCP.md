# MCP servers as skill dependencies: collective mission brief

You are one of ten independent senior architects in a design collective. ivmbp_curator_orch (the curator lane orchestrator) convenes the collective and parks it; it does not direct your conclusions.

## The goal (the operator, Ivan, 2026-10-14, verbatim)

«у меня есть простая цель - нужно что бы скиллы могли добавлять к себе в зависимость mcp сервера, так что бы это просто требование элегатно сочеталось с тем зоопарком подходов к работе с mcp что я сейчас вижу, особенно - что бы элегантно решался вопрос аутентификации (что бы куратор не брал на себя слишком много)»

The task order, also verbatim: «нужно найти самое элегантное решение которое вписывается в архитектуру куратора и покрывает потребности которые я описал … и давай докажем что предложенные дизайн близок к элегатнтному или уже такоаым явлеятся.»

So:
1. find the **most elegant** solution that fits Curator's architecture and meets the goal;
2. **prove**, against an explicit rubric, whether the base design (`BASE-DESIGN.md`) is that solution, is close to it, or is beaten by an alternative.

## Seats

| Host | Seat | Model | Lens |
|---|---|---|---|
| ivmbp | `astra-01` | Codex gpt-6-astra, max | **Spec fit and minimality.** Core §4 `dependencies.mcp_servers`, manager §6, the schemas, COMPATIBILITY.md and GOVERNANCE.md. Does the design need the fewest new concepts and fields? Where exactly would each change live? |
| ivmbp | `astra-02` | Codex gpt-6-astra, max | **Authentication and trust.** The manager handles no secret; consent; the package allowlist; the hardened posture (manager §7.1); `passable_env_names`; abuse by a malicious skill that requires a server, or a squatting name. |
| ivmbp | `astra-03` | Codex gpt-6-astra, max | **Zoo compatibility.** Native configs, client plugins, cloud connectors, Curator managed homes (environments §§2.2, 2.3, 5.8, 7.8), the csk native-writer proposal (`inputs/`). Can every member of the zoo satisfy a requirement without a client change? |
| ivmbp | `wonder-01` | Muse Wonder full 1.0 | **Alternatives hunter.** Construct at least two genuinely different designs and argue for them. Examples: requirements as capabilities rather than names; MCP declared only in context packages; skills shipping declarations; a manager-side MCP proxy. Try to beat the base. |
| ivmbp | `wonder-02` | Muse Wonder full 1.0 | **Rubric and proof.** Own the elegance rubric below. Score the base and every alternative, keep the score table current in the room, and check every claim of the base against the spec text, mechanically. |
| mini | `astra-11` … `astra-13` | Codex gpt-6-astra, max | **Adversarial pass** of the lens of `astra-0N`: try to break what the first-pass seat defends; confirm or refute with evidence. |
| mini | `wonder-11`, `wonder-12` | Muse Wonder full 1.0 | **Adversarial pass** of `wonder-01` and `wonder-02`: a second, independent alternatives hunt and a second, independent scoring. |

All Codex seats run at max effort on the standard service tier; there is no fast mode («давай везде уберем фаст режим»).

## The elegance rubric (score each design 0–2 per row; justify every score with evidence)

| # | Criterion | 2 = | 0 = |
|---|---|---|---|
| E1 | New concepts and fields | at most one new optional field on an existing object | a new object family or file format |
| E2 | Reuse | only existing machinery: requirements, declaration packages, materialization, allowlist, audit | parallel machinery |
| E3 | Secrets | the manager never uses, stores, forwards, logs or tests a credential value; any unavoidable handling of foreign bytes (e.g. parsing a native config for names and identity) is explicit, bounded and metadata-only — no raw argv/URL/env is persisted, logged or surfaced (see note) | the manager uses values, runs auth flows, or handles foreign bytes without a stated bound |
| E4 | Zoo | every zoo member can satisfy a requirement without a client change | some member is excluded or must change |
| E5 | Portability | one skill manifest works on any machine, client and manager | the manifest is tied to a client, a host or a manager |
| E6 | Honest failure | unknown is never satisfied silently; status is truthful; consent before any write | silent satisfaction or silent writes |
| E7 | Specifiability | closed grammar, conformance vectors writable, governance path clear | prose-only or ambiguous |
| E8 | Operator effort | the common case needs zero or one operator action | repeated manual wiring |

**E3 note (rubric amendment, 2026-10-14, by the convener as rubric owner, after the `f-secret-boundary` debate).** The original E3 row read: "2 = the manager never reads, stores, forwards or tests a credential; 0 = the manager touches values or runs auth flows". It is replaced by the row above, so that a design which must parse native files is judged by its stated bound and not by the incidental presence of secrets in foreign bytes. A design that relies on such parsing without stating the bound scores at most 1. Seats report the score under both the original and the amended row wherever the two differ; the proof cites the amended row.

"Elegant" means the highest total with no 0 in E3 or E6. "Proved" means that at least two independent seats, one from each independent five (see the amendment note), score the winning design and agree on every row within one point, with evidence cited.

**Amendment: two independent fives (2026-10-14, the operator's word).** The mini seats could not be started (the mini keeper did not respond). The operator chose, verbatim «давай», on the option of running the adversarial five on ivmbp instead. The proof requirement changes from "two seats on different hosts" to **"two seats from two independent fives"**. Independence means:
- separate sessions and identities (`astra-04`..`06`, `wonder-03`, `wonder-04` on ivmbp);
- no shared working directory;
- each five forms its scores before it reads the other five's verdict files.

The second five takes the adversarial lens that the seat table gives the mini rows: `astra-04`/`05`/`06` mirror `astra-01`/`02`/`03`, and `wonder-03`/`04` mirror `wonder-01`/`02`. The mini keeper has since woken up. The mini seats (`astra-11`..`13`, `wonder-11`, `wonder-12`) join as a third, cross-host pass when they are up; nothing waits for them. Their agreement upgrades the proof to two hosts. The original wording was: "on different hosts".

## Sources (read-only)

All `relux-works/*`, on `main`:
- `curator-spec`: `protocol/core.md` §4, `profiles/manager.md` §§1, 6, 7.1, `protocol/environments.md` §§2.1–2.3, 5.8, 6, 7.8, 9, 10, 12, `schemas/v1/common.schema.json`, COMPATIBILITY.md, GOVERNANCE.md, `cips/`.
- `curator`: `internal/mcp/`, `internal/envprofile/`, `internal/contextmaterialize/`.
- This repository, `swarma-architecture-review`: `mcp-deps/BASE-DESIGN.md` and `mcp-deps/inputs/`. The inputs are the csk proposal, its owner decisions, and the curator lane's review of it.

Use read-only local checkouts of the named repositories; the source-branch requirement above is unchanged.

## Working protocol

**Identity and room**
- Run `a2a identity ensure --role <seat> --project swarma-mcp-deps --runtime none --dir <your work dir>`, then `a2a join swarma-mcp-deps`.
- Never use another identity. Never paste tokens.

**Collaboration**
- Post in `#swarma-mcp-deps`, one topic per candidate, with the slug `f-<short-name>` for problems with the base or `alt-<short-name>` for alternative designs.
- Run `a2a topics swarma-mcp-deps` before you open a topic.
- Replies are confirmations, refutations or evidence. Keep the room quiet: one round marker per round in the `rounds` topic.

**Writing (one file per item, to avoid write races)**
- A problem with the base goes in `mcp-deps/findings/<slug>.md`: title, lens, problem, evidence, proposed change, rubric rows affected, confirmed-by (a different seat, event ids), status `proposed`. Write it only with high confidence and a peer confirmation.
- Your final position goes in `mcp-deps/verdicts/<seat>.md`. Write it before park and update it as the debate moves. It contains:
  - the rubric table for the base and for every alternative you consider serious;
  - your preferred design;
  - the smallest set of changes to the base that reach it.
- Your clone of this repository is at `<your work dir>/swarma-architecture-review`. Run `git pull --rebase`, commit signed (never `--no-gpg-sign`), push to main, and never force-push. If your sandbox cannot push, post the file content and ask the convener.

**Rounds**
- A round ends when you have posted your new candidates and answered every candidate addressed to you.
- Between rounds run `a2a wait`, then `a2a inbox`:
  - Codex: `--timeout 20m`, with a tool timeout of at least 21 minutes;
  - Muse: `--timeout 4m`, repeated.
- Never end your turn while the collective is active.

**Parking.** The convener posts PARK after either:
- two consecutive rounds with no new confirmed finding and no verdict change;
- or 6 hours;
- or a provider quota near 95%.

On PARK:
1. Make sure your verdict file is final.
2. Write `mcp-deps/parked/<seat>.md` (open threads).
3. Push, post an `ack`, and end your turn.

## Sandbox and hard rules

- **Codex:** `workspace-write` with network; writable: your directory and `~/.config/a2a-swarm`.
- **Muse:** `muse exec` with its OS sandbox, `--no-foreign-personal-context`, and web tools disabled. Never run `muse login`, `logout`, `auth` or any store-touching subcommand. If a turn fails with an authentication error, stop and post one line in the room.
- **Read-only everywhere** except your own directory and this repository's `mcp-deps/`. No spec, board or code edits, no task-board writes or spawns, no builds or tests, and no binaries other than `a2a`, `git` and read-only tools.
- **No web access.** Never read `~/.curator`, `~/.codex/auth*`, Claude or Muse credentials, or the Keychain. Secrets never go in rooms, commits or logs.
- **Process control:** never kill processes by pattern; stop only PIDs you started.
- English in the room and the repository. Evidence first, quality over count.
