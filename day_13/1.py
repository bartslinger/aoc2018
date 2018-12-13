#!/usr/bin/env python3

import sys
import numpy as np
from operator import attrgetter

filename = 'input'
if (len(sys.argv) > 1):
	filename = sys.argv[1]
f = open(filename, 'r')
lines = f.readlines()
f.close()

class TrackNode(object):
	def __init__(self, x, y, section_type):
		self.section_type = section_type
		self.x = x
		self.y = y
		self.nbs = [None, None, None, None]
		self.vehicle = None

	def __repr__(self):
		return repr((self.x, self.y, self.section_type, self.vehicle))

class Vehicle(object):
	def __init__(self, node, orientation):
		self.location = node
		self.orientation = orientation
		self.next_turn = -1 # -1, 0, 1 for left, fwd, right

	def __repr__(self):
		return repr((self.location.x, self.location.y, self.orientation))

	def move(self):
		crashed_into = None
		# check if next location is free
		if self.location.nbs[self.orientation].vehicle != None:
			print("Collision!")
			crashed_into = self.location.nbs[self.orientation].vehicle
		self.location.vehicle = None
		self.location = self.location.nbs[self.orientation]
		self.location.vehicle = self
		assert self.location != None
		if self.location.section_type == '/':
			if self.orientation == 0:
				self.orientation = 1
			elif self.orientation == 1:
				self.orientation = 0
			elif self.orientation == 2:
				self.orientation = 3
			elif self.orientation == 3:
				self.orientation = 2
		if self.location.section_type == '\\':
			if self.orientation == 0:
				self.orientation = 3
			elif self.orientation == 1:
				self.orientation = 2
			elif self.orientation == 2:
				self.orientation = 1
			elif self.orientation == 3:
				self.orientation = 0
		if self.location.section_type == '+':
			self.orientation += self.next_turn
			self.orientation %= 4
			self.next_turn += 1
			if self.next_turn == 2:
				self.next_turn = -1
		if crashed_into != None:
			self.location.vehicle = None
		return crashed_into

# read input
track_nodes = list()
vehicles = list()

width = len(list(lines[0])) - 1
height = len(lines)
print("width:", width, "height:", height)
grid = np.ndarray([height, width], dtype=int)
orientations = '^>v<'
for y in range(0, height):
	l = list(lines[y])
	for x in range(0, width):
		grid[y,x] = -1
		if l[x] in '/-\\+|':
			track_nodes.append(TrackNode(x, y, l[x]))
			grid[y,x] = len(track_nodes)-1
		if l[x] in orientations:
			o = l[x]
			l[x] = l[x].replace('>', '-').replace('<', '-')
			l[x] = l[x].replace('^', '|').replace('v', '|')
			track_nodes.append(TrackNode(x, y, l[x]))
			vehicles.append(Vehicle(track_nodes[-1], orientations.find(o)))
			track_nodes[-1].vehicle = vehicles[-1]
			grid[y,x] = len(track_nodes)-1

def node_at(x,y):
	global track_nodes
	global grid
	if grid[y,x] != None:
		return track_nodes[grid[y,x]]
	else:
		return None

print("connecting the tracks")
# connect the tracks
for n in track_nodes:
	if n.section_type == '+':
		n.nbs = [node_at(n.x, n.y-1), node_at(n.x+1, n.y), node_at(n.x, n.y+1), node_at(n.x-1, n.y)]
	if n.section_type == '|':
		n.nbs = [node_at(n.x, n.y-1), None, node_at(n.x, n.y+1), None]
	if n.section_type == '-':
		n.nbs = [None, node_at(n.x+1, n.y), None, node_at(n.x-1, n.y)]
	if n.section_type == '\\':
		node_left = node_at(n.x-1, n.y)
		if node_left != None:
			if node_left.section_type == '+' or node_left.section_type == '-':
				# north-east corner
				n.nbs = [None, None, node_at(n.x, n.y+1), node_at(n.x-1, n.y)]
				continue
		# south-west corner
		n.nbs = [node_at(n.x, n.y-1), node_at(n.x+1, n.y), None, None]
	if n.section_type == '/':
		node_left = node_at(n.x-1, n.y)
		if node_left != None:
			if node_left.section_type == '+' or node_left.section_type == '-':
				# south-east corner
				n.nbs = [node_at(n.x, n.y-1), None, None, node_at(n.x-1, n.y)]
				continue
		# north-west corner
		n.nbs = [None, node_at(n.x+1, n.y), node_at(n.x, n.y+1), None]

graveyard = TrackNode(-1, -1, '+')

num_vehicles = len(vehicles)
print("Starting with", num_vehicles, "vehicles")
while num_vehicles > 1:
	# sort vehicles by position
	vs = sorted(vehicles, key=attrgetter('location.y', 'location.x'))
	for v in vs:
		if v.location == graveyard:
			pass
		else:
			crashed_into = v.move()
			if crashed_into:
				print(v.location.x, v.location.y, crashed_into)
				v.location = graveyard
				crashed_into.location = graveyard
				num_vehicles -= 2
				print(num_vehicles)

print(vehicles)
