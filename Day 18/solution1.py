from pathlib import Path
import re
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

walls = []
l = 70
n_bytes = 0
with p.open('r') as f:
    for line in f.readlines():
        n_bytes += 1
        walls.append(tuple(reversed([int(x) for x in re.findall(r'\d+', line)])))
        if n_bytes == 3000: #let's binary search it lol
            break

#between 3000 and 3002

dirs = [(0,1),(1,0),(-1,0),(0,-1)]
dist = {}
prev = {}
Q = []
for row in range(l+1):
    for col in range(l+1):
        dist[(row, col)] = float('inf')
        prev[(row, col)] = None
        Q.append((row, col))
dist[(0,0)] = 0

while Q:
    row, col = min(Q, key=lambda x: dist[x])
    Q.remove((row, col))
    
    for d in dirs:
        r, c = d
        if 0 <= row+r <= l and 0 <= col+c <= l and (row+r, col+c) not in walls:
            alt = (dist[(row, col)] + 1)
            print(row, col, r, c, dist[(row+r, col+c)])
            if alt < dist[(row+r, col+c)]:
                dist[(row+r, col+c)] = alt
                prev[(row+r, col+c)] = (row, col)
            
print(dist[(l,l)])

# for row in range(l+1):
#     r = ''
#     for col in range(l+1):
#         r += '#' if (row, col) in walls else '.'
#     print(r)