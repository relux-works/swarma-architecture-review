"""Bounded independent controls for the conformance checker and JSON boundary."""

import copy
import unittest

from common import Refused, strict_loads
from run_vectors import compare, differences, forbidden_matches


class Controls(unittest.TestCase):
    # Proves exact comparison detects a wrong semantic value and does not merge JSON bool/int.
    def test_exact_semantic_difference(self):
        expected = {"result": {"currentness": "current", "count": 1}}
        self.assertEqual(differences(expected, copy.deepcopy(expected)), [])
        changed = copy.deepcopy(expected)
        changed["result"]["currentness"] = "none"
        self.assertEqual(differences(changed, expected), [("/result/currentness", "none", "current")])
        self.assertEqual(differences(True, 1), [("/", True, 1)])

    # Proves each supported forbidden predicate detects its planted violation, including present null.
    def test_forbidden_controls(self):
        report = {"a": None, "xs": [1, "x"], "flag": True}
        for predicate in [{"path": "/a", "test": "exists"},
                          {"path": "/flag", "test": "equals", "value": True},
                          {"path": "/xs", "test": "contains", "value": "x"},
                          {"path": "/xs", "test": "size_equals", "value": 2}]:
            self.assertTrue(forbidden_matches(report, predicate))
            self.assertFalse(forbidden_matches({}, predicate))
        self.assertFalse(forbidden_matches(report, {"path": "/flag", "test": "equals", "value": 1}))

    # Proves declared normalization preserves non-handle fields and checks equality before replacing handles.
    def test_normalization_control(self):
        expected = {"result": {"handle": "@h1", "same": "@h1", "count": 1}}
        vector = {"expected": expected, "forbidden": [], "normalization": {
            "fresh_handles": ["/result/handle", "/result/same"],
            "equal_handles": [["/result/handle", "/result/same"]], "distinct_handles": [], "equivalent_outputs": []}}
        actual = {"result": {"handle": "a" * 32, "same": "a" * 32, "count": 1}}
        self.assertEqual(compare(actual, vector), ([], []))
        actual["result"]["same"] = "b" * 32
        self.assertIn("equal_handles violated", compare(actual, vector)[1][0])
        actual["result"]["count"] = 2
        self.assertEqual(compare(actual, vector)[0], [("/result/count", 2, 1)])

    # Proves malformed JSON is rejected by the intended code, with valid nearby controls accepted.
    def test_closed_json(self):
        self.assertEqual(strict_loads('{"n": 1, "b": true}'), {"n": 1, "b": True})
        for text in ['{"n":1,"n":2}', '{"n":1.0}', '{"n":NaN}', '{"n":9007199254740992}', '"\\ud800"']:
            with self.assertRaises(Refused) as caught:
                strict_loads(text)
            self.assertEqual(caught.exception.code, "invalid_json")


if __name__ == "__main__":
    unittest.main()
