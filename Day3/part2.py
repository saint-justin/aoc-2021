def reduce_for_pref(arr, bit_pos, pref):
  print(f'\nBit Position: {bit_pos}')
  print(f'{"std" if pref == "greater" else "rev"}: [{arr}]')
  diff = 0
  for line in arr:
    if line[bit_pos] == '1': diff += 1
    else: diff -= 1

  print(f'Diff: {diff} ==> Preferring {"1" if diff <= 0 else "0"}')

  out = []
  for line in arr:
    if diff >= 0 and line[bit_pos] == '1': out.append(line)
    elif diff < 0 and line[bit_pos] == '0': out.append(line)
  
  print(f'Out: {out}')
  return out

def reduce_for_oxy(arr, bit_pos):
  return reduce_for_pref(arr, bit_pos, "1", "0")

def reduce_for_co2(arr, bit_pos):
  return reduce_for_pref(arr, bit_pos, "0", "1")

def dec_from_bin(arr):
  sum = 0
  current = 1
  for i in range(len(arr)-1, -1, -1):
    sum += (current) * arr[i]
    current *= 2
  return sum

with open(r'c:\Users\gearp\Desktop\Coding\AoC_21\Day3\input_test.txt') as f:
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
    
  print('Starting cycles...')
  print(std)
  position = 0
  while len(std) > 1:
    std = reduce_for_oxy(std, position)
    inv = reduce_for_co2(inv, position)
    position += 1
    print(f'Standard: {std}')
    print(f'Inverted: {inv}')

  std_dec = dec_from_bin(std[0])
  inv_dec = dec_from_bin(inv[0])
  print(f'std: {std_dec}   inv: {inv_dec}   out: {std_dec * inv_dec}')
