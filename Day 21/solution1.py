from pathlib import Path
import heapq
from collections import deque
import re
import sys
test = True
# test = False
p = Path(__file__).with_name('test.txt' if test else 'input.txt')


codes = []
with p.open('r') as f:
    codes = [line.strip() for line in f.readlines()]
    
keypad_locations = {
    'A': (3,2),
    '0': (3,1),
    '1': (2,0),
    '2': (2,1),
    '3': (2,2),
    '4': (1,0),
    '5': (1,1),
    '6': (1,2),
    '7': (0,0),
    '8': (0,1),
    '9': (0,2)
}
    
directional_locations = {
    '<': (1,0),
    'v': (1,1),
    '>': (1,2),
    '^': (0,1),
    'A': (0,2)
}
    
def key_to_dir(location, input):
    if location == input:
        return 'A'
    #always go right then up, or down then left, or right then down, always go up then left
    output = ''
    r_0, c_0 = keypad_locations[location]
    r_1, c_1 = keypad_locations[input]

    if c_0 < c_1: #maybe move right
        output += ''.join(['>'] * (c_1 - c_0))
        
    if r_0 > r_1: #maybe move up
        output += ''.join(['^'] * (r_0 - r_1))
        
    if r_0 < r_1: #maybe move down
        output += ''.join(['v'] * (r_1 - r_0))
        
        
    if c_0 > c_1: #maybe move left
        output += ''.join(['<'] * (c_0 - c_1))
        
    return output + 'A'
    
    
def dir_to_dir(location, input):
    if location == input:
        return 'A'
    output = ''
    r_0, c_0 = directional_locations[location]
    r_1, c_1 = directional_locations[input]

    if c_0 < c_1: #maybe move right
        output += ''.join(['>'] * (c_1 - c_0))
        
    if r_0 > r_1: #maybe move up
        output += ''.join(['^'] * (r_0 - r_1))
        
    if r_0 < r_1: #maybe move down
        output += ''.join(['v'] * (r_1 - r_0))
        
    if c_0 > c_1: #maybe move left
        output += ''.join(['<'] * (c_0 - c_1))
        
    return output + 'A'
    
def get_complexity(code):
    numeric = int(re.findall(r'\d+', code)[0])
    print(code)
    
    temp = ''
    location = 'A'
    for input in code:
        temp += key_to_dir(location, input)
        location = input
        
    print(temp)
        
    location = 'A'
    code, temp = temp, ''
    for input in code:
        temp += dir_to_dir(location, input)
        location = input
        
    print(temp) 
        
    location = 'A'
    code, temp = temp, ''
    for input in code:
        temp += dir_to_dir(location, input)
        location = input
    print(temp)
    print(numeric, len(temp))
    print()
    return numeric * len(temp)
    
print(sum([get_complexity(code) for code in codes]))
print(126384)

        
# code_to_input = {
#     ('A', '0'): '<vA<AA>>^AvAA<^A>A',
#     ('0', '2'): '<v<A>>^AvA^A',
#     ('2', '9'): ''
# }
    
"""

3                       7 Door (Robot 1)
             < <   ^ ^  A Robot 2
   v  < <    A A >^A A >A Robot 3
 v<A <A A >>^A              Me
                   Me
   <A A v<A A >>^A Robot 3
    ^ ^   < <    A Robot 2
   3             7

"""



"""
                   3                                        7               9                         A
             ^     A         ^ ^            <   <           A       > >     A           v v v         A
        <    A  >  A    <    A A    v  <    A   A  > >   ^  A   v   A A  ^  A   v  <    A A A  >   ^  A
     v<<A >>^A vA ^A v<<A >>^A A  v<A <A >>^A   A vA A ^<A >A v<A >^A A <A >A v<A <A >>^A A A vA ^<A >A 68
     
A -> <v<A >>^A vA ^A  <vA   <A A >>^A  A   vA <^A >A A  vA ^A <vA >^A A <A >A <v<A >A >^A A A vA <^A >A
        <    A  >  A    v    < <    A  A    >   ^  A A   >  A
             ^     A                <  <           ^ ^      A
                   3                                        7

<<vA>>^AvA^A <<vAA>A>^AAvA<^A>AAvA  ^A<vA>^AA<A>A<<vA>A>^AAAvA<^A>A
<v<A>>^AvA^A <vA<AA>>^AAvA<^A>AAvA  ^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
"""