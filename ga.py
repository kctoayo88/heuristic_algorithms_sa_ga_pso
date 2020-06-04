# coding: utf-8
# refer to https://blog.csdn.net/zzzzjh/article/details/80633573
import numpy as np
import random
import matplotlib.pyplot as plt
import time

class GA(object):
    def __init__(self, x_range, fitness_function, pop_size, iteration_max, p_crossover, p_mutation, plot):
        self.bounds_begin = x_range[0] # lower bound
        self.bounds_end = x_range[1]   # upper bound
        self.fitness_function = fitness_function
        self.bit_length = int(np.log2((self.bounds_end - self.bounds_begin) / 0.0001)) + 1 # the length of chromosome
        self.pop_size = pop_size
        self.iteration_max = iteration_max
        self.p_crossover = p_crossover
        self.p_mutation = p_mutation
        self.population = np.random.randint(0, 2, size = (self.pop_size, self.bit_length)) # initialize the population
        self.plot = plot

    # get the fitness value
    def fitness(self, population):
        fit_value = []
        cumsump = []
        for i in population:
            x = self.transform2to10(i)
            xx = self.bounds_begin + x * (self.bounds_end - self.bounds_begin) / (pow(2, self.bit_length) - 1)
            s = self.fitness_function(xx)
            fit_value.append(s)
        f_sum = sum(fit_value)
        every_population = [x / f_sum for x in fit_value]
        cumsump.append(every_population[0])
        every_population.remove(every_population[0])
        for j in every_population:
            p = cumsump[-1] + j
            cumsump.append(p)
        return cumsump

    # select two population to crossover
    def select(self, cumsump):
        seln = []
        for i in range(2):
            j = 1
            r = np.random.uniform(0, 1)
            prand = [x - r for x in cumsump]
            while prand[j] < 0:
                j = j + 1
            seln.append(j)
        return seln

    # crossover the population
    def crossover(self, seln, pc):
        d = self.population[seln[1]].copy()
        f = self.population[seln[0]].copy()
        r = np.random.uniform()
        if r < pc:
            c = np.random.randint(1, self.bit_length - 1)
            a = self.population[seln[1]][c:]
            b = self.population[seln[0]][c:]
            d[c:] = b
            f[c:] = a
            g = d
            h = f
        else:
            g = self.population[seln[1]]
            h = self.population[seln[0]]
        return g, h

    # mutation of the populations
    def mutation(self,scnew,p_mutation):
        r = np.random.uniform(0, 1)
        if r < p_mutation:
            v = np.random.randint(0, self.bit_length)
            scnew[v] = abs(scnew[v] - 1)
        else:
            scnew = scnew
        return scnew
 
    # convert the binary to decimal
    def transform2to10(self, population):
        x = 0
        n = self.bit_length
        p = population.copy()
        p = p.tolist()
        p.reverse()
        for j in range(n):
            x = x + p[j] * pow(2, j)
        return x


    def slover(self):
        scnew = []

        # decode the initial x
        decode_dna = self.transform2to10(self.population[0])
        curr_x = self.bounds_begin + decode_dna * (self.bounds_end - self.bounds_begin) / (pow(2, self.bit_length) - 1)
        print ('Init x:        ', curr_x)

        cumsump = self.fitness(self.population)

        start_time = time.time()

        # use ga to find the minimum
        for i in range(self.iteration_max):
            for j in range(0, self.pop_size, 2):
                seln = self.select(cumsump)  #return the selected order
                scro = self.crossover(seln, self.p_crossover)  #returen two chromosome
                s1 = self.mutation(scro[0], self.p_mutation)
                s2 = self.mutation(scro[1], self.p_mutation)
                scnew.append(s1)
                scnew.append(s2)

            self.population = scnew
            cumsump = self.fitness(self.population)

            # decode the x
            x_list = []
            for dna in self.population:
                decode_dna = self.transform2to10(dna)
                curr_x = self.bounds_begin + decode_dna * (self.bounds_end - self.bounds_begin) / (pow(2, self.bit_length) - 1)
                x_list.append(curr_x)

            # get y from the decoded x
            y_list = []
            for curr_x in x_list:
                y_list.append(self.fitness_function(curr_x))

            # get the minimum
            fmin = y_list.index(min(y_list))
            x = x_list[fmin]

            x_list_in_gen = x_list[-(self.pop_size):]
            y_list_in_gen = y_list[-(self.pop_size):]

            if i % 100 == 0:
                print ('Current x:     ', x)

            # show the animation
            if self.plot == True:
                scatter_best_x = x
                scatter_best_y = self.fitness_function(x)
                plt_x = plt.scatter(x_list_in_gen, y_list_in_gen, c = 'b')
                plt_best = plt.scatter(scatter_best_x, scatter_best_y, c = 'r')
                plt.pause(0.01)
                plt_x.remove()
                plt_best.remove()

        end_time = time.time() - start_time

        print('Optimal x:     ', x)
        print('Computing time:', end_time)
        return x