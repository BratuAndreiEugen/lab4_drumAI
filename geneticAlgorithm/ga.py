import heapq
from random import randint

from geneticAlgorithm.chromosome import Chromosome


class GA:
    def __init__(self, param=None, problParam=None):
        self.__param = param
        self.__problParam = problParam
        self.__population = []

    @property
    def population(self):
        return self.__population

    def initialisation(self):
        # visited = []
        # for i in range(0, self.__problParam['noNodes']):
        #     visited.append([0 for j in range(0, self.__problParam['noNodes'])])
        for _ in range(0, self.__param['popSize']):
            c = Chromosome(self.__problParam)
            c.generateRepres()
            self.__population.append(c)

        heapq.heapify(self.__population)

    def evaluation(self):
        for c in self.__population:
            c.fitness = self.__problParam['function'](c, self.__problParam)

    def bestChromosome(self):
        best = self.__population[0]
        for c in self.__population:
            if (c.fitness < best.fitness):
                best = c
        return best

    def worstChromosome(self):
        worst = self.__population[0]
        for c in self.__population:
            if (c.fitness > worst.fitness):
                worst = c
        return worst

    def selection(self):
        pos1 = randint(0, self.__param['popSize'] - 1)
        pos2 = randint(0, self.__param['popSize'] - 1)
        if (self.__population[pos1].fitness < self.__population[pos2].fitness):
            return pos1
        else:
            return pos2

    def oneGeneration(self):
        # creeaza o generatie complet noua prin selectie si mutatie
        newPop = []
        for _ in range(self.__param['popSize']):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        self.__population = newPop
        self.evaluation()
        heapq.heapify(self.__population)

    def oneGeneration2(self):
        # creeaza o generatie partial noua (prin selectie si mutatie) si partial veche ( din populatia anterioara )
        newPop = []
        r = randint(0, len(self.__population) - 1)
        for _ in range(r):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        for i in range(r, len(self.__population)):
            newPop.append(self.__population[i])

        self.__population = newPop
        self.evaluation()
        heapq.heapify(self.__population)

    def oneGenerationElitism(self):
        # creeaza o generatie noua prin adaugarea celui mai bun cromozom si in rest prin selectie si mutatie
        newPop = [self.bestChromosome()]
        for _ in range(self.__param['popSize'] - 1):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)

        self.__population = newPop
        self.evaluation()
        heapq.heapify(self.__population)

    def oneGenerationElitism2(self):
        # creeaza o treime din generatie prin crossover cu cel mai bun cromozom si 2/3 din populatie prin selectie si mutatie
        newPop = [self.bestChromosome()]
        for _ in range(int(self.__param['popSize']/3)*2):
            p1 = self.__population[self.selection()]
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)
        for _ in range(int(self.__param['popSize'] / 3) * 2, self.__param['popSize'] - 1):
            p1 = self.bestChromosome()
            p2 = self.__population[self.selection()]
            off = p1.crossover(p2)
            off.mutation()
            newPop.append(off)

        self.__population = newPop
        self.evaluation()
        heapq.heapify(self.__population)
