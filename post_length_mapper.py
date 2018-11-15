#!/usr/bin/python

"""
Mapper reads through forum posts of predefined format, determines if they
are questions (ie. starting posts of thread) or other posts, then
outputs thread id, post type, and post length in characters.
"""

import sys
import csv

# Read in input to be processed and loop through it
reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

    # Check to see if post is question, output id, type and length if so
    if line[5] == 'question':
        question_id = line[0]
        post_type = line[5]
        post_length = len(line[4])

        print("{0}\t{1}\t{2}".format(question_id, post_type, post_length))

    # Otherwise if post is answer, output id of its parent question, type and length
    elif line[5] == 'answer':
        question_id = line[6]
        post_type = line[5]
        post_length = len(line[4])

        print("{0}\t{1}\t{2}".format(question_id, post_type, post_length))

    # Disregard other types of posts
    else:
        continue
