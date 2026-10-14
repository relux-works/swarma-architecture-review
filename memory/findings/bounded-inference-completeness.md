# Boundaries on computation need an explicit completeness result

- Lens: semantics and formal core.
- Author: astra-03 (five 1).
- Status: proposed.
- Confidence: high.

## Problem

The base explicitly bounds ATMS explanations and affected-subgraph work, but its example `recall` result has only a four-valued epistemic status. It does not distinguish a complete lack of support from an unfinished search, nor explanation-display truncation from incomplete status computation.

With `(A AND B) -> C` and `(D AND E) -> C`, withdrawing B does not remove C's other support. If a budget retained or traversed only the first path, reporting C as unsupported is wrong. Retaining an old supported label after a cutoff can also be wrong. Finding both positive and negative witnesses establishes conflict even when further enumeration is incomplete.

## Evidence

- `memory/inputs/SKETCH.ru.md`, part 1 §4 (bounded ATMS) and §6 (`recall` example); part 2 §§5,8 already limit invalidation to registered dependencies and postpone full ATMS. This finding narrows an underspecified contract; it does not accuse the base of promising semantic omniscience.
- de Kleer, *An assumption-based TMS*, https://dekleer.org/Publications/An%20Assumption-Based%20TMS.pdf , pp.144–145 (label invariants), p.152 (intermediate label completeness), accessed 2026-10-14. The complete-label invariant is not a property of an arbitrary interrupted update.
- Concrete outcomes S04–S07,S17 in [semantics companion](../designs/bounded-support-semantics-astra-03.md).

## Proposed change

Return positive and negative witnesses with separate per-polarity evaluation completeness, snapshot/freshness and source coverage. Keep explanation enumeration limits independent. Mark affected results dirty atomically before delayed recomputation, and never serve a stale label as current. Bound guarantees to the registered, authorized graph; never equate that with all natural-language implications.

## Rubric rows affected

R6 (honest epistemics), R7 (testability), R8 (useful bounded first slice).

## Confirmed by

- astra-06, five 2, event `$6jxHbLsDl-Lkefu_yhwLyBeLhFIr4aFr8vtcXgP56qg` in `f-bounded-inference`; independent initial verdict frozen before reading five 1. Explicitly confirmed the counterexample and distinguished rendering from computation limits.
- Candidate event: `$OBDtFuUr2q0hTYIsRiTtWssnyOD-dUIel-auBGhnyYU`.
