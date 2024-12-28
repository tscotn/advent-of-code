from pathlib import Path
import re
import functools
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')
towels = set()
designs = []
with p.open('r') as f:
    for line in f.readlines():
        if ',' in line:
            towels = set(line.strip().split(', '))
        elif line.strip() != '':
            designs.append(line.strip())
print(towels)

max_towel_stripes = len(max(towels, key=lambda x: len(x)))

#I could put the towels into a trie?
#I could divide/conquer

# match chars i through n until a match is found or , then chop that off and repeat. If no match is found, 

"""
cases:
the design is empty. then it can be formed, return True
the design has one stripe. If it is a towel, return True
the design has two stripes. If the first is a towel and the second is a towel or the full thing is a towel, return true.
"""

"""
some of these aren't getting got even though they should

rrrgubgggurwruwrgrbbrwbbbrwubwwuuwgwuwwu isn't found, not sure if it should be though
"""

@functools.lru_cache()
def find_towel(design):
    if len(design) == 0:
        return True
    if len(design) == 1:
        return design in towels
    if len(design) == 2:
        if design in towels:
            return True
    if len(design) == 3:
        if design in towels:
            return True
    if len(design) == 4:
        if design in towels:
            return True
    if len(design) == 5:
        if design in towels:
            return True
    if len(design) == 6:
        if design in towels:
            return True
    for i in range(len(design)):
        # if i >= max_towel_stripes+1:
        #     return False
        # print('checking', design[:i], (design[:i] in towels))
        if design[:i] in towels and find_towel(design[i:]):
            return True
    return False

possible_designs = 0
for design in designs:
    found = find_towel(design)
    if not found:
        print(design)
    # print(found, design)
    possible_designs += found
    # exit()
    
print(possible_designs)

#260 is too low