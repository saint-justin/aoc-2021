import pathlib
instructions = [line.strip() for line in open(f'{pathlib.Path().resolve()}/input_test.txt')]

# Grab the base polymer and remove the empty line
polymer = instructions.pop(0)
instructions.pop(0)

# Helper to find all instances of a given character set
def get_all_pair_positions(pair):
  positions = []
  for i in range(0, len(polymer) - 1):
    if polymer[i] + polymer[i + 1] == pair:
      positions.append(i)
  return positions  

# Executes a single set of polymer instructions on our polymer
def execute_polymer_instruction(instructions, polymer):
  instructions = instructions.split(' -> ')
  identifier, insertion = instructions[0], instructions[1]
  print(f'\nPolmer: {polymer}   \nIdentifier: {identifier}   Insertion: {insertion}')
  places_to_insert = get_all_pair_positions(identifier)[::-1]
  print(f'Polymer Pair Detections: {places_to_insert}')
  for position in places_to_insert:
    polymer = polymer[:position] + insertion + polymer[position:]


# for i in range (0, 10):
for line in instructions:
  execute_polymer_instruction(line, polymer)

print(f'Expected final readout: 1588\nActual polymer length: {len(polymer)}')