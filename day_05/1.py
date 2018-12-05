#!/usr/bin/env python3

import sys
import re
from datetime import datetime
import numpy as np

# Import data
filename = 'input'
if (len(sys.argv) > 1):
	filename = sys.argv[1]
f = open(filename, 'r')
line = []
line[:0] = f.read().strip()
f.close()

# Convert characters to numbers
numbers = [ord(c) for c in line]

def remaining_length(numbers):
	# Iterate over polymer
	length = len(numbers)
	active = np.ones(length, dtype=int)
	prev = 0
	for cur in range(1,len(numbers)):
		if prev < 0:
			prev = cur
			continue
		diff = abs(numbers[cur] - numbers[prev])
		if diff == 32:
			# set these two to inactive
			active[cur] = 0
			active[prev] = 0
			length -= 2
			while active[prev] == 0 and prev >= 0:
				prev -= 1
				if prev < 0:
					break
		else:
			prev = cur

	return length

print("Answer 1:", remaining_length(numbers))

lengths = [0] * 26
for i in range(0,26):
	nums_stripped = [n for n in numbers if n != 65+i and n != 65+32+i]
	lengths[i] = remaining_length(nums_stripped)
	print(chr(i+65+32), lengths[i])

min_idx = np.argmin(lengths)
print("Answer 2:", chr(min_idx+65), lengths[min_idx])
