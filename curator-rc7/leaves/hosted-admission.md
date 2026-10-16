# H-ADMIT — Exact-plan admission and one-start durability

Owner repository: **skill-project-management**. Size: **5**.

Normative clauses: hosted §§3/4/5/6/7; CIP-0016 leaf 4 admission half. Attack surface: accepting byte-consistent but unauthorized/stale plans, or executing twice after crash/retry.

Acceptance: through the actual authenticated control route, strictly decode negotiated successor only; recompute full CCJ-1 digest; independently verify board/owner/runtime/generation, reservation/expiry, exec guard, path confinement, runtime capabilities, closed policy and Curator receipt using the published verification surface. Matching digest never supplies authority. Repeat required binding/exec/content checks at actual start. Preserve exact planned process without daemon-env merge, defaults, PATH relookup, shell conversion, secret resolution or repair.

Durably record original provenance/admitted generation and consume reservation before start. Distinguish prepared, admitted, started and unknown crash outcomes. Retry can return a recorded result, never launch twice or treat unknown liveness as absence. Preserve initial snapshot/overlay baselines. Reject unsupported node-source hosted injection until separately adopted. Keep old route refusal behavior intact.

| Positive control | Negative / forbidden effect |
| --- | --- |
| Valid successor plus live correct reservation reaches a recording factory exactly once | Digest field omission/mutation, invalid exec guard, wrong binding, expired/replayed reservation or unsupported capability starts zero providers |
| Recorded admitted retry returns the original outcome | Crash at each record/start boundary or unknown process state cannot trigger a second start |
| Same protected content and declared state pass required recheck | Snapshot/overlay/exec swap after initial admission refuses at actual start; receipt is not trusted merely because supplied by caller |
| Exact full environment/process is passed to each adapter | Poisoned daemon env or legacy defaults cannot add/change a value; no secret appears in public outcomes/logs |

Controls: digest restricted to argv/binary; generation ignored; unknown liveness treated absent. Each must fail the intended real-route test rather than setup. Privately synthetic credentials only.

Dependencies/paths: H-WIRE, H-PREP, HOST-HOME-CODE, H-FORMS/import guard; `hosted_control.go`, `hosted_decode.go`, durable session/provenance records and actual provider-start boundary. Serialize manager/control changes with H-PREP and runtime adapter wiring. Provider-specific native behavior is qualified separately; passing a recording factory is not capability advertisement.
