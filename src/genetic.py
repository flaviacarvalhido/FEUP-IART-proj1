from structure.Structure import *
from parserfunc import *
from copy import *
import random


# genetic algorithm where each generation has a percentage of the previous generation individuals
def steadyStateGenetic(data, popSize, numGens, survivorRate, mutationRate):

    t0 = time.perf_counter()
    survivorsSize = int(popSize*survivorRate)
    percetageMutation = int(popSize*mutationRate)
    population = generatePop(popSize, data)

    numGensWithoutImprovement = 0
    best = 0
    iter = 0

    while numGensWithoutImprovement < numGens:

        # sort the polulation by its fitness
        population = sorted(population, key=lambda x: (x[0]))
        population.reverse()

        survivors = population[-survivorsSize:]

        population = survivors
        while len(population) < popSize:
            child = classicalCrossover(survivors, data)

            # mutate by a given rate
            if random.randint(0, popSize) < mutationRate*popSize:
                child[1].mutate()
                child[0] = data.evaluation(child[1])

            population.append(child)

        population = sorted(population, key=lambda x: (x[0]))
        population.reverse()

        bestofGen = population[0][0]
        solofGen = population[0][1]
        print('Generation nº', iter, ': Best Solution ->', best)
        iter += 1

        if bestofGen > best:
            best =bestofGen
            bestSol = solofGen

        elif(bestofGen <= best):
            numGensWithoutImprovement += 1

    print("No evolution detected after",
          numGensWithoutImprovement, "generations. Stopping")
    t1 = time.perf_counter()
    
    return bestSol, t1-t0


# genetic algorithm where each generation starts empty and is built with the children of the previous generation
def generationalGenetic(data, popSize, numGens, mutationRate):

    t0 = time.perf_counter()
    percetageMutation = int(popSize*mutationRate)
    population = generatePop(popSize, data)
    currentGeneration = 0
    previousSol = 0
    numGensWithoutImprovement = 0
    best = 0
    iter = 0
    while numGensWithoutImprovement < numGens:
        nextGen = []

        # sort the polulation by its fitness
        population = sorted(population, key=lambda x: (x[0]))
        population.reverse()

        while len(nextGen) < popSize:
            child = classicalCrossover(population, data)

            # mutate by a given rate
            if random.randint(0, popSize) < mutationRate*popSize:
                child[1].mutate()
                child[0] = data.evaluation(child[1])

            nextGen.append(child)

        population = sorted(nextGen, key=lambda x: (x[0]))
        population.reverse()

        bestofGen = population[0][0]
        solofGen = population[0][1]
        print('Generation nº', iter, ': Best Solution ->', best)
        iter += 1

        if bestofGen > best:
            best = bestofGen
            bestSol = solofGen
        elif(bestofGen <= best):
            numGensWithoutImprovement += 1

    print("No evolution detected after",
          numGensWithoutImprovement, "generations. Stopping")
    t1 = time.perf_counter()
    return bestSol, t1-t0


# returns two parents for reprodutction based on tournamentSelection
def tournament(population):
    subgroupLen = int(len(population)/10)
    randomGroup1 = random.sample(population, subgroupLen)
    randomGroup2 = random.sample(population, subgroupLen)

    randomGroup1 = sorted(randomGroup1, key=lambda x:  (x[0]))
    randomGroup1.reverse()

    randomGroup2 = sorted(randomGroup2, key=lambda x:  (x[0]))
    randomGroup2.reverse()

    return [randomGroup1[0], randomGroup2[0]]


# crossover function: children are created from a part of each parents caches (the crosspoint is choosen randomly)
def classicalCrossover(population, data):
    parents = tournament(population)
    x = parents[0]
    y = parents[1]

    # choose the crosspoint
    crossPoint = random.randrange(len(x[1].caches))

    cachesX = (x[1].caches)
    cachesY = (y[1].caches)

    # build new cache groups
    c1 = cachesX[0:crossPoint]+cachesY[crossPoint:len(cachesY)]
    c2 = cachesY[0:crossPoint]+cachesX[crossPoint:len(cachesY)]

    child1 = deepcopy(x[1])
    child2 = deepcopy(y[1])

    for i in range(crossPoint):
        swapCachesContent(child1.caches[i], y[1].caches[i])
        swapCachesContent(child2.caches[i], x[1].caches[i])

    ev1 = data.evaluation(child1)
    ev2 = data.evaluation(child2)

    # choose the best child
    if(ev1 > ev2):
        return [ev1, child1]
    else:
        return [ev2, child2]


# generates population with popSize of random individuals
def generatePop(popSize, data):
    population = []
    for i in range(popSize):
        individual = data.generateRandomSol()

        population.append([data.evaluation(individual), individual])

    return population


def testEval():
    data = readData('src/input/small.in')
    sol = Solution(data.numCaches, data.sizeCaches)
    sol.caches[0].addVideo(data.videos[2])
    sol.caches[1].addVideo(data.videos[1])
    sol.caches[1].addVideo(data.videos[3])
    sol.caches[2].addVideo(data.videos[0])
    sol.caches[2].addVideo(data.videos[1])

    print(data.evaluation(sol))  # should be 1850000


def testMut():
    data = readData('src/input/small.in')
    sol = Solution(data.numCaches, data.sizeCaches)
    sol.caches[0].addVideo(data.videos[2])
    sol.caches[1].addVideo(data.videos[1])
    sol.caches[1].addVideo(data.videos[3])
    sol.caches[2].addVideo(data.videos[0])
    sol.caches[2].addVideo(data.videos[1])
    sol.printVideosinCaches()  # should be 1850000
    sol.mutate()
    sol.printVideosinCaches()
    print('ev:', data.evaluation(sol))


def testMut2():
    data = readData('src/input/me_at_the_zoo.in')
    sol = data.generateRandomSol()
    sol.printVideosinCaches()  # should be 1850000
    sol.mutate()
    print('---')
    sol.printVideosinCaches()


def testCross():

    data = readData('src/input/small.in')
    pop = generatePop(5, data)
    child = classicalCrossover(pop, data)
    child[1].printVideosinCaches()
    print(child[0])
