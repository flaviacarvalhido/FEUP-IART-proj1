from structure.Structure import *
from parserfunc import *

from copy import *
import random



def ils(numIters,ILSiters,alpha,beta):
    data=readData('../src/input/me_at_the_zoo.in')
    
    inicialSol=data.generateRandomSol()
    currSol=localSearch(data,inicialSol)
    print(currSol)
    currEv=data.evaluation(currSol)

    for n in range(ILSiters):
        perturbationSol=currSol.perturbate()
        perturbationSol.printVideosinCaches()
        newSol=localSearch(data,perturbationSol)
        newEv=data.evaluation(newSol)
        if( newEv> currEv):
            currSol=newSol
            currEv=newEv
            break;







def localSearch(data,startsol):
    currentSol=startsol
    done=False
    while done==False:
        bestViz=currentSol
        neighb=data.neighbourhood(currentSol)

        for n in neighb:
            if(data.evaluation(n)>data.evaluation(bestViz)):
                bestViz=n
        if currentSol==bestViz:
            done=True
        else:
            currentSol=bestViz
    return currentSol


def testPerturbation():

    data=readData('../src/input/me_at_the_zoo.in')
    inicialSol=data.generateRandomSol()
    inicialSol.printVideosinCaches()
    pert=inicialSol.perturbate()
    pert.printVideosinCaches()


testPerturbation()
# ils(10,5,0,0.1)
