# -*- coding: utf-8 -*-
# refer to https://blog.csdn.net/AI_BigData_wh/article/details/77943787
import numpy as np
import matplotlib.pyplot as plt
import time

class SA(object):
  def __init__(self, x_range, fitness_function, init_T, min_T, iter_L, delta, Plot):
    self.xrange = x_range
    self.fitness_function = fitness_function
    self.init_T = init_T
    self.min_T = min_T
    self.iter_L = iter_L
    self.delta = delta
    self.plot = Plot 

  def slover(self):
    # initialize the x
    x = np.random.uniform(self.xrange[0], self.xrange[1])
    now_t = self.init_T
    print ('Init x:        ', x)

    start_time = time.time()
    
    # use sa to find the minimum
    while now_t > self.min_T:
        for i in np.arange(1, self.iter_L):
            fun_val = self.fitness_function(x)
            # randomly generate new x within the range
            x_new = np.random.uniform(self.xrange[0], self.xrange[1])
            if x_new >= self.xrange[0] and x_new <= self.xrange[1]:
                fun_new = self.fitness_function(x_new)
                res = fun_new - fun_val
                # get the minimum
                if res < 0:
                    x = x_new
                else:
                    p = np.exp( - (res) / (1 * now_t))
                    if np.random.rand() < p:
                        x = x_new

                if i % 100 == 0:
                  print ('Current x:     ', x)

                # show the animation
                if self.plot == True:
                    scatter_best_x = x
                    scatter_best_y = self.fitness_function(x)
                    plt_best = plt.scatter(scatter_best_x, scatter_best_y, c='r')
                    plt.pause(0.01)
                    plt_best.remove()

        # get the temperature after cooling
        now_t = now_t * self.delta
    
    end_time = time.time() - start_time
    print('Optimal x:     ', x)
    print('Computing time:', end_time)
    return x