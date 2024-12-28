from pulp import *
from pathlib import Path
import re
from math import exp, log, gcd
import numpy as np
test = True
# test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

def simple_linear_diophantine_r(a, b):
    q, r = divmod(a, b)
    if r == 0:
        return (0, b)
    else:
        x, y = simple_linear_diophantine_r(b, r)
        return (y, x - q * y)

def solve(X, Y, Prize):
    print(simple_linear_diophantine_r(X[0], Y[0]))
    return 0
    

total = 0
X, Y, Prize = None, None, None
with p.open('r') as f:
    for line in f.readlines():
        if line.startswith("Button A:"):
            X = [int(x) for x in re.findall(r"\d+", line)]
        if line.startswith("Button B:"):
            Y = [int(y) for y in re.findall(r"\d+", line)]
        if line.startswith("Prize:"):
            Prize = [int(p) for p in re.findall(r"\d+", line)]
            
            s = 0
            for i in range(2):
                if Prize[i] % gcd(X[i], Y[i]) == 0:
                    s+=1
                    # print(X[i], Y[i], Prize[i], "has valid solution")
            if s == 2:
                print(X, Y, Prize, "has valid solution")
                t = solve(X, Y, Prize)
                total += t
print(total)