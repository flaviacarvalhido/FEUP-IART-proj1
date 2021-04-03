from structure.Structure import *
from parserfunc import *

from copy import *
import random


# iterated local search algorithm
def ils(numIters,data):
    
    t0=time.perf_counter()

    #start with a random solution
    inicialSol=data.generateRandomSol()
    currSol=localSearch(data,inicialSol)
    currEv=data.evaluation(currSol)

    # perturbate the best solution and search for better neighbours
    for n in range(numIters):
        perturbationSol=currSol.perturbate()     
        newSol=localSearch(data,perturbationSol)
        newEv=data.evaluation(newSol)
        print('Iteration',n,': best solution was',newEv)
    
        if( newEv> currEv):
            currSol=newSol
            currEv=newEv
            

    t1=time.perf_counter()
    # print('\nBest solution found was:', currEv)
    # currSol.printVideosinCaches()
    # print('\nTook', t1-t0, 's\n\n')
    return currSol, t1-t0




def localSearch(data,currentSol):
   
    while True:
        bestViz=deepcopy(currentSol)
        bestVizEv=data.evaluation(bestViz)
        currentSolEv=bestVizEv
        neighb=data.neighbourhood(currentSol)

        for n in neighb:
            # n.printVideosinCaches()           
            nEv=data.evaluation(n)
           
            if(nEv>bestVizEv):
                bestVizEv=nEv
                bestViz=n
        if currentSolEv==bestVizEv:
            break
        else:
            currentSol=bestViz
    
    return currentSol




def testPerturbation():

    data=readData('src/input/vws_small.in')
    inicialSol=data.generateRandomSol()
    inicialSol.printVideosinCaches()
    pert=inicialSol.perturbate()
    print('--------')
    pert.printVideosinCaches()


# testPerturbation()

# ils(30,readData('../src/input/me_at_the_zoo.in'))
