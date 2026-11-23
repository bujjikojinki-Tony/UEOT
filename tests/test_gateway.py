"""Synthetic integration tests for gateway; no formal UEOT conformance claim."""
import unittest
from runtime.gateway import SyntheticGateway


def fixture():
    return SyntheticGateway(
        assignments=[{"code": "RIS-P001", "objectId": "SSC-001",
                      "start": "2026-01-01", "end": None}],
        bases=[{"id": "BL-03", "objectId": "SSC-001", "configuration": "M6",
                "approved": True, "start": "2026-01-01", "end": None}],
        assertions=[{"objectId": "SSC-001", "property": "RatedFlow", "role": "Design",
                     "configuration": "M6", "basis": "BL-03", "value": 505,
                     "unit": "m3/h", "evidence": "EV-01", "authority": "AU-01",
                     "start": "2026-01-01", "end": None}],
        evidence={"EV-01": {"version": "1", "approved": True}},
        authorities={"AU-01"},
        profiles={"P-01": {}},
        edges=[("SSC-001", "VALVE-01"), ("VALVE-01", "STOP-01")],
        stop_targets={"STOP-01"},
    )


class GatewayTests(unittest.TestCase):
    def query(self, gateway):
        return gateway.query("RIS-P001", "RatedFlow", "Design", "M6",
                             "2026-06-15", "P-01")

    def test_success_is_synthetic_candidate_not_engineering_approval(self):
        result = self.query(fixture())
        self.assertEqual(result["decisionState"], "SYNTHETIC_CANDIDATE")
        self.assertEqual(result["data"]["value"], 505)
        self.assertTrue(result["syntheticOnly"])
        self.assertTrue(result["auditRef"])

    def test_missing_evidence_blocks(self):
        g = fixture()
        g.evidence.clear()
        self.assertEqual(self.query(g)["reason"], "EVIDENCE_MISSING")

    def test_basis_conflict_blocks(self):
        g = fixture()
        g.bases.append({**g.bases[0], "id": "BL-04"})
        self.assertEqual(self.query(g)["reason"], "BASIS_CONFLICT")

    def test_authority_conflict_blocks(self):
        g = fixture()
        g.assertions.append({**g.assertions[0], "value": 510, "authority": "AU-02"})
        g.authorities.add("AU-02")
        self.assertEqual(self.query(g)["reason"], "MULTI_AUTHORITY_CONFLICT")

    def test_access_denied_blocks(self):
        g = fixture()
        result = g.query("RIS-P001", "RatedFlow", "Design", "M6",
                         "2026-06-15", "P-01", permitted_evidence=False)
        self.assertEqual(result["reason"], "EVIDENCE_ACCESS_DENIED")

    def test_unknown_object_no_fallback(self):
        g = fixture()
        result = g.query("UNKNOWN", "RatedFlow", "Design", "M6",
                         "2026-06-15", "P-01")
        self.assertEqual(result["reason"], "IDENTITY_NOT_FOUND")

    def test_missing_configuration_blocks(self):
        g = fixture()
        result = g.query("RIS-P001", "RatedFlow", "Design", None,
                         "2026-06-15", "P-01")
        self.assertEqual(result["reason"], "CONFIGURATION_REQUIRED")

    def test_stop_and_human_review(self):
        g = fixture()
        result = g.impact("SSC-001")
        self.assertNotIn("STOP-01", result["data"]["potentialImpactSet"])
        self.assertIn("STOP-01", result["data"]["graphReachability"])
        rejected = g.impact("SSC-001", ["VALVE-01"])
        self.assertEqual(rejected["reason"], "HUMAN_APPROVAL_MISSING")
        approved = g.impact("SSC-001", ["VALVE-01"],
                            [{"objectId": "VALVE-01", "approved": True,
                              "approverType": "HUMAN"}])
        self.assertEqual(approved["data"]["confirmedImpact"], ["VALVE-01"])

    def test_audit_excludes_sensitive_values(self):
        g = fixture()
        self.query(g)
        self.assertEqual(len(g.audit), 1)
        self.assertNotIn("505", repr(g.audit))
        self.assertEqual(g.audit[0]["operation"], "query")


if __name__ == "__main__":
    unittest.main()
