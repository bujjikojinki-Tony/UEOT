"""Loopback-only read-only HTTP demo. Synthetic fixtures, NOT production."""
from __future__ import annotations
import argparse
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

from runtime.gateway import SyntheticGateway

ROOT = Path(__file__).resolve().parents[1]
STATIC = ROOT / "browser" / "index.html"


def demo_gateway():
    return SyntheticGateway(
        assignments=[
            {"code": "RIS-P001", "objectId": "SSC-001", "start": "2026-01-01", "end": None},
            {"code": "RIS-V001", "objectId": "VALVE-01", "start": "2026-01-01", "end": None}],
        bases=[
            {"id": "BL-03", "type": "DesignBasis", "objectId": obj,
             "configuration": "M6", "approved": True, "start": "2026-01-01", "end": None}
            for obj in ("SSC-001", "VALVE-01")],
        assertions=[
            {"objectId": "SSC-001", "property": "RatedFlow", "role": "Design",
             "configuration": "M6", "basis": "BL-03", "value": 505, "unit": "m3/h",
             "evidence": "EV-01", "authority": "AU-01", "start": "2026-01-01", "end": None},
            {"objectId": "VALVE-01", "property": "NominalDiameter", "role": "Design",
             "configuration": "M6", "basis": "BL-03", "value": 150, "unit": "mm",
             "evidence": "EV-02", "authority": "AU-01", "start": "2026-01-01", "end": None}],
        evidence={"EV-01": {"synthetic": True}, "EV-02": {"synthetic": True}},
        authorities={"AU-01"}, profiles={"P-01": {}},
        edges=[("SSC-001", "VALVE-01"), ("VALVE-01", "STOP-01")],
        stop_targets={"STOP-01"})


CATALOG = [
    {"id": "SSC-001", "name": "安全注入泵 A", "code": "RIS-P001", "pbs": "泵组件",
     "fbs": "安全注入功能", "gbs": "RIS 系统", "wbs": "设计审查", "property": "RatedFlow"},
    {"id": "VALVE-01", "name": "出口隔离阀", "code": "RIS-V001", "pbs": "阀门组件",
     "fbs": "流路隔离功能", "gbs": "RIS 系统", "wbs": "变更评估", "property": "NominalDiameter"}]


def make_handler(gateway):
    class Handler(BaseHTTPRequestHandler):
        def send_json(self, payload, status=200):
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            url = urlsplit(self.path)
            if url.path == "/":
                data = STATIC.read_bytes()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.send_header("Cache-Control", "no-store")
                self.send_header("X-Content-Type-Options", "nosniff")
                self.end_headers()
                self.wfile.write(data)
                return
            if url.path == "/api/objects":
                self.send_json({"syntheticOnly": True, "objects": CATALOG})
                return
            if url.path == "/api/query":
                q = parse_qs(url.query)
                get = lambda name: q.get(name, [""])[0]
                if get("code") not in {x["code"] for x in CATALOG}:
                    self.send_json({"decisionState": "NO_DEFINITIVE_CLAIM",
                                    "reason": "UNKNOWN_OBJECT", "syntheticOnly": True}, 404)
                    return
                if get("property") not in {"RatedFlow", "NominalDiameter"}:
                    self.send_json({"decisionState": "NO_DEFINITIVE_CLAIM",
                                    "reason": "INVALID_PROPERTY", "syntheticOnly": True}, 400)
                    return
                result = gateway.query(get("code"), get("property"), "Design",
                                       get("configuration") or None,
                                       get("validAt"), "P-01")
                self.send_json(result)
                return
            if url.path == "/api/impact":
                q = parse_qs(url.query)
                root = q.get("root", [""])[0]
                if root not in {x["id"] for x in CATALOG}:
                    self.send_json({"decisionState": "NO_DEFINITIVE_CLAIM",
                                    "reason": "UNKNOWN_OBJECT", "syntheticOnly": True}, 404)
                    return
                self.send_json(gateway.impact(root))
                return
            self.send_json({"error": "NOT_FOUND"}, 404)

        def do_POST(self):
            self.send_json({"error": "READ_ONLY"}, 405)

    return Handler


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    server = ThreadingHTTPServer(("127.0.0.1", args.port), make_handler(demo_gateway()))
    print(f"UEOT synthetic-only demo: http://127.0.0.1:{args.port}/")
    server.serve_forever()


if __name__ == "__main__":
    main()
