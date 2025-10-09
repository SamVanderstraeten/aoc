from iterembla import Iterembla
from assembla import Assembla
from iterembla import Iterembla

file = open("input/8.sam", "r")
lines = file.readlines()

# Part I
assembla = Assembla(lines)
(finished, acc) = assembla.exec()
print(acc)

# Part II
for i in range(0,len(lines)):
    line = lines[i]
    linescopy = [l for l in lines]

    (instr, val) = line.split()
    if instr == "nop":
        linescopy[i] = "jmp " + val
    elif instr == "jmp":
        linescopy[i] = "nop " + val

    assembla = Assembla(linescopy)
    (finished, acc) = assembla.exec()
    if finished:
        print(acc)
        break
