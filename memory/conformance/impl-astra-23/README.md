# astra-23 package-only evaluator

Independent Python standard-library implementation of `memory/spec/`. The first
implementation and full report are produced before source-design, companion,
notes, inputs, other-evaluator, ledger or divergence-topic intake. It neither
imports the package's authoring helpers nor selects behavior by vector IDs.

`engine.py` accepts only the initial state, operations and query. It models atomic
state transitions; `evaluator.py` computes authorized bounded evidence; `common.py`
handles exact references, canonical JSON, schema shapes and refusals. The runner
alone loads expected outputs and normalization. Initial snapshots are trusted
admitted synthetic inputs, as required by K-API-2; this is not a production intake
validator or a protected deployment.

## Tools and commands

Python 3 is the only runtime dependency. Run from the repository root:

```sh
python3 -B memory/conformance/impl-astra-23/test_controls.py
python3 -B memory/conformance/impl-astra-23/test_semantics.py
python3 -B memory/conformance/impl-astra-23/run_vectors.py
```

The runner reads every JSON vector under `memory/spec/kernel/vectors/` and writes
`RESULTS.md` and `RESULTS.json` here. Each semantic vector executes from a fresh
deep-copied state. Every deployment vector is explicitly unsupported for actual
qualification; simulated transitions cannot prove host, transport or custody
boundaries. A nonzero runner exit means at least one execution or comparison fails.

For a pinned package snapshot, supply `--spec-root PATH --package-commit SHA`.
`--output PATH.md` keeps additional versioned reports separate. `FIRST-RUN.md`
and `FIRST-RUN.json` preserve the independent baseline. Git records and publishes
signed seat-owned artifacts; a2a carries round markers and divergence notices.
Readiness/check logs and the initial package copy live in `.temp/`.

## Exact comparison

All operation results, final results and postconditions are compared recursively
with typed JSON equality. Handle normalization replaces only declared paths;
syntax, equality, distinctness, forbidden predicates and equivalent-output pairs
are checked. Output shapes are checked against the published closed schemas.
All exact field differences are retained in both reports. The bounded checker
controls plant semantic, forbidden-effect and equality violations with valid
controls. A single run does not prove uniform randomness or timing isolation.

## Scope and limitations

The finite fixture API is implemented without external execution, source reads,
network access or live publication. Policy facts are admitted test inputs. Results
report observed conformance, including defects and unsupported qualification;
they do not establish service security. Known discrepancies are retained for judge
classification before semantic implementation changes.

The current evaluator also implements the 0.2 integration-lineage grammar,
per-owner declassification decisions/revocation, pinned captured-item delivery,
and versioned projection exclusions. Clause-derived product controls include
missing-owner atomic rejection, release/revoke delivery, integration input
completeness, exclusion isolation and the B01 missing-fact regression witness.
`DIVERGENCES.md` records judge classifications and pending package discrepancies.

To run independently authored cases without merging their totals into canonical
conformance, use:

```sh
python3 -B memory/conformance/impl-astra-23/run_vectors.py --vector-root memory/conformance/cases --output memory/conformance/impl-astra-23/SUPPLEMENTAL.md
```

A case outside the selected package's closed grammar is reported unsupported;
select its original package with --spec-root to run it without conversion.

The 0.2.1 evaluator scopes unresolved dirty causes through authorized pre-revision
impact paths, requires explicit self-declaration identity bindings, and applies
publication currentness only to authorized publication-source associations.
Explicit-target history is restricted to the selected sequence identities.
RELEASE-0.2.1-FIRST preserves the pre-fix R7-024 report; FIRST-RUN preserves the
original package-only independence baseline. Current canonical results are 57/57
semantic with eight deployment cases unsupported; fourteen controls pass. The
source-state precedence control covers resolved, policy-denied, lost and empty
source lists without upgrading evidence, including real current-source exhaustion.
