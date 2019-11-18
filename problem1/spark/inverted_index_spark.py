from __future__ import print_function
from pyspark import SparkContext
import json


#wordCount = textFile.flatMap(lambda row:json.loads(row)[1].split(' ')).map(lambda word:(word,1)).reduceByKey(lambda a,b:a+b)

def mapper(record):
    keys = record[1].split(" ")
    value = record[0]
    res = []
    for key in keys:
        res.append((key, value))
    return res

def reducer(v1, v2):
    if type(v1) == type([]) and type(v2) == type([]):
        return list(set(v1 + v2))
    elif type(v1) == type([]) and type(v2) != type([]):
        return list(set(v1.append(v2)))
    elif type(v1) != type([]) and type(v2) == type([]):
        return list(set(v2.append(v1)))
    else:
        return list(set([v1, v2]))


sc = SparkContext('local', 'test')
textFile = sc.textFile("file:///home/root/bigdata/problem1//books.json")
invertedIndex = textFile.flatMap(lambda row: (json.loads(row)))
invertedIndex = invertedIndex.flatMap(mapper)
invertedIndex = invertedIndex.reduceByKey(reducer)

invertedIndex.foreach(print)
