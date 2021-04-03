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
        
        # stopping
        currEval = data.evaluation(bestSolution)

        if(lastEval==currEval): 
            counter+=1  
        else: 
            counter=0
            lastEval = currEval

        if(counter == stoppingIterations):
            break


    t1=time.perf_counter()
    return bestSolution, t1-t0


# data=readData('src/input/small.in')
# result=tabuSearchStatic(data, 10)
# print(data.evaluation(result))





# def tabuSearchReactive(data):
#     sol=data.generateRandomSol()

#     bestSolution = sol                                     # TODO: sol is a randomly generated initial Solution
#     bestCandidate = sol
#     tabuList = []
#     tabuList.append(sol)

#     while():                                                # TODO: stopping condition
#         neighborhood = bestCandidate.getNeighbors()         # TODO: get all the neighbors available. implement getNeighbors in class Solution
#         bestCandidate = neighborhood[0]
#         for candidate in neighborhood:
#             if not tabuList.contains(candidate) and candidate.evaluation() > bestCandidate.evaluation():
#                 bestCandidate = candidate

#         if(bestCandidate.evaluation() > bestSolution.evaluation()):
#             bestSolution = bestCandidate

#         tabuList.append(bestCandidate)
#         if(len(tabuList) > maxTabuSize):                    # TODO: tabu tenure dynamic
#             tabuList.pop(0)
        
#     return bestSolution
