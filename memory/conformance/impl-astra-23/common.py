"""Independent wire helpers for the package-only semantic evaluator."""

import copy
import datetime
import hashlib
import json
import re
import secrets


def cjson(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(b"bounded-evidence:cjson-v1\0" + cjson(value).encode()).hexdigest()


def key(value):
    if value is None:
        return None
    value = value.get("envelope", value)
    return value["id"], value["version"]


def ref(value):
    k = value if isinstance(value, tuple) else key(value)
    return {"id": k[0], "version": k[1]}


def refs(values):
    return [ref(k) for k in sorted(set(key(v) if isinstance(v, dict) else v for v in values))]


def stamp(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", value):
        raise Refused("invalid_time")
    try:
        return datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=datetime.timezone.utc)
    except ValueError as error:
        raise Refused("invalid_time") from error


def applicable(valid, at):
    return at == "any" or (valid["kind"] == "known" and valid["from"] <= at
                           and (valid["to"] is None or at < valid["to"]))


class Refused(Exception):
    def __init__(self, code):
        self.code = code
        super().__init__(code)

    def response(self):
        retry = {"version_conflict", "policy_mismatch", "stale_generation",
                 "erasure_incomplete", "publication_stale", "unavailable"}
        return {"type": "refusal", "code": self.code, "retryable": self.code in retry}


def receipt(operation, outcome, records=(), custody=(), status=None):
    return {"type": "receipt", "operation": operation, "outcome": outcome,
            "receipt_handle": secrets.token_hex(16), "refs": refs(records),
            "custody": sorted(set(custody)), "erasure_status": status}


def strict_loads(text):
    def pairs(items):
        out = {}
        for k, v in items:
            if k in out:
                raise Refused("invalid_json")
            out[k] = v
        return out

    def invalid(_):
        raise Refused("invalid_json")

    try:
        value = json.loads(text, object_pairs_hook=pairs, parse_float=invalid, parse_constant=invalid)
    except (ValueError, UnicodeError) as error:
        raise Refused("invalid_json") from error

    def walk(x):
        if type(x) is int and not -9007199254740991 <= x <= 9007199254740991:
            invalid(x)
        if isinstance(x, str) and any(0xD800 <= ord(c) <= 0xDFFF for c in x):
            invalid(x)
        if isinstance(x, dict):
            for k, v in x.items():
                walk(k)
                walk(v)
        if isinstance(x, list):
            for v in x:
                walk(v)
    walk(value)
    return value


class Grammar:
    """Closed structural subset used by the published schemas; no external resolver."""

    def __init__(self, directory):
        self.schemas = {p.stem.split(".")[0]: strict_loads(p.read_text())
                        for p in directory.glob("*.schema.json")}
        self.registry = {s["$id"]: s for s in self.schemas.values()}

    def matches(self, x, schema):
        if "$ref" in schema:
            target = self.registry.get(schema["$ref"])
            return target is not None and self.matches(x, target)
        if "oneOf" in schema:
            return sum(self.matches(x, s) for s in schema["oneOf"]) == 1
        if "const" in schema and (type(x) is not type(schema["const"]) or x != schema["const"]):
            return False
        if "enum" in schema and not any(type(x) is type(v) and x == v for v in schema["enum"]):
            return False
        t = schema.get("type")
        typ = {"object": dict, "array": list, "string": str, "integer": int,
               "boolean": bool, "null": type(None)}
        if t and type(x) is not typ[t]:
            return False
        if t == "object":
            if not set(schema.get("required", ())) <= x.keys():
                return False
            properties = schema.get("properties", {})
            if schema.get("additionalProperties") is False and not x.keys() <= properties.keys():
                return False
            return all(self.matches(v, properties[k]) for k, v in x.items() if k in properties)
        if t == "array":
            return (len(x) >= schema.get("minItems", 0)
                    and all(self.matches(v, schema.get("items", {})) for v in x))
        return True

    def check(self, x, name, proposal=False):
        schema = self.schemas[name]
        if proposal:
            schema = copy.deepcopy(schema)
            env = schema["properties"]["envelope"]
            for k in ("submitter", "recorded", "admission_class"):
                env["properties"].pop(k)
                env["required"].remove(k)
            representation = env["properties"]["representation_ref"]["oneOf"][0]
            representation["properties"].pop("checked", None)
            if "checked" in representation["required"]:
                representation["required"].remove("checked")
        if not self.matches(x, schema):
            raise Refused("invalid_shape")
