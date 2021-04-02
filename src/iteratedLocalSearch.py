from structure.Structure import *
from parserfunc import *

from copy import *
import random



def ils(numIters):
    data=readData('../src/input/videos_worth_spreading.in')
    
    inicialSol=data.generateRandomSol()
    currSol=localSearch(data,inicialSol)
    currEv=data.evaluation(currSol)

    for n in range(numIters):
        perturbationSol=currSol.perturbate()
        # perturbationSol.printVideosinCaches()
        newSol=localSearch(data,perturbationSol)
        newEv=data.evaluation(newSol)
        print('newev',newEv)
        if( newEv> currEv):
            currSol=newSol
            currEv=newEv
            

    print(data.evaluation(currSol))




def localSearch(data,currentSol):
   
 
    while True:
        bestViz=deepcopy(currentSol)
        bestVizEv=data.evaluation(bestViz)
        currentSolEv=bestVizEv
        neighb=data.neighbourhood(currentSol)
       
        # bestViz.printVideosinCaches()
       
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

    data=readData('../src/input/vws_small.in')
    inicialSol=data.generateRandomSol()
    inicialSol.printVideosinCaches()
    pert=inicialSol.perturbate()
    print('--------')
    pert.printVideosinCaches()


# testPerturbation()

ils(30)
