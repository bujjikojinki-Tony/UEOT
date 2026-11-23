"""UEOT experimental reference runtime. Synthetic-only; NOT the frozen official implementation."""
from __future__ import annotations
from datetime import date

def active(item, at):
    return item["start"] <= at and (item.get("end") is None or at < item["end"])

def resolve_object(assignments, code, at):
    candidates = sorted({a["objectId"] for a in assignments if a["code"] == code and active(a, at)})
    if not candidates:
        return {"status": "NOT_FOUND", "candidates": []}
    if len(candidates) > 1:
        return {"status": "AMBIGUOUS", "candidates": candidates}
    return {"status": "RESOLVED", "objectId": candidates[0], "candidates": candidates}

def get_basis(bases, object_id, configuration, at):
    matches = [b for b in bases if b["objectId"] == object_id and b["configuration"] == configuration and b["approved"] and active(b, at)]
    if len(matches) == 1:
        return {"status": "RESOLVED", "selectedBasis": matches[0]["id"]}
    return {"status": "BASIS_CONFLICT" if len(matches) > 1 else "NOT_FOUND", "selectedBasis": None}

def get_assertions(assertions, object_id, property_id, role, configuration, at, evidence, authorities):
    candidates = [a for a in assertions if a["objectId"] == object_id and a["property"] == property_id and a["role"] == role and active(a, at)]
    configs = {a["configuration"] for a in candidates}
    if configuration is None and len(configs) > 1:
        return {"decisionState": "NO_DEFINITIVE_CLAIM", "reason": "CONFIGURATION_AMBIGUOUS", "candidates": sorted(configs)}
    candidates = [a for a in candidates if a["configuration"] == configuration]
    if len(candidates) != 1:
        return {"decisionState": "NO_DEFINITIVE_CLAIM", "reason": "ASSERTION_NOT_UNIQUE"}
    a = candidates[0]
    if a["evidence"] not in evidence:
        return {"decisionState": "NO_DEFINITIVE_CLAIM", "reason": "EVIDENCE_MISSING"}
    if a["authority"] not in authorities:
        return {"decisionState": "GOVERNANCE_ESCALATION", "reason": "AUTHORITY_UNVERIFIED"}
    return {"decisionState": "DEFINITIVE_SYNTHETIC_ONLY", "assertion": a}

def traverse_graph(edges, root, stop_targets):
    reachable, potential, seen, stack = set(), set(), {root}, [root]
    while stack:
        node = stack.pop()
        for src, dst in edges:
            if src != node:
                continue
            reachable.add(dst)
            if dst in stop_targets:
                continue
            potential.add(dst)
            if dst not in seen:
                seen.add(dst)
                stack.append(dst)
    return {"graphReachability": sorted(reachable), "potentialImpactSet": sorted(potential), "stopTargets": sorted(reachable & set(stop_targets))}

def get_evidence(evidence, evidence_id, permitted):
    if not permitted:
        return {"status": "ACCESS_DENIED"}
    return {"status": "FOUND", "data": evidence[evidence_id]} if evidence_id in evidence else {"status": "NOT_FOUND"}

def resolve_profile(profiles, profile_id):
    return {"status": "RESOLVED", "profile": profiles[profile_id]} if profile_id in profiles else {"status": "NOT_FOUND"}
