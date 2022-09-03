# gol.py
# Katherine (Kate) Maschmeyer
# CSCI 77800 Fall 2022
# collaborators: None on Python version
# On Java version:
# * Yeidy Levels - YLevels <-- driving
# * Usman Ahmed - usman0527 <-- designated slacker
# * Rachel Kaufman - RACHELKAUFMAN <-- collab
# * Kate Maschmeyer - kmaschm <-- collab, have made additional comments/formatting changes
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

import random
# using random to seed Game of Life

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
def countNeighbours(board, r, c):
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
              if board[i][j] == ALIVE: 
                counter = counter + 1
     
  return counter


# precond: given a board and a cell
# postcond: return next generation cell state based on CGOL rules
# (alive 'X', dead ' ')

def getNextGenCell(board, r, c):

  currentStatus = board[r][c]
  aliveNeighbours = countNeighbours(board, r, c);

  if currentStatus == DEAD and aliveNeighbours == 3:
    return ALIVE  # birth
  
  if currentStatus == ALIVE and (aliveNeighbours == 2 or aliveNeighbours == 3):
    return ALIVE # survivors
    
  return DEAD # COD: overcrowding (> 3) or isolation (< 2)
  

# generate and return a new board representing next generation
def generateNextBoard(board):
  rows = len(board)
  cols = len(board[0])
  nextBoard = createNewBoard(rows, cols)

  for i in range(rows):
    for j in range(cols):
      setCell (nextBoard, i, j, getNextGenCell(board, i, j)); 
      
    
  return nextBoard
  
  

# ##############TESTING#############
board = createNewBoard(25,25);

# # puts living cells into top left corner of board and prints it out
# setCell(board, 0, 0, 'X')
# setCell(board, 0, 1, 'X')
# setCell(board, 1, 0, 'X')
# setCell(board, 2, 2, 'X')
# setCell(board, 3, 3, 'X')
# setCell(board, 2, 3, 'X')

# print("Generation 0")
# printBoard(board)
# print("--------------------------\n\n")
# print("Row 0, Col 0 has " + str(countNeighbours(board, 0, 0)) + " neighbours") # 2
# print("Row 0, Col 1 has " + str(countNeighbours(board, 0, 1)) + " neighbours") # 2
# print("Row 0, Col 1 has " + str(countNeighbours(board, 1, 1)) + " neighbours") # 4
# print("Row 1, Col 2 has " +str(countNeighbours(board, 1, 2)) + " neighbours") # 3
# print("Row 3, Col 1 has " + str(countNeighbours(board, 3, 1)) + " neighbours") # 1
# print("Row 5, Col 5 has " + str(countNeighbours(board, 5, 5)) + " neighbours") # 0
# print("Row 0, Col 0 will become " + getNextGenCell(board, 0, 0))  # X (survived)
# print("Row 1, Col 1 will become " + getNextGenCell(board, 1, 1)) # returned a space for DEAD (overcrowded)
# print("Row 1, Col 2 will become " + getNextGenCell(board, 1, 2)) # X (birth)
# print("Row 5, Col 5 will become " + getNextGenCell(board, 5, 5)) # returned a space for DEAD (dtayed dead)



for i in range(len(board)):
  for j in range(len(board[0])):
    if random.random() > 0.9: # expect 10% of board alive 
      setCell (board, i, j, ALIVE)


print("Generation 0")
printBoard(board)
print("--------------------------\n\n")

for i in range(10):
  board = generateNextBoard (board);
  print("Generation " + str(i))
  printBoard(board)
  print("--------------------------\n\n")

