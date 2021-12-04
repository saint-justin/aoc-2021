total = 0

with open(r'c:\Users\gearp\Desktop\Coding\AoC_21\Day1\input.txt', encoding='utf8') as f:
  arr = []
  for line in f:
    num = int(line)
    if len(arr) < 3: 
      arr.append(num)
      continue
    else:
      sum1 = sum(arr)
      arr.pop(0)
      arr.append(num)
      sum2 = sum(arr)
      if sum2 > sum1:
        total += 1
    prev = num

print(total)