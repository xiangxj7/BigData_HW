from __future__ import print_function
from pyspark import SparkContext
import json

sc = SparkContext('local', 'test')
# textFile = sc.textFile("file:///home/xiangxj7/BigData/MapReduce Assignments(data)/problem3//friends.json")
textFile = sc.textFile("hdfs:///user/root/input//friends.json")
friendCount = textFile.map(lambda row: json.loads(row))
friendCount = friendCount.map(lambda record: (record[0], 1))
friendCount = friendCount.reduceByKey(lambda a, b: a + b)

friendCount.foreach(print)
friendCount.saveAsTextFile("spark_result.txt")