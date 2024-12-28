from pathlib import Path
import re
from collections import defaultdict

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()

def recursive_test(sum, sum_so_far, operands):
    # print(sum_so_far)
    if len(operands) == 0:
        # print(sum==sum_so_far)
        return sum == sum_so_far
    return recursive_test(sum, sum_so_far + operands[0], operands[1:]) or recursive_test(sum, sum_so_far * operands[0], operands[1:])

c = 0
for line in lines:
    s, operands = line.split(': ')
    s = int(s)
    operands = [int(o) for o in operands.split(' ')]
    print(int(s), operands)
    if recursive_test(s, operands[0], operands[1:]):
        c += s
print(c)