#!/usr/bin/env python3

import sys
import numpy as np
from collections import OrderedDict

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
	#print(a, "requires", b)
	if b not in requirements[a]:
		requirements[a].append(b)

requirements = OrderedDict(sorted(requirements.items(), key=lambda t: t[0]))
workers = [''] * 5
print(workers)

def get_free_worker():
	for i in range(0,5):
		if workers[i] == '':
			return i

answer = []
second = 0
while True:
	finished = True
	for i, r in requirements.items():
		if r == []:
			answer.append(i)
			#print("removing all", i)
			# remove this item from all requirements
			for ii,rr in requirements.items():
				if i in requirements[ii]:
					requirements[ii].remove(i)
					# annoying python changes type to none if list is empty
					if requirements[ii] == None:
						requirements[ii] = []
			requirements.pop(i)
			finished = False
			break
	if finished:
		break
	print(workers)
	second += 1

print("Answer 1:", ''.join(answer))
