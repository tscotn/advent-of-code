from pathlib import Path
p = Path(__file__).with_name('input.txt')

lines = []
with p.open('r') as f:
    lines = f.readlines()[0]

compact = []
k = 0
for i, j in enumerate(lines):
    if i % 2 == 0:
        compact += ([k] * int(j))
        k+=1
    else:
        compact += (['.'] * int(j))
print(compact)

removed = 0
rev_compact = [i for i in reversed(compact) if i != '.']
for i, j in enumerate(compact):
    if j == '.':
        removed += 1
        compact[i] = rev_compact[0]
        rev_compact = rev_compact[1:]
    
s = 0
for i, j in enumerate(compact[:-removed]):
    s += (i*j)
print(s)