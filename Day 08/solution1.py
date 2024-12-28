from pathlib import Path
p = Path(__file__).with_name('input.txt')

lines = []
with p.open('r') as f:
    lines = [line[:-1] for line in f.readlines()]

freq = {}
for row, line in enumerate(lines):
    for col, l in enumerate(line):
        if l != '.': freq[l] = freq.get(l, []) + [(row, col)]

def is_valid(x, y): return (0 <= x <= len(lines[0])-1) and (0 <= y <= len(lines)-1)

nodes = set()
for key, antennas in freq.items():
    for i, antenna_a in enumerate(antennas):
        for antenna_b in antennas[i+1:]:
            x_1, y_1, x_2, y_2, valid_1, valid_2 = *antenna_a, *antenna_b, False, False
            
            a_1, b_1 = (x_1 - (x_2-x_1), y_1 - (y_2-y_1))
            if is_valid(a_1, b_1): 
                nodes.add((a_1, b_1))
                valid_1 = True
                    
            a_2, b_2 = (x_2 + (x_2-x_1), y_2 + (y_2-y_1))
            if is_valid(a_2, b_2):
                nodes.add((a_2, b_2))
                valid_2 = True
                
print(len(nodes))