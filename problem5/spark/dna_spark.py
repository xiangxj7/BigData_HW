from __future__ import print_function
from pyspark import SparkContext
import json



sc = SparkContext('local', 'test')
textFile = sc.textFile("hdfs:///user/root/input//dna.json")
# textFile = sc.textFile("file:///home/xiangxj7/BigData/MapReduce Assignments(data)/problem5//dna.json")
dnaRRD = textFile.map(lambda row: json.loads(row))
dnaRRD = dnaRRD.map(lambda record: (record[1][:-10], record[0]))
dnaRRD = dnaRRD.reduceByKey(lambda a, b: a).map(lambda x: x[0])
dnaRRD.foreach(print)
dnaRRD.saveAsTextFile("spark_result.txt")