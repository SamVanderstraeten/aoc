from machine import Machine
from itertools import permutations

file = open("input/day7.txt", "r")
lines = file.readlines()
fields = [int(x) for x in lines[0].split(",")]

max_output = 0
highest = 0
for config in permutations([5, 6, 7, 8, 9]):
    amps = [Machine("AMP " + "ABCDE"[x], fields[:], [config[x]]) for x in range(0, len(config))]
    running = True
    out = (False, 0)
    while running:
        for amp in amps:
            amp.add_input(out[1])
            out = amp.run()

            #print(amp.name + " outputs " + str(out[1]) + "(halted: " + str(out[0]) + ")")

            if out[0] == True: # halted
                running = False
                break

    # Amps halted -> get last output to AMP E
    thruster_output = amps[-1].last_output
    print("Thrust output: %d (config: %s)" % (thruster_output, str(config)))
    highest = max(highest, thruster_output)

print("Highest possible thrust: " + str(highest))