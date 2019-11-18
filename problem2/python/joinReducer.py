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


res = []
dic = {}
for line in sys.stdin:
    line = line.strip()

    key, value = line.split("\t")
    value = json.loads(value)
    dic.setdefault(key, [])
    dic.get(key).append(value)
for key in dic:
    # for value in values:
    values = dic.get(key)
    for value in values:
        if value[0] == 'order':
            order = value

    for value in values:
        if value[0] == 'line_item':
            res.append((order + value))

jenc = json.JSONEncoder()
for item in res:
   print(jenc.encode(item))