#!/usr/bin/env python3

import collections

# Import data
f = open('input', 'r')
lines = f.read().splitlines()
f.close()

#lines = ['abcde', 'adcde']
sz = len(lines[0])
linecount = len(lines)

# For each list where one character is left out
for i in range(0, sz):
	newlines = [''] * linecount
	for j in range(0, linecount):
		newlines[j] = lines[j][0:i] + lines[j][i+1:]
	#print(newlines)

	# In newlines, search for duplicates
	duplicates = [item for item, count in collections.Counter(newlines).items() if count > 1]
	if len(duplicates) > 0:
		print(duplicates)
