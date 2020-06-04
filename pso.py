# coding: utf-8
# refer to https://blog.csdn.net/zhaozx19950803/article/details/79854466
import random
import numpy as np
import matplotlib.pyplot as plt
import time

class Particle(object):
    def __init__(self):
        self.p = 0 # current position of particle
        self.v = 0 # current velocity of particle
        self.p_best = 0 # the best position of particle
        
class PSO(object):
    def __init__(self, x_range, fitness_function, w, c1, c2, N, iter_N, plot):
        self.x_range = x_range
        self.fitness_function = fitness_function
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.g_best = 0 # the best position of particles
        self.N = N
        self.pop = [] # the particles
        self.iter_N = iter_N
        self.plot = plot
        
    # get the g_best
    def get_g_best(self, pop):
        for bird in pop:
            if bird.fitness < self.fitness_function(self.g_best):
                self.g_best = bird.p
                
    # initialize the particles
    def init_population(self, pop, N):
        for i in range(N):
            bird = Particle()
            bird.p = np.random.uniform(self.x_range[0], self.x_range[1])
            bird.fitness = self.fitness_function(bird.p)
            bird.p_best = bird.fitness
            pop.append(bird)
        # get the g_best
        self.get_g_best(pop)
        
    # update the position and velocity of particles
    def update(self, pop):
        for bird in pop:
            v = self.w * bird.v + self.c1 * random.random() * (bird.p_best - bird.p) + self.c2 * random.random() * (self.g_best - bird.p)
            p = bird.p + v
            if self.x_range[0] < p < self.x_range[1]:
                bird.p = p
                bird.v = v
                # update the fitness value of particles
                bird.fitness = self.fitness_function(bird.p)
                # get the minimum
                if bird.fitness < self.fitness_function(bird.p_best):
                    # update the p_best
                    bird.p_best = bird.p
    
    def slover(self):
        # initialize the particles and get initial x
        self.init_population(self.pop, self.N)
        print ('Init x:        ', self.pop[0].p)

        start_time = time.time()

        # use pso to find the minimum
        for i in range(self.iter_N):
            # update the position and velocity
            self.update(self.pop)
            # update the g_best
            self.get_g_best(self.pop)
            
            if i % 100 == 0:
                print ('Current x:     ', self.g_best)

            # # show the animation
            if self.plot == True:
                scatter_x = np.array([ind.p for ind in self.pop])
                scatter_y = np.array([ind.fitness for ind in self.pop])
                scatter_best_x = self.g_best
                scatter_best_y = self.fitness_function(self.g_best)
                plt_x = plt.scatter(scatter_x, scatter_y, c = 'b')
                plt_best = plt.scatter(scatter_best_x, scatter_best_y, c = 'r')
                plt.pause(0.01)
                plt_x.remove()
                plt_best.remove()

        end_time = time.time() - start_time

        x = self.pop[0].p
        print('Optimal x:     ', x)
        print('Computing time:', end_time)
        return x