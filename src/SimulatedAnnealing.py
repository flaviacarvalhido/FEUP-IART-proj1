from structure.Structure import *
from parserfunc import *
import math
import random

def simulatedAnnealing():
  data=readData('../src/input/small.in')
  initialSol=data.generateRandomSol()
  tMin = 0.0001
  alpha = 0.9
  t = 1
  currentSol = initialSol

  while t > tMin:
    print('new it')
    for i in range(100):
      newSol = neighbourFunc(data,currentSol)
      if data.evaluation(newSol) > data.evaluation(currentSol):
        currentSol = newSol
      else:
        ap = math.pow(math.e, (data.evaluation(currentSol) - data.evaluation(newSol))/t)
        if ap > random.random():
          currentSol = newSol
    t = t*alpha
  
  return currentSol


simulatedAnnealing()