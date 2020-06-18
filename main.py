# -*- coding: utf-8 -*-
import argparse
import numpy as np
import matplotlib.pyplot as plt

x_range = [-7, 7]

# SA parameters
init_T = 1000       # initial temperature
min_T = 1           # minimum of temperature
delta = 0.99        # cooling coefficient
k = 0.1             # scaling coefficient
iter_N_SA = 100     # number of iteration

# GA parameters
pop_size_GA = 50    # size of population
pcrossover = 0.5    # probability of crossover
pmutation = 0.5     # probability of mutation
iter_N_GA = 100     # number of iteration

# PSO parameters
pop_size_PSO = 50   # size of population
w = 0.1             # weight
c1 = 0.5            # coefficient of p_best
c2 = 2              # coefficient of g_best
iter_N_PSO = 100    # number of iteration

# objective funtion
def fitness_function(x):
  return 2 * np.cos(x) - x + x ** 2 / 10

def main(algorithm, plot):
  if plot == 'y':
    _plot = True
  else:
    _plot = False

  # plot the figure
  plt.figure()
  x = np.linspace(x_range[0], x_range[1], 300)
  y = fitness_function(x)
  plt.plot(x, y)

  plt.ion()
  
  # implement the algorithms
  if algorithm == 'sa':
    from sa import SA
    sa = SA(x_range, fitness_function, iter_N_SA, min_T, iter_N_SA, delta, k, _plot)
    optimal_x = sa.slover()
 
  if algorithm == 'ga':
    from ga import GA
    ga = GA(x_range, fitness_function, pop_size_GA, iter_N_GA, pcrossover, pmutation, _plot)
    optimal_x = ga.slover()

  if algorithm == 'pso':
    from pso import PSO
    pso = PSO(x_range, fitness_function, w, c1, c2, pop_size_PSO, iter_N_PSO, _plot)
    optimal_x = pso.slover()
  
  # get the optimal y
  optimal_y = fitness_function(optimal_x)
  print('Optimal y:     ', optimal_y)

  plt.plot(optimal_x, optimal_y, '*r', ms = 10)
  plt.ioff()
  plt.show()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('-algorithm', type = str, default = 'sa', help = 'choose a algorithm (sa / ga / pso)')
  parser.add_argument('-plot', type = str, default = 'n', help = 'show the animation (y / n)')
  args = parser.parse_args()
  main(args.algorithm, args.plot)