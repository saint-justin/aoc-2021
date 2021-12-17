def dec_from_bin(arr):
  sum = 0
  current = 1
  for i in range(len(arr)-1, -1, -1):
    sum += (current) * arr[i]
    current *= 2
  return sum


with open(r'c:\Users\gearp\Desktop\Coding\AoC_21\Day3\input.txt') as f:
  arr = []
  for line in f:

    if len(arr) == 0:
      for i in range(0, len(line)-1): 
        arr.append(0)

    for i in range(0, len(line)-1): 
      if (line[i] == '0'): arr[i] -= 1
      else: arr[i] += 1

  bin = []
  for num in arr:
    if num > 0: bin.append(1)
    elif num < 0: bin.append(0)

  rev = []
  for num in bin:
    if num == 1: rev.append(0)
    else: rev.append(1)

  bin_dec = dec_from_bin(bin)
  rev_dec = dec_from_bin(rev) 
  print(f'bin: {bin_dec}   rev: {rev_dec}   product: {bin_dec * rev_dec}')