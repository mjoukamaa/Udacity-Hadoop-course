#!/usr/bin/python

"""
For each key, mapper counts the number of values
associated with it, then prints out the ten keys
with largest number values associated with them.
"""

import sys

# Initialize variables for holding keys, values, and value number count
valuesList = []
topList = []
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
        
        # Determine number of values of associated
        # with previous key, store into valuesList
        topList.append((len(valuesList),oldKey))
        
        # Reset valuesList for new key
        oldKey = thisKey
        valuesList = []

    # Process current key-value pair
    oldKey = thisKey
    valuesList.append(thisValue)

# When exiting loop, determine number of values
# associated with last key, store into valuesList
if oldKey != None:
    topList.append((len(valuesList),oldKey))

# Print top ten keys with most
# values associated with them
for item in sorted(topList, reverse = True)[:10]:
    print("{0}\t{1}".format(item[1], item[0]))
