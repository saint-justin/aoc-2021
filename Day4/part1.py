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
      tempBoard.append(line[:-1].split())
  boards.append(tempBoard)

  print(f'draws in order: {draws}')
  tBoards = []
  for board in boards:
    tBoard = []
    for line in board:
      tLine = []
      for entry in line:
        tLine.append((entry, 0))
      tBoard.append(tLine)
    tBoards.append(tBoard)
  
  for tBoard in tBoards:
    print('\nNew Board!')
    for line in tBoard:
      printableLine = []
      for entry in line:
        printableLine.append(entry[1])
      print(printableLine)
  
  