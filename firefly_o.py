import math
import random
import firefly

class Population:
  population = []
  leader = []
  def __init__(self, member_count):
    for i in range(member_count):
      temp_firefly = firefly.Firefly()
      self.population.append(temp_firefly)
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
      if (member.best_intensity < leader.best_intensity):
        leader = member
    return leader

  def population_update(self, iterations):
    for i in range(iterations):
      leader = self.identify_leader()
      for firefly in self.population:
        firefly.update(leader)

test = Population(25)
test.display_leader()
test.population_update(100)
print '*' * 80
test.display_leader()

