import random
from random import randint

from numpy import choose

from utils.utils import generatePath, justGenerate


class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        # self.__repres = [generateNewValue(problParam['min'], problParam['max']) for _ in range(problParam['noDim'])]
        # self.__fitness = 0.0
        self.__fitness = 0.0

    def generateRepres(self, visited=[]):
        self.__repres = justGenerate(self.__problParam)

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        n = min(len(self.repres), len(c.repres))
        m = max(len(self.repres), len(c.repres))
        pos = []
        for i in range(0, n):
            if self.repres[i] == c.repres[i]:
                pos.append(i)
        chosen = random.choice(pos)
        offspring1 = []
        offspring2 = []
        for i in range(0, chosen):
            offspring1.append(self.repres[i])
            offspring2.append(c.repres[i])
        offspring1.append(self.repres[chosen])
        offspring2.append(self.repres[chosen])
        for i in range(chosen +1, len(self.repres)):
            offspring2.append(self.repres[i])
        for i in range(chosen + 1, len(c.repres)):
            offspring1.append(c.repres[i])


        c = Chromosome(self.__problParam)
        i = randint(0,1)
        if i == 0:
            c.repres = offspring1
        else:
            c.repres = offspring2
        return c

    def mutation(self):
        pass


    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness

    def __hash__(self):
        return hash(str(self))

    def __lt__(self, other):
        return self.fitness < other.fitness # cromozomul cu fitness mai mic va fi considerat cel mai mic ( util pentru heapify = min heap)