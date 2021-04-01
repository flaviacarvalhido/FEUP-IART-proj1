from structure.Structure import *
from parserfunc import *
import math
import random

def simulatedAnnealing(data):
  initialSol=data.generateRandomSol()
  tMin = 0.0001
  alpha = 0.9
  t = 1
  currentSol = initialSol

  while t > tMin:
    print('new it')
    for i in range(100):
      newSol = neighbourFunc(data,currentSol)
      if data.evaluation(newSol) >= data.evaluation(currentSol):
        #print("better func")
        currentSol = newSol
      else:
        var = -(data.evaluation(currentSol) - data.evaluation(newSol))/10000000000
        print(data.evaluation(currentSol) - data.evaluation(newSol))
        ap = math.pow(math.e, var/t)
        #print("AP VALUE:" + str(ap))
        if ap > random.random():
          print("VALUES:")
          print(ap)
          print(random.random())
          currentSol = newSol
    t = t*alpha
  print("--------")
  currentSol.printVideosinCaches()
  print('ev:',data.evaluation(currentSol))

  return currentSol


#simulatedAnnealing()
#print("end function")
