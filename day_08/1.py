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

meta = np.array([],dtype=int)

def get_metadata(idx):
	global meta
	child_nodes = input[idx]
	meta_len = input[idx+1]
	idx += 2
	for n in range(0, child_nodes):
		idx = get_metadata(idx)
	meta = np.concatenate((meta, input[idx:idx+meta_len]), axis=0)
	idx += meta_len
	return idx

get_metadata(0)
print(sum(meta))
