'''
    Iterative alternative to Assembla (recursive)
'''

class Iterembla:
    def __init__(self, instructions):
        self.rules = []
        self.instructions = instructions
        self.acc = 0

    def exec(self):
        i = 0
        while i < len(self.instructions):
            if i in self.rules:
                return (False, self.acc)
            else:
                self.rules.append(i)
                
            line = self.instructions[i].strip()
            (instr, val) = line.split()
            if instr == "acc":
                self.acc += int(val)
                i += 1
            elif instr == "jmp":
                i += int(val)
            elif instr == "nop":
                i += 1

        return (True, self.acc)

        