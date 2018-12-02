#!/usr/bin/env python3

from collections import OrderedDict
import string
from operator import mul
from functools import reduce

# Import data
f = open('input', 'r')
lines = f.read().splitlines()
f.close()

# Test

#lines = ['abcdef',
#         'bababc',
#         'abbcde',
#         'abcccd',
#         'aabcdd',
#         'abcdee',
#         'ababab']

# numbers to count
sz = len(lines[0])

counters = [0] * sz

for line in lines:
	# create histogram of each line
	histogram = OrderedDict((c,0) for c in string.ascii_lowercase)
	for c in line:
		histogram[c] += 1

	linecounters = []
	# add counts to global counter
	for l in histogram:
		cnt = histogram[l]
		if cnt not in linecounters and cnt > 1:
			linecounters.append(cnt)

	# Add to the global counter
	for l in linecounters:
		counters[l] += 1


# Multiply all
multipliers = [c for c in counters if c > 0]
print(multipliers)

product = reduce(mul,multipliers,1)
print("Answer:",product)
