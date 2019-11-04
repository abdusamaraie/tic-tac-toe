'''
  Simple Game Project: a tic tac toe game to demonstrate string manipulation, and using list,
'''

# Print or Display board

# Get player position

# start the game 
  
# To clear the screen after displaying the board use:
#test_board = ['#','X','O','X','O','X','O','X','O','X']

# Print out the board
def display_board(board):
  '''
  print the board to terminal and display a nice board structure
  '''
  print('\n'*100) # clear screen
  print('     |     |    ')
  print(f'  {board[7]}  |  {board[8]}  |  {board[9]}  ')
  print('-----------------')
  print(f'  {board[4]}  |  {board[5]}  |  {board[6]}  ')
  print('-----------------')
  print(f'  {board[1]}  |  {board[2]}  |  {board[3]}  ')
  print('     |     |    ')

# Take player input
def player_input():
  '''
  Ask player to choose between x or o at the beginning of the game
  '''

  marker = ''

  #keep asking player 1 to choose x or o
  while marker != 'X' and marker != 'O':
    marker = input("Please choose X or O: ")
  player1 = marker
  # give player 2 the opposite marker
  if player1 == 'X':

    player2 = 'O'
  else:
    player2 = 'X'

  return (player1,player2)

# place player choice on the board
# this function takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
def place_marker(board,marker,position):
  '''
  put the player marker choice on the board
  '''
  
  if not full_board_check(board) and space_check(board,position):
    board[position] = marker
  else:
    print("The game is a tie")

# check who won
def win_check(board,mark):
  ''' 
  This function takes a board and a mark and then checks if that mark won
  '''
  #Check rows
  return ([mark]*3 == board[1:4] or [mark]*3 == board[4:7] or [mark]*3 == board[7:10] or
  #Check columns
  board[1:8:3] == [mark]*3 or board[2:9:3] == [mark]*3 or board[3:10:3] == [mark]*3 or
  #Check diagonals
  board[1:10:4] == [mark]*3 or board[3:8:2] == [mark]*3)

# check if a space on the board is free and available
def space_check(board, position):
  ''' 
  This function takes a board and a position and then checks if that position is free
  '''
  return board[position] == ' '
    


# check if a board is full, and return True if full else return False
def full_board_check(board):
  '''
  checks if the board is full which means its a tie game and return True if thats the case
  '''
  return ' ' not in board
    


def player_choice(board):
  '''
  Ask player for next move or position(1-9) and use the space_check() to check if space is free.
  '''
  position = int(input("Choose your next position: (1-9) "))
  if space_check(board,position=0) and position in range(1,9):
    return position
  else:
    print("the position you chose is not free")

# ask if players want to play again
def replay():
  '''
  Ask user if he want to play again
  '''
  return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

''' ---------------end of function defs-----------------'''

  

if __name__ == "__main__":

  print('Welcome to Tic Tac Toe!')
  # main algorithm
  while True:
  # Set the game up here
    # we have two players and we need to distinguish between them
    player1 = input("Do you want to be X or O?")
    print("Player 1 will go first") 
    if player1 == 'X':
      player2 = 'O'
    else:
      player2 = 'X'

    # ask if ready to play and display empty board
    answer = input("Are you ready to play? enter y/n.")
    if answer.lower() == 'y':
      # display the empty board and start the game
      game_on = True
    
      board = [' ']*10
      #test_board = ['#','X','O','X','O','X','O','X','O','X']
      display_board(board)
    else:
      game_on = False

    while game_on:
          #Player 1 Turn then  
          # ask player 1 for choice
          position = player_choice(board)
          place_marker(board,player1,position) 
          display_board(board)
          if win_check(board,player1):
            print("congragulation!, you won")
            game_on=False
          elif full_board_check(board):
            print("Tie game!")
            game_on = False
          else:
          #Player2's turn.
              # take in player input
            position = player_choice(board)
            place_marker(board,player2,position) 
            display_board(board)
              # check if the game is won
            if win_check(board,player2):
              print("congragulation!, you won")
              game_on =False
              #pass
      


    if not replay():
      break 
  