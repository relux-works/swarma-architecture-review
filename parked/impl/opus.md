# opus: track 2 park note

Seat `macmini_swarma-review-3_opus` (Claude Opus 5.5, max effort). Track-2 roles:
- lens 7 reviewer (workforce and cost);
- reliability and recovery author for the cycle-3 findings this seat owns;
- `impl/PLAN.ru.md` translator.

This note holds residuals that `impl/PLAN.md` does not carry. The convener's final PARK `$0f6SCaEg9fsXqOxzg0VmbDmUeMudiNKP-1RIaY9TB30` names them: the Russian terminology, plus wonder-12's two wording notes.

## 1. Late Russian wording notes for the next revision

wonder-12 (`$BcawPOyN86U4NaBF206QtlqPk5JDd9A4PFlMOYGr-Qc`) left two optional notes. They arrived after parity closed and are not applied in `3ca77ab`:

1. **RU:241, "Pause new producers".** «Приостановить новых авторов» is the rendering. «авторов изменений» reads more precisely.
   - The same «автор» for producer appears in §§2, 9 and 10. If this note is adopted, change it in all of them.
2. **RU:253, "durable host/mailbox".** «надёжный» reads as "reliable", but durable here means persisted, long-lived storage.
   - The plan renders "durable" as «надёжный» throughout: 17 lines, among them «надёжный подписанный почтовый ящик», «надёжное хранение полного содержимого», «надёжные заявки», «надёжных частей служб» and the §13 rows.
   - A later revision should pick one term, for example «долговременный» or «с сохранением на диске», and apply it everywhere "durable" is meant. «надёжный» should stay only where the English says reliable or robust.

wonder-11 and wonder-13 read their rows in both languages and left no Russian wording notes (`$1x4dzextwAtSIidHBz6OvUTNvPtceWJUXpQEwSnhV4Y`, `$ajyWSPt1evt47lQZyis9_jmxA5ecXg8LMiuKohGb5kc`).

## 2. Russian terminology for later operator-facing documents

`impl/PLAN.ru.md` translates the frozen English `b1ca0ce`. Parity review settled the renderings below. Use them when the Russian book (`wiki/book/swarma/ru`) or other operator documents are refreshed from the plan, so the two Russian texts do not drift apart.

| English | Russian | Why |
|---|---|---|
| lens | ракурс | avoids the calque «линза» |
| workspace (materialized B) | рабочая копия | «рабочее место» is the workplace |
| intake (launcher input) | формат входа | book usage; «приём» is work admission |
| admission (work / class, host, donor) | приём / допуск | |
| exporter / materializer | программа выгрузки / программа развёртывания | |
| activation | включение | |
| waiver (export obligation) | снятие обязательства | «отказ» stays refusal |
| standing discard of refused exports | постоянно действующее разрешение на отбрасывание | an optional operator preauthorization, not continuous deletion |
| CONNECT authority / application origin | authority (имя хоста и порт) / origin | not «полномочия» or «источник» |
| hosted (session-host launch route) | запуск через хост сессий (hosted) | GitHub-hosted lanes are «облачные раннеры» |
| interpreted-input closure | замыкание интерпретируемых входов: весь допущенный вызов и всё, что он загружает | not an inventory |
| signature / key suite | набор алгоритмов подписи / ключей | |
| issue fresh broker authority | заново выдать полномочия в области авторизации брокера (гранты и привязки по новым решениям оператора) | the broker is the domain, not the grantee |
| successors (rollback) | последующие записи состояния | not session successors |
| lock revalidation | результат заново сверяется с текущим состоянием под снова взятой блокировкой | the lock itself is not what gets checked |
| durable | open (see §1, note 2) | «надёжный» is reliable |

Book terms stay as in `wiki/book/swarma/ru` at `87f387d`: учётка, запускатель, хост сессий, выгрузка, забор, квитанция, квалификация, приёмка, окно обслуживания.

## 3. Translation record

- **Signed chain:** `4761e45` → `5f6f029` → `dc422fe` → `0df2591` → `ebfac2b` → `3ca77ab`. The final RU is `3ca77ab`.
- **Final parity checks against EN `b1ca0ce`:**
  - 14 h2 and 3 h3 headings;
  - 120 table lines with matching column counts;
  - the 52-link multiset, including 44 unique finding links;
  - all event IDs and graph edges;
  - unchanged identifiers.
- **Reviewer corrections applied:**
  - CONNECT authority and origin;
  - the session-host hosted route;
  - interpreted-input closure;
  - broker-domain reissuance;
  - state-record successors;
  - no SH2 PTY survival promise;
  - standing discard as an operator preauthorization;
  - lock revalidation;
  - "subject to" for early durable output.
- **Self-found corrections:** intake, algorithm suite, challenge, and worker-entry permission refusal.
- **Confirmations:** lenses 1–7 confirmed parity on the final head.

## 4. What I would examine next

- **Book chapter 14** («Где мы и что дальше»). When it is refreshed from this plan, it needs the milestone set (P0, S0a, S1, S0b, S2, W, T, A, H, SH1/C1), the frozen revision `b1ca0ce` and the terms above, including whatever term §1 note 2 settles for "durable". The plan's own follow-ups, such as the restore-format and P0 operator-packet publication, are already in `impl/PLAN.md` §§4 and 8.
