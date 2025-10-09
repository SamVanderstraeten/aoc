class Assembla:
    def __init__(self, instructions):
        self.rules = []
        self.instructions = instructions
        self.acc = 0

    def exec(self, i=0):
        if i in self.rules:
            return (False, self.acc)
        else:
            self.rules.append(i)

        if i >= len(self.instructions):
            return (True, self.acc)

        line = self.instructions[i].strip()
        (instr, val) = line.split()
        if instr == "acc":
            self.acc += int(val)
            return self.exec(i+1)
        elif instr == "jmp":
            return self.exec(i+int(val))
        elif instr == "nop":
            return self.exec(i+1)