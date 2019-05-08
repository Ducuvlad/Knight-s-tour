import unittest
from numpy.random import random
from random import randint
import random
from random import sample
class Individual:
    #perm is a permutation of touples (x,y)
    #size is the size of the board
    def __init__ (self,size,perm):
        self.size=size
        self.perm=perm
        self.fit=0
        self.beginOfSequence=1000
    def fitness(self): #todo cate perechi alaturate sunt in saritura calului
                        #todo poti schimba reprezentarea
        longestSequence=0
        currentSequenceLen = 1

        for index in range(0,len(self.perm)-1):

            xy1 = (self.perm[index][0] - 2, self.perm[index][1] - 1)
            xy2 = (self.perm[index][0] - 2, self.perm[index][1] + 1)
            xy3 = (self.perm[index][0] + 2, self.perm[index][1] - 1)
            xy4 = (self.perm[index][0] + 2, self.perm[index][1] + 1)
            xy5 = (self.perm[index][0] - 1, self.perm[index][1] - 2)
            xy6 = (self.perm[index][0] - 1, self.perm[index][1] + 2)
            xy7 = (self.perm[index][0] + 1, self.perm[index][1] - 2)
            xy8 = (self.perm[index][0] + 1, self.perm[index][1] + 2)
            #print(xy1,xy2,xy3,xy4,xy5,xy6,xy7,xy8)
            if self.perm[index + 1] == xy1 or self.perm[index + 1]==xy2 or self.perm[index + 1]==xy3 or self.perm[index + 1]==xy4 or self.perm[index + 1]==xy5 or self.perm[index + 1]==xy6 or self.perm[index + 1]==xy7 or self.perm[index + 1]==xy8:
                currentSequenceLen += 1
        self.fit= currentSequenceLen

    def mutation(self,probability):
        r = random.random()
        if r > probability:
            idx = range(len(self.perm))
            i1, i2 = random.sample(idx, 2)
            self.perm[i1], self.perm[i2] = self.perm[i2], self.perm[i1]

    def orderedCrossover(self, ind2):
        """Executes an ordered crossover (OX) on the input
        individuals. The two individuals are modified in place. This crossover
        expects :term:`sequence` individuals of indices, the result for any other
        type of individuals is unpredictable.
        :param self: The first individual participating in the crossover.
        :param ind2.perm: The second individual participating in the crossover.
        :returns: A tuple of two individuals.
        Moreover, this crossover generates holes in the input
        individuals. A hole is created when an attribute of an individual is
        between the two crossover points of the other individual. Then it rotates
        the element so that all holes are between the crossover points and fills
        them with the removed elements in order.
        """
        '''
        size = len(self.perm)-self.fit
        size=randint(1,size)
        print("Size="+str(size))
        numbers = []
        for i in range(self.fit, self.fit+size):
            numbers.append(i)
        a = 0
        b = self.fit
        '''
        size = len(self.perm)
        a, b = random.sample(range(size), 2)
        if a > b:
            a, b = b, a
        #todo check this shit out
        #print("Lenght of permutation"+str(len(self.perm)))
        #if b>=len(self.perm):
        #    b=len(self.perm)-1
        #print("a:"+str(a)+" b:"+str(b))
        #iteration 2
        newPerm1 = [0] * size
        newPerm2 = [0] * size
        for i in range(a,b+1):
            newPerm1[i]=self.perm[i] #cut part from 1st parent
            newPerm2[i]=ind2.perm[i] #cut part from 2nd parent
        i=(b+1)%size
        while 0 in newPerm1:
            #print("i="+str(i))
            #print(ind2.perm)
            #print(newPerm1)
            oldi=i
            while (ind2.perm[i] in newPerm1):
                i = (i + 1) % size
            newPerm1[oldi]=ind2.perm[i]
            i=(oldi+1)%size
        i = (b + 1)%size

        while 0 in newPerm2:
            #print("------------")
            #print("i="+str(i))
            #print(self.perm)
            #print(newPerm2)
            oldi = i
            while (self.perm[i] in newPerm2):
                #print("i=" + str(i))
                i = (i + 1) % size
            newPerm2[oldi] = self.perm[i]
            i = (oldi + 1) % size

        return Individual(size,newPerm1),Individual(size,newPerm2)
        #iteration 1

        '''
        holes1={}
        holes2={}
        for e in self.perm:
            holes1[e]=True
        for e in ind2.perm:
            holes2[e]=True
        for i in range(size):
            if i < a or i > b:
                holes1[ind2.perm[i]] = False
                holes2[self.perm[i]] = False

        # We must keep the original values somewhere before scrambling everything
        temp1, temp2 = self.perm, ind2.perm
        k1, k2 = b + 1, b + 1
        for i in range(size):
            if not holes1[temp1[(i + b + 1) % size]]:
                self.perm[k1 % size] = temp1[(i + b + 1) % size]
                k1 += 1

            if not holes2[temp2[(i + b + 1) % size]]:
                ind2.perm[k2 % size] = temp2[(i + b + 1) % size]
                k2 += 1

        # Swap the content between a and b (included)
        for i in range(a, b + 1):
            self.perm[i], ind2.perm[i] = ind2.perm[i], self.perm[i]
        self.mutation(0.5)
        ind2.mutation(0.5)
        return self, ind2
        '''


class TestStringMethods(unittest.TestCase):

    def test_fit(self):
        in1=Individual(3,[(0,0),(1,2),(2,0)])
        in1.fitness()
        assert(in1.fit==3)

        in2 = Individual(5, [(0, 0), (1, 2), (2, 0),(1,1),(2,3)])
        in2.fitness()
        assert (in2.fit == 4)

    def test_crossover(self):
        in1 = Individual(3, [(1,1), (2, 2), (3, 3), (4 , 4),(5, 5) ])
        in2 = Individual(3, [(5 ,5), (3, 3),(2, 2),  (1,1), (4, 4) ])
        in3,in4=in1.orderedCrossover(in2)
        print(in1.perm,in2.perm)
        print(in3.perm,in4.perm)
