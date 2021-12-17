import pathlib
path = f'{pathlib.Path().resolve()}'
data = [[int(num) for num in line.split(',')] for line in open(f'{path}/input.txt')][0]
print(data)

def cycle(arr):
  out = []
  for item in arr:
    if item == 0:
      out.append(6)
      out.append(8)
    else:
      out.append(item - 1)
  return out


for i in range(0, 80):
  data = cycle(data)
  print(f'Cycle number {i} completed! There are {len(data)} lanternfish!')

print(len(data))
