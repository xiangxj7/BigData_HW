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
asymmetric_friendships = []
for line in sys.stdin:
    line = line.strip()
    key, value = line.split("\t")

    res.setdefault(key, {})
    res[key].setdefault(value, 0)
    res[key][value] += 1

for key in res:
    for key1 in res[key]:
        if(res[key][key1] == 1):
            asymmetric_friendships.append((key, key1))
jenc = json.JSONEncoder()
for item in asymmetric_friendships:
    print(jenc.encode(item))
