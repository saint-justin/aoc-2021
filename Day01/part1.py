total = 0

with open(r'c:\Users\gearp\Desktop\Coding\AoC_21\Day1\input.txt', encoding='utf8') as f:
  prev = 0
  for line in f:
    num = int(line)
    if prev == 0: 
      prev = num
      continue
    elif num > prev: 
      total += 1
    prev = num

print(total)