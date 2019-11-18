#!/usr/bin/env python

import sys
import json

def out_dic(dic):
    result = []
    for key in dic:
        result.append((key, dic[key]))
    jenc = json.JSONEncoder()
    for item in result:
       print(jenc.encode(item))

inverted_index = {}

for line in sys.stdin:
    # print(line)
    line = line.strip()

    word, filename = line.split("\t", 1)

    try:
        inverted_index.setdefault(word, [])
        if filename not in inverted_index.get(word):
            inverted_index.get(word).append(filename)
    except ValueError:
        pass
# print("-----------------------------------------------")
# print(inverted_index)
# print("-----------------------------------------------\n")
out_dic(inverted_index)

