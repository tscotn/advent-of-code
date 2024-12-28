"""
2,4,1,1,7,5,1,5,4,2,5,5,0,3,
2,4,1,1,7,5,1,5,4,2,5,5,0,3,
2,4,1,1,7,5,1,5,4,2,5,5,0,3,
2,4,1,1,7,5,1,5,4,2,5,5,0,3,
2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3,2,4,1,1,7,5,1,5,4,2,5,5,0,3

2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0

2,4 - bst(4) -> B = A % 8
1,1 - bxl(1) -> B = B XOR 1
7,5 - cdv(5) -> C = self.A // 2**self.B
1,5 - bxl(5) -> B = B XOR 5 (101 bitwise)
4,2 - bxc ->    B = B XOR C
5,5 - out ->    print B % 8
0,3 - adv(3) -> A = A // 8
3,0 - jnz(0) -> always jump to the beginning, but A must be 0 after the 15th jump

out(5)
    B % 8 = 2,4,1,1,7,5,1,5,4,2,5,5,0,3,3,0

    15. out(5) B is a multiple of 3
    16. out(5) B is a multiple of 8


A ? % 8 = 0..7, // 8
B 0..7 XOR 1, XOR 101, XOR C -> 2
C ?

1) -> 2
    2,4 - bst -> B = A % 8
    1,1 - bxl -> B = B XOR 1
    7,5 - cdv -> C = A // 2**B
    1,5 - bxl -> B = B XOR 5 (101 bitwise)
    4,2 - bxc -> B = B XOR C
    5,5 - out -> print B % 8!
    0,3 - adv -> A = A // 8
2) -> 4
3) -> 1
4) -> 1
5) -> 7
6) -> 5
7) -> 1
8) -> 5
9) -> 4
10)-> 2
11)-> 5
12)-> 5
13)-> 0
14)-> 3
15)-> 3
16)-> 0
    2,4 - bst -> B = A % 8
    1,1 - bxl -> B = B XOR 1
    7,5 - cdv -> C = A // 2**B
    1,5 - bxl -> B = B XOR 5 (101 bitwise)
    4,2 - bxc -> B = B XOR C
    5,5 - out -> print B % 8!
    0,3 - adv -> A = A // 8 = 0

ALL A operations:

A ? % 8 = 0..7, // 8
B 0..7 XOR 1, XOR 101, XOR C -> 2
C ?

constraints: A < 8
B is a multiple of 8

A candidates:
0,1,2,3,4,5,6,7,8

16)-> 0

If A has to be divided by 8 16 times and only end up with 0 through 7 on the last run,

A = 4! (* 8**16)
C = A // 2**A % 8 XOR 1
B = A XOR 1 XOR 5 XOR (A // 2**A XOR 1) (% 8 = 0)



doesn't matter what B or C are, they will always get reset before they're read



37
4

298 ['3', '3', '0'] 0

OR

301 ['3', '3', '0'] 0


2390 ['0', '3', '3', '0'] 0
OR
2408 ['0', '3', '3', '0'] 0
OR
2414 ['0', '3', '3', '0'] 0


19124 ['5', '0', '3', '3', '0'] 0
OR
19269 ['5', '0', '3', '3', '0'] 0

152996 ['5', '5', '0', '3', '3', '0'] 0
OR
152999 ['5', '5', '0', '3', '3', '0'] 0
OR
154155 ['5', '5', '0', '3', '3', '0'] 0

1223970
OR
1223997 ['2', '5', '5', '0', '3', '3', '0'] 0
OR
1233244


9791760 ['4', '2', '5', '5', '0', '3', '3', '0'] 0
9791761 ['4', '2', '5', '5', '0', '3', '3', '0'] 0
9791762 ['4', '2', '5', '5', '0', '3', '3', '0'] 0
9791983 ['4', '2', '5', '5', '0', '3', '3', '0'] 0
9865952 ['4', '2', '5', '5', '0', '3', '3', '0'] 0
9865953 ['4', '2', '5', '5', '0', '3', '3', '0'] 0
"""

print(4*8**15, 5*8**15)
print(4*8, (5*8)-1)

32, 4

