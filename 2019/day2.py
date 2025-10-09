file = open("input/day2.txt", "r")
lines = file.readlines()

original_g = [int(x) for x in lines[0].split(",")]
target = 19690720

def params(fields, i):
    if fields[i] == 1 or fields[i] == 2: # sum        
        return fields[i+1:i+4]
    else:
        return ()

def execute(fields, pointer = 0):
    p = params(fields, pointer)
    if fields[pointer] == 1: # sum        
        fields[p[2]] = fields[p[0]] + fields[p[1]]
        return execute(fields, pointer + 4)
    elif fields[pointer] == 2: # mult
        fields[p[2]] = fields[p[0]] * fields[p[1]]
        return execute(fields, pointer + 4)
    elif fields[pointer] == 99: # end
        # Ended
        return fields[0]
    else: # Unknown opcode
        return -1

def run(fields, args):
    # set arguments
    fields[1] = args[0]
    fields[2] = args[1]

    try:
        result = execute(fields)
        return result
    except:
        return -1

for noun in range(0, 100):
    for verb in range(0, 100):
        result = run(original_g[:], (verb, noun))

        if result == target:
            print("Found input " + str(verb) + str(noun) + " = " + str(target))
            break