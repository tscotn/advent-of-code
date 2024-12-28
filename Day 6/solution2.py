from pathlib import Path
import re
from collections import defaultdict

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = [[l for l in line] for line in f.readlines()]
    
start = None
for i, line in enumerate(lines):
    for j, l in enumerate(line):
        if l == '^':
            start = (i, j, '^')
            break

dir_map = {
    '^': (-1, 0, '>'),
    '>': (0, 1, 'v'),
    'v': (1, 0, '<'),
    '<': (0, -1, '^'),
}

c = 0

for row in range(len(lines)):
    print(row)
    for col in range(len(lines[0])-1):
        # print('testing at', row, col)
        curr = start
        lines_temp = [line.copy() for line in lines]
        lines_temp[row][col] = '#'
        visited_with_direction = set()
        try:
            while True:
                if curr in visited_with_direction: #if we take a step in a direction we've gone before
                    c += 1
                    raise Exception('I\'m going in circles')
                visited_with_direction.add(curr)
                
                i, j, d = curr
                a, b, d_1 = dir_map[d]
                if lines_temp[i+a][j+b] != '#':
                    curr = (i+a, j+b, d) #advance
                    if not (0 <= i+a <= len(lines_temp) and 0 <= j+b <= len(lines_temp[0])): #unless advancing would go out of bounds
                        raise Exception("yeesh")
                else: #or turn
                    curr = (i, j, d_1)
        except Exception as e:
            # print(e, i, j)
            pass
print(c)