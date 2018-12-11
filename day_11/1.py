#!/usr/bin/env python3

import numpy as np

def get_power(x,y,serial):
	rack_id = x + 10
	power_level = rack_id * y
	power_level += serial
	power_level *= rack_id
	power_level %= 1000
	power_level //= 100
	power_level -= 5
	return power_level

assert get_power(3,5,8) == 4
assert get_power(122,79,57) == -5
assert get_power(217,196,39) == 0
assert get_power(101,153,71) == 4

def find_most_power(serial, square_size):
	grid = np.ndarray([300,300], dtype=int)
	for i in range(0,300):
		for j in range(0,300):
			x = j+1
			y = i+1
			grid[i,j] = get_power(x,y,serial)

	# iterate over grid to find most power
	most_power = -10*square_size*square_size
	most_power_x = -1
	most_power_y = -1
	for i in range(0,300-square_size+1):
		for j in range(0,300-square_size+1):
			square = grid[i:i+square_size,j:j+square_size]
			power = sum(sum(square))
			if power > most_power:
				most_power = power
				most_power_x = j+1
				most_power_y = i+1

	return [most_power_x, most_power_y, most_power]

assert find_most_power(18, 3)[0:2] == [33,45]
assert find_most_power(42, 3)[0:2] == [21,61]

# Step 1: build a 300x300 grid with power levels
serial = 1133 # puzzle input
print("Answer 1:", find_most_power(serial, 3))

# 2: Try with all square sizes
for ss in range(1,300):
	most_power = -10*ss*ss
	most_power_location = [0, 0]
	power = find_most_power(serial, ss)
	print(ss, power)
	if power[2] > most_power:
		most_power = power
