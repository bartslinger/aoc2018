#!/usr/bin/env python3

import sys
import numpy as np
import re

# Import data
filename = 'input'
if (len(sys.argv) > 1):
	filename = sys.argv[1]
f = open(filename, 'r')
lines = f.readlines()
f.close()


lights = []
for line in lines:
	line = line.strip().replace('<', ',').replace('>', ',').split(',')
	light = {'x': int(line[1]), 'y': int(line[2]),'vx': int(line[4]), 'vy': int(line[5])}
	lights.append(light)

def show_letter(letter):
	for row in letter:
		str1 = ''.join(str(e) for e in row)
		str1 = str1.replace('0', ' ')
		str1 = str1.replace('1', '#')
		print(str1)

def show_sky(steps):
	global lights
	coords = np.zeros((len(lights),2), dtype=int)
	for i in range(0, len(lights)):
		l = lights[i]
		coords[i,:] = [l['x'] + steps * l['vx'], l['y'] + steps * l['vy']]
	print(min(coords[:,1]), max(coords[:,1]))
	coords -= [min(coords[:,0]), min(coords[:,1])]
	letters_per_row = 20
	for l in range(min(coords[:,0]), max(coords[:,0]), 6*letters_per_row):
		# print one letter
		letter = np.zeros([10,6*letters_per_row], dtype=int)
		cc = [c for c in coords if c[0] >= l and c[0] < l+6*letters_per_row]
		for c in cc:
			letter[c[1], c[0]-l] = 1
		show_letter(letter)

show_sky(10136)
exit(0)

# iterate until only 8 values of y are present
for i in range(10127, 10150):
	y_values = set()
	for l in lights:
		y = l['y'] + i * l['vy']
		y_values.add(y)
	print(i, len(y_values))
	if len(y_values) == 8:
		print(i)
		show_sky(i)
		exit(0)
