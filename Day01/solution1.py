from pathlib import Path

p = Path(__file__).with_name('input.txt')

list1 = []
list2 = []

with p.open('r') as f:
    lines = f.readlines()
    for line in lines:
        a, b = line.split('   ')
        list1 += [int(a)]
        list2 += [int(b)]
        
list1.sort()
list2.sort()
        
s = 0
for i in range(len(list1)):
    s += abs(list1[i] - list2[i])
    
print(s)

#3574690