class Machine:
    def __init__(self, name, fields, inputs):
        self.name = name
        self.inputs = inputs
        self.outputs = []
        self.fields = fields[:] + [0 for i in range(0, 10000)]
        self.pointer = 0
        self.last_output = -1
        self.halted = False
        self.base = 0

    def clear_inputs(self):
        self.inputs = []

    def add_input(self, input):
        self.inputs.append(input)

    def add_instruction(self, line):
        self.inputs = []
        for c in line:
            self.add_input(ord(c))
        self.add_input(ord("\n"))

    def get_params(self, instr, param_modes):
        if instr == 1 or instr == 2 or instr == 7 or instr == 8: # sum, mult, less, equal  
            r = self.fields[self.pointer+1:self.pointer+4]
            for j in range(0, len(r)):
                if param_modes[j] == "0" and not j == 2:
                    r[j] = self.fields[r[j]]
                if param_modes[j] == "2":
                    if j == 2:
                        r[j] = self.base + r[j]
                    else:
                        r[j] = self.fields[self.base + r[j]]
            return r
        elif instr == 3: # input
            r = self.fields[self.pointer+1:self.pointer+2]
            for j in range(0, len(r)):
                if param_modes[j] == "2":
                    r[j] = self.base + r[j]
            return r
        elif instr == 4 or instr == 9: # output
            if param_modes[0] == "0":
                return [self.fields[self.fields[self.pointer+1]]]
            if param_modes[0] == "2":
                return [self.fields[self.base + self.fields[self.pointer+1]]]
            return self.fields[self.pointer+1:self.pointer+2]
        elif instr == 5 or instr == 6: # jump
            r = self.fields[self.pointer+1:self.pointer+3]
            for j in range(0, len(r)):
                if param_modes[j] == "0":
                    r[j] = self.fields[r[j]]
                if param_modes[j] == "2":
                    r[j] = self.fields[self.base + r[j]]
            return r
        else:
            return []

    def run(self):
        self.running = True
        while self.running:           
            pter = "0000" + str(self.fields[self.pointer])
            instr = int(pter[-2:])
            param_modes = pter[0:-2][::-1]
            
            p = self.get_params(instr, param_modes)
            newpointer = self.pointer + len(p) + 1

            if instr == 1: # sum 
                self.fields[p[2]] = p[0] + p[1]
            elif instr == 2: # mult
                self.fields[p[2]] = p[0] * p[1]    
            elif instr == 3: # input
                if len(self.inputs) == 0:
                    #self.inputs.append(-1)
                    self.running = False
                else:
                    input = self.inputs.pop(0)
                    #print("INPUT: " + str(input))
                    self.fields[p[0]] = input
            elif instr == 4:
                output = p[0]
                self.last_output = output
                self.pointer = newpointer
                self.outputs.append(output)
                self.running = False
                return output
            elif instr == 5: # jump if true
                if not p[0] == 0:
                    newpointer = p[1]
            elif instr == 6: # jump if false
                if p[0] == 0:
                    newpointer = p[1]
            elif instr == 7: # less than
                self.fields[p[2]] = 1 if p[0] < p[1] else 0
            elif instr == 8: # equal
                self.fields[p[2]] = 1 if p[0] == p[1] else 0
            elif instr == 9: # adjust relative base
                self.base += p[0]
            elif instr == 99: # end
                self.halted = True
                return -1
            else: # Unknown opcode
                print("UNKNOWN OPCODE: " + str(instr))
                return -1

            if not (len(p) == 3 and p[2] == self.pointer):
                self.pointer = newpointer

        return self.outputs