"""Proposed synthetic regressions; must be executed in CI to claim results."""
import unittest
from runtime.ueot_runtime import resolve_object, get_basis, get_assertions, traverse_graph

class FindingTests(unittest.TestCase):
    def test_f_r2_001_stop(self):
        result = traverse_graph([("pump", "valve"), ("valve", "stop")], "pump", {"stop"})
        self.assertIn("stop", result["graphReachability"])
        self.assertNotIn("stop", result["potentialImpactSet"])

    def test_f_r3_001_half_open_and_ambiguity(self):
        a = [{"code": "RIS-P001", "objectId": "old", "start": "2026-01-01", "end": "2026-06-01"},
             {"code": "RIS-P001", "objectId": "new", "start": "2026-06-01", "end": None}]
        self.assertEqual(resolve_object(a, "RIS-P001", "2026-06-01")["objectId"], "new")
        a.append({"code": "RIS-P001", "objectId": "other", "start": "2026-05-01", "end": "2026-07-01"})
        self.assertEqual(resolve_object(a, "RIS-P001", "2026-06-01")["status"], "AMBIGUOUS")

    def test_f_r3_002_basis_conflict(self):
        b = [{"id": x, "objectId": "pump", "configuration": "M6", "approved": True,
              "start": "2026-01-01", "end": None} for x in ("BL03", "BL04")]
        self.assertEqual(get_basis(b, "pump", "M6", "2026-06-01")["status"], "BASIS_CONFLICT")

    def test_f_r3_003_authority_gate(self):
        a = [dict(objectId="pump", property="flow", role="Design", configuration="M6",
                  start="2026-01-01", end=None, evidence="E1", authority="A1", value=505)]
        self.assertEqual(get_assertions(a, "pump", "flow", "Design", "M6", "2026-06-01", {"E1"}, set())["decisionState"], "GOVERNANCE_ESCALATION")

    def test_f_r3_004_configuration_ambiguity(self):
        a = [dict(objectId="pump", property="flow", role="Design", configuration=c,
                  start="2026-01-01", end=None, evidence="E1", authority="A1", value=v)
             for c, v in (("M6", 505), ("M7", 510))]
        self.assertEqual(get_assertions(a, "pump", "flow", "Design", None, "2026-06-01", {"E1"}, {"A1"})["reason"], "CONFIGURATION_AMBIGUOUS")

    def test_f_r3_005_temporary_basis_separation(self):
        design = {"id": "DB01", "type": "DesignBasis"}
        temporary = {"id": "TM01", "type": "TemporaryApplicableBasis"}
        self.assertNotEqual(design["type"], temporary["type"])
        self.assertEqual(design["id"], "DB01")

    def test_unknown_code(self):
        self.assertEqual(resolve_object([], "UNKNOWN", "2026-06-01")["status"], "NOT_FOUND")

    def test_missing_evidence(self):
        a = [dict(objectId="pump", property="flow", role="Design", configuration="M6",
                  start="2026-01-01", end=None, evidence="E1", authority="A1", value=505)]
        self.assertEqual(get_assertions(a, "pump", "flow", "Design", "M6", "2026-06-01", set(), {"A1"})["reason"], "EVIDENCE_MISSING")

if __name__ == "__main__":
    unittest.main()
