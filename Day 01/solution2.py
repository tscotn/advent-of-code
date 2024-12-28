from pathlib import Path

p = Path(__file__).with_name('input.txt')

list1 = []
list2 = {}

with p.open('r') as f:
    lines = f.readlines()
    for line in lines:
        a, b = line.split('   ')
        a = int(a)
        b = int(b)
        list1 += [a]
        list2[b] = list2.get(b, 0) + 1
        
s = 0
for a in list1:
    s += a * list2.get(a, 0)
    
print(s)

#22565391