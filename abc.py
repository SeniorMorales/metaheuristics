import math
import random
import optimization
import bee

class Hive:
  population = []
  leader = []
  def __init__(self, member_count):
    for i in range(member_count):
      temp = bee.Bee()
      self.population.append(temp)

    self.leader = self.identify_leader()
    for member in self.population:
      member.probability = self.probability(member)

  def display(self):
    for member in self.population:
      member.display()
      print '-' * 80

  def display_leader(self):
    self.leader.display()

  def identify_leader(self):
    leader = []
    for member in self.population:
      if leader == []:
        leader = member
      if member.fit > leader.fit:
        leader = member
    self.leader = leader
    return leader

  def probability(self, member):
    leader_fit = self.leader.fit
    return 0.9 * (member.fit / leader_fit) + 0.1

  def employed(self):
    for i in range(len(self.population)):
      index = random.randrange(0, len(self.population))
      member = self.population[index]
      neighbor = member.neighbor()

      # Put something to keep the neighbor within the bounds here.

      if neighbor.fit > member.fit:
        self.population[index] = neighbor

  def onlooker(self):
    t = 0
    while t < len(self.population):
      member = self.population[t]
      if random.random() < self.probability(member):
        neighbor = member.neighbor()

        # Put something here to keep the neighor within the bounds here.

        if neighbor.fit > member.fit:
          self.population[t] = neighbor
      t += 1

  def scout(self, new_count=10):
    for i in range(new_count):
      temp = bee.Bee()
      self.population.append(temp)

  def population_update(self):
    self.scout()
    self.employed()
    self.onlooker()
    self.identify_leader()

one = Hive(10)
one.display_leader()
print '*' * 80
for i in range(100):
  one.population_update()
one.display_leader()
