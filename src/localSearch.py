
from structure.Structure import *
from parserfunc import *
import random


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


def testLocalSearch():
    data=readData('../src/input/me_at_the_zoo.in')
    inicialSol=data.generateRandomSol()
    lc=localSearch(data, inicialSol)
    print(data.evaluation(lc))


testLocalSearch()