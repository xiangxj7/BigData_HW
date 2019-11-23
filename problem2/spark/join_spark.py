from __future__ import print_function
from pyspark import SparkContext
import json

def join(arr):
    array = []
    for i in arr[1]:
        if i[0] == "order":
            order = i
    for i in arr[1]:
        if i[0] == "line_item":
            array.append((order + i))
    return(array)




sc = SparkContext('local', 'test')
# textFile = sc.textFile("file:///home/xiangxj7/BigData/MapReduce Assignments(data)/problem2//records.json")
textFile = sc.textFile("hdfs:///user/root/input//records.json")
joinRDD = textFile.map(lambda row: (json.loads(row)[1], [json.loads(row)]))
joinRDD = joinRDD.reduceByKey(lambda a, b: a + b)
joinRDD = joinRDD.flatMap(join)

joinRDD.foreach(print)
joinRDD.saveAsTextFile("spark_result.txt")