pos = [0,0,0]
d = { 'up': -1, 'down': 1  }

with open(r'c:\Users\gearp\Desktop\Coding\AoC_21\Day2\input.txt') as f:
  for line in f:
    split = line.split()
    num = int(split[1])
    if split[0] == 'forward': 
      pos[0] += num
      pos[1] += num * pos[2]
    else: 
      pos[2] += num * d[split[0]]

print(pos[0] * pos[1])