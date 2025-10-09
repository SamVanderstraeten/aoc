file = open("input/16.sam", "r")
hex = file.readline()
#hex="CE00C43D881120"
bits = ''.join([("0000" + bin(int(x,16))[2:])[-4:] for x in hex])
versionNumbers = 0

def read_packet(bits, i=0):
    global versionNumbers
    result = 0

    # Parse version of packet
    version = int(bits[i:i+3],2)
    i += 3
    versionNumbers += version

    # Parse type
    type = int(bits[i:i+3],2)
    i += 3

    if type == 4: # Literal value
        value = ""
        while True:
            next = bits[i:i+5]
            i += 5
            value += next[1:]
            if next[0] == '0': break
        result = int(value,2)
    else: # All other: operator
        lengthTypeID = bits[i:i+1]
        i += 1
        sub_results = []
        if lengthTypeID == '0':
            subPacketBitLength = int(bits[i:i+15], 2)
            i += 15
            cursor = i+subPacketBitLength
            # Read subpackets for length x
            while i < cursor-1:
                i, num = read_packet(bits, i) # TODO should we pass on the length limit of the package?     
                sub_results.append(num)
        else: #lengthTypeId == 1
            numberOfSubPackets = int(bits[i:i+11], 2)
            i += 11
            # Read x subpackets
            for n in range(numberOfSubPackets):
                i, num = read_packet(bits, i)
                sub_results.append(num)

        if type==0:
            result = sum(sub_results)
        elif type==1:
            result = 1
            for n in sub_results:
                result *= n
        elif type==2:
            result = min(sub_results)
        elif type==3:
            result = max(sub_results)
        elif type==5:
            result = 1 if sub_results[0] > sub_results[1] else 0
        elif type==6:
            result = 1 if sub_results[0] < sub_results[1] else 0
        elif type==7:
            result = 1 if sub_results[0] == sub_results[1] else 0
        #print("Result of type", type,"on",sub_results,":",result)
    return i, result

i, result = read_packet(bits)
print("Part I:", versionNumbers)
print("Part II:", result)