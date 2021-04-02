
from structure.Structure import *
from parserfunc import *
import random


def localSearch(data,currentSol):
    # print('Current')
    # currentSol.printVideosinCaches()
    # print('---------')
    done=False
    # print('startsol', data.evaluation(currentSol))
    while done==False:
        bestViz=(currentSol)
        bestVizEv=data.evaluation(bestViz)
        currentSolEv=bestVizEv
        neighb=data.neighbourhood(currentSol)
        # print('bestviz')
        # bestViz.printVideosinCaches()
        # print('vis size',len(neighb))
       
        for n in neighb:
            # print('n')
            # n.printVideosinCaches()
            # print('------')
            nEv=data.evaluation(n)
            # print('vizev:', nEv)
            if(nEv>bestVizEv):
                bestVizEv=nEv
                bestViz=n
        if currentSolEv==bestVizEv:
    
            print(currentSolEv)
            # currentSol.printVideosinCaches()
            done=True
        else:
            currentSol=bestViz
        # print('best neib',bestVizEv)
        # currentSol.printVideosinCaches()
        # bestViz.printVideosinCaches()
    return currentSol


def testLocalSearch():
    data=readData('../src/input/vws_small.in')
    inicialSol=data.generateRandomSol()
    inicialSol.printVideosinCaches()
    lc= localSearch(data, inicialSol)
    lc.printVideosinCaches()
    print(data.evaluation(lc))


testLocalSearch()