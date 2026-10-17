# Source-derived evaluator — astra-22

This independent Python standard-library model was written without reading
`memory/spec/`. Its only semantic sources were kernel v0.2, the support-semantics
companion and the bounded-evidence design at `6d14828`. `evaluator.py` began as the
source baseline at `4d4ef45`; judge-classified corrections are tracked in
`DIVERGENCES.md`; the future package adapter must map syntax without learning
answers from a vector's expected output.

The model implements signed finite AND/OR support, qualified premises, distinct
completeness and explanation limits, authorized logical work, temporal/mode/pin
applicability, root-origin sets, synthetic admission/sequence/refusal behavior,
authority-ordered currentness, declared incompatibility without signed opposition,
basic audience handles/redaction and exclusion, lineage constraints, scoped declassification,
delivery rechecks, immutable snapshot values and synthetic erasure fences.

## Normalized model boundary

The source documents deliberately leave concrete wire grammar to R7. This model
therefore takes already-admitted normalized assertions, roots, rules and sources.
Exact version references are unique IDs in this representation; a wire adapter
must preserve version distinctions when generating these IDs. Unknown package
operations will be unsupported rather than approximated as successes.

Assertions carry `id`, `issuer`, `subject`, exact `schema`, `perspective`, `slot`
and optional temporal/disclosure metadata. Roots carry an explicit signed target,
qualification and exact pins. Sufficient rules are checked ground conjunctions;
alternatives are disjunctions. `Memory` models synthetic state only; it does not
write any external authority, journal, publisher or retained payload store.

## Source-level choices to scrutinize in package comparison

- A finite pass orders claims topologically, roots in normalized input order,
  and same-conclusion rules in input order. Root and rule budgets are separate.
  The source has no closed numeric-work-unit or traversal-order grammar.
- A clean witnessed path takes precedence over a conflicted alternative.
  Without a witness, premise quality is `not_fully_checked`. After R7-012,
  authorized unavailable source associations remain `prior_assessment_only`;
  `resolvable_now` is vacuous only when no unavailable association exists.
- Root qualifications default to semantic review, exact test result, formal
  entailment, independent attestation and direct declaration. The supplied
  evidence policy can narrow/replace this list. Documentary/signature checks
  alone are not semantic roots under the default policy.
- A missing freshness horizon is `not_applicable`; at or after an explicit
  horizon the item is stale. Valid intervals are half-open. Normalized times must
  have comparable precision and representation; the model does not invent them.
- Complete evaluation is over registered authorized dependencies only.
  Corpus coverage defaults to `unknown` and needs an explicit declared value.
- Independent origin identity survives copies; the model returns a root set,
  not a confidence score. It never turns witness counts into decision authority.
- The literal snapshot placeholder represents a predeclared normalization of
  unrelated fresh handles. It is not a handle generator, distribution test,
  pagination implementation, timing claim or deployment security qualification.
- Admission supports exact retry identity and explicit assertion replacement.
  Other wire-level revision event shapes need an explicit mapping or a reported
  unsupported result; historical bytes are never changed.
- Erasure models content-dependency reachability and refusal, not actual purge
  completion across sinks/backups. No managed deployment is installed or tested.

These choices are published before package intake. Any mismatch remains a
divergence until classified by the judge; an adapter must not silently change
them to obtain a passing score.

## Tools and evidence

Run the source controls from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 memory/conformance/impl-astra-22/source_checks.py
```

The controls use `unittest` from the Python standard library. Post-package wire
controls run with `python3 memory/conformance/impl-astra-22/adapter_checks.py`. Each test states
its claim and material limits. They include nearby positive/negative examples,
post-refusal state comparisons and bounded comparator/JSON-parser control plants.
Logs are under `.temp/astra-22/`; progress is in `WORKLOG.md`.

After PACKAGE LANDED, the wire adapter and runner were added:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 memory/conformance/impl-astra-22/run_vectors.py
```

This loads every package vector and writes `RESULTS.md` and `RESULTS.json` in this
directory. `--package PATH` selects a different package checkout; `--out PATH`
selects the report destination. `--vectors memory/conformance/cases` runs a
separate adversarial inventory; choose a distinct output path for that report. `runs/0.1.0-first.*` preserves the first comparison.
The executor receives no vector identifier or expected answer. Unsupported paths
are explicit, and every supported response and postcondition is compared exactly
after only the vector's declared normalization. Divergences are documented before
fixing them. The initial adapter deliberately exposes the frozen core's gaps.

Git publishes signed commits to main as required by the mission;
a2a supplies rounds, divergence reports and PARK coordination.

## Current coverage limits

The package adapter now maps read-only recall/capture, ordinary and authority
currentness, declared incompatibility, freshness, basic audience aliases and
exclusion. Independent wire admission, raw admission and CAS revisions now run
through `transactions.py`; `transaction_checks.py` contains atomicity controls.
The first 0.2.1 run exposes the missing self-declaration identity gate (ASTRA22-05),
which is preserved for classification. It still explicitly rejects unsupported
erasure/publication transaction wire operations,
exact proof-path enumeration, dynamic dirty closure, live multi-owner release
checks and unconfirmed imported-publication currentness. RESULTS.md lists the
precise per-vector boundaries; source model unit controls alone do not count as
package-vector passes. Original frozen evidence is retained unchanged.
