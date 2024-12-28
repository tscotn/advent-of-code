from pathlib import Path
import heapq
from collections import deque
import sys
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')


grid = []
with p.open('r') as f:
    grid = [[l for l in line.strip()] for line in f.readlines()]

# walls = set()
start = None
end = None
for row, line in enumerate(grid):
    for col, l in enumerate(line):
        row, col = int(row), int(col)
        # if l == '#':
        #     walls.add((row, col))
        if l == 'S':
            start = (row, col)
        elif l == 'E':
            end = (row, col)

dirs = [(0,1),(1,0),(-1,0),(0,-1)]

def dijkstras():
    dist = {}
    prev = {}
    Q = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            dist[(row, col)] = float('inf')
            prev[(row, col)] = None
            if (row, col) == start:
                heapq.heappush(Q, (0, row, col))
            else:
                heapq.heappush(Q, (float('inf'), row, col))
    dist[start] = 0

    while Q:
        _, row, col = heapq.heappop(Q)
        
        for d in dirs:
            r, c = d
            if 0 <= row+r < len(grid) and 0 <= col+c < len(grid[0]) and grid[row+r][col+c] != '#':
                alt = (dist[(row, col)] + 1)
                # print(row, col, r, c, dist[(row+r, col+c)])
                if alt < dist[(row+r, col+c)]:
                    dist[(row+r, col+c)] = alt
                    prev[(row+r, col+c)] = (row, col)
                    heapq.heappush(Q, (alt, row+r, col+c))
    return dist

dists = dijkstras()
print('min w/out cheats:', dists[end])

s = 0
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == '#':
            # for a, b in [((-1,0), (0,1)), ((-1,0), (1,0)), ((-1,0), (0,-1)), ((0,-1), (0,1)), ((0,1), (1,0)), ((0,-1), (1,0))]:
            for a, b in [((-1,0), (1,0)), ((0,-1), (0,1))]:
                r_a, c_a = a
                r_b, c_b = b
                if 0 <= row+r_a < len(grid) and 0 <= col+c_a < len(grid[0]) and 0 <= row+r_b < len(grid) and 0 <= col+c_b < len(grid[0]):
                    if grid[row+r_a][col+c_a] in '.SE' and grid[row+r_b][col+c_b] in '.SE':
                        new_dist = (dists[end] - max(dists[(row+r_a, col+c_a)], dists[(row+r_b, col+c_b)])) + 2 + min(dists[(row+r_a, col+c_a)], dists[(row+r_b, col+c_b)])
                        if new_dist+100 <= dists[end]:
                            print('cheat at', row, col, 'w/ dist', new_dist, 'saves', dists[end] - new_dist, 's')
                            s+=1
                    
            # print(row, col) 
print(s)
#1385 is low lol
#6966 is high ahhh