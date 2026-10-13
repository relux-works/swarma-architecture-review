# Swarma implementation strategy quorum (track 2): mission brief

You are one seat of the implementation-strategy quorum. It starts the moment review cycle 3 (track 1) parks, with no gap («запускай второй цикл сразу после первого без ожидания 2.5 часа», owner, 2026-10-13). **The same seats move over with their loaded context.** That is the 'same quorum with the same contexts' the owner asked for. ivan-curator convenes and parks it; it does not direct your conclusions.

The operator's words, 2026-10-13, verbatim:
- «отедльным треком потом запускай отдельный такой же кворум который получит все такие же контексты, ссылки на все репозитории которые уже/будут задействованы в платформе, и пускаю прорабатывают самую належную стратегию имплментации платформы - какие приоритеты, что делаем в каком порядке, что бы не делать лишнюю работу и тд. на выходе должен быть документ план имплментации, который силами opus5-5 переведен на нормальынй русский язык.»
- «только ревью которое на поиск плана оптмизации нужно будет запустить ПОСЛЕ (что бы не откнуться в рейт лимиты) это отдельный трек будет» — «но тоже приоритетный»

## Your task

Work out the **most reliable strategy for implementing the Swarma platform**, as it is specified after cycles 1–3 and waves 3–5b:
- what to build first and why;
- in which order, with which dependencies;
- what can run in parallel;
- how to avoid wasted work: no throwaway interim mechanisms, no rework caused by building against moving contracts, no premature generality;
- how to qualify each step;
- how to cut over from the spm monolith;
- which risks threaten the schedule.

The output is one document, `impl/PLAN.md`, then its Russian translation `impl/PLAN.ru.md`, made by the Claude Opus 5.5 seat.

## Context

**Everything track 1 had.** See `MISSION-3.md`, "Sources", including the second-machine clone list. Also read the outcome of track 1: `FINDINGS.md` and `cycle3/findings/*.md`.

**Every repository involved now or planned** (relux-works, `main` unless stated):

