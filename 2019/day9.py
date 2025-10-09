from stepmachine import Machine

file = open("input/old/day9.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]

machine = Machine("C", fields, [2])

out = machine.run()
print(str(out), end='')