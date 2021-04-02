from structure.Structure import *
from parserfunc import *


# sBest ← s0
# bestCandidate ← s0
# tabuList ← []
# tabuList.push(s0)
# while (not stoppingCondition())
#     sNeighborhood ← getNeighbors(bestCandidate)
#     bestCandidate ← sNeighborhood[0]
#     for (sCandidate in sNeighborhood)
#         if ( (not tabuList.contains(sCandidate)) and (fitness(sCandidate) > fitness(bestCandidate)) )
#             bestCandidate ← sCandidate
#         end
#     end
#     if (fitness(bestCandidate) > fitness(sBest))
#         sBest ← bestCandidate
#     end
#     tabuList.push(bestCandidate)
#     if (tabuList.size > maxTabuSize)
#         tabuList.removeFirst()
#     end
# end
# return sBest



def tabuSearchStatic(data, stoppingIterations):
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

    # TODO: bestSolution.evaluation() -> variable

    while(1):                                                
        neighbourhood=data.neighbourhood(bestCandidate)
        bestCandidate = neighbourhood[0]
        for candidate in neighbourhood:
            if not candidate in tabuList and data.evaluation(candidate) > data.evaluation(bestCandidate):
                bestCandidate = candidate

        if(data.evaluation(bestCandidate) > data.evaluation(bestSolution)):
            bestSolution = bestCandidate

        tabuList.append(bestCandidate)
        if(len(tabuList) > maxTabuSize):                    # n^1/2; n->neighbourhoodSize
            tabuList.pop(0)
        
        currEval = data.evaluation(bestSolution)

        if(lastEval==currEval): 
            counter+=1  
            print("Stopping "+ str(counter))
        else: 
            counter=0
            lastEval = currEval

        if(counter == stoppingIterations):
            break

    return bestSolution


data=readData('src/input/videos_worth_spreading.in')
result=tabuSearchStatic(data, 10)
print(data.evaluation(result))



# def tabuSearchDynamic(data):
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
