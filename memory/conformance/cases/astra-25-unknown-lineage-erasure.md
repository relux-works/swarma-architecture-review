# ASTRA25-09: unknown lineage retains its known erasure lower bound

Status: R7-038 rejected as a normative defect and retained as regression coverage.
Original package `0.2.1-draft` at `f31d58f`; current fixtures explicitly migrated to
`0.2.2-draft`, adding private/read erase receipt context with unchanged expectations.
Owner: astra-25.

## Clause and separating input

Kernel 7.1 and K-DISC-1 distinguish a model's citations from integration-supplied
inputs. An incomplete integration fact yields `lineage: unknown`, while its
known lower-bound inputs still constrain retention and erasure. K-ERASE-1/3
require transitive closure and forbid current-generation writes from erased
inputs. This combines the v0.2 lineage delta with S20/S26; the earlier owned
late-writer case used complete lineage only.

```text
A and independent B are admitted private inputs.
U has lineage=unknown; its trusted incomplete model fact lists known input A.
A's payload and U's cache are reachable controlled custody sinks.
Erase A; closure must also fence U and purge its cache.
Then admit D at the NEW current disposition generation:
  D proposes lineage=[]; the integration fact is incomplete with known input A.
```

| Observation | Unknown treated as no traversable inputs | Known lower bound retained |
| --- | --- | --- |
| Fenced record closure | A only | A and U |
| U cache | remains | purged |
| New-current-generation D | admitted | erasure_fenced, no write |

The recommended second reading is already explicit in the package. The first is
an implementation risk at the intersection of two independently implemented
features; it is not claimed to be an equally valid reading of the complete prose.
The fact's inputs override D's empty cited lineage; copying the new generation
does not grant permission to reintroduce erased content.

## Positive control and execution

[`astra-25-unknown-lineage-erasure.vector.json`](astra-25-unknown-lineage-erasure.vector.json)
checks closure, complete custody purge and exact fenced refusal. Its
[`independent-control`](astra-25-unknown-lineage-erasure-independent-control.vector.json)
changes only D's trusted known input to B and expects an admitted private unknown
record. It does not authorize audience publication or claim complete lineage.
The original A/U erasure still completes. Thus rejecting every unknown record
cannot satisfy the pair. Both use an initial-cut query of A; erasure must remain
in force even for that historical query.

The package evaluator passes both exact traces; the source evaluator currently
reports erase unsupported. All fifteen owned fixtures structurally validate.
Code/input hashes and exact results are in
[`astra-25-evaluator-results.json`](astra-25-evaluator-results.json), runs
`astra23-phase2-unknown-erasure` and `astra22-phase2-unknown-erasure`.
This is modeled lineage/fence/custody behavior, not actual deletion evidence.
Keep the pair for the source implementation's phase-2 erasure run.

Judge event `$Gfb8hRoyoU6bjoszyLeRlFn2ss9BBGiDTXjcxGzfih8` independently validates
both original fixtures and exact package outcomes. No source ambiguity, new
architecture or package correction is required. The `0.2.2` owned migration run
retains both package passes and explicit source unsupported results.
