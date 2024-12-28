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
        self.output.append(self.combo(operand) % 8)

# The bdv instruction (opcode 6) works exactly like the adv instruction except that the result is stored in the B register. (The numerator is still read from the A register.)
    def bdv(self, operand):
        self.B = int(self.A / (2 ** self.combo(operand)))

# The cdv instruction (opcode 7) works exactly like the adv instruction
    def cdv(self, operand):
        self.C = int(self.A / (2 ** self.combo(operand)))

    def run(self):
        i = 0
        while i < len(self.Program):
            # print(i)
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
    
    def find_A(self):
        i = 1125899906842624
        done = False
        while not done:
            # print("checking", i)
            if i % 10000 == 0:
                print(i)
            self.A = i
            self.output = []
            self.run()
            if self.output == self.Program:
                print(i)
                done = True
            i+=1
    
    # def print(self):
    #     print(','.join(self.output))
    #     print("A:", self.A, "B:", self.B, "C:",self.C, "output:", ','.join(self.output))

p = program()
p.find_A()

#lower bound =  281474976710656
#upper bound = 1970324836974592

#I've reached 281474981460000