# UEOT Experimental MVP — Integrated Gateway & Browser

## Scope

This code is an **experimental synthetic-only implementation**. It is not the official frozen UEOT Runtime and has not passed industrial or regulatory validation.

- `runtime/ueot_runtime.py`: six basic reference functions.
- `runtime/governance.py`: authority conflicts, temporary basis and human review gates.
- `runtime/gateway.py`: integrated query/impact entry points and in-memory metadata-only audit.
- `tests/`: synthetic unit and integration tests.
- `browser/index.html`: standalone offline synthetic object browser with PBS/FBS/GBS/WBS views.

## Run

Python 3.10+; no third-party dependencies:

```bash
python3 -m unittest discover -s tests -v
```

Open `browser/index.html` in a browser for a **static demonstration**. The HTML is not connected to the Python gateway. It has no production data, authentication or approval workflow.

## Integration query path

`resolve_profile → resolve_object → get_basis → assertion selection → get_evidence → resolve_authority → synthetic answer + auditRef`

Failure conditions block a definitive claim. Successful synthetic responses deliberately use `SYNTHETIC_CANDIDATE`.

## Known limitations

1. Audit records are in-memory and not tamper evident.
2. There is no HTTP API, durable storage, authorization service or cross-source snapshot consistency.
3. Browser is static and does not execute actual engineering queries.
4. Evidence validation checks reference presence only, not signatures, source integrity or engineering approval.
5. Basis handling is simplified and is not a full UEOT BasisConsistency implementation.
6. Authority precedence is a demonstration, not a verified domain profile.
7. Graph traversal uses untyped edges and simplified stop-target semantics.
8. No formal 12-axiom audit, independent oracle pilot, production SLA or safety certification.
9. The CI run status must be checked independently; a committed workflow is not proof of passing tests.

## Next acceptance milestone

Implement a read-only local HTTP adapter for the synthetic gateway, integrate Browser against its response contract, and add persisted audit and role-based evidence access. Freeze a test commit and attach actual run logs before any PASS claim.
