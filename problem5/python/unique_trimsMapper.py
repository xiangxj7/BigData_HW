#!/usr/bin/env python

import json
import sys


for line in sys.stdin:
    line = line.strip()

    record = json.loads(line)
    key, value = record[0], record[1]

    print("%s\t%s" % (value[:-10], key))