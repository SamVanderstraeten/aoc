file = open("input/6.sam", "r")                     
fish = [int(x) for x in file.readline().split(",")]
num_for_state = [fish.count(i) for i in range(0,9)]
for i in range(0, 256):
    new_kids = num_for_state.pop(0)
    num_for_state.append(new_kids)
    num_for_state[6] += new_kids
print(sum(num_for_state))