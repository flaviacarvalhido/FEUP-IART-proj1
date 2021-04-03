from structure.Structure import *
from parserfunc import *


#melhor numero de iterações para small: 20
# hill climbing algorithm
def hillClim(data):
  currentSol=data.generateRandomSol()
  count = 0
  while True:
    if count >= 20:
      print('ev:',data.evaluation(currentSol))
      #currentSol.printVideosinCaches()
      return currentSol
    newSol = neighbourFunc(data, currentSol)
    if data.evaluation(newSol) > data.evaluation(currentSol):
      currentSol = newSol
      count = 0
    else:
      count += 1

