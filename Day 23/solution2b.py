from pathlib import Path
import heapq
from collections import deque
import re
import sys
test = True
# test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

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
        

# counts = {}
# for a, bs in network.items():
#     for b in bs:
#         counts[b] = counts.get(b, 0) + 1
# print(counts)

# connected = set()
# for a, bs in network.items():
#     if a not in {'ar', 'bx', 'cc', 'ew', 'jz', 'lj', 'nx', 'og', 'rd', 'tj', 'ug', 'wd', 'dh', 'fg', 'gz', 'ho', 'ic', 'jb', 'jh'}:
#         if not connected:
#             connected.add(a)
#         for b in bs:
#             connected_to_all = True
#             for c in connected:
#                 if b not in network[c]:
#                     connected_to_all = False
#                     break
#             if connected_to_all:
#                 connected.add(b)

# print(','.join(sorted(list(connected))))

#try group of 14

for a, bs in network.items():
    lan = set([a])
    for b in bs:
        connected = True
        for c in lan:
            if b not in network[c]:
                connected = False
        if connected:
            lan.add(b)
    if len(lan) > 12:
        print(','.join(sorted(list(lan))))
#not ar,bx,cc,ew,jz,lj,nx,og,rd,tj,ug,wd
#not dh,fg,gz,ho,ic,jb,jh,ni,pu,rw,sk,ty