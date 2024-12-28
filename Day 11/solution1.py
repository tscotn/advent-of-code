from pathlib import Path
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

# lines = []
# with p.open('r') as f:
#     lines = f.readlines()

# print(lines)
lines = [6]

def blink(lines):
    new = []
    for i in lines:
        if i == 0:
            new += [1]
        elif len(str(i)) % 2 == 0:
            j = str(i)
            left = int(j[:int((len(j)/2))])
            # print(left)
            right = int(j[int((len(j)/2)):])
            # print(right)
            new += [left, right]
        else:
            new += [(i * 2024)]
    return new

# next = [11, 33023, 4134, 564, 0, 8922422, 688775]
next = [6]
total = 0
done = False
while not done:
    for i in range(75): #until 25
        print(i)
        lines = blink(lines[0])
        next += lines[1:]
    total += len(lines)
    if not next:
        done = True
print(len(lines))


#6
#11
#33023
#4134
#564
#0
#8922422
#688775

#6 11 33023 4134 564 0 8922422 688775