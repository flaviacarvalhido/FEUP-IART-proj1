from structure.Structure import neighbourFunc


#pode ser preciso uma função para dar randomize de uma solução inicial

#basic hill climbing random
def hillClimbing(initialSol):
  count = 0
  currentSol = initialSol
  while True:
    if count >= 30:
      return currentSol
    newSol = neighbourFunc(currentSol)
    if newSol.evaluation() > currentSol.evaluation():
      currentSol = newSol
      count = 0
      break
    else: count += 1
  
    
