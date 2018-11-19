#!/usr/bin/python

import sys

nodeIds = []
oldKey = None

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisValue = data
    if oldKey and oldKey != thisKey:

        numberHits = len(nodeIds)
        distinctIds = set(nodeIds)
        distinctIds = sorted(list(distinctIds))

        print("{0}\t{1}\t{2}".format(oldKey, numberHits, distinctIds))

        oldKey = thisKey
        nodeIds = []


    oldKey = thisKey

    try:
        nodeIds.append(int(thisValue))

    except:
        continue

if oldKey != None:

    numberHits = len(nodeIds)
    distinctIds = set(nodeIds)
    distinctIds = sorted(list(distinctIds))

    print("{0}\t{1}\t{2}".format(oldKey, numberHits, distinctIds))
