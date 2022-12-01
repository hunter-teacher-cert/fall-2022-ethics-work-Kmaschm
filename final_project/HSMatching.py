# HSMatching.py
# CSCI 77800 Fall 2022
# Final Project: High School Matching Algorithm - Code Portion
# by Shana Elizabeth Henry and Katherine (Kate) Maschmeyer
# 
# Demonstrates the algorithm & set up displayed in videos from https://medium.com/algorithms-in-the-wild/decoding-the-nyc-school-admission-lottery-numbers-bae7148e337d
# Students are set up for processing in random order (not alphabetical), but results are the same 


import random
#import uuid  - chose to use student lottery numbers from the video for ease/clarity of demonstration

# Student - EXAMPLE:
#  Ali = Student("Ali", 3, (Red, Blue, Yellow), True, {Red: False, Yellow: False, Blue: False}, 0, None)
class Student:
  def __init__(self, student_name, lottery_num, school_rankings,  priority, zoning, next_pref, current_match):
    self.student_name = student_name  # string
    self.lottery_num = lottery_num # int
    self.school_rankings = school_rankings # tuple (won't change)
    self.priority = priority # boolean
    self.zoning = zoning # dictionary {School : boolean}
    self.next_pref = next_pref # int (will refer to rankings)
    self.current_match = current_match # School

  # Full print out of info
  def __str__(self):
    info = f"Student Name: {self.student_name}\nLottery Number: {self.lottery_num}\nRankings: "
    for i in range(len(self.school_rankings)):
      info += f"{i+1}: {self.school_rankings[i].school_name} "
    info += f"\nPriority: {self.priority}\nZoned:" 
    for school in self.zoning:
      info += f" {school.school_name}: {self.zoning[school] }"
    info += "\nNext Top Preference: "
    # once matching algorithm is done, next pref might be out of bounds, so skip if full
    if self.next_pref < len(self.school_rankings)-1:
      info += f"{self.school_rankings[self.next_pref].school_name}\n"
    else:
      info += "\n"
    if(self.current_match is not None):
      info += f"Current Match: {self.current_match.school_name}"
    else: 
      info += "Current Match: None"
    info +="\n"
    return info


    
# School - EXAMPLE: 
#  Red = School("🔴Red", True, 3, 0, {})
# uses color emoji in school name to help make printouts easier to read
class School:
  def __init__(self, school_name, zoned, avail_seats, priority_seats, student_matches):
    self.school_name = school_name  # string
    self.zoned = zoned # boolean
    self.avail_seats = avail_seats # int
    self.priority_seats = priority_seats # int (chose to use int number of seats instead of percentage for clarity)
    self.student_matches = student_matches # dictionary {Student: Student.lottery_num} - storing lottery number for ease later

  # Full print out of info
  def __str__(self):
    info = f"School Name: {self.school_name}\nZoned: {self.zoned}\nAvailable Seats: {self.avail_seats}\nPriority Seats: {self.priority_seats}\nStudent Matches: "
    for st in self.student_matches:
      info += f"{st.student_name} "
    if len(self.student_matches) == 0:
      info += "[None yet]"
    info += "\n"
    return info


    
# takes in a dictionary: student: lottery_num
# return the student with the lowest (worst) lottery number 
def lowest_lottery_num(st_dict): 
  return max(st_dict, key=st_dict.get)


# takes in a student and a zoned school that is already full with matches
# returns student that doesn't match/needs to be removed from matched list
def zoned_school_matching(stu, sch):
  zoned_st = {}
  unzoned_st = {}
  
  # separate matched students into zoned and unzoned
  for matched_st in sch.student_matches:
    if matched_st.zoning.get(sch):
      zoned_st.update({matched_st: matched_st.lottery_num})
    else:
      unzoned_st.update({matched_st: matched_st.lottery_num})
  
  # if student is zoned for the school,  
  if stu.zoning.get(sch):
    print(f"{stu.student_name} is zoned for {sch.school_name}")

    # check if there are unzoned students matched at zoned school
    if len(unzoned_st) > 0: 
      # want to remove *unzoned* student with lowest lottery num
      print("Going to unseat unzoned student with lowest lottery number...")
      return lowest_lottery_num(unzoned_st) 
    else: # no zoned spots taken by unzoned students
      # get zoned student with lowest lottery num (could be current student)
      zoned_st.update({stu: stu.lottery_num})
      return lowest_lottery_num(zoned_st) 
  
  else: # student NOT zoned for school
    # get unzoned student with lowest lottery num (could be current student)
    unzoned_st.update({stu: stu.lottery_num})
    return lowest_lottery_num(unzoned_st)   


  
