import pathlib
path = f'{pathlib.Path().resolve()}/aoc-2021/Day4'

# Generates all "rows" or "columns" or "diagonals" which could result in a winning board
def check_board(board, done):
  if done:
    return False

  potential_winners = []
  columns = []
  diagonal_1 = []
  diagonal_2 = []

  for i in range(0, 5):
    # Rows
    potential_winners.append(board[i])
    column = []

    for j in range(0, 5):
      # Columns
      column.append(board[i][j])

      # Diagonals
      if i == j: 
        diagonal_1.append(board[i][j])
      if i + j == 4:
        diagonal_2.append(board[i][i])
    columns.append(column)

  # Appending columns + diagonals to the to-be-checked list
  for col in columns:
    potential_winners.append(col)
  potential_winners.append(diagonal_1)
  potential_winners.append(diagonal_2)

  # Actually check every collected data point
  for set in potential_winners:
    check_bingo_success = all([item[1] for item in set])

    if check_bingo_success:
      return True
  
  return False


# Update all boards then check them
boards = []
def update_all_boards(new_number):
  for board in boards:
    update_single_board(new_number, board[0])

def update_single_board(new_number, board):
  for row in board:
    for i in range(len(row)):
      if row[i][0] == new_number:
        row[i] = (row[i][0], True)
        return

# Checks each board for a winner
def check_all_boards(entry):
  for i, board in enumerate(boards):
    if check_board(board[0], board[1]):
      print('Winner found!')
      calculate_winner_score(board[0], entry)
      boards[i] = [board[0], True]

def calculate_winner_score(board, entry):
  unmarked_numbers = 0
  for row in board:
    for item in row:
      if item[1] == False:
        unmarked_numbers += int(item[0])
  print(f'Unmarked Numbers: {unmarked_numbers}   Last Entry Pulled: {entry}   Score: {unmarked_numbers * int(entry)}')


with open(f'{path}/input.txt') as f:
  draws = ''

  # Split up the text input into usable data
  tempBoard = []
  for line in f:
    if draws == '':
      draws = line.strip()
    elif line == '\n':
      if len(tempBoard) > 0:
        boards.append(tempBoard)
      tempBoard = []
    else:
      tupled = []
      for entry in line.strip().split():
        tupled.append(entry)
      tempBoard.append(tupled)
  boards.append(tempBoard)

  for i, board in enumerate(boards):
    for j, row in enumerate(board):
      for k, item in enumerate(row): 
        boards[i][j][k] = [item, False]


  for i, board in enumerate(boards):
    boards[i] = [board, False]
    print(f'\n{boards[i]}')


  
  # Solve for thing
  winner = False
  draws = draws.split(',')

  for entry in draws:
    if all([board[1] for board in boards]):
      print('Done early!')
      break
    update_all_boards(entry)
    check_all_boards(entry)
  print('All entries drawn!')


  

