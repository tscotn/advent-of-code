from pathlib import Path
import re
from collections import defaultdict

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()
    
start = None
for i, line in enumerate(lines):
    for j, l in enumerate(line):
        if l == '^':
            start = (i, j, '^')
            # lines[i][j] = '.'
            break
# print(start)

dir_map = {
    '^': (-1, 0, '>'),
    '>': (0, 1, 'v'),
    'v': (1, 0, '<'),
    '<': (0, -1, '^'),
}

done = False
visited = set()
try:
    while not done:
        i, j, d = start
        visited.add((i, j))
        a, b, d_1 = dir_map[d]
        if lines[i+a][j+b] != '#':
            start = (i+a, j+b, d) #advance
            if not (0 <= i+a <= len(lines) and 0 <= j+b <= len(lines[0])): #unless advancing would 
                raise Exception("yeesh")
        else:
            start = (i, j, d_1)
except Exception as e:
    print(e, i, j)
    print(len(visited))