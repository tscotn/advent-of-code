from pathlib import Path
import heapq
from collections import deque
import re
import sys
test = True
# test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

secrets = []
with p.open('r') as f:
    secrets = [int(line.strip()) for line in f.readlines()]
    
def mix(secret, to_mix):
    return secret ^ to_mix

def prune(secret):
    return secret % 16777216
    
def get_next(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    return prune(mix(secret, secret * 2048))
    
bananas_total = {}
a = 1
for secret in secrets:
    print(a, secret)
    a+=1
    sequences_to_bananas = {}
    prices = [int(str(secret)[-1])]
    # print(prices[-1])
    sequences = []
    for i in range(2000):
        secret = get_next(secret)
        price = int(str(secret)[-1])
        change = price - prices[-1]
        # print(price, '(' + str(change) + ')')
        
        sequences += [change]
        prices.append(price)
        
        if len(sequences) >= 4:
            sequence = tuple(sequences[-4:])
            if sequence not in sequences_to_bananas:
                sequences_to_bananas[sequence] = price
        
    for s, b in sequences_to_bananas.items():
        bananas_total[s] = bananas_total.get(s, 0) + b

print(max(bananas_total.values()))

# for sequence, total in bananas_total.items():
#     if total > 20:
#         print(sequence, total)

#387 is too low
#1932 is too high