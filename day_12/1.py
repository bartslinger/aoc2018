#!/usr/bin/env python3

import sys
import numpy as np

initial_state = "#........#.#.#...###..###..###.#..#....###.###.#.#...####..##..##.#####..##...#.#.....#...###.#.####"
#initial_state = "#..#.#..##......###...###"

filename = 'input'
if (len(sys.argv) > 1):
	filename = sys.argv[1]
f = open(filename, 'r')
lines = f.readlines()
f.close()

patterns = []
for l in lines:
	if l[9] == '#':
		patterns.append(list(l.strip()[0:5]))

generations = 20
max_growth = 2 * generations
#initial_state = ".#..."
initial_state = ('.'*max_growth) + initial_state + ('.'*max_growth)
initial_state = list(initial_state)

prev = 0
print(''.join(initial_state))
for z in range(0, generations):
	next_state = ['.'] * len(initial_state)
	for i in range(2, len(initial_state)-2):
		fragment = initial_state[i-2:i+2+1]
		if fragment in patterns:
			next_state[i] = '#'
	#print(''.join(next_state))
	initial_state = next_state

	# find the sum
	total = 0
	for i in range(0, len(initial_state)):
		if initial_state[i] == '#':
			total += i - max_growth

	print(z, total, total-prev)
	prev = total
