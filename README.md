# Heuristic algorithms for SA GA PSO


## Overview

Implement the heuristic algorithms to solve the one-dimensional optimization problem.


## Intorduction

This repo provides the three different algorithms (Simulated Annealing Algorithm, Genetic Algorithm, Particle Swarm Optimization Algorithm) to find the minimum of objective function.
However, the animation shows the calculation process for each iteration and it can be closed.


## Usage

1. Clone this repo.  
```
git clone https://github.com/kctoayo88/heuristic_algorithms_sa_ga_pso.git
```  
  
2. Install the packages(If it needs).
```
pip install numpy matplotlib
```  
  
3. Execute the program.
```
python main.py -algorithm=sa -plot=y
```  
-algorithm=[sa/ga/pso]: the algorithm that you want to use
-plot=[y/n]: show the animation or not
  
For details:
```
python main.py -h
```  
  
## Reference

[1] Simulated annealing (https://en.wikipedia.org/wiki/Simulated_annealing)  
[2] Genetic algorithm (https://en.wikipedia.org/wiki/Genetic_algorithm)  
[3] Particle swarm optimization (https://en.wikipedia.org/wiki/Particle_swarm_optimization)  
