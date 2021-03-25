from structure.Structure import *
from parserfunc import *
import random

def genetic(popSize, numGens):
    start=readData('src/input/small.in')
    
    generatePop(popSize,start)


def generatePop(popSize,start):
    population=[]
    for i in range(popSize):
        individual=readData('src/input/small.in').generateRandomSol()
        individual.printVideosinCaches()
       
        
        population.append(individual.evaluation())

    
    return population


genetic(50,10)





def testEval():
    start=readData('src/input/small.in')
    start.caches[0].addVideo(start.videos[2])
    start.caches[1].addVideo(start.videos[1])
    start.caches[1].addVideo(start.videos[3])
    start.caches[2].addVideo(start.videos[0])
    start.caches[2].addVideo(start.videos[1])
    print(start.evaluation())##should be 1850000