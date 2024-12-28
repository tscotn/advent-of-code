from pulp import *
from pathlib import Path
import re
test = True
# test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

def solve(A, B, Prize):
    print(A, B, Prize)
# minimize a + b
# (a * 94) + (b * 22) = 8400
# (a * 34) + (b * 67) = 5400

    Lp_prob = LpProblem('Problem', LpMinimize)  
    
    # Create problem Variables  
    a = LpVariable("a", lowBound = 0, cat = "Integer")   # Create a variable x >= 0 
    b = LpVariable("b", lowBound = 0, cat = "Integer")   # Create a variable y >= 0 
    
    # Objective Function 
    Lp_prob += a + b
    
    # Constraints: 
    Lp_prob += (a * A[0]) + (b * B[0]) == Prize[0]
    Lp_prob += (a * A[1]) + (b * B[1]) == Prize[1]

    # print(Lp_prob) 
    
    status = Lp_prob.solve()   # Solver 
    if LpStatus[status] == 'Optimal':  # The solution status 
        # print(value(Lp_prob.objective))
        print("found optimal solution")
        print(value(a), value(b))
        return (3*value(a)) + value(b)

    # print(value(a), value(b), value(Lp_prob.objective))   

total = 0
A = None
B = None
Prize = None
with p.open('r') as f:
    for line in f.readlines():
        if line.startswith("Button A:"):
            A = [int(a) for a in re.findall(r"\d+", line)]
        if line.startswith("Button B:"):
            B = [int(b) for b in re.findall(r"\d+", line)]
        if line.startswith("Prize:"):
            Prize = [int(p) for p in re.findall(r"\d+", line)]
            
            s = solve(A, B, Prize)
            if s != None:
                total += s
                exit()
            
print(total)