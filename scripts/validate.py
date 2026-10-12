#!/usr/bin/env python3
"""Validate data/programs.json: schema, CSV sync, null report, URL checks.
Usage: python scripts/validate.py [--no-net] [--strict]  (403/429/timeouts = WARN by default: many government sites block scripts)"""
import csv, json, sys, pathlib, urllib.request, urllib.error, concurrent.futures as cf
root = pathlib.Path(__file__).resolve().parent.parent
try: import jsonschema
except ImportError: sys.exit("pip install jsonschema")
data = json.load(open(root/"data/programs.json")); E = data["entries"]; fail = False
for e in jsonschema.Draft202012Validator(json.load(open(root/"schema/programs.schema.json"))).iter_errors(data): print("SCHEMA:", list(e.path), e.message); fail = True
ids = [x["id"] for x in E]
if len(set(ids)) != len(ids): print("DUPLICATE ids"); fail = True
if [r["id"] for r in csv.DictReader(open(root/"data/programs.csv"))] != ids: print("CSV out of sync"); fail = True
nulls = {}
for x in E:
    for k, v in x.items():
        if v is None: nulls[k] = nulls.get(k, 0) + 1
print(f"{len(E)} programs, {len({x['iso2'] for x in E})} countries"); print("null counts:", dict(sorted(nulls.items(), key=lambda kv: -kv[1])))
if "--no-net" not in sys.argv:
    urls = sorted({x["source_url"] for x in E} | {u for x in E for u in x["extra_source_urls"]} | {x["emigro_guide_url"] for x in E if x["emigro_guide_url"]})
    def chk(u):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"Mozilla/5.0 (relocation-requirements-ru validator)"}), timeout=25) as r: return u, r.status
        except urllib.error.HTTPError as e: return u, e.code
        except Exception as e: return u, type(e).__name__
    with cf.ThreadPoolExecutor(8) as ex:
        for u, st in ex.map(chk, urls):
            tag = "OK  " if st == 200 else ("FAIL" if "--strict" in sys.argv or st in (404, 410) else "WARN")
            fail |= tag == "FAIL"; print(tag, st, u)
print("RESULT:", "FAIL" if fail else "PASS"); sys.exit(1 if fail else 0)
