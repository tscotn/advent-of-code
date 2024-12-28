from pathlib import Path
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')


lines = []
with p.open('r') as f:
    lines = [line.strip() for line in f.readlines()]

neighbors = {
    '^': (-1,0),
    'v': (1,0),
    '<': (0,-1),
    '>': (0,1)
}

opposites = {
    '^': 'v',
    'v': '^',
    '>': '<',
    '<': '>'
}

dist = {}
prev = {}
Q = []
target = []
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if lines[row][col] != '#':
            for dir in neighbors.keys():
                dist[(row, col, dir)] = float('inf')
                prev[(row, col, dir)] = None
                Q.append((row, col, dir))
                
                if lines[row][col] == 'S':
                    dist[(row, col, '>')] = 0
                    
                if lines[row][col] == 'E':
                    target.append((row, col, dir))

def edge_cost(dir, new_dir):
    if opposites[dir] == new_dir:
        return float('inf')
    return 1 if dir == new_dir else 1001

# print(Q)

while Q:
    row, col, dir = min(Q, key=lambda x: dist[x]) #this is slow as beans
    Q.remove((row, col, dir))
    
    for new_dir, coord in neighbors.items():
        r, c = coord
        # print(row+r, col+c, dir)
        if 0 <= row+r < len(lines) and 0 <= col+c < len(lines[0]) and lines[row+r][col+c] != '#':
            alt = dist[(row, col, dir)] + edge_cost(dir, new_dir)
            # print('checking', row+r, col+c, 'from', row, col, 'with alt dist', alt)
            if alt < dist[(row+r, col+c, new_dir)]:
                dist[(row+r, col+c, new_dir)] = alt
                prev[(row+r, col+c, new_dir)] = (row, col, dir)

# print(dist)

for t in target:
    print(dist[t])
    
# print(prev)