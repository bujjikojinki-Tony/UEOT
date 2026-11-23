"""Additional synthetic governance regressions; no claim of official conformance."""
import unittest
from runtime.governance import resolve_authority, resolve_applicable_basis, validate_impact_decision


def assertion(authority, value):
    return {"authority": authority, "value": value, "unit": "m3/h",
            "start": "2026-01-01", "end": None}


class GovernanceTests(unittest.TestCase):
    def test_multi_authority_conflict_blocks(self):
        result = resolve_authority([assertion("design", 505), assertion("vendor", 510)],
                                   {"design", "vendor"}, "2026-06-15")
        self.assertEqual(result["status"], "GOVERNANCE_ESCALATION")
        self.assertEqual(result["reason"], "MULTI_AUTHORITY_CONFLICT")
        self.assertIsNone(result["selected"])

    def test_explicit_precedence_resolves(self):
        result = resolve_authority([assertion("design", 505), assertion("vendor", 510)],
                                   {"design", "vendor"}, "2026-06-15",
                                   precedence={"design": 2, "vendor": 1})
        self.assertEqual(result["status"], "RESOLVED_BY_PROFILE")
        self.assertEqual(result["selected"]["value"], 505)

    def test_equal_precedence_conflict_blocks(self):
        result = resolve_authority([assertion("design", 505), assertion("vendor", 510)],
                                   {"design", "vendor"}, "2026-06-15",
                                   precedence={"design": 1, "vendor": 1})
        self.assertEqual(result["reason"], "PRECEDENCE_TIE")

    def test_unverified_authority_blocks(self):
        result = resolve_authority([assertion("unknown", 505)], {"design"}, "2026-06-15")
        self.assertEqual(result["reason"], "AUTHORITY_UNVERIFIED")

    def test_temporary_basis_time_scope_and_preservation(self):
        bases = [
            {"id": "DB01", "type": "DesignBasis", "objectId": "valve",
             "configuration": "M6", "approved": True, "start": "2026-01-01", "end": None},
            {"id": "TM01", "type": "TemporaryApplicableBasis", "objectId": "valve",
             "configuration": "M6", "approved": True, "start": "2026-06-01", "end": "2026-07-01"},
        ]
        before = resolve_applicable_basis(bases, "valve", "M6", "2026-05-31")
        during = resolve_applicable_basis(bases, "valve", "M6", "2026-06-15")
        after = resolve_applicable_basis(bases, "valve", "M6", "2026-07-01")
        self.assertEqual(before["effectiveBasis"], "DB01")
        self.assertEqual(during["effectiveBasis"], "TM01")
        self.assertEqual(during["designBasis"], "DB01")
        self.assertEqual(after["effectiveBasis"], "DB01")
        self.assertEqual(bases[0]["id"], "DB01")

    def test_overlapping_temporary_bases_block(self):
        bases = [{"id": x, "type": "TemporaryApplicableBasis", "objectId": "valve",
                  "configuration": "M6", "approved": True, "start": "2026-06-01",
                  "end": "2026-07-01"} for x in ("TM01", "TM02")]
        self.assertEqual(resolve_applicable_basis(bases, "valve", "M6", "2026-06-15")["status"],
                         "BASIS_CONFLICT")

    def test_confirmed_impact_requires_human_approval(self):
        self.assertEqual(validate_impact_decision({"valve"}, {"valve"}, [])["reason"],
                         "HUMAN_APPROVAL_MISSING")
        self.assertEqual(validate_impact_decision(
            {"valve"}, {"valve"},
            [{"objectId": "valve", "approved": True, "approverType": "AI"}])["reason"],
            "HUMAN_APPROVAL_MISSING")
        self.assertEqual(validate_impact_decision(
            {"valve"}, {"valve"},
            [{"objectId": "valve", "approved": True, "approverType": "HUMAN"}])["status"],
            "ACCEPTED_SYNTHETIC_ONLY")

    def test_confirmed_not_in_potential_rejected(self):
        self.assertEqual(validate_impact_decision(
            {"valve"}, {"motor"},
            [{"objectId": "motor", "approved": True, "approverType": "HUMAN"}])["reason"],
            "CONFIRMED_NOT_POTENTIAL")


if __name__ == "__main__":
    unittest.main()
