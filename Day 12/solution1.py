from pathlib import Path
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

lines = []
with p.open('r') as f:
    lines = [line[:-1] for line in f.readlines()]
    
counted = set()

dirs = [(0, 1),(0,-1), (1, 0), (-1,0)]
def search(key, row, col, area, perimeter):
    area += 1
    counted.add((row, col))
    for r, c in dirs:
        if (row+r, col+c) not in counted:
            if 0 <= row+r < len(lines) and 0 <= col+c < len(lines[0]) and lines[row+r][col+c] == key:
                area, perimeter = search(key, row+r, col+c, area, perimeter)
            else:
                perimeter += 1
        elif 0 <= row+r < len(lines) and 0 <= col+c < len(lines[0]) and lines[row+r][col+c] != key:
            perimeter += 1
            
    return area, perimeter

#for each character, check all sides and add to a dictionary, then print from dictionary

total = 0
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if (row, col) not in counted:
            key = lines[row][col]
            area, perimeter = search(key, row, col, 0, 0)
            print(key, area, perimeter)
            total += (area * perimeter)
print(total)
        