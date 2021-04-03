from structure.Structure import *
from parserfunc import *


# penalized features: number of empty caches (penaltyCaches), number of requested videos that are not in caches (penaltyVideos)

# define glsEvaluation: evualtuates solution and penalizes certain features if verified
def glsEvaluation(data, sol, penaltyCaches, penaltyVideos, penaltyFactor):
    evaluation = data.evaluation(sol)

    evaluation += penaltyFactor * (sol.emptyCaches() * penaltyCaches + sol.notCachedVideos(data) * penaltyVideos)

    return evaluation

# define glsUtility: calculates utility of feature in given solution


def glsUtility(data, sol, penaltyCaches, penaltyVideos, costCaches, costVideos):
    utilityCaches = sol.emptyCaches() * (costCaches / (1 + penaltyCaches))
    utilityVideos = sol.notCachedVideos(
        data) * (costVideos / (1 + penaltyVideos))

    return utilityCaches, utilityVideos


def gls(data, stoppingIterations, penaltyFactor):

    t0 = time.perf_counter()

    currSolution = data.generateRandomSol()
    bestSolution = currSolution

    penaltyCaches = 0
    penaltyVideos = 0

    costCaches = 1000
    costVideos = 500

    currEval = data.evaluation(bestSolution)
    counter = 0
    lastEval = 0
    iter = 0

    while(1):

        # search for bestCandidate in neighbourhood according to glsEvaluation function
        neighbourhood = data.neighbourhood(currSolution)
        bestCandidate = neighbourhood[0]
        for candidate in neighbourhood:
            if glsEvaluation(data, candidate, penaltyCaches, penaltyVideos, penaltyFactor) > glsEvaluation(data, bestCandidate, penaltyCaches, penaltyVideos, penaltyFactor):
                bestCandidate = candidate

        # select better solution
        if glsEvaluation(data, bestCandidate, penaltyCaches, penaltyVideos, penaltyFactor) > glsEvaluation(data, currSolution, penaltyCaches, penaltyVideos, penaltyFactor):
            currSolution = bestCandidate
            if data.evaluation(currSolution) > data.evaluation(bestSolution):
                bestSolution = currSolution
        else:
            utilityCaches, utilityVideos = glsUtility(
                data, currSolution, penaltyCaches, penaltyVideos, costCaches, costVideos)
            if(utilityCaches > utilityVideos):
                penaltyCaches += 1
            else:
                penaltyVideos += 1

        currEval = data.evaluation(bestSolution)
        print("Iteration nº", iter, ": Best Solution ->", currEval)
        iter += 1

        # stopping
        if(lastEval == currEval):
            counter += 1
        else:
            counter = 0
            lastEval = currEval

        if(counter == stoppingIterations):
            print("No evolution detected after",
                  stoppingIterations, "iterations. Stopping")
            break

    t1 = time.perf_counter()
    return bestSolution, t1-t0
