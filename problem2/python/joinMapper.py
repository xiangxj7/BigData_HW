#!/usr/bin/env python

import json
import sys


for line in sys.stdin:
    line = line.strip()

    record = json.loads(line)
    key, value = record[1], record
    print('%s\t%s' % (key, json.dumps(value)))