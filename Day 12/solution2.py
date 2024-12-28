from pathlib import Path
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

lines = []
with p.open('r') as f:
    lines = [line[:-1] for line in f.readlines()]
    
counted = set()

def in_bounds(row, col):
    return 0 <= row < len(lines) and 0 <= col < len(lines[0])

def is_match(row, col, key):
    return lines[row][col] == key

p = False
# p = True

up_down = [(-1,0, "upper"), (1, 0, "lower")]
left_right = [(0,-1, "left"), (0, 1, "right")]
diagonals = [(1,1), (-1,-1), (1,-1), (-1,1)]
def search(key, row, col, area, sides):
    if (row, col) in counted:
        return area, sides
    area += 1
    counted.add((row, col))
    for r, c, n_1 in up_down:
        for x, y, n_2 in left_right:
        # try to identify a corner
        
        # check if up/down is in bounds and the same key and hasn't been searched -> search it
        # else if left/right is not in bounds or is not the same key
        # add a corner
        # else if left/right is in bounds and is the same key, search left/right
            # print("checking", row, col)
            if not in_bounds(row+r, col+c) and not in_bounds(row+x, col+y): # two sides out of bounds
                if p: print(n_1, n_2, row, col)
                sides += 1
            elif in_bounds(row+r, col+c) and not is_match(row+r, col+c, key) and not in_bounds(row+x, col+y): #one side out of bounds, other in but wrong key
                if p: print(n_1, n_2, row, col)
                sides += 1
            elif in_bounds(row+x, col+y) and not is_match(row+x, col+y, key) and not in_bounds(row+r, col+c): #one side out of bounds, other in but wrong key
                if p: print(n_1, n_2, row, col)
                sides += 1
            elif in_bounds(row+r, col+c) and not is_match(row+r, col+c, key) and in_bounds(row+x, col+y) and not is_match(row+x, col+y, key):
                if p: print(n_1, n_2, row, col)
                sides += 1
            if in_bounds(row+r, col+c) and is_match(row+r, col+c, key):
                area, sides = search(key, row+r, col+c, area, sides)
            if in_bounds(row+x, col+y) and is_match(row+x, col+y, key):
                area, sides = search(key, row+x, col+y, area, sides) #step left or right
    for r, c, n_1 in up_down:
        for x, y, n_2 in left_right:
        #if the diagonal is in bounds, if it's the top left, check that top and left are both matches and increment
            if in_bounds(row+r,col+y) and not is_match(row+r,col+y,key) and is_match(row+r, col+c, key) and is_match(row+x, col+y, key):
                if p: print("diagonal", row, col)
                sides+=1
    return area, sides

total = 0
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if (row, col) not in counted:
            key = lines[row][col]
            area, sides = search(key, row, col, 0, 0)
            print(key, area, sides)
            total += (area * sides)
print(total)
        
#sides == vertices