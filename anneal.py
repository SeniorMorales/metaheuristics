import math
import random
import optimization

state = [random.randrange(100), random.randrange(100)]
neighborhood = [state]

max_eval = 100
eval_count_energy = 0

def fitness(state):
  return optimization.de_jong(state[0], state[1])

def neighbor(state, x_range=1.0, y_range=1.0):
  new_neighbor = list(state)
  new_neighbor[0] += random.uniform(-x_range, x_range)
  new_neighbor[1] += random.uniform(-y_range, y_range)
  return new_neighbor

def temperature(value, adjustment=10000):
  return adjustment * value

state = [random.randrange(100), random.randrange(100)]

def annealing(state):
  current = list(state)
  energy = fitness(current)

  i = 100
  while i > 0:
    candidate = neighbor(current, 10, 10)
    candidate_energy = fitness(candidate)
    prob = math.exp(-(candidate_energy - energy) / temperature(i))

    if candidate_energy <= energy:
      current = list(candidate)
      energy = candidate_energy
    else:
      if random.random() > prob:
        current = list(candidate)
        energy = candidate_energy
    i -= 1
  return current


print state
print fitness(state)
test = annealing(state)
print test
print fitness(test)
