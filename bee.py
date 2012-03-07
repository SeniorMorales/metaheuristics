import math
import random
import optimization

class Bee:
  def __init__(self, x=0, y=0, lower=-100, upper=100):
    self.lower = lower
    self.upper = upper
    self.food = [(x + random.uniform(lower, upper) +
                  random.random() * (upper - lower)),
                 (y + random.uniform(lower, upper) +
                  random.random() * (upper - lower))]
    self.value = self.objective()
    self.fit = self.fitness()
    self.probability = 0

  def objective(self):
    return optimization.de_jong(self.food[0], self.food[1])

  def fitness(self):
    result = 0
    if self.value >= 0:
      result = 1 / (self.value + 1)
    else:
      result = 1 + abs(value)
    return result

  def display(self):
    print "Food is at x = " + str(self.food[0]) + ", y = " + str(self.food[1])
    print "Food has the value of " + str(self.value)
    print "This bee has fitness of " + str(self.fit)
    print ("The probability of this bee being selected is " +
      str(self.probability))

  def neighbor(self, x_grad=25, y_grad=25):
    x_diff = random.uniform(-x_grad, x_grad)
    y_diff = random.uniform(-y_grad, y_grad)
    other = Bee(self.food[0], self.food[1], x_diff, y_diff)
    return other
