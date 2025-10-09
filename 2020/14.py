file = open("input/14.sam", "r")
lines = file.readlines()

def decoder_v1():
  mem = {}
  for line in lines:
      loc, value = line.strip().split(" = ")

      # make 0 for defined zero in mask => AND operation
      # make 1 for defined one in mask => OR operation
      if loc == "mask":
        and_mask = int(value.replace("X", "1"), 2)
        or_mask = int(value.replace("X", "0"), 2)
      else:
        register = loc[4:-1]
        mem[int(register)] = (int(value) & and_mask) | or_mask

  return sum(mem.values())

def decoder_v2():
  base_mask = ''
  registers = {}

  for line in lines:
    address, val = line.strip().split(" =" )

    if address == "mask":
      base_mask = val.strip()

    else:
      register = int(address[4:-1])
      register_mask = ''

      for i in range(len(base_mask)):
        if base_mask[i] == 'X':
          register_mask += 'X'
        else:
          register_mask += str(int(base_mask[i]) | ((register >> len(base_mask) - 1 - i) & 1))
      
      for register in apply_masks(register_mask):
        registers[register] = int(val)

  return sum(registers.values())


def apply_masks(mask: str):
  zeroes = mask.replace('X', '0', 1)
  if zeroes == mask:
    return [int(mask, 2)]

  return apply_masks(zeroes) + apply_masks(mask.replace('X', '1', 1))

print("V1:",decoder_v1())
print("V2:",decoder_v2())