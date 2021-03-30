from structure.Structure import *
import parser.py

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


def tabuSearch(sol):
    bestSolution = sol                                      # TODO: sol is a randomly generated initial Solution
    bestCandidate = sol
    tabuList = []
    tabuList.append(sol)

    while():                                                # TODO: stopping condition
        neighborhood = bestCandidate.getNeighbors()         # TODO: get all the neighbors available. implement getNeighbors in class Solution
        bestCandidate = neighborhood[0]
        for candidate in neighborhood:
            if not tabuList.contains(candidate) and candidate.evaluation() > bestCandidate.evaluation():
                bestCandidate = candidate

        if(bestCandidate.evaluation() > bestSolution.evaluation()):
            bestSolution = bestCandidate

        tabuList.append(bestCandidate)
        if(len(tabuList) > maxTabuSize):                    # TODO: tabu tenure dynamic
            tabuList.pop(0)
        
    return bestSolution
