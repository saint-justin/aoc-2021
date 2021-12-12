import pathlib
data = [line.strip() for line in open(f'{pathlib.Path().resolve()}/input.txt')]

dictionary = {}
dictionary['('] = ')'
dictionary['['] = ']'
dictionary['{'] = '}'
dictionary['<'] = '>'

def find_first_error(line):
  stack = []
  for char in line:
    if char in dictionary:
      stack.append(char)
    else:
      if dictionary[stack.pop()] != char:
        return char
  return -1

syntax_error_sum = 0
for line in data:
  err = find_first_error(line)
  if err != -1:
    if err == ')':
      syntax_error_sum += 3
    elif err == ']':
      syntax_error_sum += 57
    elif err == '}':
      syntax_error_sum += 1197
    elif err == '>':
      syntax_error_sum += 25137
    else:
      print(f'Invalid Error Character: {err}')

print(f'Syntax Error Sum: {syntax_error_sum}')  