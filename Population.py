from copy import deepcopy

import Individual
import unittest
from numpy.random import random
from random import randint
import random
from random import sample
class population:
    def __init__(self,noPop,indiv,size):
        self.noPop=noPop
        self.indiv=indiv
        self.size=size

    def evaluate(self):
        for e in self.indiv:


            if e.fit==0:
                e.fitness()
            if e.fit>self.size*self.size-4:
                return e
            #print(e.fit)
        #print("Bye")
        return None

    def choose(self,choices):
        max = sum(choices.values())
        pick = random.uniform(0, max)
        current = 0
        for key, value in choices.items():
            current += value
            if current > pick:
                return key
    def selection(self,pressure):
        #ranking selection
        rankedSelect = sorted(self.indiv, key=lambda indiv:indiv.fit,reverse=True)
        self.indiv = rankedSelect[:self.noPop]
        dictValueRank={}
        bsize=self.size**2
        for i in range(len(rankedSelect)):
            dictValueRank[rankedSelect[i]]=(2-pressure)/(bsize)+2*i*(pressure-1)/(bsize*(bsize-1))

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
        #for i in self.indiv:
            #print (i.perm)
        return self.indiv[0].fit
