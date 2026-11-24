"""Proposed WP-03B regression oracle, synthetic only.

Run separately: python -m unittest discover -s audit_tests -v
Failures are retained as evidence, not suppressed. Proposed semantics require
review against frozen masters; this suite is not formal conformance.
"""
import unittest
from runtime.ueot_runtime import traverse_graph, get_assertions
from runtime.gateway import SyntheticGateway
from runtime.governance import resolve_applicable_basis

def fixture():
    return SyntheticGateway(
        assignments=[dict(code="P",objectId="A",start="2026-01-01")],
        bases=[dict(id="D",type="DesignBasis",objectId="A",configuration="M6",approved=True,start="2026-01-01")],
        assertions=[dict(objectId="A",property="Flow",role="Design",configuration="M6",basis="D",value=505,unit="m3/h",evidence="E",authority="U",start="2026-01-01")],
        evidence={"E":{"approved":True}},authorities={"U"},profiles={"P":{}},
        edges=[("A","B"),("B","C")],stop_targets={"B"})

def query(g, at="2026-06-15", config="M6"):
    return g.query("P","Flow","Design",config,at,"P")

class ProposedOracle(unittest.TestCase):
    def test_A01_stop_excludes_target(self):
        g=fixture()
        self.assertNotIn("B",g.impact("A")["data"]["potentialImpactSet"])
    def test_A01_raw_reachability_beyond_stop(self):
        self.assertIn("C",traverse_graph([("A","B"),("B","C")],"A",{"B"})["graphReachability"])
    def test_A01_cycle_excludes_root(self):
        self.assertNotIn("A",traverse_graph([("A","B"),("B","A")],"A",set())["potentialImpactSet"])
    def test_A02_temporary_does_not_conflict_with_design_query(self):
        g=fixture()
        g.bases.append(dict(g.bases[0],id="T",type="TemporaryApplicableBasis",scope=["Other"]))
        self.assertEqual(query(g)["decisionState"],"SYNTHETIC_CANDIDATE")
    def test_A02_expired_temporary_restores_design(self):
        g=fixture()
        g.bases.append(dict(g.bases[0],id="T",type="TemporaryApplicableBasis",end="2026-06-15"))
        self.assertEqual(query(g)["data"]["basis"],"D")
    def test_A03_missing_design_blocks_temporary(self):
        g=fixture()
        g.bases[0]["type"]="TemporaryApplicableBasis"
        self.assertNotEqual(resolve_applicable_basis(g.bases,"A","M6","2026-06-15")["status"],"RESOLVED")
    def test_A04_revoked_evidence_blocks(self):
        g=fixture()
        g.evidence["E"]["approved"]=False
        self.assertNotEqual(query(g)["decisionState"],"SYNTHETIC_CANDIDATE")
    def test_A04_expired_evidence_blocks(self):
        g=fixture()
        g.evidence["E"]["end"]="2026-06-15"
        self.assertNotEqual(query(g)["decisionState"],"SYNTHETIC_CANDIDATE")
    def test_A05_direct_assertion_without_basis_blocks(self):
        g=fixture()
        del g.assertions[0]["basis"]
        self.assertNotEqual(get_assertions(g.assertions,"A","Flow","Design","M6","2026-06-15",g.evidence,g.authorities)["decisionState"],"DEFINITIVE_SYNTHETIC_ONLY")
    def test_A06_self_declared_human_not_authorization(self):
        g=fixture()
        g.stop_targets.clear()
        r=g.impact("A",["B"],[{"objectId":"B","approved":True,"approverType":"HUMAN"}])
        self.assertNotIn("B",r["data"].get("confirmedImpact",[]))
    def test_A07_losing_evidence_not_supporting(self):
        g=fixture()
        g.authorities.add("V")
        g.evidence["F"]={"approved":True}
        g.assertions.append(dict(g.assertions[0],value=510,authority="V",evidence="F"))
        g.profiles["P"]["authorityPrecedence"]={"U":2,"V":1}
        self.assertEqual(query(g)["data"]["evidenceRefs"],["E"])
    def test_A08_missing_configuration_blocks(self):
        self.assertEqual(query(fixture(),config=None)["decisionState"],"NO_DEFINITIVE_CLAIM")
    def test_A09_invalid_date_blocks(self):
        self.assertNotEqual(query(fixture(),at="2026-99-99")["decisionState"],"SYNTHETIC_CANDIDATE")
