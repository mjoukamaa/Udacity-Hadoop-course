#!/usr/bin/python

import sys

valueTotal = 0
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data
    if oldKey and oldKey != thisKey:
        print("{0}\t{1}".format(oldKey, valueTotal))
        oldKey = thisKey
        valueTotal = 0

    oldKey = thisKey
    valueTotal += float(thisValue)

if oldKey != None:
    print("{0}\t{1}".format(oldKey, valueTotal))
