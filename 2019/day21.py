from stepmachine import Machine

file = open("input/day21.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]

# Part I
springbot = Machine("SpringBot 1.0", fields, [])

# Hole at A, B or C and ground at D > JUMP
program = [
    "NOT A T",
    "NOT B J",
    "OR T J",
    "NOT C T",
    "OR T J",
    "AND D J"
]

for instr in program:
    springbot.add_instruction(instr)
springbot.add_instruction("WALK")

while not springbot.halted:
    out = springbot.run()
    if out < 1000 and out >= 0:
        print(chr(out), end='')
    else:
        print(out)

# Part II
springbot = Machine("SpringBot 2.0", fields, [])

# Same as before, but look forward, only jump if landing on D is safe (i.e. bot can move on or can jump again)
program = [
    "NOT A T",
    "NOT B J",
    "OR T J",
    "NOT C T",
    "OR T J",
    "AND D J",
    "NOT H T",
    "NOT T T",
    "OR E T",
    "AND T J"
]

for instr in program:
    springbot.add_instruction(instr)
springbot.add_instruction("RUN")

while not springbot.halted:
    out = springbot.run()
    if out < 1000 and out >= 0:
        print(chr(out), end='')
    else:
        print(out)