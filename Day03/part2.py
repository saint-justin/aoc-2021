import pathlib
path = f'{pathlib.Path().resolve()}/Day3'

def reduce(arr, bit_pos, a, b):
  if len(arr) == 1: 
    return arr

  diff = 0
  for line in arr:
    if line[bit_pos] == '1': diff += 1
    else: diff -= 1

  out = []
  for line in arr:
    if diff >= 0 and line[bit_pos] == a: out.append(line)
    elif diff < 0 and line[bit_pos] == b: out.append(line)
  return out

def reduce_for_oxy(arr, bit_pos):
  return reduce(arr, bit_pos, '1', '0')

def reduce_for_co2(arr, bit_pos):
  return reduce(arr, bit_pos, '0', '1')

def dec_from_bin(arr):
  sum = 0
  current = 1
  for i in range(len(arr)-1, -1, -1):
    sum += current * int(arr[i])
    current *= 2
  return sum


with open(f'{path}/input.txt') as f:
  std = []
  co2 = []
  for line in f:
    std.append(line[0:-1])
    co2.append(line[0:-1])
    
  position = 0
  while True:
    std = reduce_for_oxy(std, position)
    co2 = reduce_for_co2(co2, position)
    
    if len(std) == 1 and len(co2) == 1: 
      break

    position += 1

  std_dec = dec_from_bin(std[0])
  co2_dec = dec_from_bin(co2[0])
  print(f'\nstd: {std_dec}   co2: {co2_dec}   out: {std_dec * co2_dec}')
