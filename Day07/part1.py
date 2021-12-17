import pathlib
path = f'{pathlib.Path().resolve()}'
data = [[int(num) for num in line.split(',')] for line in open(f'{path}/input.txt')][0]
cache = {}

sum = 0
for item in data:
  sum += item
position = round(sum / len(data)) # Start at the mean

def cost_to_scuttle(position):
  if position in cache:
    return cache[position]

  sum = 0
  for item in data:
    sum += max(item, position) - min(item, position)
  cache[position] = sum
  return sum

while True:
  one_over = cost_to_scuttle(position + 1)
  position_cost = cost_to_scuttle(position)
  one_under = cost_to_scuttle(position - 1)
  cheapest = min(one_over, position_cost, one_under)
  if cheapest == position_cost:
    break
  elif cheapest == one_over:
    position += 1
  else:
    position -= 1 

print(f'Cheapest position is: {position}   \nCost at {position} is: {cost_to_scuttle(position)}')