from pathlib import Path
import re
from collections import defaultdict
import functools

p = Path(__file__).with_name('input.txt')

lines = []

with p.open('r') as f:
    lines = f.readlines()

lines = [line[:-1] for line in lines]

freq = {}
for row, line in enumerate(lines):
    for col, l in enumerate(line):
        if l != '.': freq[l] = freq.get(l, []) + [(row, col)]

def is_valid(x, y): return (0 <= x <= len(lines[0])-1) and (0 <= y <= len(lines)-1)

nodes = set()
for key in freq.keys():
    for i, antenna_a in enumerate(freq[key]):
        for antenna_b in freq[key][i+1:]:
            x_1, y_1 = antenna_a
            x_2, y_2 = antenna_b
            nodes.add(antenna_a)
            nodes.add(antenna_b)
            valid_1, valid_2 = False, False
            #go up
            a_1, b_1 = (x_1 - (x_2-x_1), y_1 - (y_2-y_1))
            if (0 <= a_1 <= len(lines[0])-1) and (0 <= b_1 <= len(lines)-1): 
                nodes.add((a_1, b_1))
                valid_1 = True
            while valid_1:
                a_1, b_1 = (a_1 - (x_2-x_1), b_1 - (y_2-y_1))
                if (0 <= a_1 <= len(lines[0])-1) and (0 <= b_1 <= len(lines)-1): 
                    nodes.add((a_1, b_1))
                else:
                    valid_1 = False
                    
            #go down
            a_2, b_2 = (x_2 + (x_2-x_1), y_2 + (y_2-y_1))
            if (0 <= a_2 <= len(lines[0])-1) and (0 <= b_2 <= len(lines)-1):
                nodes.add((a_2, b_2))
                valid_2 = True
            while valid_2:
                a_2, b_2 = (a_2 + (x_2-x_1), b_2 + (y_2-y_1))
                if (0 <= a_2 <= len(lines[0])-1) and (0 <= b_2 <= len(lines)-1): 
                    nodes.add((a_2, b_2))
                else:
                    valid_2 = False
            # print(key, antenna_a, antenna_b)
            # print('\t', (x_1 - (x_2-x_1), y_1 - (y_2-y_1)), valid_1)
            # print('\t', (x_2 + (x_2-x_1), y_2 + (y_2-y_1)), valid_2)
for n in nodes:
    print(n)
print(len(nodes))


# from pathlib import Path
# p = Path(__file__).with_name('input.txt')

# lines = []
# with p.open('r') as f:
#     lines = [line[:-1] for line in f.readlines()]

# freq = {}
# for row, line in enumerate(lines):
#     for col, l in enumerate(line):
#         if l != '.': freq[l] = freq.get(l, []) + [(row, col)]

# def is_valid(x, y): return (0 <= x <= len(lines[0])-1) and (0 <= y <= len(lines)-1)

# nodes = set()

# def try_add(x, y):
#     if is_valid(x, y):
#         nodes.add((x, y))
#         return True
#     else:
#         return False
        
# for key in freq.keys():
#     for i, antenna_a in enumerate(freq[key]):
#         for antenna_b in freq[key][i+1:]:
#             x_1, y_1, x_2, y_2, valid_1, valid_2 = *antenna_a, *antenna_b, False, False
#             nodes.add(antenna_a)
#             nodes.add(antenna_b)
            
#             a_1, b_1 = (x_1 - (x_2-x_1), y_1 - (y_2-y_1))
#             valid_1 = try_add(a_1, b_1)
#             while valid_1:
#                 a_1, b_1 = (a_1 - (x_2-x_1), b_1 - (y_2-y_1))
#                 valid_1 = try_add(a_1, b_1)
                    
#             a_2, b_2 = (x_2 + (x_2-x_1), y_2 + (y_2-y_1))
#             valid_1 = try_add(a_2, b_2)
#             while valid_2:
#                 a_2, b_2 = (a_2 + (x_2-x_1), b_2 + (y_2-y_1))
#                 valid_1 = try_add(a_2, b_2)
# print(len(nodes))