"""Synthetic UEOT application gateway (experimental, not formal conformance).

This gateway integrates the existing six service functions with governance gates.
The in-memory audit log is deliberately NOT production-grade or tamper evident.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any
from uuid import uuid4

from runtime.ueot_runtime import (
    resolve_object, get_basis, get_assertions, get_evidence,
    resolve_profile, traverse_graph,
)
from runtime.governance import resolve_authority, resolve_applicable_basis, validate_impact_decision


@dataclass
class SyntheticGateway:
    assignments: list = field(default_factory=list)
    bases: list = field(default_factory=list)
    assertions: list = field(default_factory=list)
    evidence: dict = field(default_factory=dict)
    authorities: set = field(default_factory=set)
    profiles: dict = field(default_factory=dict)
    edges: list = field(default_factory=list)
    stop_targets: set = field(default_factory=set)
    audit: list = field(default_factory=list)

    def _result(self, operation: str, state: str, data: Any = None, reason: str | None = None):
        audit_id = str(uuid4())
        result = {"operation": operation, "decisionState": state, "data": data,
                  "reason": reason, "auditRef": audit_id,
                  "syntheticOnly": True}
        # Only metadata is stored: no sensitive evidence or assertion values.
        self.audit.append({"auditRef": audit_id, "operation": operation,
                           "decisionState": state, "reason": reason})
        return result

    def query(self, code: str, property_id: str, role: str, configuration: str | None,
              valid_at: str, profile_id: str, permitted_evidence: bool = True):
        profile = resolve_profile(self.profiles, profile_id)
        if profile["status"] != "RESOLVED":
            return self._result("query", "NO_DEFINITIVE_CLAIM", reason="PROFILE_UNAVAILABLE")
        identity = resolve_object(self.assignments, code, valid_at)
        if identity["status"] != "RESOLVED":
            return self._result("query", "NO_DEFINITIVE_CLAIM",
                                {"candidates": identity.get("candidates", [])},
                                "IDENTITY_" + identity["status"])
        object_id = identity["objectId"]
        if configuration is None:
            return self._result("query", "NO_DEFINITIVE_CLAIM",
                                reason="CONFIGURATION_REQUIRED")
        basis = get_basis(self.bases, object_id, configuration, valid_at)
        if basis["status"] != "RESOLVED":
            return self._result("query", "NO_DEFINITIVE_CLAIM", reason=basis["status"])
        candidate = [a for a in self.assertions
                     if a["objectId"] == object_id and a["property"] == property_id
                     and a["role"] == role and a["configuration"] == configuration
                     and a["start"] <= valid_at
                     and (a.get("end") is None or valid_at < a["end"])
                     and a.get("basis") == basis["selectedBasis"]]
        if not candidate:
            return self._result("query", "NO_DEFINITIVE_CLAIM", reason="ASSERTION_NOT_FOUND")
        if not permitted_evidence:
            return self._result("query", "NO_DEFINITIVE_CLAIM", reason="EVIDENCE_ACCESS_DENIED")
        for a in candidate:
            ev = get_evidence(self.evidence, a["evidence"], permitted_evidence)
            if ev["status"] != "FOUND":
                return self._result("query", "NO_DEFINITIVE_CLAIM", reason="EVIDENCE_MISSING")
        auth = resolve_authority(candidate, self.authorities, valid_at,
                                 precedence=profile["profile"].get("authorityPrecedence"))
        if auth["status"] not in ("CONSISTENT", "RESOLVED_BY_PROFILE"):
            return self._result("query", "NO_DEFINITIVE_CLAIM",
                                reason=auth.get("reason", auth["status"]))
        chosen = auth["selected"]
        return self._result("query", "SYNTHETIC_CANDIDATE",
                            {"objectId": object_id, "property": property_id,
                             "value": chosen["value"], "unit": chosen.get("unit"),
                             "valueRole": role, "configuration": configuration,
                             "basis": basis["selectedBasis"],
                             "evidenceRefs": sorted({a["evidence"] for a in candidate}),
                             "authority": chosen["authority"]})

    def impact(self, root: str, confirmed: list | None = None, decisions: list | None = None):
        graph = traverse_graph(self.edges, root, self.stop_targets)
        confirmed = confirmed or []
        if confirmed:
            review = validate_impact_decision(graph["potentialImpactSet"],
                                              confirmed, decisions or [])
            if review["status"] != "ACCEPTED_SYNTHETIC_ONLY":
                return self._result("impact", "NO_DEFINITIVE_CLAIM", graph,
                                    review["reason"])
        graph["confirmedImpact"] = sorted(confirmed)
        return self._result("impact", "SYNTHETIC_CANDIDATE", graph)

    def temporary_basis(self, object_id: str, configuration: str, valid_at: str):
        result = resolve_applicable_basis(self.bases, object_id, configuration, valid_at)
        state = "SYNTHETIC_CANDIDATE" if result["status"] == "RESOLVED" else "NO_DEFINITIVE_CLAIM"
        return self._result("temporary_basis", state, result,
                            None if state == "SYNTHETIC_CANDIDATE" else result["status"])
