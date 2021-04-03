from structure.Structure import *
from parserfunc import *

def tabuSearchStatic(data, stoppingIterations):

    t0=time.perf_counter()

    sol=data.generateRandomSol()

    neighborhoodSize = data.neighbourhoodSize()
    maxTabuSize = int(neighborhoodSize**(1/2))

    bestSolution = sol                                     
    bestCandidate = sol
    tabuList = []
    tabuList.append(sol)

    currEval = data.evaluation(bestSolution)
    counter=0
    lastEval=0

    iter=0

    while(1):       

        #search for bestCandidate in neighbourhood according to tabuList and evaluation function
        neighbourhood=data.neighbourhood(bestCandidate)
        bestCandidate = neighbourhood[0]
        for candidate in neighbourhood:
            if not candidate in tabuList and data.evaluation(candidate) > data.evaluation(bestCandidate):
                bestCandidate = candidate

        #select better solution
        if(data.evaluation(bestCandidate) > data.evaluation(bestSolution)):
            bestSolution = bestCandidate

        # update TabuList
        tabuList.append(bestCandidate)
        if(len(tabuList) > maxTabuSize):                    # maxTabuSize -> n^1/2; n->neighbourhoodSize
            tabuList.pop(0)
        
        currEval = data.evaluation(bestSolution)
        print("Iteration nº", iter, ": Best Solution ->", currEval)
        iter += 1

        # stopping
        if(lastEval==currEval): 
            counter+=1  
        else: 
            counter=0
            lastEval = currEval

        if(counter == stoppingIterations):
            print("No evolution detected after", stoppingIterations, "iterations. Stopping")
            break


    t1=time.perf_counter()
    return bestSolution, t1-t0


