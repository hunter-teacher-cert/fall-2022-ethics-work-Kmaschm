class Student:
  def __init__(self, student_name, lottery_num, school_rankings,  priority, zoning, current_pref):
    self.student_name = student_name
    self.lottery_num = lottery_num
    self.school_rankings = school_rankings
    self.priority = priority
    self.zoning = zoning
    self.current_pref = current_pref
 
  def __str__(self):
    info = f"Student Name: {self.student_name}\nLottery Number: {self.lottery_num}\nRankings: "
    for i in range(len(self.school_rankings)):
      info += f"{i+1}: {self.school_rankings[i].school_name} "
    info += f"\nPriority: {self.priority}\n" 
    info += f"Zoned: {self.zoning}\n"
    info += f"Current Top Preference: {self.school_rankings[self.current_pref].school_name}" 
    return info


class School:
  def __init__(self, school_name, zoned, avail_seats, priority_seats, student_matches):
    self.school_name = school_name
    self.zoned = zoned
    self.priority_seats = priority_seats
    self.student_matches = student_matches

    
  def __str__(self):
    info = f"School Name: {self.school_name}\nZoned:{self.zoned}\nPriority Seats: {self.priority_seats}\nStudent Matches: "
    for student in self.student_matches:
        info += f"{student.student_name} "
    return info





def main():
  Red = School("Red", True, 3, 0, [])
  Yellow = School("Yellow", False, 3, 0, [])
  Blue = School("Blue", False, 3, 0, [])
  print(Red)

  # student_name, lottery_num, rankings, priority, zoning, curr_pref
  Ali = Student("Ali", 3, [Red, Blue, Yellow], True, False, 0)
  Bee = Student("Bee", 5, [Red, Yellow, Blue], True, False, 0)
  Cal = Student("Cal", 9, [Blue, Red, Yellow], False, True, 0)
  Dan = Student("Dan", 2, [Blue, Red, Yellow], True, False, 0)
  Eva = Student("Eva", 8, [Red, Yellow, Blue], False, False, 0)
  Flo = Student("Flo", 1, [Blue, Yellow, Red], False, True, 0)
  Gus = Student("Gus", 6, [Blue, Red, Yellow], True, True, 0)
  Hal = Student("Hal", 4, [Blue, Red, Yellow], False, False, 0)
  Isa = Student("Isa", 7, [Red, Yellow, Blue], False, False, 0)
  
  print(Ali)

if __name__=="__main__":
    main()





