#!/usr/bin/python

import sys

# Initialize variables for holding keys and values
nodeIds = []
oldKey = None

# Loop through key-value pairs
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong, skip this line
        continue

    thisKey, thisValue = data
    
    # Note when reducer moves to new key
    if oldKey and oldKey != thisKey:

        # Determine how many times current word 
        # appears (incl. multiple hits in one post)
        numberHits = len(nodeIds)
        # Use set() to get only distinct forum posts
        # current word appears in
        distinctIds = set(nodeIds)
        # Sort distinct posts for more usable index
        distinctIds = sorted(list(distinctIds))

        print("{0}\t{1}\t{2}".format(oldKey, numberHits, distinctIds))

        # Reset nodeIds for new key
        oldKey = thisKey
        nodeIds = []


    oldKey = thisKey

    try:
        nodeIds.append(int(thisValue))

    except:
        continue


# When exiting loop, perform index building process for last word
if oldKey != None:

    numberHits = len(nodeIds)
    distinctIds = set(nodeIds)
    distinctIds = sorted(list(distinctIds))

    print("{0}\t{1}\t{2}".format(oldKey, numberHits, distinctIds))
