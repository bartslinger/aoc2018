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

input = [int(l) for l in lines[0].strip().split(' ')]

def get_metadata(idx):
	val = 0
	child_nodes = input[idx]
	meta_len = input[idx+1]
	idx += 2
	child_values = []

	if child_nodes == 0:
		val = sum(input[idx:idx+meta_len])

	else:
		for n in range(0, child_nodes):
			idx, child_val = get_metadata(idx)
			child_values.append(child_val)
		node_meta = input[idx:idx+meta_len]
		for i in node_meta:
			i = i - 1 # make index zero based
			if i < len(child_values):
				val += child_values[i]
	idx += meta_len
	return idx, val

idx, val = get_metadata(0)
print("Answer 2:", val)
