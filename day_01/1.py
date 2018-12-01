#!/usr/bin/env python3

f = open('input_1', 'r')
sum = 0
for line in f.readlines():
	sum = sum + int(line)

print(sum)
