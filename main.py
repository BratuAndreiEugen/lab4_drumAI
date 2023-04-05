from geneticAlgorithm.chromosome import Chromosome
from geneticAlgorithm.fitnessFunctions import fitness1
from geneticAlgorithm.ga import GA
from utils.gmlReader import converter
from utils.reader import reader
from utils.utils import matrix_to_adjacency, bfs
from utils.weird_reader import readFromTSP


def various_tests():
    # m = converter("C:\Proiecte SSD\Python\lab4AI\\tests\\verif.gml")
    # dict = {}
    # dict['matrix'] = m
    # dict['noNodes'] = len(m)
    #
    # d1 = matrix_to_adjacency(dict)
    # d1['start'] = 0
    # d1['end'] = 2
    # print(d1)

    d2 = matrix_to_adjacency(reader("C:\\Proiecte SSD\\Python\\lab4AI\\tests\\easy_01_tsp.txt"))
    d2['start'] = 0
    d2['end'] = 2
    print(d2)

    c = Chromosome(d2)
    c.repres = [0, 3, 1, 2]
    c1 = Chromosome(d2)
    c1.repres = [0, 1, 3, 2]
    print(c, c1)
    print(c.mutation())
    print(c)
    print(fitness1(c, d2))

    dexp = {}
    dexp['noNodes'] = 10
    dexp['start'] = 0
    dexp['end'] = 9
    c = Chromosome(dexp)
    c1 = Chromosome(dexp)
    c.repres = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 9]
    c1.repres = [0, 'C', 'G', 'E', 'A', 'F', 'H', 'B', 'D', 9]
    print(c, c1)
    print(c.crossover(c1))

def runAlg(path, wrong_indexes=0, gml=0, user_start=-1, user_end=-1, generations=100, popSize=10, weird=0):
    problParam = {}
    if weird == 1:
        problParam = matrix_to_adjacency(readFromTSP(path))
    else:
        if gml == 0:
            problParam = matrix_to_adjacency(reader(path))
            if wrong_indexes == 1:
                problParam['start'] -= 1
                problParam['end'] -= 1
        elif gml == 1:
            daux = {}
            daux['start'] = user_start
            daux['end'] = user_end
            daux['matrix'] = converter(path)
            daux['noNodes'] = len(daux['matrix'])
            problParam = matrix_to_adjacency(daux)

    if user_end >= 0 and user_start >= 0:
        problParam['start'] = user_start
        problParam['end'] = user_end
    print(problParam)

    populationParams = {}
    problParam['function'] = fitness1
    problParam['forGenerate'] = 0
    populationParams['popSize'] = popSize
    ga = GA(populationParams, problParam)
    ga.initialisation()
    ga.evaluation()
    numberOfGenerations = generations
    bestPaths = [ga.bestChromosome()]
    while numberOfGenerations > 0:
        numberOfGenerations -= 1
        ga.oneGenerationElitism2()
        best = ga.bestChromosome()
        print(best)
        if best.fitness < bestPaths[0].fitness:
            bestPaths = [best]
        elif best.fitness == bestPaths[0].fitness:
            bestPaths.append(best)
        bestPaths = list(set(bestPaths))
    print("\nSOLUTIE :")
    print(bestPaths)
    return bestPaths


# daux = {}
# daux['matrix'] = converter("C:\Proiecte SSD\Python\lab4AI\\tests\myNetworks\\test2.gml")
# daux['noNodes'] = len(daux['matrix'])
# daux['start'] = 0
# daux['end'] = 0
# pr = matrix_to_adjacency(daux)
# bfs(pr)
# print(daux['noNodes'])

#runAlg("C:\\Proiecte SSD\\Python\\lab4AI\\tests\\easy_01_tsp.txt", generations=300, popSize=4, wrong_indexes=1)
#runAlg("C:\Proiecte SSD\Python\lab4AI\\tests\\verif.gml", gml=1)
#runAlg("C:\Proiecte SSD\Python\lab4AI\\tests\karate\\karate.gml", gml=1, generations=300, popSize=300)

runAlg("C:\\Proiecte SSD\\Python\\lab4AI\\tests\\easy_01_tsp.txt", wrong_indexes=1)
#runAlg("C:\\Proiecte SSD\\Python\\lab4AI\\tests\\easy_06_tsp.txt", wrong_indexes=1)
#runAlg("C:\\Proiecte SSD\\Python\\lab4AI\\tests\\others\\hard_test", wrong_indexes=1, generations=500, popSize=300)
#runAlg("C:\\Proiecte SSD\\Python\\lab4AI\\tests\\fricker26.txt", wrong_indexes=1, user_start= 1, user_end= 15, generations=1000, popSize=300)
#runAlg("C:\Proiecte SSD\Python\lab4AI\\tests\\berlin52.txt", weird=1,user_start= 1, user_end= 13, generations=200, popSize=200)
#runAlg("C:\Proiecte SSD\Python\lab4_drumAI\\tests\hard_01_tsp.txt", wrong_indexes=1, generations=200, popSize=200)