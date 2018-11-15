#!/usr/bin/python

"""
This mapper reads through forum posts of predefined format and splits their message
body into separate words by space, punctuation or certain special characters. It
outputs separated words as keys and post ids as values.
"""

import sys
import csv
import re

# Define characters to split text on
split_chars = re.compile(r'[\s\.,!\?:;"\(\)<>\[\]#\$=\-/]')

# Read in input to be processed and loop through it
reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    # Split text part of forum post (line[4]) and print
    # each splitted part with forum post id (line[0])
    try:
        for word in (re.split(split_chars, line[4])):
            print("{0}\t{1}".format(word.lower(), line[0]))

    # Ignore lines that don't split as expected
    except:
        continue
