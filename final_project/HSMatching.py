# HSMatching.py
# CSCI 77800 Fall 2022
# Final Project: High School Matching Algorithm - Code Portion
# by Shana Elizabeth Henry and Katherine (Kate) Maschmeyer
# 
# Demonstrates the algorithm & set up displayed in videos from https://medium.com/algorithms-in-the-wild/decoding-the-nyc-school-admission-lottery-numbers-bae7148e337d

#import uuid

# EXAMPLE:
#  Ali = Student("Ali", 3, (Red, Blue, Yellow), True, {Red: False, Yellow: False, Blue: False}, 0, None)
class Student:
  def __init__(self, student_name, lottery_num, school_rankings,  priority, zoning, current_pref, current_match):
    self.student_name = student_name  # string
    self.lottery_num = lottery_num # int
    self.school_rankings = school_rankings # tuple
    self.priority = priority # boolean
    self.zoning = zoning # dictionary (School : boolean)
    self.current_pref = current_pref # School
    self.current_match = current_match # School
 
  def __str__(self):
    info = f"Student Name: {self.student_name}\nLottery Number: {self.lottery_num}\nRankings: "
    for i in range(len(self.school_rankings)):
      info += f"{i+1}: {self.school_rankings[i].school_name} "
    info += f"\nPriority: {self.priority}\nZoned:" 
    for school in self.zoning:
      info += f" {school.school_name}: {self.zoning[school] }"
    info += f"\nCurrent Top Preference: {self.school_rankings[self.current_pref].school_name}\n"
    if(self.current_match is not None):
      info += f"Current Match: {self.current_match.school_name}"
    else: 
      info += "Current Match: None"
    return info

  def is_zoned_for(school):
    return self.zoning[school]


    
# EXAMPLE: 
#  Red = School("Red", True, 3, 0, [])
class School:
  def __init__(self, school_name, zoned, avail_seats, priority_seats, student_matches):
    self.school_name = school_name  # string
    self.zoned = zoned # boolean
    self.avail_seats = avail_seats # int
    self.priority_seats = priority_seats # int
    self.student_matches = student_matches # list

    
  def __str__(self):
    info = f"School Name: {self.school_name}\nZoned: {self.zoned}\nAvailable Seats: {self.avail_seats}\nPriority Seats: {self.priority_seats}\nStudent Matches: "
    for student in self.student_matches:
        info += f"{student.student_name} "
    return info

# takes in a dictionary: student: lottery_num
# return the student with the lowest lottery number
def lowest_lottery_num(st_dict):
  return max(st_dict, key=st_dict.get)
    
# takes in a student and a zoned school that has matches
# returns a student with the lowest lottery number that has the same zoning status as st
def zoned_school_matching(st, sch):
  unzoned_st = {}
  zoned_st = {}

  # separate matched students into zoned and unzoned
  for st in school.student_matches:
    if st.zoning.get(school):
      zoned_st.update({st: st.lottery_num})
    else:
      unzoned_st.update({st: st.lottery_num})
  # if student is zoned for the school,  
  if student.is_zoned_for(school):
    zoned_st.update({student: student.lottery_num})
    return lowest_lottery_num(zoned_st) 
  else: 
    unzoned_st.update({student: student.lottery_num})
    return lowest_lottery_num(unzoned_st)   
    
       
          
      # elif student.priority:
      #   # student has priority
      # else:  # student is not zoned or have priority
        
          
          
      
      

def set_match(student, school):
  print(f"*****Matching: {student.student_name} and {school.school_name} *****")
  student.current_match = school
  student.current_pref += 1
  #school.student_matches.update({student: student.lottery_num})
  school.student_matches.append(student)
  school.avail_seats -= 1
  
     


def main():
  Red = School("Red", True, 3, 0, [])
  Yellow = School("Yellow", False, 3, 0, [])
  Blue = School("Blue", False, 3, 0, [])
  # print("**********School***********")
  # print(Red)

  # student_name, lottery_num, rankings, priority, zoning, curr_pref
  Ali = Student("Ali", 3, (Red, Blue, Yellow), True, {Red: False, Yellow: False, Blue: False}, 0, None)
  Bee = Student("Bee", 5, (Red, Yellow, Blue), True, {Red: False, Yellow: False, Blue: False}, 0, None)
  Cal = Student("Cal", 9, (Blue, Red, Yellow), False, {Red: True, Yellow: False, Blue: False}, 0, None)
  Dan = Student("Dan", 2, (Blue, Red, Yellow), True, {Red: False, Yellow: False, Blue: False}, 0, None)
  Eva = Student("Eva", 8, (Red, Yellow, Blue), False, {Red: False, Yellow: False, Blue: False}, 0, None)
  Flo = Student("Flo", 1, (Blue, Yellow, Red), False, {Red: True, Yellow: False, Blue: False}, 0, None)
  Gus = Student("Gus", 6, (Blue, Red, Yellow), True, {Red: True, Yellow: False, Blue: False}, 0, None)
  Hal = Student("Hal", 4, (Blue, Red, Yellow), False, {Red: False, Yellow: False, Blue: False}, 0, None)
  Isa = Student("Isa", 7, (Red, Yellow, Blue), False, {Red: False, Yellow: False, Blue: False}, 0, None)

  # while unmatched_students > 0:
  #   student = unmatched_students[0]
  #   school = student.current_pref
  #   if school.avail_seats > 0:
  #     set_match(student, school)
  #     unmatched_students.remove(student)
  #   else: # no free seats
  #     if school.zoned:
  #        st = zoned_school_matching(st, school)
  #        if st equals student:
  #          # keep going
  #        else: 
  #          set_match(student, school)
  #          unmatched_students.remove(student)
  #          # now match st
  #     elif school.priority_seats > 0:
  #       # priority vs non-priority seat
  #     else: # School is not zoned and has no priority seats

  
  # print("*******Student**********")
  # print(Ali)

  # unmatched_students = [Ali, Bee, Cal, Dan, Eva, Flo, Gus, Hal, Isa]

  # # print("*******Matching: Ali & Red*********")
  # set_match(Ali, Red)
  # set_match(Bee, Red)

  # print("*******Student**********")
  # print(Ali)
  # print("*******Student**********")
  # print(Bee)
  # print("**********School***********")
  # print(Red)

  stu = {Ali: 3, Bee: 5, Cal: 9, Dan: 2}
  print(lowest_lottery_num(stu))


if __name__=="__main__":
    main()





