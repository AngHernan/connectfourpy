import connectfour

def _user_interface():
  '''interface for connect four game
  '''

  welcome()
  game = connectfour.new_game()
  choice = game_choice()

  if choice == 'drop':
    print_game(game)
    _drop_game(game)
    
  elif choice == 'pop':
    print_game(game)
    _pop_game(game)
  
def welcome():
  '''prints welcome message
  '''

  print('Welcome to Connect 4')
  print()
  
def print_game (game: connectfour.GameState):
  '''Prints current state of the game
  '''
  
  _print_colnumber(game)
  _print_rows(game)
  

def game_choice() -> str:
  '''Prompts user for the choice of game they want
  '''
  try:
    x = input('What version of the game would you like to play, Drop or Pop? ')
    print()
    return x.lower()
    
  except ValueError:
      _invalid_res()
      game_choice()

def move(game: connectfour.GameState) -> int:
  '''prompts color for a move and returns a column number as integer
  '''
    
  m = int(input(_player_name(game.turn) + ', please enter a number between 1 and ' + str(connectfour.BOARD_COLUMNS)+ ': ')) -1
  print()
  return m

def drop_(game: connectfour.GameState) -> str:
  '''Runs the Drop move of Connect 4
  '''
  
  try:
    game = connectfour.drop(game, move(game))
    print_game(game)

    return game

  except ValueError:
    _move_invalid()
    _drop_game(game)
    
  except connectfour.InvalidMoveError:
    _move_invalid()
    _drop_game(game)
    
def pop_(game: connectfour.GameState) -> str:
  '''Runs the Pop move Connect 4
  '''
  
  try:
    game = connectfour.pop(game, move(game))
    print_game(game)

    return game
        

  except ValueError:
    _move_invalid()
    _pop_game(game)

  except connectfour.InvalidMoveError:
    _move_invalid()
    print('Make sure your piece is in the column!')
    print()
    _pop_game(game)

   
def _drop_game(game: connectfour.GameState):
    game = drop_(game)
    
    if connectfour.winner(game) == 0:
      _drop_game(game)
      
    else:
      _winner(game)
      _play_again()

def _pop_game (game: connectfour.GameState):
  '''Runs the pop game of Connect 4
  '''
  
  try:
    x = input(_player_name(game.turn) + ', Drop or Pop? ')
    if x.lower() == 'pop':
      game = pop_(game)
    elif x.lower() == 'drop':
      game = drop_(game)
    
  except ValueError:
    _invalid_response()
    pop_game()

  else:
    if connectfour.winner(game) == 0:
      _pop_game(game)
      
    else:
      _winner(game)
      _play_again() 
  
def _player_name(turn: int):
  '''Returns string of player name
  '''

  player = ''
  
  if turn == 1:
    player = 'Red'
  elif turn ==2:
    player = 'Yellow'
  return player

def _print_colnumber(game: connectfour.GameState):
  '''Prints the columns for the game
  '''

  ColNum = ' '
  for i in range(1,connectfour.BOARD_COLUMNS + 1):
    ColNum += str(i) + '  '
  print(ColNum)
  print()

def _print_rows (game: connectfour.GameState):
  '''Prints the rows for the game
  '''

  for l in range(len(game.board)-1):
    row = ' '
    for m in game.board:      
      row += str(m[l]) + '  '
    print(_trans_numbs(row))
  print()  
    
def _trans_numbs(s:str) -> str:
  '''translates number to symbols for players and empty spaces
  '''
  
  table = str.maketrans('012','.RY')
  return s.translate(table)   

def _winner(game: connectfour.GameState):
  '''prints winner of the game
  '''
  winner = _player_name(connectfour.winner(game))
  print(winner + ' wins the game!')

def _invalid_res():
  '''prints invalid response
  '''

  print('Not a valid response, try again!')
  
def _move_invalid():
  '''prints invalid move message'''
  print('Not a valid move!')

def _play_again():
  '''Prompts players if they want to play again
  '''
  
  try:
    ans = input('Would you like to play again? Y or N? ')
    if ans.upper() == 'Y':
      _user_interface()
    elif ans.upper() == 'N':
      print('Okay, Goodbye')
      
  except ValueError:
    _invalid_res()
    _play_again()
 
  
  
if __name__ == '__main__':
	_user_interface()
