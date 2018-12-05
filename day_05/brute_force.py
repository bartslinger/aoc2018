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
print(numbers)

while True:
	startlen = len(numbers)
	for i in range(0, len(numbers)-1):
		diff = abs(numbers[i+1] - numbers[i])
		if diff == 32:
			del numbers[i:i+2]
			print(startlen-2)
			break
	endlen = len(numbers)
	if startlen == endlen:
		break
print(numbers)
print(len(numbers))
