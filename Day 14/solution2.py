from pathlib import Path
import re
from functools import reduce
from operator import mul
from time import sleep
# test = True
test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')

# max_y = 11
# max_x = 7

max_y = 101
max_x = 103

# print(max_x // 2)
# print((max_x // 2) + 1)

time = 6000
done = False
while not done:
    if time > 10000:
        done = True
    # initial = {}
    end = {}

    quadrants = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    }
    with p.open('r') as f:
        for line in f.readlines():
            y, x, v_y, v_x = [int(l) for l in re.findall(r'-?\d+', line)]
            # initial[(x,y)] = initial.get((x,y),0) + 1
            # print(x, y, v_x, v_y)
            x_pos = (x + (v_x * time)) % max_x
            y_pos = (y + (v_y * time)) % max_y
            end[(x_pos,y_pos)] = end.get((x_pos,y_pos),0) + 1
            # print(x_pos, y_pos)
            # exit()
            if 0 <= x_pos < (max_x // 2):
                if 0 <= y_pos < (max_y // 2): 
                    # print("\tq 1")
                    quadrants[1] += 1
                elif (max_y // 2) < y_pos:
                    # print("\tq 2")
                    quadrants[2] += 1
            elif (max_x // 2) < x_pos:
                if 0 <= y_pos < (max_y // 2):
                    # print("\tq 3")
                    quadrants[3] += 1
                elif (max_y // 2) < y_pos:
                    # print("\tq 4")
                    quadrants[4] += 1
    # print(quadrants)
    # print(reduce(mul,quadrants.values()))

# for row in range(max_x):
#     print(''.join([str(initial.get((row, col), '.' if row == (max_x // 2) or col == (max_y // 2) else ' ')) for col in range(max_y)]))
    
# print()
        # if all([end.get((i, max_y // 2), 0) > 0 for i in range(20)]):
        # if end.get(((max_x // 2), (max_y -1)), 0) > 0:
        if time % 103 == 90:
            for row in range(max_x):
                print(''.join(['X' if (row, col) in end else ' ' for col in range(max_y)]))
            sleep(.4)
            # print(''.join([' ' if row == (max_x // 2) or col == (max_y // 2) else str(end.get((row, col), '.')) for col in range(max_y)]))
            # done = True
            print(time)
        time+=1

#10000 is too high


#2949
#5034
#5137
#5240