# takes in a student and a school with priority set asides that is already full with matches
# returns the student that will either not match or will be removed from matched list
def priority_school_matching(student, school):
  pr_seats = school.priority_seats
  pr_st = {}
  nonpr_st = {}

  # separate matched students into priority and not priority
  for st in school.student_matches:
    if st.priority:
      pr_st.update({st: st.lottery_num})
    else:
      nonpr_st.update({st: st.lottery_num})

  if student.priority:
    print(f"{student.student_name} has priority and {school.school_name} has {pr_seats} priority seats.")
    if len(pr_st) < pr_seats: # priority seat open (currently occupied by nonpriority student)
      # student has priority & not all seats are full, so grab nonpriority student with lowest lottery number
      print("Going to unseat nonpriority student with lowest lottery number...")
      return lowest_lottery_num(nonpr_st)
    else: # priority seats full
      # check priority students & current student - lowest lottery number will not match (or be removed) 
      pr_st.update({student: student.lottery_num}) 
      return lowest_lottery_num(pr_st) 
 
  else: # student does not have priority
    nonpr_st.update({student: student.lottery_num})
    return lowest_lottery_num(nonpr_st) 
  
    
      
# sets match for student and school
def set_match(student, school):
  print(f">> Temp Matching: {student.student_name} and {school.school_name}\n")
  student.current_match = school
  student.next_pref += 1
  school.student_matches.update({student: student.lottery_num})
  school.avail_seats -= 1
  
     


