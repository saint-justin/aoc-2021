pos = [0,0]

with open(r'c:\Users\gearp\Desktop\Coding\AoC_21\Day2\input.txt') as f:
  for line in f:
    split = line.split()
    num = int(split[1])
    if split[0] == 'forward': pos[0] += num
    elif split[0] == 'up': pos[1] -= num
    elif split[0] == 'down': pos[1] += num
    else: print('ERROR')

print(f'X: {pos[0]}   Y: {pos[1]}')
print(pos[0] * pos[1])