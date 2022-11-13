class Student:
  def __init__(self, name, lottery_num, school_rankings, zoning, priority, current_pref):
    self.name = name
    self.lottery_num = lottery_num
    self.school_rankings = school_rankings
    self.zoning = zoning
    self.priority = priority
    self.current_pref = current_pref
  def __str__(self):
    return f"{self.name} Lottery: {self.lottery_num}"



s1 = Student("Al", 5, ["Red", "Yellow", "Blue"], False, False, "Red")

print(s1)