def main():

  # Schools:
  # school_name, zoned, avail_seats, priority_seats, student_matches
  Red = School("🔴Red", True, 3, 0, {})
  Blue = School("🔵Blue", False, 3, 2, {})
  Yellow = School("🟡Yellow", False, 3, 1, {})

  print("**************SCHOOL INFORMATION**************\n")
  print("*****RED*****")
  print(Red)
  print("*****BLUE*****")
  print(Blue)
  print("*****YELLOW*****")
  print(Yellow)  


  # Students:
  # student_name, lottery_num, rankings, priority, zoning, next_pref, current_match
  Ali = Student("Ali", 3, (Red, Blue, Yellow), True, {Red: False, Yellow: False, Blue: False}, 0, None)
  Bee = Student("Bee", 5, (Red, Blue, Yellow), True, {Red: False, Yellow: False, Blue: False}, 0, None)
  Cal = Student("Cal", 9, (Blue, Red, Yellow), False, {Red: True, Yellow: False, Blue: False}, 0, None)
  Dan = Student("Dan", 2, (Blue, Red, Yellow), True, {Red: False, Yellow: False, Blue: False}, 0, None)
  Eva = Student("Eva", 8, (Red, Yellow, Blue), False, {Red: False, Yellow: False, Blue: False}, 0, None)
  Flo = Student("Flo", 1, (Blue, Yellow, Red), False, {Red: True, Yellow: False, Blue: False}, 0, None)
  Gus = Student("Gus", 6, (Blue, Red, Yellow), True, {Red: True, Yellow: False, Blue: False}, 0, None)
  Hal = Student("Hal", 4, (Blue, Red, Yellow), False, {Red: False, Yellow: False, Blue: False}, 0, None)
  Isa = Student("Isa", 7, (Red, Yellow, Blue), False, {Red: False, Yellow: False, Blue: False}, 0, None)

  # list of all students before matching
  unmatched_students = [Ali, Bee, Cal, Dan, Eva, Flo, Gus, Hal, Isa]

  print("**************STUDENTS**************")
  for st in unmatched_students:
    print(f"*****{st.student_name}*****")
    print(st)
  print("")

  # testing to see if order matters
  print("Randomizing order of students...")
  random.shuffle(unmatched_students)
  
  print(">>>>>>> Starting Matching Algorithm...\n")

  # setting up algorithm
  student = unmatched_students[0]
  school = student.school_rankings[student.next_pref]

  # match all students
  while len(unmatched_students) > 0:
    
    print(f"Attempting match for {student.student_name} at {school.school_name}...")
    
    if school.avail_seats > 0:  # seats available!
      print(f"Seat available at {school.school_name}")
      set_match(student, school) # match student & school

      # update unmatched students
      if student in unmatched_students:
        unmatched_students.remove(student)

      # set up next student (if there is one)
      if len(unmatched_students) > 0:
        student = unmatched_students[0]
        school = student.school_rankings[student.next_pref]
    
    else: # no free seats
      print(f"No open seats at {school.school_name}. Rearranging may happen.")
      # Zoning...
      if school.zoned:
        # look at zoned matches & find either student doesn't match (returns our student) or someone needs to be unseated because student was the better match (returns the student to be unseated)
        z_rem_st = zoned_school_matching(student, school)
      
        # if student will be unseated 
        if z_rem_st != student:
          print(f"<< Unmatching {z_rem_st.student_name} from {school.school_name} to seat {student.student_name}")
          # unmatch z_rem_st
          school.student_matches.pop(z_rem_st)
          school.avail_seats += 1
          # add removed student back to unmatched list
          if z_rem_st not in unmatched_students:
            unmatched_students.insert(0, z_rem_st)
          # match student
          set_match(student, school)
          if student in unmatched_students:
            unmatched_students.remove(student)
          # now try to match removed student with the next school on their list
          student = z_rem_st
          school = z_rem_st.school_rankings[z_rem_st.next_pref]
        
        else: # not a match
          print(f"{student.student_name} did not match at {school.school_name}")
          # keep going with current student
          student.next_pref += 1
          school = student.school_rankings[student.next_pref]

      # Priority set asides... (assuming zoning & priority are mutually exclusive for this code)
      elif school.priority_seats > 0:
         # look at priority matches & find either student doesn't match (returns our student) or someone needs to be unseated because student was the better match (returns the student to be unseated)
        p_rem_st = priority_school_matching(student, school)

        # if a student will be unseated 
        if p_rem_st != student:
          print(f"<< Unmatching {p_rem_st.student_name} from {school.school_name} to seat {student.student_name}")
          # unmatch p_rem_st
          school.student_matches.pop(p_rem_st)
          school.avail_seats += 1
          # add removed student back to unmatched list
          if p_rem_st not in unmatched_students:
            unmatched_students.insert(0, p_rem_st)
          # match student
          set_match(student, school)
          if student in unmatched_students:
            unmatched_students.remove(student)
          # now try to match removed student with the next school on their list
          student = p_rem_st
          school = p_rem_st.school_rankings[p_rem_st.next_pref]
        
        else: # not a match
          print(f"{student.student_name} did not match at {school.school_name}")
          # keep going with current student
          student.next_pref += 1
          school = student.school_rankings[student.next_pref]
        
      else:
        # non-zoned, non-priority, look only at lottery num
        # find either student doesn't match (returns our student) or someone needs to be unseated because student was the better match (returns the student to be unseated)
        rem_stud = lowest_lottery_num(school.student_matches)
       
        # if a student will be unseated 
        if rem_stud != student:
          # unmatch rem_st
          school.student_matches.pop(rem_stud)
          school.avail_seats += 1
          # add removed student back to unmatched list
          if rem_stud not in unmatched_students:
            unmatched_students.insert(0, rem_stud)
          # match student
          set_match(student, school)
          if student in unmatched_students:
            unmatched_students.remove(student)
          # now try to match removed student with the next school on their list
          student = rem_stud,       
          school = rem_stud.school_rankings[rem_stud.next_pref]
        else: # student didn't match
           # keep going with current student
          student.next_pref += 1
          school = student.school_rankings[student.next_pref]
 # end of whileloall students now matched
  
  
  print("\nAll students matched!\n")
  print("\n**************Matching Algorithm Complete!**************\n")

  # student list just for printing later 
  st_list = [Ali, Bee, Cal, Dan, Eva, Flo, Gus, Hal, Isa]
  
  print("*******STUDENTS after Matching*******")
  for st in st_list:
    print(f"{st.student_name} matched at {st.current_match.school_name}, which was their #{st.next_pref} choice")
  print("\n")

  print("*******SCHOOLS after Matching*******")
  print("*****RED after Matching*****")
  print(Red)
  print("*****BLUE after Matching*****")
  print(Blue)
  print("*****YELLOW after Matching*****")
  print(Yellow)  

  
  
 


if __name__=="__main__":
    main()





