# H-CODEX — Exact private app-server and durable policy

Owner repository: **skill-project-management**. Size: **5**.

Normative clauses: hosted §§1/3/4/5/6 and §8 question 3; CIP-0016 leaf 6. Typed settings delivery belongs to the separate CIP-0018 project-management leaf and is a dependency, not duplicated ownership here.

Attack surface: private home preparation and cold resume overriding the caller's admitted process/policy.

Acceptance: execute the already composed app-server with prepared private endpoint, full env/home, native goals disabled and all startup settings/policy covered. Retain private managed-client transport; no public endpoint or app-server PTY. Stop using legacy `preparePrivateCodexHome` on this new route: Curator alone prepares initial bytes and credentials. Policy/trust record stays beside the home. Neither host nor launcher rewrites native/managed/private `config.toml`; only supported startup/thread APIs implement the published closed policy.

Actual supported app-server qualification must prove policy with conflicting native config across thread start, repeated attach and forced cold typed resume. Missing support blocks activation for a supported-mechanism decision; config rewriting or weaker policy is not a fallback. Endpoint bind/readiness failure records refusal without changing endpoint/argv; retry requires new reservation/plan. Text-directive goals need acknowledgment, with native goals still disabled.

| Positive control | Negative / forbidden effect |
| --- | --- |
| Prepared complete plan starts an app-server, private client attaches and typed thread resumes | Interactive conversion, late flags/env, public binding or PTY wrapping cannot pass exact-process checks |
| Declared narrowed policy survives conflicting native config, repeated attach and cold resume | Thread/start-only policy, receiver config rewrite, ambient MCP import or duplicate profile selector fails |
| Free reserved endpoint and exact plan bind successfully | Port collision/readiness failure cannot choose another endpoint or launch a retry from the old plan |
| Same snapshot plus valid writable runtime state resumes after source changes | Drift/missing original receipt or unknown liveness refuses; no native auth relinking or baseline replacement |

Controls: omit startup policy but retain thread/start policy; rewrite one config key; append --listen at receiver. Each must fail the intended real adapter/entry test. Fake app-server results do not qualify vendor cold resume.

Dependencies/paths: H-WIRE/H-PREP/H-ADMIT/H-FORMS, HOST-HOME-CODE, qualified Codex settings/store policy and its project-management delivery leaf. `tools/board-cli/internal/sessionmanager/codex_host.go`, private client/restore/goal paths and real adapter tests. Serialize with that settings leaf and existing Codex lifecycle work. All initial config bytes remain Curator-owned and later native writes runtime-owned.
