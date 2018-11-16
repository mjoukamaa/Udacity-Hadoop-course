#!/usr/bin/python

"""
Reducer calculates average answer length in
relation to length of question answers have
been posted under.
"""

import sys

# Initialize variables for holding keys
# (ie. question ids), question and answer
# lengths plus number of answers per question
questionLength = 0
answerLengthTotal = 0
answerCounter = 0
oldKey = None

# Loop through keys and their values
for line in sys.stdin:
    data = line.strip().split("\t")

    if len(data) != 3:
        # Something has gone wrong, skip this line
        continue

    thisKey, postType, postLength = data

    # Note when reducer moves to new key
    if oldKey and oldKey != thisKey:

        # Calculate average answer length
        # to question if there are any answers,
        # output question id, question length,
        # and average answer length
        if answerCounter > 0:
            answerLengthAvg = answerLengthTotal / answerCounter
            print("{0}\t{1}\t{2}".format(oldKey, questionLength, answerLengthAvg))

        # If no answers, output question id,
        # question length and zero for average
        # answer length
        else:
            print("{0}\t{1}\t{2}".format(oldKey, questionLength, answerLengthTotal))

        # Reset holding variables
        # for next key
        oldKey = thisKey
        answerLengthTotal = 0
        answerCounter = 0

    # Process current key-value pair
    oldKey = thisKey

    try:
        # Record length by post type,
        # increase counter for answers
        if postType == 'question':
            questionLength = int(postLength)
        elif postType == 'answer':
            answerLengthTotal += int(postLength)
            answerCounter += 1
    except:
        continue

# When exiting loop, repeat average
# answer length calculation and output
# process for last question id
if oldKey != None:

    if answerCounter > 0:
        answerLengthAvg = answerLengthTotal / answerCounter
        print("{0}\t{1}\t{2}".format(oldKey, questionLength, answerLengthAvg))

    else:
        print("{0}\t{1}\t{2}".format(oldKey, questionLength, answerLengthTotal))
