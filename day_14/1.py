#!/usr/bin/env python3

import sys
import numpy as np

def get_score(after):
    num_recepies = after + 11
    r = np.ndarray((num_recepies+1), dtype=int)

    r[0] = 3
    r[1] = 7

    elves = [0, 1]

    head = 1

    while head < num_recepies - 1:
        new_recepy = r[elves[0]] + r[elves[1]]
        #print(new_recepy)
        if new_recepy > 9:
            head += 1
            r[head] = 1
        head += 1
        r[head] = new_recepy % 10

        # move the elves
        elves[0] = (elves[0] + 1 + r[elves[0]]) % (head + 1)
        elves[1] = (elves[1] + 1 + r[elves[1]]) % (head + 1)
        #print(r[0:head+1])
        #print(elves)

    answer = r[after:after+11]
    number = 0
    multiplier = 1000000000
    for i in answer:
        number += multiplier * i
        multiplier //= 10
    return number

assert get_score(9)    == 5158916779 
assert get_score(5)    == 124515891
assert get_score(18)   == 9251071085
assert get_score(2018) == 5941429882
print("Answer 1:", get_score(793061))
