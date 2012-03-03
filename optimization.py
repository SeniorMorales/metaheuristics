import math

pi = math.pi
eu = math.e

# global minimum: 0 at 0,0
def de_jong(x, y):
  return pow(x, 2) + pow(y, 2)

# global minimum: 0 at 0,0
def axis_parallel_hyperellipsoid(x, y):
  return pow(x, 2) + 2 * pow(y, 2)

# global minimum: 0 at 0,0
def rotate_hyperellipsoid(x, y):
  return pow(x, 2) + (pow(x, 2) + pow(y, 2))

# global minumum: 0 at 1,1
def rosenbrock_valley(x, y):
  return 100 * pow(y - pow(x, 2), 2) + pow(1 - x, 2)

def rastrigin(x, y):
  return (10 * 2 + (pow(x, 2) - 10 * math.cos(2 * pi * x)) + 
    pow(y, 2) - 10 * math.cos(2 * pi * y))

def schwefel(x, y):
  return -x * math.sin(math.sqrt(abs(x))) - y * math.sin(math.sqrt(abs(y)))

# global minimum: 0 at 0,0
def griewangk(x, y):
  return (((pow(x, 2) + pow(y, 2)) / 4000) - math.cos(x) 
    * math.cos(y/math.sqrt(2)) + 1)

# global minimum: 0 at 0,0
def sum_of_different_power(x, y):
  return pow(abs(x), 2) + pow(abs(y), 3)

# Langermann: multimodal
# Michalewicz: mutlimodal

# Recommended constants define in function.  Make arguments instead?
# minimum: 0.397887 at -pi,12.275
# minimum: 0.397887 at pi,2.275
# minimum: 0.397887 at 9.43278,2.475
def branin(x_1, x_2):
  a = 1
  b = 5.1/(4 * pow(pi, 2))
  c = 5 / pi
  d = 6
  e = 10
  f = 1 / (8 * pi)
  return (a * pow(x_2 - b * pow(x_1, 2) + c * x_1 - d, 2) + e * (1 - f) *
    math.cos(x_1) + e)

# global minimum: -1 at pi,pi
def easom(x_1, x_2):
  return (-math.cos(x_1) * math.cos(x_2) * math.exp(-pow(x_1 - pi, 2) -
    pow(x_2 - pi, 2)))

# Goldstein-Price: broken formatting

# minimum: -1.0316 at -0.0898,0.7126
# minimum: -1.0316 at 0.0898,-0.7126
def six_hump_camel_back(x_1, x_2):
  return ((4 - 2.1 * pow(x_1, 2) + pow(x_1, 4) / 4) * pow(x_1, 2) + x_1 * x_2 +
    (-4 + 4 * pow(x_2,2)) * pow(x_2, 2))

def drop_wave(x_1, x_2):
  return (-((1 + math.cos(12 * math.sqrt(pow(x_1, 2) + pow(x_2, 2))))) /
    (1/2 * pow(x_1, 2) + pow(x_2, 2) + 2))
