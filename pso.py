import math
import random
import particle

class Population:
  population = []
  leader = []
  def __init__(self, member_count):
    for i in range(member_count):
      temp_particle = particle.Particle()
      self.population.append(temp_particle)
    self.leader = self.identify_leader()

  def display(self):
    for member in self.population:
      member.display()
      print '-' * 80

  def display_leader(self):
    self.leader.display()

  def identify_leader(self):
    leader = []
    for member in self.population:
      if (leader == []):
        leader = member
      if (member.best_fit < leader.best_fit):
        leader = member
    return leader

  def population_update(self, iterations):
    for i in range(iterations):
      self.leader = self.identify_leader()
      for member in self.population:
        member.update(self.leader)

test = Population(100)
test.display()
print '*' * 80
test.display_leader()
print '-' * 80
test.population_update(10)
test.display()
print '*' * 80
test.display_leader()
