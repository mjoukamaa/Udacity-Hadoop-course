#!/usr/bin/python

"""
Reducer sums up numerical values associated with each
key into totals, then prints out the highest total
and the key associated with it.
"""

import sys

# Initialize variables for holding keys and value totals
valueTotal = 0
highestTotal = 0
oldKey = None
highestKey = None

# Loop through key-value pairs
for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        # Something has gone wrong, skip this line
        continue

    thisKey, thisValue = data

    # Note when reducer moves to new key
    if oldKey and oldKey != thisKey:

        # Determine if final total associated
        # with key is highest so far
        if valueTotal > highestTotal:
            highestTotal = valueTotal
            highestKey = oldKey

        # Reset valueTotal for new key
        oldKey = thisKey
        valueTotal = 0

    # Process current key-value pair,
    # ignore values that can't be summed
    oldKey = thisKey
    try:
        valueTotal += float(thisValue)
    except:
        continue

# When exiting loop, check if final total
# associated with last key is highest
if oldKey != None:

    if valueTotal > highestTotal:
        highestTotal = valueTotal
        highestKey = oldKey

# Print highest total and key associated with it
print("{0}\t{1}".format(highestKey, highestTotal))
