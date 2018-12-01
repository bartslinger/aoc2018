#!/usr/bin/env python3

import time
import numpy as np

f = open('input', 'r')
input = [int(line) for line in f.readlines()]

def get_first_double_freq(input):
	sum = 0
	a = np.array([0])
	while True:
		for line in input:
			sum = sum + int(line)
			i = np.searchsorted(a, sum)
			a = np.insert(a, i, sum)
			if len(a)-1 == i:
				continue
			if a[i+1] == sum:
				print("already seen: ",  sum)
				return sum

test_1_input = [1, -1]
get_first_double_freq(test_1_input)

test_2_input = [3, 3, 4, -2, -4]
get_first_double_freq(test_2_input)

test_3_input = [-6, +3, +8, +5, -6]
get_first_double_freq(test_3_input)

test_4_input = [+7, +7, -2, -7, -4]
get_first_double_freq(test_4_input)

start = time.time()
print("final answer (takes some time):")
print(get_first_double_freq(input))
end = time.time()
print("Elapsed time:", round(end-start,2), "seconds")
