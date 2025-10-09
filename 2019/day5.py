file = open("input/day5.txt", "r")
lines = file.readlines()
original_g = [int(x) for x in lines[0].split(",")]

input = 5
output = ''

def get_params(fields, instr, i, param_modes):
    if instr == 1 or instr == 2 or instr == 7 or instr == 8: # sum, mult, less, equal  
        r = fields[i+1:i+4]
        for j in range(0, len(r)):
            if param_modes[j] == "0" and not j == 2:
                r[j] = fields[r[j]]
        return r
    elif instr == 3: # input
        return fields[i+1:i+2]
    elif instr == 4: # output
        if param_modes[0] == "0":
            return [fields[fields[i+1]]]
        return fields[i+1:i+2]
    elif instr == 5 or instr == 6: # jump
        r = fields[i+1:i+3]
        for j in range(0, len(r)):
            if param_modes[j] == "0":
                r[j] = fields[r[j]]
        return r
    else:
        return []

def execute(fields, pointer = 0):
    pter = "0000" + str(fields[pointer])
    instr = int(pter[-2:])
    param_modes = pter[0:-2][::-1]

    p = get_params(fields, instr, pointer, param_modes)

    newpointer = pointer + len(p) + 1

    if instr == 1: # sum 
        fields[p[2]] = p[0] + p[1]
        print("Write " + str(p[0]) + "+" + str(p[1]) + " to " + str(p[2]))
    elif instr == 2: # mult
        fields[p[2]] = p[0] * p[1]    
        print("Write " + str(p[0]) + "*" + str(p[1]) + " to " + str(p[2]))    
    elif instr == 3: # input
        fields[p[0]] = input
        print("Write " + str(input) + " to " + str(p[0]))
    elif instr == 4:
        print("OUTPUT: " + str(p[0]))
        output = p[0]
    elif instr == 5: # jump if true
        print("JIT " + str(p[0]))
        if not p[0] == 0:
            newpointer = p[1]
    elif instr == 6: # jump if false
        print("JIF " + str(p[0]))
        if p[0] == 0:
            newpointer = p[1]
    elif instr == 7: # less than
        print("LESS " + str(p[0]) + " < " + str(p[1]) + " to " + str(p[2]))
        fields[p[2]] = 1 if p[0] < p[1] else 0
    elif instr == 8: # equal
        print("EQUAL " + str(p[0]) + " == " + str(p[1]) + " to " + str(p[2]))
        fields[p[2]] = 1 if p[0] == p[1] else 0
    # process first field (param mode)
    elif instr == 99: # end
        # Ended
        return "END. DIAGNOSTIC CODE: " + str(output)
    else: # Unknown opcode
        print("Unknown: " + str(instr))
        return -1

    if len(p) == 3 and p[2] == pointer:
        return execute(fields, pointer)

    return execute(fields, newpointer)

def run(fields): #(fields, args)
    # set arguments
    #fields[1] = args[0]
    #fields[2] = args[1]

    try:
        result = execute(fields)
        return result
    except:
        return -1

print("Size: " + str(len(original_g)))
result = run(original_g[:])
print(result)

