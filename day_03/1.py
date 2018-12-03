#!/usr/bin/env python3

import re
import numpy as np

# Import data
f = open('input', 'r')
lines = f.read().splitlines()
f.close()

patches = {}

sz = [1000, 1000]
#lines = ['#1 @ 1,3: 4x5']
for line in lines:
	matchObj = re.match(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
	g = matchObj.group
	patches[g(1)] = {'x': int(g(2)), 'y': int(g(3)), 'width': int(g(4)), 'height': int(g(5))}
	# check if rectangle is bigger
	xmax = patches[g(1)]['x'] + patches[g(1)]['width']
	ymax = patches[g(1)]['y'] + patches[g(1)]['height']
	if xmax > sz[0]:
		sz[0] = xmax
	if ymax > sz[1]:
		sz[1] = ymax

# create array of zeros
rect = np.zeros(sz)

for id, p in patches.items():
	for i in range(0, p['width']*p['height']):
		x = p['x'] + (i%p['width'])
		# damn, so difficult to do c-style integer division
		y = p['y'] + int(np.floor(i/p['width']))
		rect[x,y] += 1

# go through the patches again, but now check which one reads only 1's
# ugly copy
for id, p in patches.items():
	found = True
	for i in range(0, p['width']*p['height']):
		x = p['x'] + (i%p['width'])
		y = p['y'] + int(np.floor(i/p['width']))
		if rect[x,y] > 1:
			found = False
	if found:
		print("Unique patch ID:",id)

r = [s for s in rect.flatten() if s > 1]
print("Number of squares:",len(r))
