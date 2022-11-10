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
  * Zoned (boolean)
  * Priority (boolean)
  * Current match (school object)

School object:
  * Name (string)
  * Zoned (boolean)
  * Number of seats (int)
  * % of priority seats (float?)

## Algorithm

Set up students, schools

Create mutable list of unmatched students (alphabetical order?)

Functions:
  student.match(school) - set matches in each student & school object, 
  student.lookForMatch()






while unmatched_students.len > 0:
  currStudent = unmatched_students[0]

  
  currSchool = currStudent's current top school
  





    if currSchool has a spot:
      match
    else 
      if currSchool is zoned:
        if currStudent is zoned for currSchool
          
        else:
          if currStudent has priority:
            if currSchool has priority spots
          else:
            look at non-zoned students & currStudent's lottery numbers
            if currStudent has lowest lottery number
              set currStudent's current top school to next one on list, then restart matching
      else 
      
    
  












## HS matching algorithm
Need:
* For each school: Name, current match, & ranking of studemts
* For each student: Name, current match, & ranking of schools

Seems to be variation of Gale–Shapley algorithm (dealing with stable marriage problem)

However:
* there are ____ HS schools in NYC
* students only rank their top 12 schools 
 
How will we deal with # of schools? 

### NOTES
* working to maximize overall student satisfaction

* 


### Matching algorithm alone:
* Assume N schools, N students
* Need to store:
  * for each school: current match (default == free), whether it is zoned, how may set asides there are 
  * for each student: current match (default == free), ranking of schools
  * number of schools that don't have a match (initial = all)

#### Flow:
Set all schools', students' matches to free

```
while free_students.len() > 0:
  T = free_students[0]
  if T.currentChoice has space -> match
  else:
    check priority of school:
      if no priority
        check set aside
          if no set aside
            check lottery number
      else -> school has priority
      
```



OLD version of matching, before clarification
```
while free_schools.len() > 0:
  S = free_schools[0]
  T = 1st student on S's list (that S hasn't tried to match with)
  if T.match != free:
    S_prime = T.get_match()
    if T.rank(S) > T.rank(S_prime)
      S_prime.set_match(free)
      T.set_match(S)
      S.set_match(T)
  else:
    T.set_match(S)
    S.set_match(T)
```