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
    
s = 0
for secret in secrets:
    for i in range(2000):
        secret = get_next(secret)
    s += secret
print(s)