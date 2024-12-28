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
        if c == 'X':
            #get horizontal
            count+=((ws[i][j+1] == 'M' and ws[i][j+2] == 'A' and ws[i][j+3] == 'S')
            +(ws[i][j-1] == 'M' and ws[i][j-2] == 'A' and ws[i][j-3] == 'S')
            #get vertical
            +(ws[i+1][j] == 'M' and ws[i+2][j] == 'A' and ws[i+3][j] == 'S')
            +(ws[i-1][j] == 'M' and ws[i-2][j] == 'A' and ws[i-3][j] == 'S')
            #get diagonal
            +(ws[i+1][j+1] == 'M' and ws[i+2][j+2] == 'A' and ws[i+3][j+3] == 'S')
            +(ws[i+1][j-1] == 'M' and ws[i+2][j-2] == 'A' and ws[i+3][j-3] == 'S')
            +(ws[i-1][j+1] == 'M' and ws[i-2][j+2] == 'A' and ws[i-3][j+3] == 'S')
            +(ws[i-1][j-1] == 'M' and ws[i-2][j-2] == 'A' and ws[i-3][j-3] == 'S'))
print(count)
#get horizontal - XMAS - SAMX

#get vertical 
#X  S
#M  A
#A  M
#S  X

#get diagonal
#X       X S       S
# M     M   A     A
#  A   A     M   M
#   S S       X X