| Repository | Role |
|---|---|
| `swarma-user-manager` | privileged user manager and launcher (spec; implementation to come) |
| `swarma-dispatcher` | launch dispatcher (spec plus draft schemas) |
| `swarma-credential-broker` | credential broker (spec) |
| `swarma-session-host` | session host (spec, SH1 extraction tooling, `docs/`) |
| `curator-agent-launcher` | `curator-run`, the executor and plan composer (code, released v0.2.0; v0.3.0 pending) |
| `curator`, `curator-spec` | Curator (profiles, environments) and its spec with CIP-0008…0012 |
| `curator-network-profiles-dev` | network profiles: N15, N16, proxies |
| `skill-project-management` | task-board, the spm monolith; board import spec (#604), board runners |
| `skill-agents-management` | harness plugins and model registry used by the launcher |
| `a2a-swarm` | the coordination bus |
| `swarm-platform-architecture` | trust contract, VISION, C4 and sequences |
| `worker-jail` | remote-workplace protocol v2.1 (container path, egress service) |
| `agent-session-host` | legacy hosted-launch contract (being harvested) |
| `wiki` | the book, decisions, glossary, naming |
| boards `swarma-*-board` | private task boards per module |

Hosts and runners: the operator's Mac mini (agents, platform services; currently overloaded, see the park rules), an OVH Linux host with ephemeral runners (the first candidate for untrusted workloads and verification), GitHub-hosted runners (qualification), and a second operator machine.

## Lenses (seat assignment as in track 1; everyone roams)

1. **Critical path and slicing.** Slice 0 (one protected Claude launch), slice 1 (Codex), slice 2 (enforced networking), the remote worker milestone A, and SH1/SH2+ of the session host. What is the minimum first slice that proves the boundary?
2. **Dependency graph and contract freezing.** Which formats must be published before code (grant/revocation/broker frames, `workspace-result/1`, plan intake, operator acts), and in which order, to avoid rebuilding.
3. **Extraction from spm.** What moves out of task-board when, and what stays. How to keep today's work running during the move (tb-sessiond, runners, the board).
4. **Qualification and verification.** The runner strategy (GitHub-hosted, OVH ephemeral), the per-host capability matrix, the mutation and negative-vector suites, the gates that are the real arbiters.
5. **Security first steps.** The static range deny, the operator account and phone path, the transfer path, credential leasing: what must exist before ANY external contributor is admitted.
6. **Operations and cut-over.** Host bring-up (Linux first or macOS first), the maintenance windows, rollbacks, the operator's daily work, the park and unpark discipline on shared hosts.
7. **Agent workforce and cost.** Which task classes go to which models and harnesses, review policy, token budget per slice, and how to stay inside provider rate limits.
8. **Risks and kill criteria.** What could derail the schedule, early warning signs, and when to stop and redesign.

## Working protocol

**Room and identity.** `#swarma-impl-plan`.
- Keep your cycle-3 identity (`A2A_AGENT` is already set) and just run `a2a join swarma-impl-plan`. Do not create a new identity.
- Your work directory and clone stay the same.
- Post in `#swarma-impl-plan` only. `#swarma-review-3` is parked.

**Seat assignment.** The first seat named in each lens holds the pen for its section. Seats with no lens listed review across all lenses.

| Lens | Seats |
|---|---|
| 1 critical path and slicing | astra-01 (pen), astra-11, sol-01, sol-11 |
| 2 dependency graph and contract freezing | astra-10 (pen), astra-02, astra-12, astra-20, wonder-03, wonder-13 |
| 3 extraction from spm | astra-04 (pen), astra-14, sol-02 |
| 4 qualification and verification | astra-05 (pen), astra-15, astra-06, astra-16, sol-12 |
| 5 security first steps | fable (pen), astra-08, astra-18, astra-09, astra-19, sol-13 |
| 6 operations and cut-over | astra-03 (pen), astra-13, sol-03, sol-14 |
| 7 agent workforce and cost | astra-07 (pen), astra-17, opus |
| 8 risks and kill criteria | wonder (pen), wonder-01, wonder-02, wonder-11, wonder-12 |

- **Assembler:** core astra. **Translator:** opus, who writes `impl/PLAN.ru.md`.
- The Muse seats rejoin when their provider quota resets. Until then their lens's other seats carry the work. If the pen holder is paused, the next seat in its row takes the pen.

**Inputs from track 1.** The 42+ confirmed findings in `cycle3/findings/` are binding inputs. The plan must say, for each, in which phase it gets fixed: before which slice, or which slice it blocks.

**Phases**
1. **Section drafts.** Each lens produces one section file, `impl/sections/<lens-slug>.md`. Several seats share a lens: agree in the room who holds the pen, and the others review. Post a summary and the file path.
2. **Reconciliation.** One topic per conflict between sections, slug `c-<short-name>`. Resolve it with evidence from the specs and findings. A resolution needs confirmations from at least two seats on different lenses.
3. **Assembly.** The core astra seat assembles `impl/PLAN.md`:
   - goals and non-goals;
   - principles;
   - phases and slices, each with scope, acceptance, dependencies, owner lane and estimate;
   - the critical path;
   - parallel tracks;
   - qualification gates;
   - the risk register;
   - "what we deliberately do not build";
   - open owner decisions.

   Every seat reviews it, and objections go in topics.
4. **Translation.** The Claude Opus 5.5 seat writes `impl/PLAN.ru.md`: natural Russian for the operator, the same structure, technical identifiers unchanged. Avoid calques, and follow the book's style (`wiki/book/swarma/ru`).
5. **Park.** When both files are committed and no open conflict remains, ivan-curator posts PARK.

**Writes.** Use `impl/` in `relux-works/swarma-architecture-review`. Commits are signed, with `git pull --rebase` first; never force-push. Section files avoid write races. Only the assembler edits `PLAN.md`, and only the Opus seat edits `PLAN.ru.md`.

**Rounds, waits, sandbox and hard rules.** As in `MISSION-3.md`: docs-only, no builds, tests or spawns, no web, no credential stores, and no secrets anywhere. Codex seats run max effort on the standard service tier (fast mode removed by the owner).
