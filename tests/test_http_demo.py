"""HTTP integration tests: local ephemeral server, no external dependencies."""
import json
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen, Request
from http.server import ThreadingHTTPServer

from runtime.http_demo import make_handler, demo_gateway


class HttpDemoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gateway = demo_gateway()
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), make_handler(cls.gateway))
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.url = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def get(self, path):
        with urlopen(self.url + path, timeout=3) as response:
            return response.status, json.load(response)

    def test_catalog(self):
        status, data = self.get("/api/objects")
        self.assertEqual(status, 200)
        self.assertEqual(len(data["objects"]), 2)
        self.assertTrue(data["syntheticOnly"])

    def test_pump_query(self):
        status, data = self.get(
            "/api/query?code=RIS-P001&property=RatedFlow&configuration=M6&validAt=2026-06-15")
        self.assertEqual(status, 200)
        self.assertEqual(data["decisionState"], "SYNTHETIC_CANDIDATE")
        self.assertEqual(data["data"]["value"], 505)
        self.assertTrue(data["auditRef"])

    def test_valve_query(self):
        _, data = self.get(
            "/api/query?code=RIS-V001&property=NominalDiameter&configuration=M6&validAt=2026-06-15")
        self.assertEqual(data["data"]["value"], 150)

    def test_stop_gate(self):
        _, data = self.get("/api/impact?root=SSC-001")
        self.assertIn("STOP-01", data["data"]["graphReachability"])
        self.assertNotIn("STOP-01", data["data"]["potentialImpactSet"])

    def test_unknown_object_404(self):
        with self.assertRaises(HTTPError) as caught:
            self.get("/api/query?code=UNKNOWN&property=RatedFlow")
        self.assertEqual(caught.exception.code, 404)

    def test_read_only(self):
        with self.assertRaises(HTTPError) as caught:
            urlopen(Request(self.url + "/api/query", data=b"{}", method="POST"), timeout=3)
        self.assertEqual(caught.exception.code, 405)

    def test_browser_served(self):
        with urlopen(self.url + "/", timeout=3) as response:
            body = response.read().decode("utf-8")
        self.assertIn("UEOT", body)
        self.assertIn("/api/objects", body)


if __name__ == "__main__":
    unittest.main()
