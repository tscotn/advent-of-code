from pathlib import Path
import heapq
from collections import deque
import re
import sys
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')


locks = []
keys = []
is_key = False
new_schematic = []
with p.open('r') as f:
    for line in f.readlines():
        if new_schematic == []:
            if '.....' == line.strip():
                is_key = True
                new_schematic = [0,0,0,0,0]
            else:
                is_key = False
                new_schematic = [1,1,1,1,1]
        else:
            for i, l in enumerate(line.strip()):
                if l == '#':
                    new_schematic[i]+=1
        if line.strip() == '':
            if is_key:
                keys.append(new_schematic)
            else:
                locks.append(new_schematic)
            new_schematic = []
print(locks)
print(keys)


s = 0
for lock in locks:
    for key in keys:
        print(lock, key)
        s += all([lock[i] + key[i] <= 7 for i in range(5)])
print(s)
        