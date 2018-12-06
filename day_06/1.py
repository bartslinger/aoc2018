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

coords = np.array([line.strip().split(', ') for line in lines], dtype=int)

grid_size = [max(coords[:,0]) - min(coords[:,0])+1, max(coords[:,1]) - min(coords[:,1])+1]

# shift all items to put origin at 0,0
origin = [min(coords[:,0]), min(coords[:,1])]
coords -= origin

# create the field
grid = -1000*np.ones(grid_size)
counts = np.zeros(len(coords), dtype=int)
safe_area_counter = 0

# iterate the field
for i in range(0, grid_size[0]*grid_size[1]):
	x = i % grid_size[0]
	y = i // grid_size[0]
	# calculate distance to each coordinate
	distances = np.zeros(len(coords), dtype=int)
	for i, c in enumerate(coords):
		distances[i] = abs(c[0] - x) + abs(c[1] - y)
	# total distance (for part two)
	if sum(distances) < 10000:
		safe_area_counter += 1
	# find closest coordinate
	closest = np.argmin(distances)
	if distances.tolist().count(distances[closest]) > 1:
		grid[x,y] = -1
	else:
		grid[x,y] = closest
		counts[closest] += 1

#print(grid.transpose())

# disqualify the edges (they extend to infinity)
edges = np.concatenate((grid[:,0], grid[:,-1], grid.transpose()[:,0], grid.transpose()[:,-1]), axis=0)
qualified = [c for c in range(0,len(coords)) if c not in edges]
#print(qualified)

max_area = counts[qualified[np.argmax([value for index, value in enumerate(counts) if index in qualified])]]
print("Max area:", max_area)
print("Safe area size:", safe_area_counter)
