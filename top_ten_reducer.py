#!/usr/bin/python

import sys

valuesList = []
topList = []
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 2:
        # Something has gone wrong, skip this line
        continue

    thisKey, thisValue = data

    if oldKey and oldKey != thisKey:
        topList.append((len(valuesList),oldKey))
        oldKey = thisKey
        valuesList = []

    oldKey = thisKey
    valuesList.append(thisValue)

if oldKey != None:
    topList.append((len(valuesList),oldKey))

for item in sorted(topList, reverse = True)[:10]:
    print("{0}\t{1}".format(item[1], item[0]))
