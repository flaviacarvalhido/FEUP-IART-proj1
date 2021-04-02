from structure.Structure import *
from parserfunc import *
from copy import *
import random



def ils(numIters,ILSiters,alpha,beta):
    data=readData('../src/input/small.in')
    i=1
    # while i<=numIters:
    x=data.generateRandomSol()
    s=localSearch(data,x)
    k=i
        




def localSearch(data,startsol):
    currentSol=startsol
    done=False
    while done==False:
        bestViz=currentSol
        neighb=data.neighbourhood(currentSol)

        for n in neighb:
            if(data.evaluation(n)<data.evaluation(bestViz)):
                bestViz=n
        if currentSol==bestViz:
            done=True
        else:
            currentSol=bestViz
    return currentSol

ils(10,5,0,0.1)