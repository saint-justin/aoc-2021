import pathlib

class DumboSystem:
  def __init__(self, dumbos):
    self.dumbos = dumbos
    self.flashes = 0

  def position_is_legal(self, x, y):
    if x >= 10 or y >= 10 or x < 0 or y < 0:
      return False
    return True

  def get_legal_adjacent_dumbo_positions(self, x, y):
    adjacents = []
    for i in range(-1, 2):
      for j in range(-1, 2):
        if i == 0 and j == 0:
          continue
        if self.position_is_legal(x + i, y + j):
          adjacents.append((x + i, y + j))
    return adjacents

  def flash_around_position(self, x, y):
    legal_adjacents = self.get_legal_adjacent_dumbo_positions(x, y)
    for position in legal_adjacents:
      self.dumbos[position[0]][position[1]] += 1
      if self.dumbos[position[0]][position[1]] == 10:
        self.flash_around_position(position[0], position[1])
  
  def cycle(self):
    for i in range(0, 10):
      for j in range(0, 10):
        self.dumbos[i][j] += 1
        if self.dumbos[i][j] == 10:
          self.flash_around_position(i, j)
  
  def clean_up(self):
    for i in range(0, 10):
      for j in range(0, 10):
        if self.dumbos[i][j] > 9:
          self.dumbos[i][j] = 0
          self.flashes += 1


def main():
  dumbos = [[int(num) for num in line.strip()] for line in open(f'{pathlib.Path().resolve()}/input.txt')]
  system = DumboSystem(dumbos)

  for cycle_number in range(0, 100):
    system.cycle()
    system.clean_up()
    print(f'\nCycle Number {cycle_number + 1}:\nFlashes: {system.flashes}')


      
        
  # print(f'\nCycle Number {cycle_number + 1}:\nFlashes: {total_flashes}')
  # for line in dumbos:
    # print(line)



if __name__=="__main__":
  main()