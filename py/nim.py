# nim.py
# Katherine (Kate) Maschmeyer
# CSCI 77800 Fall 2022
# collaborators: None on Python version, but original Java version:
# kmaschm - Maschmeyer, Kate 
# AliseBraick, Alise Braick
# usman0527 - Usman Ahmed
# WayneTobias, Wayne
# Jihae Park, jpark-29
#jmtheo8 - Jerusha Theobald 
#
# consulted: (None) 
# Supported: Shana & Saranii


# Python version of: https://replit.com/@Kmaschm/cohort-3-summer-work-Kmaschm#programming/1/Nim.java
#
## CURRENT STATUS
# Nim runs without errors
# Nim's algorithm:
# * game ends when number of stones <= 0.
# * Human player always goes 1st 
#  ** Program will check that human is selecting only 1-3 stones (continuously warn and prompt if not) 
#  ** Program does NOT YET double check that there are sufficient stones)
# * AI will choose (4 - # of stones human chose) each time
# ** this will result in AI winning each time
# * after each turn, program checks if there are 0 stones left.  If yes, program outputs  the player who just went has won.
# 
# 
# POSSIBLE CHANGES TO MAKE:
# * let human player choose who will go first (or some randomization of who goes first)
# * AI chooses randomly (with safeguards for sufficient stones, etc.)







# starting with a bag of 12 stones
stones = 12

 # how many stones a player has chosen to take
stonesTaken = 0


print("*****************************")
print("Welcome to Nim!")
print("*****************************")

while stones > 0:
  print(f"*****Your turn!*****\nThere are {stones} stones in our bag.\nHow many would you like to choose? 1, 2, or 3.")
  stonesTaken = input()
  stonesTaken = int(stonesTaken)
  
  # when the user tries to take less than 1 or greater than 3, this will happen
  # keep prompting for correct answer if needed
  while stonesTaken > 3 or stonesTaken < 1:
    print("Ooops, that's not a valid number of stones to take!  Try again.")
    stonesTaken = input()
    stonesTaken = int(stonesTaken)
          
  print(f"You chose to take {stonesTaken} stones.")
      
  stones -= stonesTaken
  
  if stones == 0:
    print("YOU WIN!")
    # break
  else:
    print(f"There are now {stones} stones in the bag.\n *****AI's turn*****") 
          
          
  # AI's turn - GOAL: WIN!
  stonesTaken = 4 - stonesTaken;
  print(f"The computer chose to take {stonesTaken} stones.")
  
  stones -= stonesTaken;
          
  if stones == 0:
    print("AI WINS! SORRY. :(((");
    break
  else:
    print(f"There are now {stones} stones in the bag.")
        

        


   
