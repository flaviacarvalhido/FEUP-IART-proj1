from structure.Structure import *
from parserfunc import *


# penalized features: number of empty caches (penaltyCaches), number of requested videos that are not in caches (penaltyVideos)

#define glsEvaluation
def glsEvaluation(data, sol, penaltyCaches, penaltyVideos, penaltyFactor):
    evaluation = data.evaluation(sol)

    evaluation += penaltyFactor * \
        (sol.emptyCaches() * penaltyCaches +
         sol.notCachedVideos(data) * penaltyVideos)

    return evaluation

#define glsUtility
def glsUtility(data, sol, penaltyCaches, penaltyVideos, costCaches, costVideos):
    utilityCaches = sol.emptyCaches() * (costCaches / (1 + penaltyCaches))
    utilityVideos = sol.notCachedVideos(data) * (costVideos / (1 + penaltyVideos))

    return utilityCaches, utilityVideos


# TODO: local search where??
def gls(data, stoppingIterations, penaltyFactor):

    currSolution=data.generateRandomSol()
    bestSolution=currSolution

    penaltyCaches=0      
    penaltyVideos=0

    costCaches=1000  # TODO: define cost??
    costVideos=500

    currEval = data.evaluation(bestSolution)
    counter=0
    lastEval=0

    while(1):                                                

        #search for bestCandidate in neighbourhood according to glsEvaluation function
        neighbourhood = data.neighbourhood(currSolution)
        bestCandidate = neighbourhood[0]
        for candidate in neighbourhood:
            if glsEvaluation(data, candidate, penaltyCaches, penaltyVideos, penaltyFactor) > glsEvaluation(data, bestCandidate, penaltyCaches, penaltyVideos, penaltyFactor):
                bestCandidate = candidate

        #select better solution
        if glsEvaluation(data, bestCandidate, penaltyCaches, penaltyVideos, penaltyFactor) > glsEvaluation(data, currSolution, penaltyCaches, penaltyVideos, penaltyFactor):
            currSolution = bestCandidate
            if data.evaluation(currSolution) > data.evaluation(bestSolution):
                bestSolution = currSolution
        else:
            utilityCaches, utilityVideos = glsUtility(
                data, currSolution, penaltyCaches, penaltyVideos, costCaches, costVideos)
            if(utilityCaches > utilityVideos):
                penaltyCaches += 1          # TODO: incremento de 1 é suficiente com avaliações tão altas? compensamos no penalty factor?
            else: 
                penaltyVideos += 1

        #stopping 
        currEval = data.evaluation(bestSolution)

        if(lastEval == currEval): 
            counter += 1  
        else: 
            counter = 0
            lastEval = currEval

        if(counter == stoppingIterations):
            break


    return bestSolution


# data = readData('src/input/small.in')
data = readData('src/input/me_at_the_zoo.in')
# data = readData('src/input/videos_worth_spreading.in')
# data = readData('src/input/trending_videos.in')
# data = readData('src/input/kittens.in')


#TODO: penaltyFactor tem de mudar de acordo com o dataset... mas como?
# small -> -200
# me_at_the_zoo -> -500 a -1000 ??
# videos_worth_spreading -> 
# trending_today -> 
# kittens -> 

result=gls(data, 10, -1000)
print(data.evaluation(result))
