import pathlib
path = f'{pathlib.Path().resolve()}/Day4'

with open(f'{path}/input_test.txt') as f:
  draws = ''

  boards = []
  tempBoard = []
  for line in f:
    if draws == '':
      draws = line[:-1]
    elif line == '\n':
      if len(tempBoard) > 0:
        boards.append(tempBoard)
      tempBoard = []
    else:
      tupled = []
      for entry in line[:-1].split():
        tupled.append((entry, 0))
      tempBoard.append(tupled)
  boards.append(tempBoard)

  print(f'draws in order: {draws}')
  for board in boards:
    print('\nNew Board!')
    for line in board:
      printableLine = []
      for entry in line:
        printableLine.append(entry[1])
      print(printableLine)
  
  