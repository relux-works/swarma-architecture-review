"""Exact finite proof-set families using a reduced zero-suppressed diagram.

This shares set-family structure; worst-case diagram size can still be exponential.
Only the requested prefix is enumerated. This is not a service resource guarantee.
"""

import json


class Proofs:
    def __init__(self, records):
        records = {r["id"]: r for r in records}
        order = lambda r: tuple(r.get("reference_order", (r["id"], 0)))
        self.ids = sorted(records, key=lambda k: order(records[k]))
        self.index = {k: i for i, k in enumerate(self.ids)}
        self.lex = []
        for k in self.ids:
            record = records[k]
            reference = order(record)
            value = {"id": reference[0], "version": reference[1]}
            self.lex.append(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False))
        self.nodes = [None, None]  # 0: no sets; 1: the family containing the empty set.
        self.unique = {}
        self.union_cache = {}
        self.join_cache = {}

    def node(self, variable, low, high):
        if high == 0:
            return low
        identity = (variable, low, high)
        if identity not in self.unique:
            self.unique[identity] = len(self.nodes)
            self.nodes.append(identity)
        return self.unique[identity]

    def top(self, family):
        return self.nodes[family][0] if family > 1 else len(self.ids)

    def branches(self, family, variable):
        return self.nodes[family][1:] if self.top(family) == variable else (family, 0)

    def singleton(self, reference):
        return self.node(self.index[reference], 0, 1)

    def union(self, left, right):
        if left == right or right == 0:
            return left
        if left == 0:
            return right
        pair = tuple(sorted((left, right)))
        if pair in self.union_cache:
            return self.union_cache[pair]
        variable = min(self.top(left), self.top(right))
        ll, lh = self.branches(left, variable)
        rl, rh = self.branches(right, variable)
        result = self.node(variable, self.union(ll, rl), self.union(lh, rh))
        self.union_cache[pair] = result
        return result

    def join(self, left, right):
        """The family of every set union from the two operand families."""
        if left == 0 or right == 0:
            return 0
        if left == 1:
            return right
        if right == 1:
            return left
        pair = tuple(sorted((left, right)))
        if pair in self.join_cache:
            return self.join_cache[pair]
        variable = min(self.top(left), self.top(right))
        ll, lh = self.branches(left, variable)
        rl, rh = self.branches(right, variable)
        low = self.join(ll, rl)
        high = self.union(self.join(lh, rl), self.join(ll, rh))
        high = self.union(high, self.join(lh, rh))
        result = self.node(variable, low, high)
        self.join_cache[pair] = result
        return result

    def take(self, family, count):
        """Canonical-JSON order of internally reference-sorted distinct sets."""
        result = []

        def visit(current, prefix):
            if len(result) >= count or current == 0:
                return
            choices = []
            while current > 1:
                variable, low, high = self.nodes[current]
                choices.append((variable, high))
                current = low
            has_empty = current == 1
            # At the array start, ']' sorts before '{'. After
            # a reference, ',' sorts before ']', so extensions precede termination.
            if has_empty and not prefix:
                result.append([])
            for variable, high in sorted(choices, key=lambda item: self.lex[item[0]]):
                if len(result) >= count:
                    return
                visit(high, prefix + [variable])
            if has_empty and prefix and len(result) < count:
                result.append([self.ids[v] for v in prefix])

        if count > 0:
            visit(family, [])
        return result
