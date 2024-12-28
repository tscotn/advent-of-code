from pathlib import Path
p = Path(__file__).with_name('input.txt')

lines = []
with p.open('r') as f:
    lines = f.readlines()[0]

# files = lines[::2]
# spaces = lines[1::2]

disk = []
for key, blocks in enumerate(lines):
    if key % 2 == 0:
        disk += [(int(key/2), int(blocks))]
    else:
        disk += [('.', int(blocks))]
        
rev_disk = reversed(disk.copy())
for value in rev_disk:
    key, blocks = value
    if key != '.':
        # print(key, blocks)
        for i, v in enumerate(disk[:disk.index((key, blocks))]):
            k, b = v
            if k == '.' and blocks <= b:
                j = disk.index((key, blocks))
                disk[j] = (k, blocks)
                disk[i] = (k, b-blocks)
                disk.insert(i, (key, blocks))
                break

# print(disk)
# print(''.join([str(k) * v for k, v in disk]))

i = 0
s = 0
for k, v in disk:
    for j in range(v):
        if k != '.':
            s += i * int(k)
        i += 1
print(s)
        

# s = 0
# for k, v in enumerate(''.join([str(k) * v for k, v in disk])):
#     if v != '.':
#     s += (i * int(v))
# print(s)