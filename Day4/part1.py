import pathlib
path = f'{pathlib.Path().resolve()}/aoc-2021/Day4'

# Generates all "rows" or "columns" or "diagonals" which could result in a winning board
def check_board(board):
  potential_winners = []
  columns = []
  diagonal_1 = []
  diagonal_2 = []

  for i in range(0, 5):
    # Rows
    potential_winners.append(board[i])

    for j in range(0, 5):
      # Columns
      columns.append(board[i][j])

      # Diagonals
      if i == j: 
        diagonal_1.append(board[i][j])
      if i + j == 4:
        diagonal_2.append(board[i][i])

  for col in columns:
    potential_winners.append(col)
  
  potential_winners.append(diagonal_1)
  potential_winners.append(diagonal_2)

  for set in potential_winners:
    if all([item[1] for item in set]):
      return True
  
  return False


# Update all boards then check them
boards = []
def update_all_boards(new_number):
  for board in boards:
    for row in board:
      for item in row:
        if item[0] == new_number:
          item[1] == True
          return

# Debug output to print out all the boards
def print_all_boards():
  print(f'draws in order: {draws}')
  for board in boards:
    print('\nNew Board!')
    for line in board:
      printableLine = []
      for entry in line:
        printableLine.append(entry[1])
      print(printableLine)

def check_all_boards():
  for board in boards:
    if check_board(board):
      print('Winner found!')
      print(board)
      return True

with open(f'{path}/input_test.txt') as f:
  draws = ''

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
        tupled.append((entry, False))
      tempBoard.append(tupled)
  boards.append(tempBoard)

  # Solve for thing
  winner = False
  draws = draws.split(',')

  for entry in draws:
    update_all_boards(entry)
    if check_all_boards():
      break
    print_all_boards()


  

