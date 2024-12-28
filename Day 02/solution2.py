from pathlib import Path

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

def check(t):
    for i in range(len(t)):
        l = t[:i]+t[i+1:]
        increasing = sorted(l) == l
        decreasing = sorted(l, reverse=True) == l 
        safe = check_safe(l)
        print(l, increasing, decreasing, safe)
        if (increasing or decreasing) and safe:
            return True
    return False
            
c = 0
for l in lines:
    l = l.split(' ')
    c += check([int(s) for s in l])
    
print(c)