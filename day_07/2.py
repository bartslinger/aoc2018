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

def get_free_worker():
	for i in range(0,len(workers)):
		if workers[i] == '':
			return i
	return None

def remove_from_requirements(letter):
	# remove this item from all requirements
	for ii,rr in requirements.items():
		if letter in requirements[ii]:
			requirements[ii].remove(letter)
			# annoying python changes type to none if list is empty
			if requirements[ii] == None:
				requirements[ii] = []

second = 0
while True:
	new_requirements = requirements.copy()
	for i, r in requirements.items():
		if r == []:
			# add to queue
			worker_id = get_free_worker()
			if worker_id == None:
				break
			workers[worker_id] = i * (ord(i)-65+61)
			new_requirements.pop(i)
	requirements = new_requirements.copy()

	if ''.join(workers) == '':
		break

	# do the work
	print(workers)
	for i, worker in enumerate(workers):
		if worker != '':
			removing = worker[0]
			workers[i] = worker[0:-1]
			# if that was the last one, remove from requirements
			if workers[i] == '':
				print(removing, "that was the last one")
				remove_from_requirements(removing)
	second += 1

print("Seconds:", second)
