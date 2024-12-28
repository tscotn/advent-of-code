from pathlib import Path
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

lines = []
with p.open('r') as f:
    lines = [line[:-1] for line in f.readlines()]
    
dirs = [(-1,0),(1,0),(0,-1),(0,1)]
r_limit = len(lines)
c_limit = len(lines[0])
    
def move_to(r, c, height):
    if int(lines[r][c]) == 9:# and (r,c) not in found:
        # found.add((r,c))
        return 1
    t = 0
    for x, y in dirs:
        r_in = 0 <= r+x < r_limit
        c_in = 0 <= c+y < c_limit
        if r_in and c_in and int(lines[r+x][c+y]) == height+1:
            t += move_to(r+x, c+y, height+1)
    return t
    
total = 0
for r, line in enumerate(lines):
    for c, l in enumerate(line):
        l = int(l)
        if l == 0:
            found = set()
            th = move_to(r, c, l)
            print("trailhead at", r, c, th)
            total += th
print(total)
        
