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

# Iterate over polymer
length = len(numbers)
active = np.ones(length, dtype=int)
inactive = np.zeros(length, dtype=int)
prev = 0
for cur in range(1,len(numbers)):
	diff = abs(numbers[cur] - numbers[prev])
	if diff == 32:
		# set these two to inactive
		print("removing", line[cur], line[prev])
		active[cur] = 0
		active[prev] = 0
		inactive[cur] = 1
		inactive[prev] = 1
		length -= 2
		while active[prev] == 0:
			prev -= 1
	else:
		prev = cur

print(length)
idc = active.nonzero()[0].tolist()
res = [line[i] for i in idc]
res = ''.join(res)
print(res)
#print(len(numbers), "-", len(res))
