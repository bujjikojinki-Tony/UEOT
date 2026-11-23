"""Experimental governance semantics; NOT the UEOT frozen contract.

Pure functions intentionally accept synthetic dictionaries. No persistence or approvals.
"""
from __future__ import annotations


def active(record, at):
    return record["start"] <= at and (record.get("end") is None or at < record["end"])


def resolve_authority(assertions, authority_registry, at, precedence=None):
    """Resolve conflicting assertions for one subject/property/role/configuration.

    The caller MUST pre-filter subject, property, value role and configuration.
    No timestamp-based or implicit source precedence is allowed.
    """
    valid = [a for a in assertions if active(a, at)]
    if not valid:
        return {"status": "NOT_FOUND", "selected": None}
    unknown = sorted({a["authority"] for a in valid if a["authority"] not in authority_registry})
    if unknown:
        return {"status": "GOVERNANCE_ESCALATION", "reason": "AUTHORITY_UNVERIFIED",
                "unknownAuthorities": unknown, "selected": None}
    values = {repr((a["value"], a.get("unit"))) for a in valid}
    if len(values) == 1:
        return {"status": "CONSISTENT", "selected": valid[0], "supporting": valid}
    if precedence is None:
        return {"status": "GOVERNANCE_ESCALATION", "reason": "MULTI_AUTHORITY_CONFLICT",
                "selected": None, "candidates": valid}
    ranked = [(precedence.get(a["authority"]), a) for a in valid]
    if any(rank is None for rank, _ in ranked):
        return {"status": "GOVERNANCE_ESCALATION", "reason": "PRECEDENCE_UNDEFINED",
                "selected": None, "candidates": valid}
    highest = max(rank for rank, _ in ranked)
    winners = [a for rank, a in ranked if rank == highest]
    if len({repr((a["value"], a.get("unit"))) for a in winners}) > 1:
        return {"status": "GOVERNANCE_ESCALATION", "reason": "PRECEDENCE_TIE",
                "selected": None, "candidates": winners}
    return {"status": "RESOLVED_BY_PROFILE", "selected": winners[0],
            "profileRequired": True, "supporting": winners}


def resolve_applicable_basis(bases, object_id, configuration, at):
    """Separate DesignBasis from time-scoped TemporaryApplicableBasis."""
    matching = [b for b in bases if b["objectId"] == object_id
                and b["configuration"] == configuration
                and b.get("approved", False) and active(b, at)]
    design = [b for b in matching if b["type"] == "DesignBasis"]
    temporary = [b for b in matching if b["type"] == "TemporaryApplicableBasis"]
    if len(design) > 1 or len(temporary) > 1:
        return {"status": "BASIS_CONFLICT", "designBasis": None,
                "temporaryApplicableBasis": None, "effectiveBasis": None}
    d = design[0]["id"] if design else None
    t = temporary[0]["id"] if temporary else None
    return {"status": "RESOLVED" if d or t else "NOT_FOUND",
            "designBasis": d, "temporaryApplicableBasis": t,
            "effectiveBasis": t or d, "designBasisPreserved": True}


def validate_impact_decision(potential, confirmed, decisions):
    """ConfirmedImpact requires a matching approved human decision per object."""
    potential, confirmed = set(potential), set(confirmed)
    if not confirmed <= potential:
        return {"status": "REJECTED", "reason": "CONFIRMED_NOT_POTENTIAL"}
    approved = {d["objectId"] for d in decisions if d.get("approved")
                and d.get("approverType") == "HUMAN"}
    missing = sorted(confirmed - approved)
    if missing:
        return {"status": "REJECTED", "reason": "HUMAN_APPROVAL_MISSING",
                "objects": missing}
    return {"status": "ACCEPTED_SYNTHETIC_ONLY"}
