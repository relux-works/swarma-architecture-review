# astra-23 package-only evaluator

Independent Python standard-library implementation of `memory/spec/`. The original
blind first run was committed before source designs or divergence intake. Runtime
behavior is derived from the package; no other evaluator implementation was read.
The engine receives only initial state, operations and query. Expected outputs,
vector IDs, forbidden predicates and normalization belong exclusively to the runner.

`engine.py` models atomic transitions and shared issuer-local authority order;
`evaluator.py` computes bounded evidence; `disclosure.py` handles protected lineage
and grants; `common.py` implements closed grammar, exact refs and JSON boundaries.
Initial snapshots are admitted synthetic inputs under K-API-2, not production intake.

## Current evidence

- Canonical **0.2.6-draft**, package `77b951eb86d5ba9198921d058930884918a39942`:
  `RESULTS.md/json` records 66 semantic passes, zero failures or unsupported;
  eight deployment fixtures are unsupported.
- Historical **0.2.5-draft**, package `6a04e8cfb1490569cd1de7468d2085dd4840cf51`:
  `SUPPLEMENTAL.md/json` records 68 unchanged semantic passes and one deployment
  unsupported, using the current runtime and the exact old grammar. This is a
  separate regression denominator, not additional canonical 0.2.6 coverage.
- Product controls: four new 0.2.6 groups plus 30 legacy groups pinned to 0.2.5;
  four independent checker groups also pass. `D009-CONTROLS.json` records module
  hashes, 64 three-event graph variants, 125 validated state instances (74 unique),
  and 25 native write observations, including 11 atomic exact refusals.

K-REV-3 restricts the canonical event graph by protected authority-event issuer
before reachability. Assertion-free intermediates count; foreign paths are never
contracted and cannot veto an all-issuer path. Currentness, revision CAS head and
strict replacement succession share this relation. Exact authorized replay retains
its original priority and receipt. Other retention, disclosure, erasure, restore and
late-writer behavior remains covered by the canonical and historical regressions.

## Tools and commands

Python 3 and Git are the only tools needed for local execution. From the repository
root, create the exact legacy package snapshot used by the historical tests:

```sh
python3 -B - <<'PY'
from pathlib import Path
import subprocess
commit = '6a04e8cfb1490569cd1de7468d2085dd4840cf51'
root = Path('.temp/impl-astra-23/package-0.2.5')
for name in subprocess.check_output(
        ['git', 'ls-tree', '-r', '--name-only', commit, '--', 'memory/spec'], text=True).splitlines():
    target = root / name
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(subprocess.check_output(['git', 'show', commit + ':' + name]))
cases = root / 'memory/conformance/cases'
cases.parent.mkdir(parents=True, exist_ok=True)
if not cases.exists():
    cases.symlink_to(Path('memory/conformance/cases').resolve(), target_is_directory=True)
PY
python3 -B memory/conformance/impl-astra-23/test_semantics.py --spec-root .temp/impl-astra-23/package-0.2.5/memory/spec
python3 -B memory/conformance/impl-astra-23/test_authority.py
python3 -B memory/conformance/impl-astra-23/test_controls.py
python3 -B memory/spec/checks/validate.py
python3 -B memory/conformance/impl-astra-23/run_vectors.py --package-commit 77b951eb86d5ba9198921d058930884918a39942
python3 -B memory/conformance/impl-astra-23/run_vectors.py --spec-root .temp/impl-astra-23/package-0.2.5/memory/spec --package-commit 6a04e8cfb1490569cd1de7468d2085dd4840cf51 --vector-root memory/conformance/cases --output memory/conformance/impl-astra-23/SUPPLEMENTAL.md
```

The legacy test CLI accepts `--spec-root` explicitly because its author-owned
supplemental expectations still name 0.2.5. Running those comparisons against 0.2.6
without migration reports version differences. No fixture or expected value is
rewritten by the option. The source cases remain read-only, including through the
scratch symlink. Current 0.2.6 behavior is checked by all canonical vectors and the
new authority controls. Logs and frozen inputs live under `.temp/impl-astra-23/`;
Git signed commits preserve reviewed artifacts, and a2a carries collective notices.

The runner writes exact Markdown/JSON reports beside this README; `--output PATH.md`
selects a separate report. `--spec-root PATH --package-commit SHA` pins a package.
`--vector-root PATH` selects supplemental `*.vector.json` files. Wrong-profile
supplemental inputs are unsupported, with no implicit conversion. A nonzero exit
means an execution or exact comparison failed, not a successful refusal test.

## Audit hash format

`D009-CONTROLS.json` hashes UTF-8 compact sorted-key JSON after a lossless native
encoding: every dictionary becomes `{"map": [[encoded_key, encoded_value], ...]}`
with pairs sorted by encoded-key JSON; sets become `{"set": [...]}` sorted by
encoded-item JSON; tuples become `{"tuple": [...]}`; lists recurse in order;
primitives remain unchanged. `ensure_ascii=False` applies throughout. SHA-256
uses the resulting UTF-8 bytes. The artifact specifies the same format explicitly.

No nonce is normalized in these native hashes. Initial-state and operation-input
hashes reproduce when inputs match; post-write hashes containing generated handles
are local to that execution. Native before/after equality proves the recorded
atomic refusals and replays. This differs from canonical report comparison, which
normalizes only the vector-declared handle paths.

## Comparison and preserved first observations

Every operation response, final result and postcondition is compared with typed
JSON equality and closed output schemas. Only declared fresh-handle paths are
normalized, after checking syntax, equality and distinctness. Forbidden predicates
and paired-output equivalence remain active. No random-distribution or timing
qualification is inferred from these checks.

`RELEASE-0.2.6-FIRST.md/json` preserves unchanged runtime `104fbe8`: 64 semantic
passes and S34/S39 failures before the issuer-local correction. The first is signed
at `1be6026`. The new product controls independently produced eight intended old-
runtime failures, without setup errors. `FIRST-RUN`, earlier `RELEASE-*-FIRST` and
`PHASE2-*-FIRST` reports remain immutable. Their recorded package/runtime revisions
are required for reproduction; current outputs must not replace historical failures.

[WORKLOG.md](WORKLOG.md) records rounds, test boundaries and independent review.
[DIVERGENCES.md](DIVERGENCES.md) records classifications and corrections. Semantic
simulation does not qualify real authentication, physical purge, outside-domain
witness verification, delivery isolation or hostile writers. No servers, external
execution, packages or child agents are used.
