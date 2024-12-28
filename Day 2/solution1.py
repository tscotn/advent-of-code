from pathlib import Path
import functools

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()

def check_safe(l):
    a = l[0]
    for b in l[1:]:
        if not (1 <= abs(a-b) <= 3):
            return False
        a = b
    return True

def check(l):
    increasing = sorted(l) == l
    decreasing = sorted(l, reverse=True) == l 
    safe = check_safe(l)#functools.reduce(lambda a, b: 1 <= abs(a-b) <= 3, l)
    print(l, increasing, decreasing, safe)
    return (increasing or decreasing) and safe
            
c = 0
for l in lines:
    l = l.split(' ')
    c += check([int(s) for s in l])
    
print(c)