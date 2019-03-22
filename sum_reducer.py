#!/usr/bin/python

"""
Reducer outputs for each key the total sum
of numerical values associated with it.
"""

import sys

# Initialize variables for holding keys and values
valueTotal = 0
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
        
        # Print total sum for previous key
        print("{0}\t{1}".format(oldKey, valueTotal))
        
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

# When exiting loop print total sum for last key
if oldKey != None:
    print("{0}\t{1}".format(oldKey, valueTotal))