for A in range(8):
    print(A, (((A ^ 1) ^ 5) ^ (A // (2**(A^1)))) % 8)
    # print(A * (8**15))
    """
    0 4
    1 4
    2 6
    3 7
    4 0
    5 1
    6 2
    7 3
    """
    
#lower 140737488355328
#upper 175921860444160    

exit()

#8 * 8


from pathlib import Path
import re
test = True
# test = False

class program():
    def __init__(self):
        p = Path(__file__).with_name('test.txt' if test else 'input.txt')

        self.A = None
        self.B = None
        self.C = None
        self.Program = None
        with p.open('r') as f:
            for line in f.readlines():
                if 'A' in line:
                    self.A = int(re.findall(r'\d+', line)[0])
                elif 'B' in line:
                    self.B = int(re.findall(r'\d+', line)[0])
                elif 'C' in line:
                    self.C = int(re.findall(r'\d+', line)[0])
                elif 'Program' in line:
                    self.Program = [int(x) for x in re.findall(r'\d', line)]

        self.output = []

# Combo operands 0 through 3 represent literal values 0 through 3.
# Combo operand 4 represents the value of register A.
# Combo operand 5 represents the value of register B.
# Combo operand 6 represents the value of register C.
# Combo operand 7 is reserved and will not appear in valid programs.
    def combo(self, operand):
        if operand in (0,1,2,3):
            return operand
        elif operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        elif operand == 6:
            return self.C    

#The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand.
# (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
    def adv(self, operand):
        self.A = int(self.A / (2 ** self.combo(operand)))

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
    def bxl(self, operand):
        self.B = self.B ^ operand
 
# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    def bst(self, operand):
        self.B = self.combo(operand) % 8

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand;
# if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    def jnz(self, i, operand):
        if self.A != 0:
            return operand
        else:
            return i+2

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    def bxc(self, operand):
        self.B ^= self.C

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    def out(self, operand):
        self.output.append(str(self.combo(operand) % 8))

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    def bdv(self, operand):
        self.B = int(self.A / (2 ** self.combo(operand)))

# The cdv instruction (opcode 7) works exactly like the adv instruction
    def cdv(self, operand):
        self.C = int(self.A / (2 ** self.combo(operand)))

    def run(self):
        print("running")
        i = 0
        while i < len(self.Program):
            print(i)
            opcode, operand = self.Program[i], self.Program[i+1]
            
            if opcode == 0:
                self.adv(operand)
            if opcode == 1:
                self.bxl(operand)
            if opcode == 2:
                self.bst(operand)
            if opcode == 3:
                # print('in opcode')
                i = self.jnz(i, operand)
            else:
                i+=2
            if opcode == 4:
                self.bxc(operand)
            if opcode == 5:
                self.out(operand)
            if opcode == 6:
                self.bdv(operand)
            if opcode == 7:
                self.cdv(operand)
    
    def print(self):
        print(','.join(self.output))
        print("A:", self.A, "B:", self.B, "C:",self.C, "output:", ','.join(self.output))



    #The adv instruction (opcode 0) performs division. The numerator is the value in the A register. The denominator is found by raising 2 to the power of the instruction's combo operand.
# (So, an operand of 2 would divide A by 4 (2^2); an operand of 5 would divide A by 2^B.) The result of the division operation is truncated to an integer and then written to the A register.
    def inv_adv(self, operand):
        self.A = int(self.A / (2 ** self.combo(operand)))
        
        self.A = self.A * 2 ** self.combo(operand)

# The bxl instruction (opcode 1) calculates the bitwise XOR of register B and the instruction's literal operand, then stores the result in register B.
    def bxl(self, operand):
        self.B = self.B ^ operand
 
# The bst instruction (opcode 2) calculates the value of its combo operand modulo 8 (thereby keeping only its lowest 3 bits), then writes that value to the B register.
    def bst(self, operand):
        self.B = self.combo(operand) % 8

# The jnz instruction (opcode 3) does nothing if the A register is 0. However, if the A register is not zero, it jumps by setting the instruction pointer to the value of its literal operand;
# if this instruction jumps, the instruction pointer is not increased by 2 after this instruction.
    def jnz(self, i, operand):
        if self.A != 0:
            return operand
        else:
            return i+2

# The bxc instruction (opcode 4) calculates the bitwise XOR of register B and register C, then stores the result in register B. (For legacy reasons, this instruction reads an operand but ignores it.)
    def bxc(self, operand):
        self.B ^= self.C

# The out instruction (opcode 5) calculates the value of its combo operand modulo 8, then outputs that value. (If a program outputs multiple values, they are separated by commas.)
    def out(self, operand):
        self.output.append(str(self.combo(operand) % 8))

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    def bdv(self, operand):
        self.B = int(self.A / (2 ** self.combo(operand)))

# The cdv instruction (opcode 7) works exactly like the adv instruction
    def cdv(self, operand):
        self.C = int(self.A / (2 ** self.combo(operand)))

p = program()
p.run()
p.print()


