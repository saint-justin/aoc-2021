import pathlib
path = f''
data = [[[item, False] for item in line.strip()] for line in open(f'{pathlib.Path().resolve()}/input.txt')]
height, width = len(data), len(data[0])
basin_sizes = {}

# Checks if a position should be explored
def should_be_explored(y_pos, x_pos):
  return data[y_pos][x_pos][0] != '9' and data[y_pos][x_pos][1] == False

# Explore our basin
def explore_basin_node(y_pos, x_pos, basin_id):
  if basin_id in basin_sizes:
    basin_sizes[basin_id] = basin_sizes[basin_id] + 1
  else:
    basin_sizes[basin_id] = 1

  data[y_pos][x_pos][1] = basin_id
  if x_pos + 1 < width:
    if should_be_explored(y_pos, x_pos + 1):
      explore_basin_node(y_pos, x_pos + 1, basin_id)
  if x_pos - 1 >= 0:
    if should_be_explored(y_pos, x_pos - 1):
      explore_basin_node(y_pos, x_pos - 1, basin_id)
  if y_pos + 1 < height:
    if should_be_explored(y_pos + 1, x_pos):
      explore_basin_node(y_pos + 1, x_pos, basin_id)
  if y_pos - 1 >= 0:
    if should_be_explored(y_pos - 1, x_pos):
      explore_basin_node(y_pos - 1, x_pos, basin_id)
  return True

# Explore all basins
current_id = 0
for i in range(0, len(data)):
  for j in range(0, len(data[0])):
    if should_be_explored(i, j):
      explore_basin_node(i, j, str(current_id))
      current_id += 1

# Grab the largest 3 basins and print out their sizes
largest_basins = [0, 0, 0]
for key in basin_sizes:
  size = basin_sizes[key]
  if size > largest_basins[2]:
    largest_basins.pop(0)
    largest_basins.append(size)
  elif size > largest_basins[1]:
    largest_basins.pop(0)
    largest_basins.insert(1, size)
  elif size > largest_basins[0]:
    largest_basins.pop(0)
    largest_basins.insert(0, size)

print(f'Largest 3 Basin Sizes: {largest_basins}   Key: {largest_basins[0] * largest_basins[1] * largest_basins[2]}')