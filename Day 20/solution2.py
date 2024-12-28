from pathlib import Path
import heapq
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

grid = []
with p.open('r') as f:
    grid = [[l for l in line.strip()] for line in f.readlines()]

start = None
end = None
for row, line in enumerate(grid):
    for col, l in enumerate(line):
        row, col = int(row), int(col)
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

def get_pairs():
    pairs = set()
    for i in range(0,20):
        for j in range(-20,20):
            if -20 <= (i + j) <= 20 and (i,j) != (0,0):
                pairs.add(((0,0), (i,j)))
    return pairs

pairs = get_pairs()

def in_bounds(row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

s = 0
# cheats = {}
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] in '.SE':
            for r in range(-20, 21):
                for c in range(-20, 21):
                    steps = abs(r) + abs(c)
                    if steps <= 20:
                        if in_bounds(row+r, col+c) and grid[row+r][col+c] in '.SE' and dists[(row+r, col+c)] > dists[(row, col)] and (row, col) != (row+r, col+c):
                            saves = dists[end] - (dists[end] - dists[(row+r, col+c)] + dists[(row, col)] + steps)
                            if saves >= 100:
                                s+=1
                                print('cheat', row ,col, 'to', row+r, col+c, 'saves', saves)
                                # cheats[saves] = cheats.get(saves, 0) + 1
#try...888947  or 885891



                            
#got 1007876 but it's also wrong
#this gives 2263831...which is higher than something that was too high
print(s)
#test: 7225 possible cheats

# print(len(possible_cheats))
#max max 89576760...this is how many ordered pairs there are

#what am I counting that I shouldn't be counting?
# for row in range(len(grid)):
#     for col in range(len(grid[0])):
#         if grid[row][col] in '.SE':
#             for pair in pairs:
#                 a, b = pair
#                 r_a, c_a = a
#                 r_b, c_b = b
#                 if ((row+r_a, col+c_a), (row+r_b, col+c_b)) not in checked:
#                     n_checked+=1
#                     if in_bounds(row+r_a, col+c_a) and in_bounds(row+r_b, col+c_b):
#                         if grid[row+r_a][col+c_a] in '.SE' and grid[row+r_b][col+c_b] in '.SE':
#                             new_dist = (dists[end] - max(dists[(row+r_a, col+c_a)], dists[(row+r_b, col+c_b)])) + (abs(r_b)+abs(c_b)) + min(dists[(row+r_a, col+c_a)], dists[(row+r_b, col+c_b)])
#                             if dists[end] - new_dist >= 50:
#                                 s+=1
#                                 print(s, n_checked)
#                                 # print('cheat for', r_b+c_b, 'w/ dist', new_dist, 'saves', dists[end] - new_dist, 's')
#                                 # cheats[dists[end] - new_dist] = cheats.get(dists[end] - new_dist, []) + [((row+r_a, col+c_a), (row+r_b, col+c_b))]
#                     checked.add(((row+r_a, col+c_a), (row+r_b, col+c_b)))
#                     checked.add(((row+r_b, col+c_b), (row+r_a, col+c_a)))
                    
#1635630, 1636080 are too high!!!

            # print(row, col) 
# cheats_sorted = []
# for i,j in cheats.items():
#     cheats_sorted += [(i, j)]
    
# cheats_sorted.sort()
# for time, pairs in cheats_sorted:
#     print(time, pairs)
    # print(time, len(pairs))
    # for pair in pairs:
        # start, end = pair
        # print('\tfrom', start, dists[start],'to', end, dists[end], 'in', abs(end[0]-start[0]) + abs(end[1] - start[1]),'steps')
# print(len(pairs))
#1385 is low lol
#6966 is high ahhh

#find all unique pairs that are within 20 taxicab distance

# print(32 + 31 + 29 + 39 + 25 + 23 + 20 + 19 + 12 + 14 + 12 + 22 + 4 + 3)