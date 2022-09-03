# gol.py
# Katherine (Kate) Maschmeyer
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: https://www.w3schools.com/python/default.asp

# Python version of: https://replit.com/@Kmaschm/cohort-3-summer-work-Kmaschm#programming/3/Cgol.java


# MAY BE INTERESTED IN ANIMATION IN FUTURE - POSSIBLE TODO?
   

#   The Rules of Life:

#    Survivals:
#    * A living cell with 2 or 3 living neighbours will survive for the next generation.

#    Deaths:
#    * Each cell with >3 neighbours will die from overpopulation.
#    * Every cell with <2 neighbours will die from isolation.

#    Births:
#    * Each dead cell adjacent to exactly 3 living neighbours is a birth cell. It will come alive next generation.

#    NOTA BENE:  All births and deaths occur simultaneously. Together, they constitute a single generation.

# Constants for ease of reading
ALIVE = "X"
DEAD = " "


# Create the board
def createNewBoard(rows, cols):
  board = [[DEAD for i in range(cols)] for j in range(rows)]
  return board

# Nicely print the board
def printBoard(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == DEAD:
        # print a . if dead, followed by a space
        print(".", end=" ") 
      else:
        # if not dead, print the character followed by a space
        print(board[i][j], end=" ")
    print()

# Set the value of a specified cell 
def setCell(board, r, c, val):
  board[r][c] = val

# Count the living neighbors of a cell 
def countNeighbors(board, r, c):
  counter = 0
  rows = len(board)
  cols = len(board[0])

  # r = row, c = column
  # local rows: r-1, r, r+1
  # local cols: c-1, c, c+1
 
  # r-1, c-1 | r-1, c | r-1, c+1
  # r, c-1   | r, c   | r,  c+1
  # r+1, c-1 | r+1, c | r+1, c+1
      
  # go through local rows (r-1, r, and r+1) 
  for i in range(r-1, r+2): 
      # make sure row value is valid
      if i >= 0 and i < rows:
        # go through local cols (c-1, c, and c+1) 
        for j in range(c-1, c+2): 
          # make sure col value is valid
          if j >= 0 and j < cols:
            # check that we're not in the center
            if not(i == r and j == c):
              # if the neighbor is alive, count them!
              if board[i][j] == ALIVE 
                counter++;
     
  return counter


printBoard(createNewBoard(5, 5))

