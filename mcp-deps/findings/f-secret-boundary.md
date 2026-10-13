# Literal zero-secret-byte access conflicts with native inspection

- Lens: authentication and trust.
- Author: astra-02 (ivmbp).
- Status: proposed.
- Confidence: high for the original contradiction; the convener has explicitly amended rubric E3.
- Base: `BASE-DESIGN.md`, Authentication and elegance claims; mission rubric E3.

## Problem

The base promises that the manager never reads, stores, forwards, or tests a credential, while reusing native configuration inspection. Native MCP configuration may contain credential literals, including inside the entry being checked. Reading and parsing the file contacts those bytes even if the checker never resolves a variable, authenticates, logs the value, or starts a server. A static or read-only check does not prove the literal E3 property.

The same precision is needed at the process boundary: an environment launcher intentionally transfers selected operator values to its child. A claim about the dependency checker must not silently become a claim about every Curator component.

## Evidence

Read-only source checkpoints: curator-spec `a9c03be237b723b5bf87aed070165ad6f68b2586`; curator `5234cf38833554542e68afade15951c6e56ed89e`.

- `profiles/manager.md:1085–1109` requires native configuration inspection, including mixed user files such as `~/.claude.json` and `~/.codex/config.toml`.
- `internal/mcp/mcp.go:240–288`, `entriesInFile`, reads the complete native file with `os.ReadFile` and unmarshals the document before selecting MCP entries.
- `inputs/csk-mcp-design-proposal-v1.md`, opening boundary and §§4–5, explicitly recognizes foreign credential literals in existing mixed files and describes private byte preservation. It does not claim those files are secret-free.
- `protocol/environments.md` §§5.8, 7.8, 10.3 distinguish names in manager-produced artifacts from operator values supplied at launch. The manager's declaration renderer carries names, not values; that does not establish zero byte contact for the unrelated native-file reader.

No actual native user configuration or credential was read for this finding. Evidence is specification text, source code, and supplied design inputs.

## Proposed change

Choose and name the guarantee explicitly:

1. **Literal E3:** inspect only sufficiently trusted secret-free metadata/managed records; opaque or potentially credential-bearing native cases remain unknown unless the operator supplies a scoped reliance assertion. Do not introduce an in-manager sanitizer and claim it never received the original bytes. This trades away automatic native observation and requires its own practical boundary proof.
2. **Practical secret non-management:** forbid credential-store access, secret lookup/expansion, auth execution, credential-bearing probes, secret logging/persistence/egress, and untrusted helper execution, while admitting tightly bounded private handling of foreign native-file bytes. Keep extraction/output limited to validated public metadata; failures must not echo raw documents or exception payloads. State that this is weaker than literal E3 and needs explicit acceptance before a literal elegance claim can be made.

No auth broker or manager-side MCP proxy is needed for either choice. Both keep authentication with the native client/operator. Neither may report authenticated or connected from configuration evidence.

## Rubric disposition

Review-repository commit `534e3849b3fca07c2479222886aacb34808e5bcc` amends MISSION-MCP E3 explicitly: bounded handling of foreign bytes is evaluated under an operational non-management guarantee, with no raw foreign argv/URL/env persistence, logging, or surfacing. The mission requires original and amended scores where they differ, and proof cites the amended row. This resolves the evaluation ambiguity prospectively; it does not make the base's original zero-read sentence true or eliminate the need to specify the bound. Other fields of a native config are not automatically public merely because their names are not `token` or `password`.

## Rubric rows affected

- **E3:** unrestricted native inspection cannot receive 2 under the literal wording; operational non-management is a separately labelled interpretation, not a silent rubric substitution.
- **E4:** literal non-contact limits automatic native coverage; explicit reliance can preserve usability but is not an observation.
- **E6/E7:** status and conformance must distinguish observation, assertion, and authentication not checked.

## Conformance cases to specify

- Mixed native document contains a literal credential in an unrelated field: no raw config, value, or secret-bearing parser diagnostic reaches output, logs, journals, or a remote service under the practical contract; the literal contract does not inspect the file.
- Auth-required endpoint is present: no HTTP request or native authentication command is issued by checking.
- Operator supplies an opaque-provider assertion: record reliance only; do not report observed configuration, current connectivity, or verified authentication.

## Confirmed by

- ivmbp astra-01, independent source confirmation: a2a event `$3j4jMx8hpycs3NgwhjyqVMOOgYyVA6VMacPl4B9jcjs`, topic `f-secret-boundary`.
- ivmbp astra-03, event `$BNNLe-TsyNFNmYouPQROjOUFC0OloE7afJOhQzCxCC4`.
- ivmbp wonder-02, rubric-seat independent confirmation, event `$SNRLfvcWtHxonUgOrpTBaUZnHD9ClzN9jCkBSf7RasI`. The seat proposes dual literal/operational scores; that is not an operator change to the mission rubric. Its literal numeric score is 1 while this author's literal score is 0 because the rubric's zero endpoint says the manager touches values. Both agree that unrestricted native inspection cannot earn literal 2.
- Candidate event: `$ShG0Qte90UNwUs9iIyXopnfyZQ2xy2wuUjCy6pzRMkk`.
- Different-host adversarial confirmation remains pending. The explicit rubric amendment is recorded above.
