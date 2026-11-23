# Experimental UEOT Runtime MVP — execution

This is **new exploratory code**, not recovered UEOT V1.0 reference implementation. All fixtures are synthetic. It does not implement the frozen full schema, approvals, security, audit persistence, industrial interfaces or nuclear engineering validation.

Requirements: Python 3.10+; no third-party packages.

Run from repository root:

```bash
python3 -m unittest discover -s tests -v
```

## Finding coverage caveats

- F-R2-001 STOP target: basic graph exclusion test.
- F-R3-001 temporal identity: half-open boundary and overlap test.
- F-R3-002 Basis conflict: basic conflict test.
- F-R3-003 authority: **only missing-authority gate**, not two competing valid authorities.
- F-R3-004 configuration ambiguity: two-branch ambiguity test.
- F-R3-005 temporary modification: **structural placeholder only**, no real temporal Basis lifecycle behavior.

These tests have not been executed by GitHub in this commit. Even a future PASS would establish only this synthetic implementation's behavior, not official UEOT Conformance or Pilot safety.

## Required hardening

Add a real authority precedence/conflict resolver, temporal TemporaryApplicableBasis semantics, graph typed relation profiles, persistence, snapshot consistency, audit, identity/authorization, evidence access, formal schema and independent oracle evaluation.
