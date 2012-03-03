import math
import random
import optimization

class Particle:
  def __init__(self):
    self.position = [random.randrange(0, 100), random.randrange(100)]
    self.fitness  = self.fitness_function(self.position[0], self.position[1])
    self.best_pos = [self.position[0], self.position[1]]
    self.best_fit = optimization.de_jong(self.best_pos[0], self.best_pos[1])
    self.gradient = [random.randrange(-3, 3), random.randrange(-3, 3)]

  def fitness_function(self, x, y):
    return optimization.de_jong(x, y)

  def display(self):
    print("Current Position: x = " + str(self.position[0]) + ", y = " +
      str(self.position[1]))
    print("Current Fitness:  " + str(self.fitness))
    print("Best Position:    x = " + str(self.best_pos[0]) + ", y = " +
      str(self.best_pos[1]))
    print("Best Fitness:     " + str(self.best_fit))
    print("Gradient:         x = " + str(self.gradient[0]) + ", y = " +
      str(self.gradient[1]))
  
  def update(self, leader, vec=0.5, internal=0.5, external=0.5):
    rand_p = random.random()
    rand_g = random.random()

    self.position[0] = self.position[0] + self.gradient[0]
    self.position[1] = self.position[1] + self.gradient[1]

    self.gradient[0] = (vec * self.gradient[0] + internal + rand_p *
      (self.best_pos[0] - self.position[0]) + external * rand_g *
      (leader.best_pos[0] - self.position[0]))
    self.gradient[1] = (vec * self.gradient[1] + internal * rand_p *
      (self.best_pos[1] - self.position[1]) + external * rand_g *
      (leader.best_pos[1] - self.position[1]))

    self.fitness = self.fitness_function(self.position[0], self.position[1])
    if (self.fitness < self.best_fit):
      self.best_pos[0] = self.position[0]
      self.best_pos[1] = self.position[1]
      self.best_fit = self.fitness
