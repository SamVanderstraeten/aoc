import sys, math

file = open("input/day14.txt", "r")
lines = file.readlines()

parsedict = lambda x: (x[1], int(x[0]))
tr = lambda s: dict(parsedict(x.split(' ')) for x in s.split(', '))
data = [tr(x) for line in lines for x in line.strip().split(' => ')]

l, r = [], []
for i in range(0, len(data), 2):
  l.append(data[i])
  r.append(data[i+1])

def qty(element = 'ORE', fuel = 1):
  if element == 'FUEL':
      return fuel

  q = 0
  for i, recipe in enumerate(l):
    if element in recipe:
      parent, *_ = list(r[i])
      parent_batch_qty = r[i][parent]
      q += math.ceil(qty(parent, fuel) / parent_batch_qty) * recipe[element]

  return q

print(qty('ORE', 1), 'ORE', '==> 1 FUEL')


ORE_MAX = 1_000_000_000_000
fuel_min, fuel_max = 1, 100_000_000

while (fuel_max - fuel_min) > 1:
  m = (fuel_min + fuel_max) // 2
  if qty(fuel=m) <= ORE_MAX:
    fuel_min = m
  else:
    fuel_max = m

print('1T ORE', '==>', fuel_min, 'FUEL')