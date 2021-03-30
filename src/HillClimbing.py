from structure.Structure import *
from parserfunc import *

#pode ser preciso uma função para dar randomize de uma solução inicial

#basic hill climbing random
def hillClimbing():
  data=readData('../src/input/small.in')
  initialSol=data.generateRandomSol()
  count = 0
  currentSol = initialSol
  while True:
    if count >= 30:
      return currentSol
    newSol = neighbourFunc(data,currentSol)
    if data.evaluation(newSol) > data.evaluation(currentSol):
      currentSol = newSol
      count = 0
      break
    else: count += 1
  
    
hillClimbing()