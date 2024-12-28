from pathlib import Path
import re

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()

s = 0
enabled = True
for line in lines:
    matches = re.findall(r'don\'t\(\)|do\(\)|mul\([0-9]*,[0-9]*\)', line)
    for match in matches:
        if match == "don't()":
            enabled = False
        elif match == "do()":
            enabled = True
        elif enabled:
            muls = re.findall(r'\d+', match)
            s += (int(muls[0]) * int(muls[1]))
print(s)