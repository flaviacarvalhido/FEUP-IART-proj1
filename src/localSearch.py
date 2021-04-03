
from structure.Structure import *
from parserfunc import *
import random

#local search algorithm to find a local max
def localSearch(data,currentSol):
    done=False

    while done==False:
        bestViz=(currentSol)
        bestVizEv=data.evaluation(bestViz)
        currentSolEv=bestVizEv
        neighb=data.neighbourhood(currentSol)

        #parse the neighbourhood to try to find a better solution
        for n in neighb:
            nEv=data.evaluation(n)

            if(nEv>bestVizEv):
                bestVizEv=nEv
                bestViz=n
        if currentSolEv==bestVizEv:
            print(currentSolEv)
            done=True
        else:
            currentSol=bestViz
        
    return currentSol


def testLocalSearch():
    data=readData('../src/input/me_at_the_zoo.in')
    inicialSol=data.generateRandomSol()
    inicialSol.printVideosinCaches()
    lc= localSearch(data, inicialSol)
    lc.printVideosinCaches()
    print(data.evaluation(lc))
