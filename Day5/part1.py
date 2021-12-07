import pathlib
path = f'{pathlib.Path().resolve()}/Day5'

# Line position points
position_pairs = []
slope_intercept_pairs = []
collision_positions = {}

# Parse the positions from the inputs
def parse_position_pair(line):
  split = line.split(' -> ')
  point_a = split[0].strip().split(',')
  point_b = split[1].strip().split(',')
  position_pairs.append((point_a, point_b))

# Get the y-intercept + slope from a given set of points
def get_slope_intercept_pair(point_a, point_b):
  slope = (int(point_a[1]) - int(point_b[1])) / (int(point_a[0]) - int(point_b[0]))
  y_intercept = int(point_a[1]) - (slope * int(point_a[0]))
  print(f'\nPoints:   a: [{point_a[0]},{point_a[1]}]   b: [{point_b[0]},{point_b[1]}]')
  print(f'Slope: {slope}   Y-Intercept: {y_intercept}')
  return (slope, y_intercept)

# Underlying Math
# y = (m*x) + b
# xPos = (b2 - b1) / (m1 * m2)
# yPos = m1(xPos) + b1

# Get the collision of two lines, return false if lines are parallel
def get_collision_of_two_lines(slope_intercept_a, slope_intercept_b):
  slope_a = int(slope_intercept_a[0])
  slope_b = int(slope_intercept_b[0])
  intercept_a = int(slope_intercept_a[1])
  intercept_b = int(slope_intercept_b[1])

  # If the lines are parallel, throw an error
  if slope_a == slope_b or slope_a == slope_b * -1:
    return False

  xPos = (intercept_a - intercept_b) / (slope_a * slope_b)
  yPos = (slope_intercept_a[0] * xPos) + slope_intercept_a[1]
  return (xPos, yPos)


with open(f'{path}/input_test.txt') as f:
  for line in f:
    position_pairs.append(parse_position_pair(line))

  for pair in position_pairs:
    slope_intercept_pairs.append(get_slope_intercept_pair(pair[0], pair[1]))

  for pair in slope_intercept_pairs:
    position = get_collision_of_two_lines(pair[0], pair[1])
    if position != False:
      key = f'{position[0]},{position[1]}'
      collision_positions.update(key, True)

  print('Collision Positions: ')
  for position in collision_positions:
    print(position)

  print(f'Total positions: {len(collision_positions.keys())}')
