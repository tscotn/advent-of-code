from pathlib import Path
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

grid = []
movements = ""
making_grid = True
robot_pos = None
with p.open('r') as f:
    row = 0
    for line in f.readlines():
        if 'END' in line:
            making_grid = False
        elif making_grid:
            grid.append([c for c in line if c in ('#', '.', 'O', '@')])
            if '@' in grid[-1]:
                robot_pos = (row, grid[-1].index('@'))
        else:
            movements += line.strip()
        row += 1

def print_grid():
    for line in grid:
        print(''.join(line))

dirs = {
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1),
    'v': (1, 0)
}

box = 'O'
robot = '@'
wall = '#'
empty = '.'

def move(m, row, col):
    r, c = dirs[m]
    if grid[row+r][col+c] == box:
        if not move(m, row+r, col+c)[0]:
            return False, (row, col)
    if grid[row+r][col+c] == empty:
        grid[row+r][col+c], grid[row][col] = grid[row][col], grid[row+r][col+c]
        return True, (row+r, col+c)
    return False, (row, col)

print_grid()

for m in movements:
    _, robot_pos = move(m, *robot_pos)
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
        if cell == box:
            total += ((100 * i) + j)
print(total)
        