'''
  Project discreption
'''

# Print or Display board

# Get player position

# start the game 

def main():
  print('Welcome to Tic Tac Toe!')
# main algoritm
  #while True:
      # Set the game up here
      #pass

      #while game_on:
          #Player 1 Turn
           
          
          # Player2's turn.
              # take in player input
              # check if the game is won
              #pass

      #if not replay():
          #break 

  # we have two players
  # It indicates the beginning of the game
  player1 = input("Do you want to be X or O?")
  print("Player 1 will go first") 
  if player1.lower() == 'x':
    player2 = 'o'
  else:
    player2 = 'x'
    
  # ask if ready to play and display empty board
  answer = input("Are you ready to play? enter Yes or No.")
  if answer.lower() == 'yes':
    #display_board()
    pass

  # To clear the screen after displaying the board use:
  print('\n'*100)
  test_board = ['#','X','O','X','O','X','O','X','O','X']

  # Print out the board
  def display_board(board):
    for i in board:
      pass

  # Take player input
  def player_input():
    pass

  # place player choice on the board
  # this function takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
  def place_marker(board,marker,position):
    pass

  # check who won
  ''' this function takes a board and a mark and then checks if that mark won'''
  def win_check(board,mark):
    pass

  # check if a space on the board is free and available
  ''' this function takes a board and a position and then checks if that position is free'''
  def space_check(board, position):
    pass

  # check if a board is full, and return True if full else return False
  def full_board_check(board):
    pass

  # ask player for next move or position(1-9) and use the space_check() to check if it's free.
  def player_choice(board):
    pass

  # ask if players want to play again
  def replay():
    pass


if __name__ == "__main__":
  main()

