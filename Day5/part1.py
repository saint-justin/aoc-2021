import pathlib
path = f'{pathlib.Path().resolve()}/Day5'

# Line position points
position_pairs = []
slope_intercept_pairs = []
collision_positions = {}

class ExtentsWrapper:
  def __init__(self, x_min, x_max, y_min, y_max):
    self.x_min = x_min
    self.x_max = x_max
    self.y_min = y_min
    self.y_max = y_max

# Parse the positions from the inputs
def parse_position_pair(line):
  split = line.split(' -> ')
  point_a = split[0].strip().split(',')
  point_b = split[1].strip().split(',')
  return [point_a, point_b]

# Get the y-intercept + slope from a given set of points
def get_slope_intercept_pair(point_a, point_b):
  x1 = int(point_a[0])
  y1 = int(point_a[1])
  x2 = int(point_b[1])
  y2 = int(point_b[1])
  slope = 1 if (x1 - x2) == 0 else (y1 - y2) / (x1 - x2)
  y_intercept = y1 - (slope * x1)

  # Extents are defined as xMin, yMin, xMax, yMax
  extents = ExtentsWrapper(min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2))

  return [slope, y_intercept, extents]

# Underlying Math
# y = (m*x) + b
# xPos = (b2 - b1) / (m1 * m2)
# yPos = m1(xPos) + b1

# Get the collision of two lines, return false if lines are parallel
def get_collision_of_two_lines(slope_intercept_a, slope_intercept_b):
  slope_a = slope_intercept_a[0]
  slope_b = slope_intercept_b[0]
  intercept_a = slope_intercept_a[1]
  intercept_b = slope_intercept_b[1]
  extents_a = slope_intercept_a[2]
  extents_b = slope_intercept_b[2]

  # If the lines are parallel, throw an error
  if slope_a == slope_b or slope_a == slope_b * -1:
    return False

  x_pos = (intercept_a - intercept_b) / (slope_a - slope_b)
  y_pos = (slope_intercept_a[0] * x_pos) + slope_intercept_a[1]

  print(f'\nPosition: [{x_pos}, {y_pos}]')
  print(f'A: xmin: {extents_a.x_min}   xmax: {extents_a.x_max}  ymin: {extents_a.y_min}  ymax: {extents_a.y_max}')
  print(f'B: xmin: {extents_b.x_min}   xmax: {extents_b.x_max}  ymin: {extents_b.y_min}  ymax: {extents_b.y_max}')

  x_min = min(extents_a.x_min, extents_b.x_min)
  x_max = max(extents_a.x_max, extents_b.x_max)
  y_min = max(extents_a.x_min, extents_b.x_min)
  y_max = max(extents_a.x_max, extents_b.x_max)
  if x_pos >= x_min and x_pos <= x_max and y_pos >= y_min and y_pos <= y_max:
    print('Accepted')
    return (x_pos, y_pos)
  else: 
    print('Rejected')
    return False


with open(f'{path}/input_test.txt') as f:
  for line in f:
    position_pairs.append(parse_position_pair(line))

  for pair in position_pairs:
    slope_intercept_pairs.append(get_slope_intercept_pair(pair[0], pair[1]))

  for i in range(0, len(slope_intercept_pairs)):
    for j in range(i, len(slope_intercept_pairs)):
      if i == j: 
        continue
      position = get_collision_of_two_lines(slope_intercept_pairs[i], slope_intercept_pairs[j])
      if position != False and position != None:
        print(position)
        key = f'[{round(position[0], 6)},{round(position[1], 6)}]'
        if key in collision_positions:
          collision_positions[key] = collision_positions[key] + 1
        else: 
          collision_positions[key] = 1

  important_crossings = 0
  for key in collision_positions:
    if collision_positions[key] > 1:
      important_crossings += 1
      print(f'Key: {key}   Count: {collision_positions[key]}')



  print(f'Total positions: {important_crossings}')
