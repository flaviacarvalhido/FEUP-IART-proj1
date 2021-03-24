from structure.Structure import neighbourFunc
import math
import random

def simulatedAnnealing(initialSol):
  tMin = 0.0001
  alpha = 0.9
  t = 1
  currentSol = initialSol

  while t > tMin:
    for i in range(100):
      newSol = neighbourFunc(currentSol)
      if newSol.evaluation() > currentSol.evaluation():
        currentSol = newSol
      else:
        ap = math.pow(math.E, (currentSol.evaluation() - newSol.evaluation())/t)
        if ap > random():
          currentSol = newSol
    t = t*alpha
  
  return currentSol