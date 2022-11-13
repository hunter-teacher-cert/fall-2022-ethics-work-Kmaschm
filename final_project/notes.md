# HS Matching Algorithm Project - CSCI 77800 Fall 2022
## by Shana Elizabeth Henry and Katherine (Kate) Maschmeyer

## Possible resources:
* https://www.youtube.com/watch?v=7n-bvvD6ZEc
* https://en.wikipedia.org/wiki/Gale%E2%80%93Shapley_algorithm
* https://medium.com/algorithms-in-the-wild/gaining-insights-from-the-nyc-school-admission-lottery-numbers-42dd9a98b115
* https://medium.com/algorithms-in-the-wild/decoding-the-nyc-school-admission-lottery-numbers-bae7148e337d

## HS Matching Notes
* Each student has:
  * Name
  * Generate random lottery number (using UUID)
    ```
    import uuid
    for i in range(1,10): print(uuid.uuid4())
    ```
  * Ranking of schools
  * Whether student is zoned (& for which school)
  * Whether student is in set-aside category
  * Current top preferred school 
* Each school has:
  * Name
  * Zoned or not 
  * List of student spots (initially empty, hard limit on number of spots)
  * % of seats that are set-aside (might store as number of seats that are set-aside)
  * 
* There are many more HS than students. For our simulation, we'll simulate what happened in video (equal number of students and schools)
* Algorithm works to maximize overall student satisfaction
* stable matching at end of algorithm: no student & school match that would rather be matched with each other than the pair they are match with
* students propose matches, not schools
* Take into account: lottery number, priority, zoning
* Assuming for sake of ease that priority and zoning are mutually exclusive in our algorithm

## Data structures

Student object:
  * Name (string)
  * Random lottery number (for now: int)
  * Ranking of schools (array of strings?)
  * Zoned for school (name: boolean)
  * Priority (boolean)
  * Current match (school object)

School object:
  * Name (string)
  * Zoned (boolean)
  * Number of available seats (int)
  * % of priority seats (float?)
  * Seats (array of students)

## Algorithm

Set up students, schools

Create mutable list of unmatched students (alphabetical order?)

Functions:
  student.match(school) - set matches in each student & school object, 
  student.lookForMatch() 
  school.hasPrioritySeating()
  school.lowestLotteryNumber()
  school.getMatchesWithZone()
  school.gebtMatchesWithPriority()
  




```
while unmatchedStudents.len > 0:
  currStudent = unmatchedStudents[0]

  currSchool = currStudent's current top school
  
  if currSchool has a spot:
    currStudent.match(currSchool)
    unmatchedStudents.remove(currentStudent) 
  else:  // no spots free
      if currSchool.isZoned():
        if currStudent is zoned for currSchool:
            if unzoned students already matched with school:
              remove unzoned student with lowest lottery number
              currStudent.match(currSchool)
              continue with removed student
            else: // all spots have zoned students
              find which student has lowest lottery number
              if currStudent has lowest:
                set currStudent's top school to next on list, try to match
              else:  // student has higher
                remove lowest lottery student
                currStudent.match(currSchool)
                continue with removed student  
              
        else: // student not zoned for school (but school is)
        
           
      else: // school not zoned
        if currSchool has priority spots:
            if currStudent has priority:
              if priority spots filled with priority students:
                check lottery number ...
              else:
                check students without priority - which has lowest lottery number... 
            else: // student does not have priority
            find which student has lowest lottery number
              if currStudent has lowest:
                set currStudent's top school to next on list, try to match
              else: 
                remove lowest lottery student
                currStudent.match(currSchool)
                continue with removed student

        else:  // school not zoned, no priority
          check for lowest lottery number ... 

```



