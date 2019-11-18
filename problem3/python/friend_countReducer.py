#!usr/bin/env python


import json
import sys

def out_dic(dic):
    result = []
    for key in dic:
        result.append((key, dic[key]))
    jenc = json.JSONEncoder()
    for item in result:
       print(jenc.encode(item))

res = {}
for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")

    res.setdefault(key, 0)
    res[key] = res.get(key) + int(value)

out_dic(res)
