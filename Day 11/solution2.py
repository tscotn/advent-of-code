from pathlib import Path
import functools
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

lines = []
with p.open('r') as f:
    lines = f.readlines()

lines = [int(l) for l in lines[0].split(" ")]

@functools.lru_cache(3000000)
def blink(i, n):
    if n == 75: return 1
    else:
        if i == 0: return blink(1, n+1)
        elif len(str(i)) % 2 == 0:
            j = str(i)
            left = int(j[:int((len(j)/2))])
            right = int(j[int((len(j)/2)):])
            return blink(left, n+1) + blink(right, n+1)
        else: return blink(i * 2024, n+1)

print(sum([blink(i, 0) for i in lines]))