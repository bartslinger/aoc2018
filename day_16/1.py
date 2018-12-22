#!/usr/bin/env python3

import sys
import numpy as np

def read_input(inputfile='input'):
    f = open(inputfile,'r')
    lines = f.readlines()
    f.close()
    return lines

def addr(r, a, b, c):
    r[c] = r[a] + r[b]

def addi(r, a, b, c):
    r[c] = r[a] + b

def mulr(r, a, b, c):
    r[c] = r[a] * r[b]

def muli(r, a, b, c):
    r[c] = r[a] * b

def banr(r, a, b, c):
    r[c] = r[a] & r[b]

def bani(r, a, b, c):
    r[c] = r[a] & b

def borr(r, a, b, c):
    r[c] = r[a] | r[b]

def bori(r, a, b, c):
    r[c] = r[a] | b

def setr(r, a, b, c):
    r[c] = r[a]

def seti(r, a, b, c):
    r[c] = a

def gtir(r, a, b, c):
    r[c] = 1 if a > r[b] else 0

def gtri(r, a, b, c):
    r[c] = 1 if r[a] > b else 0

def gtrr(r, a, b, c):
    r[c] = 1 if r[a] > r[b] else 0

def eqir(r, a, b, c):
    r[c] = 1 if a == r[b] else 0

def eqri(r, a, b, c):
    r[c] = 1 if r[a] == b else 0

def eqrr(r, a, b, c):
    r[c] = 1 if r[a] == r[b] else 0


opcodes = [
        addr,
        addi,
        mulr,
        muli,
        banr,
        bani,
        borr,
        bori,
        setr,
        seti,
        gtir,
        gtri,
        gtrr,
        eqir,
        eqri,
        eqrr]

class Sample:
    def __init__(self):
        self.before = []
        self.after = []
        self.i = -1
        self.a = -1
        self.b = -1
        self.c = -1
    
    def find_matches(self, funs):
        matches = [0] * len(funs)
        for idx, fun in enumerate(funs):
            inp = self.before.copy()
            fun(inp, self.a , self.b, self.c)
            if inp == self.after:
                matches[idx] = 1
        return matches

    def __repr__(self):
        return "--Sample--\nBefore: " + str(self.before) + "\nAfter: " + str(self.after) + "\nInput: " + str(self.i) + " " + str(self.a) + " " + str(self.b) + " " + str(self.c)

def parse_samples(lines):
    samples = []
    for line in lines:
        if line[0] == 'B':
            before = line.strip().replace(']', '').replace('[', ',').split(',')
            sample = Sample()
            sample.before = [int(i) for i in before[1:5]]
        elif line[0] == 'A':
            after = line.strip().replace(']', '').replace('[', ',').split(',')
            sample.after = [int(i) for i in after[1:5]]
            samples.append(sample)
        elif line[0] == '\n':
            pass
        else:
            inp = [int(i) for i in line.strip().split(' ')]
            sample.i = inp[0]
            sample.a = inp[1]
            sample.b = inp[2]
            sample.c = inp[3]
    return samples

if __name__ == "__main__":
    filename = 'input'
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    lines = read_input(filename)
    samples = parse_samples(lines)
    cnt = 0
    all_matches = {}
    print(all_matches)
    for s in samples:
        if s.i not in all_matches.keys():
            all_matches[s.i] = []
        matches = s.find_matches(opcodes)
        all_matches[s.i].append(matches)
        if sum(matches) >= 3:
            cnt += 1
    print("Answer 1:", cnt)

    opcode_by_idx = [-1] * len(opcodes)
    start = np.ones((1,len(opcodes)), dtype=int)
    for i in range(16):
        for key in all_matches.keys():
            counting = start 
            counter = 1
            for m in all_matches[key]:
                counting = counting + np.array(m)
                counter += 1
                #print(counting)
            # see if there was a unique one
            number = len([e for e in counting[0] if e == counter])
            if number == 1:
                oc = np.argmax(counting[0])
                #print("FOUND", key, oc)
                opcode_by_idx[key] = opcodes[oc]
                start[0][oc] = 0
                break
    #print(opcode_by_idx)

    # now we got the opcodes, lets run the test program
    f = open('testprog', 'r')
    lines = f.readlines()
    f.close()

    register = [0, 0, 0, 0]
    for line in lines:
        l = line.strip().split(' ')
        l = [int(l) for l in l]
        opcode_by_idx[l[0]](register, l[1], l[2], l[3])
    print("Answer 2:", register)
