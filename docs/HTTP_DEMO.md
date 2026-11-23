# Local Browser ↔ Runtime HTTP demo

**Experimental synthetic-only code. Not an official UEOT V1.0 implementation.**

From the repository root, with Python 3.10+:

```bash
python3 -m unittest discover -s tests -v
python3 -m runtime.http_demo --port 8765
```

Open **http://127.0.0.1:8765/** in a browser. Do not open the HTML using `file://` if you want API integration. Do not deploy this server to the public internet.

The Browser requests:

- `GET /api/objects` — synthetic catalog with PBS/FBS/GBS/WBS fields.
- `GET /api/query?code=RIS-P001&property=RatedFlow&configuration=M6&validAt=2026-06-15` — identity, approved basis, evidence and authority gate.
- `GET /api/impact?root=SSC-001` — GraphReachability vs PotentialImpactSet, excluding STOP targets.

All POST requests are rejected with HTTP 405. The server binds to **127.0.0.1** only. Audit references are generated in memory, not persisted or tamper-evident.

**Important limitations:** Browser currently uses hard-coded synthetic query context; no login or RBAC; evidence presence is not cryptographic verification; no real engineering configuration or current time selection; no production approvals; no durable audit; no live SSC data; no real UEOT conformance certification.

The source files and tests were committed to GitHub, but the CI outcome must be checked independently. A successful synthetic test run is not a nuclear engineering validation.
