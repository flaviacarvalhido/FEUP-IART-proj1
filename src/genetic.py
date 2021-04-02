from structure.Structure import *
from parserfunc import *
from copy import *
import random

def steadyStateGenetic(popSize, numGens, survivorRate, mutationRate):
    data=readData('../src/input/videos_worth_spreading.in')
    survivorsSize = int(popSize*survivorRate)
    percetageMutation = int(popSize*mutationRate)
    population=generatePop(popSize,data)
   
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
            child=classicalCrossover(survivors,data)
            # print('inside while')

            if random.randint(0, popSize) < mutationRate*popSize:
                child[1].mutate()
                child[0]=data.evaluation(child[1])
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
    data=readData('../src/input/videos_worth_spreading.in')
    percetageMutation = int(popSize*mutationRate)
    population=generatePop(popSize,data)
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
            child=classicalCrossover(population,data)
            # print('inside while')

            if random.randint(0, popSize) < mutationRate*popSize:
                child[1].mutate()
                child[0]=data.evaluation(child[1])
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
    subgroupLen=int(len(population)/10)
    randomGroup1 = random.sample(population, subgroupLen)
    randomGroup2 = random.sample(population, subgroupLen)


    randomGroup1 = sorted(randomGroup1, key=lambda x:  (x[0]))
    randomGroup1.reverse();
    
    randomGroup2 = sorted(randomGroup2, key=lambda x:  (x[0]))
    randomGroup2.reverse();
    #print(randomGroup1[0][0],randomGroup2[0][0])
    return [randomGroup1[0],randomGroup2[0]]
    

def classicalCrossover(population,data):
    # print('classicalCrossover')
    parents=tournament(population)
    x=parents[0]
    y=parents[1]
    #print('parent indexes:',x[0], y[0] )
    crossPoint=random.randrange(len(x[1].caches))

    cachesX=(x[1].caches)
    cachesY=(y[1].caches)

    c1=cachesX[0:crossPoint]+cachesY[crossPoint:len(cachesY)]
    c2=cachesY[0:crossPoint]+cachesX[crossPoint:len(cachesY)]

    child1=(x[1])
    child2=(y[1])

    for i in range(crossPoint):
        swapCachesContent(child1.caches[i],y[1].caches[i])
        swapCachesContent(child2.caches[i],x[1].caches[i])


  
    ev1=data.evaluation(child1)
    ev2=data.evaluation(child2)
    # print('inside classic',ev1,ev2)
    if(ev1>ev2):
        return [ev1,child1]
    else:
        return [ev2,child2]
     

def generatePop(popSize,data):
    t0=time.perf_counter()
    population=[]
    for i in range(popSize):
        individual=data.generateRandomSol()
        #individual.printVideosinCaches()
        population.append([data.evaluation(individual),individual])
    print('pop generated')
    t1=time.perf_counter()
    print(t1-t0)
    return population








def testEval():
    data=readData('../src/input/small.in')
    sol=Solution(data.numCaches,data.sizeCaches)
    sol.caches[0].addVideo(data.videos[2])
    sol.caches[1].addVideo(data.videos[1])
    sol.caches[1].addVideo(data.videos[3])
    sol.caches[2].addVideo(data.videos[0])
    sol.caches[2].addVideo(data.videos[1])
   
    print(data.evaluation(sol))##should be 1850000


def testMut():
    data=readData('../src/input/small.in')
    sol=Solution(data.numCaches,data.sizeCaches)
    sol.caches[0].addVideo(data.videos[2])
    sol.caches[1].addVideo(data.videos[1])
    sol.caches[1].addVideo(data.videos[3])
    sol.caches[2].addVideo(data.videos[0])
    sol.caches[2].addVideo(data.videos[1])
    sol.printVideosinCaches()##should be 1850000
    sol.mutate()
    sol.printVideosinCaches()
    print('ev:',data.evaluation(sol))
  
def testMut2():
    data=readData('../src/input/me_at_the_zoo.in')
    sol=data.generateRandomSol()
    sol.printVideosinCaches()##should be 1850000
    sol.mutate()
    sol.printVideosinCaches()

def testCross():

    data=readData('../src/input/small.in')
    pop=generatePop(5,data)
    child=classicalCrossover(pop,data)
    child[1].printVideosinCaches()
    print(child[0])
    

# testCross()
# generationalGenetic(50,30,0.3)
testMut2()
# testEval()
# steadyStateGenetic(70,40,0.5,0.8)