"""Independent finite-set oracles and bounded-prefix proof controls."""

import itertools
import json
import unittest

from proofs import Proofs
from evaluator import Evaluator


class ProofControls(unittest.TestCase):
    # Found proofs include only own witness roots/rules; opposite-quality roots
    # and hidden candidates never appear. Explanation truncation keeps evidence.
    def test_evaluator_proof_paths(self):
        claims = [{"id": x} for x in "ABC"]
        roots = [{"id": "ea", "target": ["A", "support"], "qualification": "semantic_review"},
                 {"id": "eb", "target": ["B", "support"], "qualification": "test_result"},
                 {"id": "opposite", "target": ["A", "oppose"], "qualification": "semantic_review"},
                 {"id": "hidden", "target": ["C", "support"], "qualification": "semantic_review", "visible": False}]
        rules = [{"id": "rule", "target": ["C", "support"], "premises": [["A", "support"], ["B", "support"]], "checked": True}]
        model = Evaluator(claims, roots, rules)
        query = {"include_paths": True, "explanation_budget": 1}
        result = model.evaluate("C", query)
        self.assertEqual(result["proof_paths"], [["ea", "eb", "rule"]])
        self.assertEqual(result["support"]["premise_quality"], "conflicted_premises_only")
        zero = model.evaluate("C", query | {"explanation_budget": 0})
        self.assertEqual(zero["proof_paths"], [])
        self.assertFalse(zero["explanation"]["complete"])
        self.assertEqual(zero["support"], result["support"])
        model.roots[0]["visible"] = False
        missing = model.evaluate("C", query)
        self.assertEqual(missing["proof_paths"], [])
        self.assertEqual(missing["support"]["witness"], "not_found")

    # Exhaustive small families independently check union/join, overlap and exact
    # distinct ordering; an output prefix equals the full oracle's same prefix.
    def test_finite_set_algebra(self):
        records = [{"id": x, "reference_order": [x, 1]} for x in "abcd"]
        manager = Proofs(records)
        subsets = [frozenset(c) for size in range(5) for c in itertools.combinations("abcd", size)]

        def encode(family):
            out = 0
            for subset in family:
                node = 1
                for x in subset:
                    node = manager.join(node, manager.singleton(x))
                out = manager.union(out, node)
            return out

        def expected(family):
            paths = [sorted(s) for s in family]
            return sorted(paths, key=lambda p: json.dumps([{"id": x, "version": 1} for x in p], sort_keys=True, separators=(",", ":")))

        families = [set(), {frozenset()}, set(subsets), set(subsets[::2]), set(subsets[1::3])]
        for left, right in itertools.product(families, repeat=2):
            with self.subTest(left=len(left), right=len(right)):
                joined = {a | b for a in left for b in right}
                for actual, oracle in ((manager.union(encode(left), encode(right)), left | right),
                                       (manager.join(encode(left), encode(right)), joined)):
                    self.assertEqual(manager.take(actual, 100), expected(oracle))
                    self.assertEqual(manager.take(actual, 2), expected(oracle)[:2])

    # Numeric reference order within each path differs from JSON lexical order
    # between paths; shorter prefixes sort after their continuations.
    def test_numeric_versions_and_prefixes(self):
        records = [{"id": "two", "reference_order": ["r", 2]},
                   {"id": "ten", "reference_order": ["r", 10]}]
        manager = Proofs(records)
        two, ten = manager.singleton("two"), manager.singleton("ten")
        family = manager.union(manager.union(two, ten), manager.join(two, ten))
        self.assertEqual(manager.take(family, 10), [["ten"], ["two", "ten"], ["two"]])
        self.assertEqual(manager.take(family, 0), [])

    # This interleaved 40-choice family has 2**40 proofs but a small shared
    # diagram; obtaining two prefixes does not materialize all combinations.
    # Other variable orders/families can still have exponential diagram size.
    def test_factored_family_prefix(self):
        records = [{"id": f"{i:02}{s}", "reference_order": [f"{i:02}{s}", 1]}
                   for i in range(40) for s in "ab"]
        manager = Proofs(records)
        family = 1
        for i in range(40):
            alternatives = manager.union(manager.singleton(f"{i:02}a"), manager.singleton(f"{i:02}b"))
            family = manager.join(family, alternatives)
        paths = manager.take(family, 2)
        self.assertEqual(paths[0], [f"{i:02}a" for i in range(40)])
        self.assertEqual(paths[1], [f"{i:02}a" for i in range(39)] + ["39b"])
        self.assertLess(len(manager.nodes), 5000)


if __name__ == "__main__":
    unittest.main(verbosity=2)
