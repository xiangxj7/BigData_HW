from __future__ import print_function
from pyspark import SparkContext
import json

def mapper(record):
    maxI = 10
    maxJ = 10
    res = []
    if record[0] == 'a':
        i = record[1]
        for j in range(maxJ + 1):
            res.append(((i, j), [record]))
    elif record[0] == 'b':
        j = record[2]
        for i in range(maxI + 1):
            res.append(((i, j), [record]))
    else:
        pass
    return res


def reducer(res):
    result = 0
    values = res[1]
    for i in values:
        for j in values:
            if i[0] == 'a' and j[0] == 'b' and i[2] == j[1]:
                result += i[3] * j[3]

    if result != 0:
        return((res[0][0], res[0][1], result))
    else:
        return (-1, -1, 0)


sc = SparkContext('local', 'test')
# textFile = sc.textFile("file:///home/xiangxj7/BigData/MapReduce Assignments(data)/problem6//matrix.json")
textFile = sc.textFile("hdfs:///user/root/input//matrix.json")
matrixRRD = textFile.map(lambda row: json.loads(row))
matrixRRD = matrixRRD.flatMap(mapper)
matrixRRD = matrixRRD.reduceByKey(lambda a, b: a + b)
matrixRRD = matrixRRD.map(reducer).filter(lambda x: x[0] != -1)


matrixRRD.foreach(print)
matrixRRD.saveAsTextFile("spark_result.txt")