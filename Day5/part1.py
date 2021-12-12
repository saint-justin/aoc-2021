import pathlib
data = [line.strip() for line in open(f'{pathlib.Path().resolve()}/input_test.txt')]

class LineInfo:
  def __init__(self, pos, min, max):
    self.position = pos
    self.extent_min = min
    self.extent_max = max


# Get the exents + positions of the vertical and horizontal lines as tuples
vertical_lines, horizontal_lines = [], []
for line in data:
  positions = [[int(num_str) for num_str in pair.split(',')] for pair in line.split(' -> ')]

  # x positions are the same, horizontal line
  x1, x2 = positions[0][0], positions[0][1]
  y1, y2 = positions[1][0], positions[1][1]
  if x1 == x2:
    line = LineInfo(x1, min(y1, y2), max(y1, y2))
    horizontal_lines.append(line)
  elif y1 == y2:
    line = LineInfo(y1, min(x1, x2), max(x1, x2))
    vertical_lines.append


  print(f'new position set: {positions}')