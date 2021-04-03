from structure.Structure import *
from parserfunc import *


#melhor numero de iterações para small: 20
# hill climbing algorithm
def hillClim(data):

  t0=time.perf_counter()

  currentSol=data.generateRandomSol()
  count = 0
  while True:
    if count >= 20:
      t1=time.perf_counter()
      return currentSol, t1-t0
    newSol = neighbourFunc(data, currentSol)
    if data.evaluation(newSol) > data.evaluation(currentSol):
      currentSol = newSol
      count = 0
    else:
      count += 1

