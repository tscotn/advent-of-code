from pathlib import Path
import re

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()

s = 0
for line in lines:
    matches = re.findall(r'mul\(\d+,\d+\)', line)
    for match in matches:
        muls = re.findall(r'\d+', match)
        s += (int(muls[0]) * int(muls[1]))
print(s)