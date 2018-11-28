#!/usr/bin/python

"""
For each data point processed, mapper determines
its type (user info/forum post), then outputs
user/post id as key and as value type plus actual
information.
"""

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:

    # Identify user info by number of fields,
    # use != to exclude header row of data
    if len(line) == 5 and line[0] != 'user_ptr_id':
        output_line = [line[0]] + ['user'] + line[1:]
        writer.writerow(output_line)

    # Identify forum posts by number of fields,
    # use != to exclude header row of data
    elif len(line) == 19 and line[0] != 'id':
        output_line = [line[3]] + ['post'] + line[:3] + line[5:10]
        writer.writerow(output_line)

    # Ignore data points with number of fields
    # differing from user info or forum posts
    else:
        continue
