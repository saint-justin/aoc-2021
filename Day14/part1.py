import pathlib
instructions = [line.strip() for line in open(f'{pathlib.Path().resolve()}/input.txt')]

# Grab the base polymer and remove the empty line
polymer = instructions.pop(0)
instructions.pop(0)
poly_pair_dict = {}

# Helper to find all instances of a given character set
def insert_all_pairs(polymer):
  new_polymer = polymer
  for i in range(len(polymer) - 2, -1, -1):
    mini_polymer = polymer[i] + polymer[i + 1]
    if mini_polymer in poly_pair_dict:
      new_polymer = new_polymer[:i+1] + poly_pair_dict[mini_polymer] + new_polymer[i+1:]
      # print(f'Insertion At: {i+1}  Pair: {mini_polymer}   Insertion: {poly_pair_dict[mini_polymer]}')
  return new_polymer



for line in instructions:
  parsed_instruction = line.split(' -> ')
  poly_pair_dict[parsed_instruction[0]] = parsed_instruction[1]

for i in range(0, 10):
  polymer = insert_all_pairs(polymer)

char_dict = {}
for ch in polymer:
  if ch in char_dict:
    char_dict[ch] = char_dict[ch] + 1
  else:
    char_dict[ch] = 1

most, least = float('-inf'), float('inf')
for key in char_dict:
  # print(f'Key: {key}   Val: {char_dict[key]}')
  if char_dict[key] > most:
    most = char_dict[key]
  if char_dict[key] < least:
    least = char_dict[key]

print(f'Expected final readout: 3073\nActual polymer length: {len(polymer)}')
print(f'Most: {most}   Least: {least}   Output: {most - least}')