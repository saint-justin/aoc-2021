import pathlib
import copy

# Class definition for a cave to simplify traversal
class Cave:
  def __init__(self, first_connection, name):
    self.connections = [first_connection]
    self.name = name
    self.is_small = True if name == name.lower() else False
  
  # Helper to get a list of legal connections
  def get_remaining_connections(self, used_connections, all_caves):
    remaining_connections = copy.deepcopy(self.connections)
    for connection in used_connections:
      if connection in remaining_connections and all_caves[connection].is_small:
        remaining_connections.remove(connection)
    return remaining_connections

  # Debug helper
  def print_connections(self):
    for connection in self.connections:
      print(f'{self.name} -> {connection}')

# Simple DFS implementation with counter for amount of solutions
def explore(all_caves, current_cave_name, explored_caves):
  solutions = 0
  current = all_caves[current_cave_name]
  to_explore = current.get_remaining_connections(explored_caves, all_caves)
  explored_caves.append(current_cave_name)
  for new_cave in to_explore:
    if new_cave == 'end':
      solutions += 1

    else:
      solutions += explore(all_caves, new_cave, copy.deepcopy(explored_caves))
  return solutions
  
# Helper function to add cave connections
def add_cave_connection(all_caves, cave_1, cave_2):
  if cave_1 in all_caves:
    all_caves[cave_1].connections.append(cave_2)
  else:
    all_caves[cave_1] = Cave(cave_2, cave_1)
  return all_caves

def main():
  # Generating cave system definition
  instructions = [line.strip() for line in open(f'{pathlib.Path().resolve()}/input.txt')]
  caves = {}
  for line in instructions:
    cave_1, cave_2 = line.split('-')
    caves = add_cave_connection(caves, cave_1, cave_2)
    caves = add_cave_connection(caves, cave_2, cave_1)

  cave_solutions = explore(caves, 'start', [])
  print(f'Cave Paths: {cave_solutions}')
  

if __name__ == '__main__':
  main()