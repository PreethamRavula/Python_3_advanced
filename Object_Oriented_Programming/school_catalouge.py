class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numberOfStudents(self):
    return self.numberOfStudents

  def set_numberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

# Testing the class:
school_1 = School('Vasavi Nikethan', 'Middle', 150)
print(school_1.get_name())
print(school_1.get_numberOfStudents())
school_1.set_numberOfStudents(200)
print(school_1.get_numberOfStudents())
print(school_1)

class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    self.pickupPolicy = pickupPolicy

  def get_pickupPolicy(self):
    return f"Pick up is after {self.pickupPolicy}pm"

  def __repr__(self):
    primary_repr = super().__repr__()
    return primary_repr + f" Pickup time is after {self.pickupPolicy}pm"


# Testing the primary school object:
primary_school_1 = PrimarySchool('Toddlers Primary School', 50, 2)
print(primary_school_1.get_level())
print(primary_school_1.get_pickupPolicy())
print(primary_school_1.get_name())
print(primary_school_1)

class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams

  def get_sportsTeams(self):
    return self.sportsTeams

  def __repr__(self):
    high_rep = super().__repr__()
    return high_rep + f" and contains {self.sportsTeams} sports teams"

# Testing the high School class:
high_school_1 = HighSchool('Desmond High School', 300, ['Basketball', 'Football', 'Badminton'] )
print(high_school_1.get_sportsTeams())
print(high_school_1.get_name())
print(high_school_1.get_level())
print(high_school_1)


  
