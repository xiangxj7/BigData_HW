#!usr/bin/env python


import json
import sys



res = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")

    if key not in res:
        res.append(key)


jenc = json.JSONEncoder()
for item in res:
    print(jenc.encode(item))
