import pathlib
data = [line.strip() for line in open(f'{pathlib.Path().resolve()}/input.txt')]
height, width = len(data), len(data[0])


# Return whether all adjacent nodes are greater than this node
def check_low_point(y_pos, x_pos):
  point_value = int(data[y_pos][x_pos])
  if x_pos + 1 < width:
    if int(data[y_pos][x_pos + 1]) <= point_value:
      return False
  if x_pos - 1 >= 0:
    if int(data[y_pos][x_pos - 1]) <= point_value:
      return False
  if y_pos + 1 < height:
    if int(data[y_pos + 1][x_pos]) <= point_value:
      return False
  if y_pos - 1 >= 0:
    if int(data[y_pos - 1][x_pos]) <= point_value:
      return False
  return True

low_points = []
for i in range(0, len(data)):
  for j in range(0, len(data[0])):
    if check_low_point(i, j):
      low_points.append((i, j))

print('Low Points:')
risk_level = 0
for point in low_points:
  print(f'Value: {data[point[0]][point[1]]}   Position: [{point[1]}, {point[0]}]')
  risk_level += int(data[point[0]][point[1]]) + 1

print(f'Map Risk Level: {risk_level}')