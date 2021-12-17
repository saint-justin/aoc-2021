import pathlib

def position_is_legal(x, y):
  if x >= 10 or y >= 10 or x < 0 or y < 0:
    return False
  return True

def get_legal_adjacent_dumbo_positions(x, y):
  adjacents = []
  for i in range(-1, 2):
    for j in range(-1, 2):
      if i == 0 and j == 0:
        continue
      if position_is_legal(x + i, y + j):
        adjacents.append((x + i, y + j))
  return adjacents

def main():
  dumbos = [[int(num) for num in line.strip()] for line in open(f'{pathlib.Path().resolve()}/input_test.txt')]

  def flash_around_position(x, y):
    new_flashes = 1
    legal_adjacents = get_legal_adjacent_dumbo_positions(x, y)
    for position in legal_adjacents:
      dumbos[position[0]][position[1]] += 1
      if dumbos[position[0]][position[1]] == 10:
        flash_around_position(position[0], position[1])
    return new_flashes

  def cycle():
    for i in range(0, 10):
      for j in range(0, 10):
        dumbos[i][j] += 1
        if dumbos[i][j] == 10:
          flash_around_position(i, j)

  total_flashes = 0
  for cycle_number in range(0, 100):
    for i in range(0, 00):
      for j in range(0, 10):
        if dumbos[i][j] > 9:
          dumbos[i][j] = 0

    print(f'\nCycle Number {cycle_number + 1}:\nFlashes: {total_flashes}')
    # for line in dumbos:
      # print(line)



if __name__=="__main__":
  main()