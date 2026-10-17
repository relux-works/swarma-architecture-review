# astra-25 PARK note

Seat: `ivmbp_swarma-memory_astra-25`, disclosure and erasure adversary.
PARK: convener `ivmbp_swarma-memory_orch`, 2026-10-17T06:33Z, rounds event
`$698CuaDIUMf-DR-20AGkuMRnSJpo1SEQgXV9GHVW3hg`, completion checked at `1f92e91`.

**R7: 2/2.** The [final verdict](../verdicts/astra-25.md) records this seat's
12 cases, 34 exact fixtures (33 semantic, one deployment) and independent
correction checks. The [aggregate](../cases/astra-25-evaluator-results.json)
retains all 90 append-only run records, including original failures.

| Evidence | Final pin and outcome |
| --- | --- |
| Released package | `6a04e8c`, 0.2.5-draft; validator green |
| Source evaluator | Runtime `946cbd8`, report/test evidence `b8189ba`; 57/57 canonical, 68/68 supplemental and 33/33 owned semantic |
| Package evaluator | Runtime `104fbe8`; 57/57 canonical, 68/68 supplemental and 33/33 owned semantic |
| Judge closure / quiet review | `9d2cdd4` / `73408ec`; 47 fixed, 10 rejected, R7-055 owner-held, no open spec or implementation bug |
| Seat restore correction / final quiet review | `b949afb` / `2c6aae3`; original four recovery traces and three late-writer controls pass, full protected states verified |

Package's 30 product and four comparer controls were independently rerun by this
seat. Source coverage is 129 controls: 12 erasure groups rerun and 117 unchanged
controls retaining prior evidence, not a claim of a fresh full 129-control run.
All fixture inputs, native first-failure snapshots and prior run records remain
unchanged by parking. No new runtime or package change is included.

## Open threads at PARK

- **R7-055, owner decision only:** [cross-issuer predecessor ordering](../OWNER-QUESTIONS.md)
  remains held for Ivan. Its native separating pair has no chosen oracle and
  stays outside executable denominators. No authority choice or evaluator fix
  has been inferred from PARK.
- **Deployment:** all eight canonical and one supplemental deployment vectors
  remain unsupported by both readers. Synthetic checks do not qualify physical
  purge, real external witnesses, sink enforcement or deployment isolation.
- **Assigned work:** no open assigned bug, unclassified intake, correction or
  directed review remains. R7-058 is judge-closed at `104fbe8`; all original
  failures and subsequent correction evidence remain linked from the verdict.

This note and the verdict complete the seat's repository parking artifacts.
The accompanying signed publication is acknowledged in the rounds topic.
