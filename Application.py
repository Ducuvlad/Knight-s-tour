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

    tuples=[]
    popl=[]
    for i in range(size):
        for j in range(size):
            tuples.append((i , j))
    for i in range(popsize):
        random.shuffle(tuples)
        individ=Individual(size,deepcopy(tuples))
        popl.append(deepcopy(individ))
        #print(tuples)
    finpop=population(popsize,popl,size)
    algo=Algorithm(size,finpop)
    #for i in finpop.indiv:
        #print(i.perm)
    evaluation,fitness,iter=algo.run()

    plt.plot(range(iter), fitness, label='BestFitness vs iteration')

    plt.xlabel('Iteration')
    plt.ylabel('BestFitness')
    plt.title("BestFitness evolution")
    plt.legend()
    plt.show()


main(5,10)


