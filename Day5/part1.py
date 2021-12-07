import pathlib
path = f'{pathlib.Path().resolve()}/aoc-2021/Day5'

# Line position points
position_pairs = []
slope_intercept_pairs = []
crossover_positions = []

# Parse the positions from the inputs
def parse_position_pair(line):
  split = line.split(' -> ')
  point_a = split[0].strip().split(',')
  point_b = split[1].strip().split(',')
  position_pairs.append((point_a, point_b))

# Parse the y-intercept + slope from a given set of points
def define_slope_intercept_pair(point_a, point_b):
  slope = (point_a[1] - point_b[1]) / (point_a[0] - point_b[0])
  y_intercept = point_a[1] - (slope * point_a[0])
  slope_intercept_pairs.append((slope, y_intercept))
  print(f'\nPoints:   a: [{point_a[0]},{point_a[1]}]   b: [{point_b[0]},{point_b[1]}]')
  print(f'Slope: {slope}   Y-Intercept: {y_intercept}')

# Get the interception of two points, return false if no
def find_interception_of_two_lines(slope_intercept_a, slope_intercept_b):



with open(f'{path}/input_test.txt') as f:
  for line in f:
    parse_position_pairs(line)
