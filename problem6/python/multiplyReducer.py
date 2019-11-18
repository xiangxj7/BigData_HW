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
    key = key.replace("(", "").replace(")", "")
    i, j = key.split(",")
    i, j = int(i), int(j)
    value = json.loads(value)

    res.setdefault((i, j), [])
    res.get((i, j)).append(value)

matrix = []
for key in res:
    result = 0
    values = res[key]
    for i in values:
        for j in values:
            if i[0] == 'a' and j[0] == 'b' and i[2] == j[1]:
                result += i[3] * j[3]

    if result != 0:
        matrix.append((key[0], key[1], result))

jenc = json.JSONEncoder()
for item in matrix:
    print(jenc.encode(item))