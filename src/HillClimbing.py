from structure.Structure import *
from parserfunc import *

# hill climbing algorithm
def hillClim(data, iterations):

  t0=time.perf_counter()

  currentSol=data.generateRandomSol()
  count = 0
  numSolCalc = 0
  while True:
    if count >= iterations:
      print("Iteration", iterations, "limit reached. Stopping")
      t1=time.perf_counter()
      return currentSol, t1-t0
    newSol = neighbourFunc(data, currentSol)
    
    numSolCalc += 1
    if data.evaluation(newSol) > data.evaluation(currentSol):
      currentSol = newSol
      count = 0
    else:
      count += 1

    print("Iteration nº", numSolCalc, ": Best Solution ->", data.evaluation(currentSol))

