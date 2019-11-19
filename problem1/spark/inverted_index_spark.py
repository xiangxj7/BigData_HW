from __future__ import print_function
from pyspark import SparkContext
import json


#wordCount = textFile.flatMap(lambda row:json.loads(row)[1].split(' ')).map(lambda word:(word,1)).reduceByKey(lambda a,b:a+b)

def mapper(record):
    keys = record[1].split(" ")
    value = record[0]
    res = []
    for key in keys:
        res.append((key, "\"" + value + "\""))
    return res



sc = SparkContext('local', 'test')
textFile = sc.textFile("file:///home/xiangxj7/BigData/MapReduce Assignments(data)/problem1//books.json")
invertedIndex = textFile.map(lambda row: json.loads(row))
invertedIndex = invertedIndex.flatMap(mapper)
invertedIndex = invertedIndex.reduceByKey(lambda a, b: a + ", " + b)
invertedIndex = invertedIndex.map(lambda x : (x[0], "[" + x[1] + "]"))

invertedIndex.foreach(print)
invertedIndex.saveAsTextFile("spark_result.txt")