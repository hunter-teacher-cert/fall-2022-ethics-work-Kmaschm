# binsearch.py
# Katherine (Kate) Maschmeyer
# CSCI 77800 Fall 2022
# collaborators: --
# consulted: --
# Python version of https://replit.com/@Kmaschm/cohort-3-summer-work-Kmaschm#programming/5/BinSearch.java
# Supported: Saranii


# binSearch(myList, target) -- searches an list for target 
# precondition: input list is all of same type and is sorted in ascending order
# postcondition: returns index of target, or returns -1 if target not found

def binSearch(myList, target):
  return binSearchRec(myList, target, 0, len(myList)-1)
 

def binSearchRec(myList, target, loPos, hiPos):
  NOT_FOUND = -1  # 
  mPos = int((loPos + hiPos) / 2);
  
  # Exit case: If lo & hi have crossed, target not present
  if hiPos < loPos:  # crossing happens when hi is less than lo
    print(f"Target, {target}, not found.")
    return NOT_FOUND
     
  # Target found
  if myList[mPos] == target:
    # print(f"Target, {target}, found at location {mPos})
    return mPos
    
  # Value at mid index higher than target
  elif myList[mPos] > target: 
    # we need to look at the lower half, so set hi to 1 below current middle
   # print(f"Target: {target}. Current location: {mPos} with value: {myList[mPos]} is too high.")
    hiPos = mPos - 1
    
  # Value at mid index lower than target
  elif myList[mPos] < target: # we need to look at the upper half, so set lo to 1 above middle location
   # print("Target: " + str(target) + ". At location " + str(mPos) + ". Value: " + str(myList[mPos]) + " is too low.")
    loPos = mPos + 1
    
  return binSearchRec(myList, target, loPos, hiPos)


######### TESTING #########
# Declare and initialize list of ints
iList = [2, 4, 6, 8, 6, 42]
print("List 1:", end=" ")
print(iList)
  
iList2 = [2, 4, 6, 8, 13, 42]
print("List 2:", end=" ")
print(iList2)

iList3 = []
for i in range(1000):
  iList3.insert(i,2*i)
# print("List 3:", end=" ")
# print(iList3)

print("***************")
print("Now testing binSearch: ");
print("List 2:", end=" ")
print(iList2)
print()
print(binSearch(iList2, 2)) # 0
print(binSearch(iList2, 4)) # 1
print(binSearch(iList2, 6)) # 2
print(binSearch(iList2, 8)) # 3
print(binSearch(iList2, 13)) # 4 
print(binSearch(iList2, 42)) # 5
print(binSearch(iList2, 43)) # -1 

print("***************")
print( "Now testing binSearch on iList3 (even integers 0 to 2*999)...")
print(binSearch(iList3, 4)) # 2
print(binSearch(iList3, 8)) # 3
print(binSearch(iList3, 5)) # -1

print(binSearch(iList3, 43)) # -1


iList4 = ["apple", "banana", "cherry"]
print("***************")
print("List 4:", end=" ")
print(iList4)
print( "Now testing binSearch on iList4...")

print(binSearch(iList4, "apple")) # 0
print(binSearch(iList4, "banana"))  # 1
print(binSearch(iList4, "cherry"))  # 2
print(binSearch(iList4, "donut"))  # -1