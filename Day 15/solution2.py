from pathlib import Path
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

grid = []
movements = ""
making_grid = True
robot_pos = None

double_wide = {
    '#': '##',
    '.': '..',
    'O': '[]',
    '@': '@.'
}

with p.open('r') as f:
    row = 0
    for line in f.readlines():
        if 'END' in line:
            making_grid = False
        elif making_grid:
            grid.append([c for c in ''.join([double_wide[c] for c in line if c in ('#', '.', 'O', '@')])])
            if '@' in grid[-1]:
                robot_pos = (row, grid[-1].index('@'))
        else:
            movements += line.strip()
        row += 1

# print(grid)

def print_grid():
    for line in grid:
        print(''.join(line))

dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0),
    '[': 1,
    ']': -1
}

box = double_wide['O']
wall = '#'
robot = '@'
empty = '.'

def move(m, row, col):
    r, c = dirs[m]
    swaps = []#[(row, col, row+r, col+c)]
    next = [(row, col)]
    while True:
        step = (next[0][0]+r, next[0][1]+c)
        check = grid[step[0]][step[1]]
        if check == wall:
            return []
        if check in box:
            next.append((step[0], step[1]))
            if m in ('^', 'v'):
                next.append((step[0], step[1]+dirs[check]))
        if (*next[0], *step) not in swaps:
            swaps.append((*next[0], *step))
        next = next[1:]
        if next == []:
            return swaps

print_grid()
# exit()

for m in movements:
    # swaps = []
    swaps = move(m, *robot_pos)
    for s in reversed(swaps):
        r, c, new_r, new_c = s
        # print('swapping', grid[r][c], 'at', r,c,'with',grid[new_r][new_c], 'at', new_r, new_c)
        grid[r][c], grid[new_r][new_c] = grid[new_r][new_c], grid[r][c]
        if grid[new_r][new_c] == robot:
            robot_pos = (new_r, new_c)
    # print(m)
    # print_grid()

# grid = [
#     "#######",
#     "#...O..",
#     "#......"
# ]

total = 0
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == box[0]:
            total += ((100 * i) + j)
print(total)
        
#too high 1551011
#too high 1548975
#too high 1536205
# 1535509