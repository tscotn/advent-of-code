from pathlib import Path
import heapq
from collections import deque
import re
import sys
test = True
# test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

gates = {}
finding_gates = True
unevaluated = []

xs = []
ys = []
zs = []

def evaluate(gate, gate1, gate2, operator):
    if operator == 'AND':
        gates[gate] = gates[gate1] and gates[gate2]
    elif operator == 'OR':
        gates[gate] = gates[gate1] or gates[gate2]
    elif operator == 'XOR':
        gates[gate] = gates[gate1] != gates[gate2]

n_gates = 0
with p.open('r') as f:
    for line in f.readlines():
        if line.strip() == '':
            finding_gates = False
        elif finding_gates:
            gate, value = line.strip().split(': ')
            gates[gate] = (int(value) == 1)
            if gate.startswith('x'):
                xs.append(gate)
            elif gate.startswith('y'):
                ys.append(gate)
            
        else:
            n_gates += 1
            conjunction, gate = line.strip().split(' -> ')
            gate1, operator, gate2 = conjunction.split(' ')
            unevaluated.append((gate, gate1, gate2, operator))
            
            if gate.startswith('z'):
                zs.append(gate)

while unevaluated:
    gate, gate1, gate2, operator = unevaluated[0]
    unevaluated = unevaluated[1:]
    if gate1 in gates and gate2 in gates:
        evaluate(gate, gate1, gate2, operator)
    if gate not in gates:
        unevaluated.append((gate, gate1, gate2, operator))

# xys = int(''.join(['1' if gates[x] else '0' for x in sorted(xs)][::-1]), 2) + int(''.join(['1' if gates[x] else '0' for x in sorted(ys)][::-1]), 2)
# if int(''.join(['1' if gates[x] else '0' for x in sorted(zs)][::-1]), 2) == xys:
#     print('found')

# for a in [xs, ys, zs]:
    # print(int(''.join(['1' if gates[x] else '0' for x in sorted(a)][::-1]), 2))

#need to get 65738163119216

# whose bits are involved?
print(len(zs))
print(bin(int(''.join(['1' if gates[x] else '0' for x in sorted(xs)][::-1]), 2) + int(''.join(['1' if gates[x] else '0' for x in sorted(ys)][::-1]), 2)))
print('0b' + ''.join(['1' if gates[x] else '0' for x in sorted(zs)][::-1]))

# 1110111100100111011011110111000110010001110000
# 1110111100101001011100110111000110001111110000
#             !!!    !!!             !!!!
#             333    222             11987654321
#             4321098765432109876543210

#to delete: x00, y00

"""
first, try swapping these
z34
z33
z32
z27
z26
z25
z11
z10
z09
z08
"""

"""
test
1010110
0001001
6 43210

"""

45 * 4 - 2

# 1110111100100111011011110111000110010001110000
# 1110111100100111011100110111000110010001110000

print(','.join(sorted(['bgs', 'z31', 'pqc', 'z13', 'swt', 'z07', 'wsv', 'rjm'])))