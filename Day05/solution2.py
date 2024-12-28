from pathlib import Path
import re
from collections import defaultdict

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()
    
#split rules and updates
#map pages to a set of the pages that must come before them

#for each update, build a list of pages that, if they show up, will fail the update.
#for the ones left, use some math to sum up the whole thing

rules = {}
for line in lines[:1176]:
    before, after = line.split('|')
    before, after = int(before), int(after)
    if after not in rules.keys():
        rules[after] = set()
    rules[after].add(before)

s = 0
for line in lines[1177:]:
    illegal = set()
    pages = line.split(',')
    legal = True
    for page in pages:
        if int(page) in illegal:
            legal = False
            break
        illegal = illegal.union(rules.get(int(page), set()))
    if not legal:
        temp = set([int(page) for page in pages])
        reordered = []
        while len(temp) > 0:
            for page in temp:
                if len(rules[page].intersection(temp - set([page]))) == 0:
                    reordered += [page]
                    temp -= set([page])
                    break
        s += reordered[int(len(reordered)/2)]

print(s)