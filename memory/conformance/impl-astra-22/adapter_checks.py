"""Wire-mapping regression controls, separate from pre-package source controls."""

import copy
import json
from pathlib import Path
import unittest

from adapter import Adapter


class AssociationControls(unittest.TestCase):
    # R7-013: the admitted mirror fixture discloses documentary attribution across
    # source/observer perspectives, without creating a semantic witness. Removing
    # the source's read grant removes its reference without leaking an error.
    def test_documentary_association_obeys_visibility(self):
        path = Path(__file__).resolve().parents[2] / "spec/kernel/vectors/semantic/S23.json"
        vector = json.loads(path.read_text())
        initial, query = vector["initial_state"], vector["query"]
        item = Adapter(initial, "control").query(query)["items"][0]
        self.assertEqual(item["source_refs"], [{"id": "rec:mirror", "version": 1}])
        self.assertEqual(item["support"]["witness"], "not_found")
        self.assertEqual(item["authority_receipt"], None)
        hidden = copy.deepcopy(initial)
        allowed = [r["envelope"]["id"] for r in initial["records"] if r["envelope"]["kind"] != "source"]
        for grant in hidden["policy"]["grants"]:
            grant["records"] = allowed
        item = Adapter(hidden, "control").query(query)["items"][0]
        self.assertEqual(item["source_refs"], [])
        self.assertEqual(item["support"]["witness"], "not_found")
        self.assertEqual(item["support"]["evaluation"], "complete")


if __name__ == "__main__":
    unittest.main(verbosity=2)
