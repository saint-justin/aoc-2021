import pathlib
path = f'{pathlib.Path().resolve()}'
data = [[int(num) for num in line.split(',')] for line in open(f'{path}/input_test.txt')][0]

sum = 0
for item in data:
  sum += item
mean = round(sum / len(data))

def cost_to_scuttle(arr, position):
  sum = 0
  for item in arr:
    sum += max(item, position) - min(item, position)
  return sum

one_over = cost_to_scuttle(data, mean + 1)
mean_exact = cost_to_scuttle(data, mean)
one_under = cost_to_scuttle(data, mean - 1)

# while True:
  # if

