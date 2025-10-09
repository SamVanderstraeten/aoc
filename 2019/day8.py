file = open("input/day8.txt", "r")
lines = file.readlines()
enc = lines[0]

w = 25
h = 6

layer_size = w*h
min_zeros = 9999999
num_layers = int(len(enc)/layer_size)
checksum = 0
msg = [[-1 for i in range(w)] for j in range(h)]
for layer_index in range(0, num_layers):
    layer = enc[layer_index*layer_size:(layer_index+1)*layer_size]

    # decode
    for row in range(0,h):
        for col in range(0,w):
            if msg[row][col] == "2" or msg[row][col] == -1:
                msg[row][col] = layer[row*w + col]

    # store checksum
    if layer.count("0") < min_zeros:
        checksum = layer.count("1") * layer.count("2")
        min_zeros = layer.count("0")

print("Checksum: " + str(checksum))

for r in range(0,h):
    for c in range(0,w):
        if msg[r][c] == "1":
            print("0 ", end='')
        else:
            print("  ", end='')
    print()



