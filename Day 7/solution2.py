from pathlib import Path
import re
from collections import defaultdict

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()

def recurse(sum, temp, operands):
    if len(operands) == 0:
        return sum == temp
    return recurse(sum, temp + operands[0], operands[1:]) or recurse(sum, temp * operands[0], operands[1:]) or recurse(sum, int(str(temp) + str(operands[0])), operands[1:])

c = 0
for line in lines:
    s, operands = line.split(': ')
    s = int(s)
    operands = [int(o) for o in operands.split(' ')]
    # print(int(s), operands)
    if recurse(s, operands[0], operands[1:]):
        c += s
print(c)