from pathlib import Path
import heapq
from collections import deque
import re
import sys
test = True
# test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

t = set()
network = {}
with p.open('r') as f:
    for line in f.readlines():
        a, b = line.strip().split('-')
        l = network.get(a, set())
        l.add(b)
        network[a] = l

        l = network.get(b, set())
        l.add(a)
        network[b] = l
       
        if a.startswith('t'):
            t.add(a)
        if b.startswith('t'):
            t.add(b)
       
sets_of_3_with_t = set()

for a, bs in network.items():
    print('checking', a)
    if a.startswith('t'):
        for b in bs:
            for c in bs:
                if b != c and c in network[b] and b in network[c]:
                    sets_of_3_with_t.add(tuple(sorted([a, b, c])))
print(len(sets_of_3_with_t))