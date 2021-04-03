from structure.Structure import *
from parserfunc import *
import math
import random

# simulated annealing algorithm
def simulatedAnnealing(data):

  t0=time.perf_counter()

  initialSol=data.generateRandomSol()
  tMin = 0.0001
  alpha = 0.9
  t = 1
  currentSol = initialSol

  while t > tMin:
    for i in range(100):
      currentEval = data.evaluation(currentSol)
      newSol = neighbourFunc(data,currentSol)
      newEval = data.evaluation(newSol)
      if newEval >= currentEval:
        currentSol = newSol
      else:
        var = -(currentEval - newEval)/10000000000
        ap = math.pow(math.e, var/t)
        rand = random.random()
        if ap > rand:
          currentSol = newSol
    t = t*alpha

  t1=time.perf_counter()

  return currentSol, t1-t0


