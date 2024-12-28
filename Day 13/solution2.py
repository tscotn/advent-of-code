# from pulp import *
from pathlib import Path
import re
from math import exp, log, gcd
import numpy as np
from sympy.solvers.diophantine.diophantine import diop_linear
from sympy.abc import a, b, x, y
from sympy import Eq, symbols
from z3 import *

test = True
# test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')
    
total = 0
X, Y, Prize = None, None, None
with open('input.txt', 'r') as f:
    for line in f.readlines():
        if line.startswith("Button A:"):
            A = [int(x) for x in re.findall(r"\d+", line)]
        if line.startswith("Button B:"):
            B = [int(y) for y in re.findall(r"\d+", line)]
        if line.startswith("Prize:"):
            # Prize = [int(p) for p in re.findall(r"\d+", line)]
            Prize = [10000000000000+int(p) for p in re.findall(r"\d+", line)]
            s = Solver()
            s.add(A[0]*a + B[0]*b == Prize[0])
            s.add(A[1]*a + B[1]*b == Prize[1])
            s.add(a>=0)
            s.add(b>=0)
            c = s.check()
            if c.r == Z3_L_TRUE:
              # print(s.model()[a])
              # print(s.model()[b])
              # print(type(s.model()[a]))
              if s.model()[a].as_long() >= 0 and s.model()[b].as_long() >= 0:
                total += 3*s.model()[a].as_long() + s.model()[b].as_long()
print(total)

#146396443013511
#146396443013491.25
#146396443013491 NOT THIS
#102380168740772

#next try:
#102555168740932