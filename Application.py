from copy import deepcopy

from Individual import Individual
import unittest
from numpy.random import random
from random import randint
import random
from random import sample
from Algorithm import Algorithm
from Population import population
import matplotlib.pyplot as plt
def main(size,popsize):
    """
    Make a horse happy by guiding it to a path on the chessboard in such a way that it
    moves to every single square once and only once. The little horsie can jump obviously
    only in the classic L shape (the chess’ horse move).

    Generate random permutations of chess board squares
    Find best individual
    Show statistics

    :param size: Size of the chess board
    :param popsize: Size of population
    """
    print("Running")
    tuples=[]
    popl=[]
    for i in range(size):
        for j in range(size):
            tuples.append((i , j))
    for i in range(popsize):
        random.shuffle(tuples)
        individ=Individual(size,deepcopy(tuples))
        popl.append(deepcopy(individ))
    finpop=population(popsize,popl,size)
    algo=Algorithm(size,finpop)

    evaluation,fitness,iter=algo.run()
    #statistics
    plt.plot(range(iter), fitness, label='BestFitness vs iteration')

    plt.xlabel('Iteration')
    plt.ylabel('BestFitness')
    plt.title("BestFitness evolution")
    plt.legend()
    plt.show()


main(5,10)


