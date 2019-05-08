from copy import deepcopy

import Individual
import unittest
from numpy.random import random
from random import randint
import random
from random import sample
class population:
    '''
    A group of individuals
    noPop: population size
    indiv: list of Individuals
    size: size of the board specified in the problem
    '''
    def __init__(self,noPop,indiv,size):
        self.noPop=noPop
        self.indiv=indiv
        self.size=size

    def evaluate(self):
        '''
        Give the newly created Individuals fitness values
        If fitness value of an individual is close to response return said individual
        :return: Individual if problem is solved , None otherwise
        '''
        for e in self.indiv:


            if e.fit==0:
                e.fitness()
            if e.fit>self.size*self.size-4:
                return e
            #print(e.fit)
        #print("Bye")
        return None

    def choose(self,choices):
        '''
        Return a random
        :param choices:
        :return:
        '''
        max = sum(choices.values())
        pick = random.uniform(0, max)
        current = 0
        for key, value in choices.items():
            current += value
            if current > pick:
                return key
    def selection(self,pressure):

        '''
        ranking selection
        Sort individuals based on fitness,trim population
        Generate new population
        :param pressure: value used to specify the selection pressure
        :return: the fitness of individual 0,presumed best Individual
        '''
        rankedSelect = sorted(self.indiv, key=lambda indiv:indiv.fit,reverse=True)
        self.indiv = rankedSelect[:self.noPop] #trim the population
        dictValueRank={}
        bsize=self.size**2
        #give each individual a rank
        for i in range(len(rankedSelect)):
            dictValueRank[rankedSelect[i]]=(2-pressure)/(bsize)+2*i*(pressure-1)/(bsize*(bsize-1))
        #choose randomly 2 individuals based on their ranks
        #generate offsprings using orderedCrossover
        #mutate the children and add them to population
        for i in range(0,10):
            indv1 = self.choose(dictValueRank)
            indv2 = self.choose(dictValueRank)
            copy1=deepcopy(indv1)
            copy2=deepcopy(indv2)
            tup=copy1.orderedCrossover(copy2)
            tup[0].mutation(0.5)
            tup[1].mutation(0.5)
            self.indiv.append(tup[0])
            self.indiv.append(tup[1])
        return self.indiv[0].fit
