import pathlib
path = f'{pathlib.Path().resolve()}'
data = [[int(num) for num in line.split(',')] for line in open(f'{path}/input.txt')][0]
cache, sum, days = {}, 0, 256

# Resursively solve for each fish
def calculate_lanternfish_generated(days_until_next_lanternfish, cycles_remaining):
  key = (days_until_next_lanternfish, cycles_remaining)
  if key in cache:
    return cache[key]

  total = 1
  while cycles_remaining > days_until_next_lanternfish:
    cycles_remaining -= days_until_next_lanternfish
    total += calculate_lanternfish_generated(9, cycles_remaining)
    days_until_next_lanternfish = 7
    
  cache[key] = total
  return total

for item in data:
  sum += calculate_lanternfish_generated(item, days)

print(f'Total amount of lanternfish after {days} days: \n{sum} Fishies')