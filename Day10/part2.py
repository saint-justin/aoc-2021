import pathlib
data = [line.strip() for line in open(f'{pathlib.Path().resolve()}/input.txt')]

error_dictionary = {}
error_dictionary['('] = ')'
error_dictionary['['] = ']'
error_dictionary['{'] = '}'
error_dictionary['<'] = '>'

inverted_dictionary = {}
for key, value in error_dictionary.items():
  inverted_dictionary[value] = key

score_dictionary = {}
score_dictionary['('] = 1
score_dictionary['['] = 2
score_dictionary['{'] = 3
score_dictionary['<'] = 4

def find_first_error(line):
  stack = []
  for char in line:
    if char in error_dictionary:
      stack.append(char)
    else:
      if error_dictionary[stack.pop()] != char:
        return -1
  return stack

syntax_error_sum = 0
syntax_stack_scores = []
for line in data:
  err = find_first_error(line)
  if err != -1:
    syntax_score = 0  
    while len(err) > 0:
      syntax_score *= 5
      syntax_score += score_dictionary[err.pop()]
    syntax_stack_scores.append(syntax_score)

syntax_stack_scores.sort()
while len(syntax_stack_scores) > 1:
  syntax_stack_scores.pop(0)
  syntax_stack_scores.pop()

print(f'Syntax Error Sum: {syntax_stack_scores[0]}')  