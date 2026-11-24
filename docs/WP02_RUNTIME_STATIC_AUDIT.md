# WP-02 Runtime pre-conformance static audit
Date: 2026-11-24. Scope: four experimental Python modules. Basis: formal release note, not the missing normative masters. No execution performed.

| ID | Severity | Source | Static finding | Proposed regression |
|---|---|---|---|---|
| A01 | High | ueot_runtime.py: traverse_graph | Reachability stops at STOP nodes, conflating unrestricted reachability with propagation. Cycles can admit root. Edges untyped. | A→STOP→B; cycle A→B→A; typed relation profile |
| A02 | High | gateway.py: query | Calls get_basis rather than resolve_applicable_basis; simultaneous design and temporary bases block as conflict. | active temporary plus design; expiry restores design |
| A03 | High | governance.py: resolve_applicable_basis | Temporary basis can resolve without design; no property scope or explicit applicability mapping. | out-of-scope temporary; missing design; unknown basis type |
| A04 | High | gateway.py: query / get_evidence | Evidence existence only; no validity, approval, source integrity or authority scope. | expired/revoked evidence and wrong authority scope |
| A05 | High | ueot_runtime.py: get_assertions | Direct legacy function can return definitive synthetic assertion without basis or context validation. | direct call with absent basis, missing context |
| A06 | High | gateway.py: impact | No profile or configuration/time context; caller-provided HUMAN string is not authenticated authorization. | fabricated approval; wrong configuration; missing profile |
| A07 | Medium | governance.py: resolve_authority / gateway.py | Profile winner selected but gateway reports evidence refs from all candidates, including losing contradictory claims. | two ranked conflicting assertions; separate supporting and rejected evidence |
| A08 | Medium | gateway.py: query | Governance escalation flattened to NO_DEFINITIVE_CLAIM; unresolved configuration has no candidate list. | assert escalation state and candidate configurations |
| A09 | Medium | ueot_runtime.py / governance.py / http_demo.py | Dates compared lexically without format validation; malformed dates can be accepted. | invalid date, missing date, boundary dates |
| A10 | Medium | gateway.py: _result / http_demo.py | Audit metadata only, no durable request context or snapshot; HTTP early rejection bypasses audit. | replay, restart, invalid input audit |
| A11 | Medium | ueot_runtime.py: resolve_object | Code-only lookup lacks namespace/source scheme; collisions across systems unresolved. | identical code in different namespaces |
| A12 | Medium | http_demo.py | Hard-coded profile and role; catalog independent from gateway; no authenticated access or request exception envelope. | catalog drift, malformed data, unsupported methods |

Severity is proposed engineering triage, not formal nuclear safety classification. A01 reachability semantics require confirmation against the missing master; root exclusion likewise requires explicit contract. A03 temporary applicability details require formal profile. All findings are static observations or proposed contract gaps, not executed failures.

## Finding mapping
F-R2-001: STOP target exclusion exists; A01/A06 remain.
F-R3-001: half-open comparison and ambiguity exist; A09/A11 remain.
F-R3-002: multiple active bases block; A02/A03/A05 remain.
F-R3-003: explicit precedence and tie gate exist; A04/A07/A08 remain.
F-R3-004: gateway blocks missing configuration; A05/A08 remain.
F-R3-005: separate helper exists but not integrated into query; A02/A03 remain.

## Audited blobs
- runtime/ueot_runtime.py: 750a8cb8d78db97ef7a6165cd1fcc7516a4f6f9f
- runtime/governance.py: eeba7f1463d9a4843a7737ab9d1f41ad2f06d967
- runtime/gateway.py: 19612d01fee56a5082ac175265b6e3adb86b381b
- runtime/http_demo.py: 9bd71dab7718c615d622216a5115c375643cce7b

## Exit decision
Static inventory complete for these four modules only. Formal Schema/API diff BLOCKED by missing masters. Regression execution NOT_VERIFIED. GO for WP-03 synthetic regression and remediation; NO-GO for formal or industrial acceptance. No runtime changes in this audit.
