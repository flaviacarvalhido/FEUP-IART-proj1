from structure.Structure import *
from parserfunc import *
from copy import *
import random

def steadyStateGenetic(popSize, numGens, survivorRate, mutationRate):
    start=readData('../src/input/me_at_the_zoo.in')
    survivorsSize = int(popSize*survivorRate)
    percetageMutation = int(popSize*mutationRate)
    population=generatePop(popSize,start)
   
    numGensWithoutImprovement=0
    best=0


    while numGensWithoutImprovement < numGens:
        
        # sort the polulation by its fitness
        population = sorted(population, key=lambda x: (x[0]))
        population.reverse()

        survivors = population[-survivorsSize:]
        population=survivors
        # for p in population:
        #     print( p[0])
        #     p[1].printVideosinCaches()
        while len(population) < popSize:
            child=classicalCrossover(survivors)
            # print('inside while')

            if random.randint(0, popSize) < mutationRate*popSize:
                child[1].mutate()
                child[0]=child[1].evaluation()
                # print('insidemut')
            population.append(child)
        # print('outside while')
        population=sorted(population, key=lambda x: (x[0]))
        population.reverse();
        # for p in population:
        #     print( p[0])
        #     p[1].printVideosinCaches()
        bestofGen=population[0][0]
        print('BEST of generation',bestofGen,best)
      
       
        if bestofGen>best: 
            best=bestofGen
           
        elif(bestofGen<=best): 
            numGensWithoutImprovement+=1
            
    
    print('Best Sol found was:', best)



def generationalGenetic(popSize, numGens, mutationRate):
    start=readData('../src/input/me_at_the_zoo.in')
    percetageMutation = int(popSize*mutationRate)
    population=generatePop(popSize,start)
    currentGeneration = 0
    previousSol=0
    numGensWithoutImprovement=0
    best=0
    while numGensWithoutImprovement < numGens:
        nextGen=[]


        # sort the polulation by its fitness
        population = sorted(population, key=lambda x: (x[0]))
        population.reverse()
        
        # for p in population:
        #     print( p[0])
        #     p[1].printVideosinCaches()
        while len(nextGen) < popSize:
            child=classicalCrossover(population)
            # print('inside while')

            if random.randint(0, popSize) < mutationRate*popSize:
                child[1].mutate()
                child[0]=child[1].evaluation()
                # print('insidemut')
            nextGen.append(child)
        # print('outside while')
        population=sorted(nextGen, key=lambda x: (x[0]))
        population.reverse();
        # for p in population:
        #     print( p[0])
        #     p[1].printVideosinCaches()
        bestofGen=population[0][0]
        print('BEST of generation',bestofGen,best)
      
       
        if bestofGen>best: 
            best=bestofGen
           
        elif(bestofGen<=best): 
            numGensWithoutImprovement+=1
            
    
    print('Best Sol found was:', best)




#returns two parents for reprodutiction based on tournamentSelection
def tournament(population):
    subgroupLen=int(len(population))
    randomGroup1 = random.sample(population, subgroupLen)
    randomGroup2 = random.sample(population, subgroupLen)


    randomGroup1 = sorted(randomGroup1, key=lambda x:  (x[0]))
    randomGroup1.reverse();
    
    randomGroup2 = sorted(randomGroup2, key=lambda x:  (x[0]))
    randomGroup2.reverse();
    #print(randomGroup1[0][0],randomGroup2[0][0])
    return [randomGroup1[0],randomGroup2[0]]
    

def classicalCrossover(population):
   
    parents=tournament(population)
    x=parents[0]
    y=parents[1]
    #print('parent indexes:',x[0], y[0] )
    crossPoint=random.randrange(len(x[1].caches))

    cachesX=deepcopy(x[1].caches)
    cachesY=deepcopy(y[1].caches)

    c1=cachesX[0:crossPoint]+cachesY[crossPoint:len(cachesY)]
    c2=cachesY[0:crossPoint]+cachesX[crossPoint:len(cachesY)]

    child1=deepcopy(x[1])
    child2=deepcopy(y[1])

    for i in range(crossPoint):
        swapCachesContent(child1.caches[i],y[1].caches[i])
        swapCachesContent(child2.caches[i],x[1].caches[i])


  
    ev1=child1.evaluation()
    ev2=child2.evaluation()
    # print('inside classic',ev1,ev2)
    if(ev1>ev2):
        return [ev1,child1]
    else:
        return [ev2,child2]
     

def generatePop(popSize,start):
    population=[]
    for i in range(popSize):
        individual=start.generateRandomSol()
        
        #individual.printVideosinCaches()
       
        population.append([individual.evaluation(),individual])
    return population




def swapCachesContent(cache1,cache2):
    vid1=deepcopy(cache1.videos)
    cache1.videos=deepcopy(cache2.videos)
    cache2.videos=deepcopy(vid1)



def testEval():
    start=readData('src/input/small.in')
    start.caches[0].addVideo(start.videos[2])
    start.caches[1].addVideo(start.videos[1])
    start.caches[1].addVideo(start.videos[3])
    start.caches[2].addVideo(start.videos[0])
    start.caches[2].addVideo(start.videos[1])
    print(start.evaluation())##should be 1850000


def testMut():
    start=readData('src/input/small.in')
    start.caches[0].addVideo(start.videos[2])
    start.caches[1].addVideo(start.videos[1])
    start.caches[1].addVideo(start.videos[3])
    start.caches[2].addVideo(start.videos[0])
    start.caches[2].addVideo(start.videos[1])
    start.printVideosinCaches()##should be 1850000
    start.mutate()
    start.printVideosinCaches()
    print('ev:',start.evaluation())
  

def testCross():

    start=readData('../src/input/small.in')
    pop=generatePop(5,start)
    child=classicalCrossover(pop)
    child[1].printVideosinCaches()
    print(child[0])
    

# testCross()

generationalGenetic(50,20,0.1)

# steadyStateGenetic(50,20,0.5,0.1)