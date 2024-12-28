from pathlib import Path
import re
from collections import defaultdict

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()

ws = defaultdict(lambda: defaultdict(lambda: False))

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        ws[i][j] = c

count = 0
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == 'S':
            count+=((ws[i][j+2] == 'S' and ws[i+1][j+1] == 'A' and ws[i+2][j] == 'M' and ws[i+2][j+2] == 'M')
            +(ws[i][j+2] == 'M' and ws[i+1][j+1] == 'A' and ws[i+2][j] == 'S' and ws[i+2][j+2] == 'M'))
        if c == 'M':
            count+=((ws[i][j+2] == 'S' and ws[i+1][j+1] == 'A' and ws[i+2][j] == 'M' and ws[i+2][j+2] == 'S')
            +(ws[i][j+2] == 'M' and ws[i+1][j+1] == 'A' and ws[i+2][j] == 'S' and ws[i+2][j+2] == 'S'))
            
print(count)

#S S S M M M M S
# A   A   A   A
#M M S M S S M S