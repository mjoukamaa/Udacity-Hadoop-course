#!/usr/bin/python

import sys
from collections import Counter

# Initialize variables for holding keys and values
valuesList = []
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

        # Determine what value appears most often with
        # given key and how many times, then print it
        valuesList = Counter(valuesList).most_common()
        highestValue = valuesList[0][0]
        highestCount = valuesList[0][1]
        print("{0}\t{1}".format(oldKey, highestValue))

        # Check to see if any other values
        # appear as often as highestCount
        for item in valuesList[1:]:

            if item[1] == highestCount:
                print("{0}\t{1}".format(oldKey, item[0]))

            else:
                break

        # Reset valuesList for new key
        oldKey = thisKey
        valuesList = []

    # Process current key-value pair
    oldKey = thisKey
    valuesList.append(thisValue)


# When exiting loop print, perform same
# determine-print-process for last key
if oldKey != None:

    valuesList = Counter(valuesList).most_common()
    highestValue = valuesList[0][0]
    highestCount = valuesList[0][1]

    print("{0}\t{1}".format(oldKey, highestValue))

    for item in valuesList[1:]:

        if item[1] == highestCount:
            print("{0}\t{1}".format(oldKey, item[0]))

        else:
            break
