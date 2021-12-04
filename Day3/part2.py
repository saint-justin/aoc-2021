import pathlib
path = f'{pathlib.Path().resolve()}/aoc-2021/Day3'

def reduce_for_oxy(arr, bit_pos):
  # print(f'\nBit Position: {bit_pos}')
  diff = 0
  for line in arr:
    if line[bit_pos] == '1': diff += 1
    else: diff -= 1

  # print(f'Diff: {diff} ==> Preferring {"1" if diff <= 0 else "0"}')

  out = []
  for line in arr:
    if diff >= 0 and line[bit_pos] == '1': out.append(line)
    elif diff < 0 and line[bit_pos] == '0': out.append(line)
  return out

def dec_from_bin(arr):
  sum = 0
  current = 1
  for i in range(len(arr)-1, -1, -1):
    sum += (current) * int(arr[i])
    current *= 2
  return sum

with open(f'{path}/input_test.txt') as f:
  arr = []
  std = []
  inv = []
  for line in f:
    std.append(line[0:-1])
    inv.append(line[0:-1])
  
  for line in f:
    if len(arr) == 0:
      for i in range(0, len(line)-1): 
        arr.append(0)
    else: break
    
  print('Starting cycles...')
  print(std)
  position = 0
  while len(std) > 1:
    std = reduce_for_oxy(std, position)
    position += 1
    # print(f'Standard: {std}')
    # print(f'Inverted: {inv}')

  std_dec = dec_from_bin(std[0])
  # inv_dec = dec_from_bin(inv[0])
  # print(f'std: {std_dec}   inv: {inv_dec}   out: {std_dec * inv_dec}')
  print(f'\nstd: {std_dec}   out: {std_dec } * inv_dec')
