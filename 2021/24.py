import functools

file = open("input/24.sam", "r")
lines = file.readlines()

# only var that matters is z, rest are local vars
@functools.lru_cache(maxsize=None)
def solve(i=0,z=0):
    if i<100:
        print("I:",i)
        print("Z:",z)
        print(solve.cache_info())      
    for n in range(1,10):
        vars={'w':0,'x':0,'y':0,'z':z}
        vars[lines[i].strip().split(" ")[1]] = n # when coming here, next instruction is always input
        
        for x in range(i+1,len(lines)):
            line = lines[x].strip().split(" ")
            instr = line[0]
            a=line[1]
            b=None
            if len(line)>2:
                b=line[2]
                if not b.isalpha():
                    vars["DUMMY"]=int(b)
                    b="DUMMY"
            if instr=="inp":
                r = solve(x, vars['z'])
                if r is not None:
                    return str(n) + r
                break
            elif instr=="add":
                vars[a] = vars[a] + vars[b]
            elif instr=="mul":
                vars[a] = vars[a] * vars[b]
            elif instr=="div":
                if vars[b]==0: break
                vars[a]= vars[a] // vars[b]
            elif instr=="mod":
                if vars[b]==0: break
                vars[a] = vars[a] % vars[b]
            elif instr=="eql":
                vars[a]=1 if vars[a]==vars[b] else 0
        
        if x >= len(lines)-1 and vars['z'] == 0:
            return str(n)
    return None

print(solve())

