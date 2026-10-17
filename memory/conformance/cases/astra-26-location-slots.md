# ASTRA26-04 — current location must not replace residence

Status: executable regression challenge, not an observed spec defect.
Seat: astra-26. Package: `0.1.0-draft` at `0ef608a`.

## Clauses and two readings

Kernel §§4 and 11.2 and package K-DOM-2/3 define location as single-valued
**per kind**, with incompatibility only inside the same slot. A convenient flat
profile implementation could instead treat `single` as one location per subject,
then choose the later record or flag different places as incompatible.

The correct reading uses the exact `kind` slot. Residence and present location
can coexist even for the same issuer, subject, perspective and valid interval.
Neither is an update to the other. Cardinality does not itself grant replacement.

## Minimal input and outputs

[Complete fixture](astra-26-location-slots.vector.json): two synthetic assertions
under `schema:location@1`, both confirmed at `2026-10-17T00:00:00Z`:

| Assertion | Kind / slot | Value | Admission sequence |
| --- | --- | --- | ---: |
| `rec:current-location@1` | `current` / `["current"]` | `synthetic-city-B` | 1 |
| `rec:residence-location@1` | `residence` / `["residence"]` | `synthetic-city-A` | 2 |

Both are queried privately at the same cut and valid time. Expected: two current
items, both fresh through October 24, no incompatibility, no evidence opposition,
no historical replacement and no `ambiguous_current`. Under the flat reading,
one item disappears or the two values conflict merely because both are locations.

This provides two valid single-slot controls together: changing the slot prevents
the cross-value conflict. P04 supplies expiry controls; P10 supplies the separate
compare-and-set requirement. The case does not claim that same-slot unreceipted
branches may be admitted as a valid initial state.

## Evidence

Shape, domain equality, references, normalization and forbidden predicates pass
the package checker functions. The frozen astra-22 core at `4d4ef45`, through its
first adapter at `0216fbb`, explicitly reports this fixture **unsupported**:
`Frozen core has no cross-assertion incompatible_with computation`. This is not
a passing test or a package defect. Exact local run evidence is in the seat
directory `.temp/r7-astra-26/owned-cases-astra22-01.json`.

Recommendation: preserve the package's existing slot semantics and use this
fixture to catch a flat-profile implementation when the evaluators support it.

## Follow-up

Judge R7-016 rejected a spec-defect allegation and retained this regression.
The package-only evaluator's first code at `0008dc3` detected an authoring error
in this fixture: it had inherited P04's positive support in expected output even
though this case contains only two assertions and no assessment. Corrected both
support channels to `not_found`, empty qualifications/roots and zero roots under
K-EVAL-1; added forbidden positive witnesses. This was a case-author error, not an
evaluator defect. The corrected fixture passes the independent evaluator exactly.
The original mismatch and corrected run are retained locally as
`owned-cases-astra23-01.json` and `owned-cases-astra23-02.json`.

The current fixture is migrated to `0.2.0-draft` with exact direct-lineage facts,
empty release decisions and exclusion sets; these additions do not change the
location-slot expectation. Current-version execution remains a separate check.
