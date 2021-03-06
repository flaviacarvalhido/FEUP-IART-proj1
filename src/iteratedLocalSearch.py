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

        if( newEv> currEv):
            currSol=newSol
            currEv=newEv

        print("Iteration nº", n, ": Best Solution ->", currEv)
            
    print("Iteration", numIters, "limit reached. Stopping")
    t1=time.perf_counter()
   
    return currSol, t1-t0




def localSearch(data,currentSol):
   
    while True:
        bestViz=deepcopy(currentSol)
        bestVizEv=data.evaluation(bestViz)
        currentSolEv=bestVizEv
        neighb=data.neighbourhood(currentSol)

        for n in neighb:
            nEv=data.evaluation(n)
           
            if(nEv>bestVizEv):
                bestVizEv=nEv
                bestViz=deepcopy(n)
        if currentSolEv==bestVizEv:
            break
        else:
            currentSol=deepcopy(bestViz)
    
    return currentSol


def testPerturbation():

    data=readData('src/input/vws_small.in')
    inicialSol=data.generateRandomSol()
    inicialSol.printVideosinCaches()
    pert=inicialSol.perturbate()
    print('--------')
    pert.printVideosinCaches()
