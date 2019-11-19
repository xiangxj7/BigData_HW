from __future__ import print_function
from pyspark import SparkContext
import json


def friend(arr):
    count = {}
    res = []
    print(arr[1])
    for i in arr[1]:
        count.setdefault(i, 0)
        count[i] += 1
    for key in count:
        if count[key] == 1:
            res.append((arr[0], key))
    return res


sc = SparkContext('local', 'test')
textFile = sc.textFile("file:///home/xiangxj7/BigData/MapReduce Assignments(data)/problem4//friends.json")
friendship = textFile.map(lambda row: json.loads(row))
friendship = friendship.flatMap(lambda record: [(record[0], [record[1]]), (record[1], [record[0]])])
friendship = friendship.reduceByKey(lambda a, b: a + b)
# friendCount = friendCount.filter(lambda x: len(x[1]) == 1)
friendship = friendship.flatMap(friend)
friendship.foreach(print)
friendship.saveAsTextFile("spark_result.txt")