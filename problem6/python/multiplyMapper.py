#!/usr/bin/env python

import sys
import json

maxI = 10
maxJ = 10
for line in sys.stdin:
    line = line.strip()

    record = json.loads(line)
    key = record[0]

    if key == 'a':
        i = record[1]
        for j in range(maxJ+1):
            print("%s\t%s" %((i, j), line))
    elif key == 'b':
        j = record[2]
        for i in range(maxI + 1):
            print("%s\t%s" %((i, j), line))
    else:
        pass
    