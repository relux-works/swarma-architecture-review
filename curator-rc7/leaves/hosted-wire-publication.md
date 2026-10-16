# H-WIRE — Publish the local hosted successor contract

Owner repository: **curator-agent-launcher**; skill-project-management jointly accepts the receiver side in its own reviewed change. Size: **3**. Follow-on activation prerequisite, not a Curator rc.7 tag blocker.

Normative clauses: `protocol/local-hosted-launches.md` §§1–3, 4 (closed policy), 5–8; CIP-0016 implementation leaf 1. The curator-spec summary is already Accepted at `5509499`; this leaf publishes the missing owning-repository wire, not that summary again.

Attack surface: incompatible peers silently broadening a frozen plan or its authority.

Acceptance:

- Jointly freeze successor identifiers, full closed plan/capability/preparation/receipt bindings, limits, framing, expiry/one-use lifecycle, backend config spelling/precedence and diagnostics. Plan `2.0.0` / protocol 10 remain recommendations until that decision; never extend `1.0.0`/protocol 9 in place.
- Cover the complete process, runtime, prepared resources/generation, snapshot and policy under CCJ-1 SHA-256 excluding only content_digest. Retain §3 limits and existing argv/env/literal/versioned-data limits. Publish a per-runtime operation matrix and required-understanding behavior.
- Bind Curator's HOST-HOME receipt/verification surface and separate backend/Codex settings transport. Publish only closed policy/trust keys beside the home; runtime config rewriting is not an option.
- Freeze same-user/local authority and explicit backend migration. Local control token/home paths confer no remote authority. Ordinary node-source setup-token injection stays unsupported on this route until an explicit amendment reconciles hosted §6; the independent headless token route changes no hosted rule.
- Preserve private plan stdin, terminal fd3/status fd4, receiver close-on-exec, length-prefixed bounded status, poison/truncation distinctions and redaction. Publish old/new compatibility vectors before enablement.

Negative/control pairs: a valid successor request negotiates; new fields under old version, missing/unknown runtime operations, conflicting schema/protocol/build, duplicate/trailing/oversize/deep JSON and unknown required extensions refuse. A whole-plan digest verifies; mutating/removing each covered field refuses despite otherwise valid syntax. Exact malformed/truncated status fixtures retain distinct outcomes; child exit alone cannot invent a typed refusal. Known-invalid carrier controls must fail the intended schema/decoder.

Dependencies/paths: HOST-HOME-SPEC and the applicable settings publication; `SPEC.md`, new owning schemas/vectors and hosted registry docs. Receiver counterpart: `tools/board-cli/internal/sessionmanager/hosted_{types,decode,errors}.go` only after publication. Serialize shared SPEC/diagnostic/config edits with v4/settings work. Runtime qualification and backend/policy owner choices remain explicit gates, not outcomes of schema validation.
