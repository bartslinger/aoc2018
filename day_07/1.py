#!/usr/bin/env python3

import sys
import numpy as np

# Import data
filename = 'input'
if (len(sys.argv) > 1):
	filename = sys.argv[1]
f = open(filename, 'r')
lines = f.readlines()
f.close()

requirements = {}

for line in lines:
	# a requires b
	a = line[36:37]
	b = line[5:6]
	if a not in requirements:
		requirements[a] = []
	if b not in requirements:
		requirements[b] = []
	print(a, "requires", b)
	if b not in requirements[a]:
		requirements[a].append(b)

print(requirements)
