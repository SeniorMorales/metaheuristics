import math
import random
import optimization

class Firefly:
  def __init__(self):
    self.position = [random.randrange(0, 100), random.randrange(0, 100)]
    self.best_pos = [self.position[0], self.position[1]]
    self.gradient = [random.randrange(-3, 3), random.randrange(-3, 3)]
    self.intensity = self.fitness_function(self.position)
    self.best_intensity = self.fitness_function(self.best_pos)
    self.absorption = 0.1

  def fitness_function(self, position):
    return optimization.de_jong(position[0], position[1])

  def display(self):
    print("Current positon: x = " + str(self.position[0]) + ", y = " +
      str(self.position[1]))
    print("Best position:   x = " + str(self.best_pos[0]) + ", y = " +
      str(self.best_pos[1]))
    print("Current intensity:   " + str(self.intensity))
    print("Best intensity:      " + str(self.best_intensity))
    print("Absorption:          " + str(self.absorption))
    print("Gradient         x = " + str(self.gradient[0]) + ", y = " +
      str(self.gradient[1]))

  def distance(self, partner):
    x_dist = partner.position[0] - self.position[0]
    y_dist = partner.position[1] - self.position[1]
    distance = abs(math.sqrt(pow(x_dist, 2) + pow(y_dist, 2)))
    return distance

  def attraction(self, partner, tweak=0.5):
    return math.exp(-partner.absorption * self.distance(partner))

  def update(self, partner, tweak=0.5):
    attract = self.attraction(partner)
    rand_p = random.random()
    rand_g = random.random()

    self.position[0] = self.position[0] + self.gradient[0]
    self.position[1] = self.position[1] + self.gradient[1]

    self.gradient[0] = (tweak * self.gradient[0] + attract * rand_p *
      (self.best_pos[0] - self.position[0]) + attract * rand_g * 
      (partner.position[0] - self.position[0]))
    self.gradient[1] = (tweak * self.gradient[1] + attract * rand_p *
      (self.best_pos[1] - self.position[1]) + attract * rand_g *
      (partner.position[1] - self.position[1]))

    self.intensity = self.fitness_function(self.position)
    if (self.intensity < self.best_intensity):
      self.best_intensity = self.intensity
      self.best_pos = self.position

"""
one = Firefly()
two = Firefly()
one.display()
print '\n'
two.display()
print one.attraction(two)
"""
