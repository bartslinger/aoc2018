#!/usr/bin/env python3

import sys
import numpy as np

#r = np.ndarray((999999999), dtype=int)
r = [3, 7]
r[0] = 3
r[1] = 7

elves = [0, 1]

head = 1
to_match = [7,9,3,0,6,1]

def add_one(value):
    global r
    global head
    head += 1
    #r[head] = value
    r.append(value)

    # check for match
    a = r[head-len(to_match):head]
    #print(type(a))
    if np.array_equal(a,np.array(to_match)):
        print(head-len(to_match))
        exit(0)
    if head % 100000 == 0:
        print(head, a)
    #print(a)

#for i in range(0, len(r)-5):
while True:
    new_recepy = r[elves[0]] + r[elves[1]]

    if new_recepy > 9:
        add_one(1)
    add_one(new_recepy % 10)

    # move the elves
    elves[0] = (elves[0] + 1 + r[elves[0]]) % (head + 1)
    elves[1] = (elves[1] + 1 + r[elves[1]]) % (head + 1)
    #print(r[0:head+1])
    #print(elves)
