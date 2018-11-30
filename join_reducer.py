#!/usr/bin/python

"""
For each user id key, reducer determines
type of data (user info/forum post), then
outputs each forum post joined with user
info of post author.
"""

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

# Initialize variables for holding keys and values
oldKey = None
user_info = []
post_info_list = []

# Loop through key-value pairs
for line in reader:

    thisKey = line[0]
    thisValue = line[1:]

    # Note when reducer moves to new key
    if oldKey and oldKey != thisKey:

        # Loop through post stored in
        # post_info_list, join author
        # user info and print each post
        for post in post_info_list:
            final_line = post[:3] + [oldKey] + post[3:8] + user_info
            writer.writerow(final_line)

        # Reset holding variables for new key
        oldKey = thisKey
        user_info = []
        post_info_list = []

    oldKey = thisKey

    # Determine type of data point, store
    # information in appropriate variable
    if thisValue[0] == 'user':
        user_info = thisValue[1:]

    elif thisValue[0] == 'post':
        post_info_list.append(thisValue[1:])

    else:
        continue

# When exiting loop, print posts
# with user info for last user id
if oldKey != None:

    for post in post_info_list:
        final_line = post[:3] + [oldKey] + post[3:8] + user_info
        writer.writerow(final_line)
