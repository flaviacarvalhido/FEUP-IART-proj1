from structure.Structure import *
from parserfunc import *
import copy 

#basic hill climbing random
def hillClimbing(data):

  initialSol=data.generateRandomSol()
  count = 0
  currentSol = initialSol
  currentEval = data.evaluation(currentSol)
  while True:
    #print("new it")
    #if count >= 15 and currentEval != 0 and currentEval == data.evaluation(currentSol): #count 10 -> small
    if count >= 30 and currentEval != 0:  
      print(currentEval)
      print('ev:',data.evaluation(currentSol))
      currentSol.printVideosinCaches()
      return currentSol

    newSol = neighbourFunc(data,currentSol)
    #print("got possible new sol")
    newEval = data.evaluation(newSol)
    if newEval > currentEval:
      #print("better sol")
      currentSol = newSol
      #print("--------SOLUTIONS--------")
      #print(currentSol)
      #print(newSol)
      #print("-------------------------")
      currentEval = newEval

      count = 0
    else: 
      count += 1
      #rint("not better sol")
    #currentSol.printVideosinCaches()
    #print("--------------------------")
    
#hillClimbing()
#print("end function")

#melhor numero de iterações para small: 20
def hillClim(data):
  currentSol=data.generateRandomSol()
  count = 0
  while True:
    if count >= 5:
      print('ev:',data.evaluation(currentSol))
      #currentSol.printVideosinCaches()
      return currentSol
    newSol = neighbourFunc(data, currentSol)
    if data.evaluation(newSol) > data.evaluation(currentSol):
      currentSol = newSol
      count = 0
    else:
      count += 1

data=readData("src/input/trending_today.in")
t0=time.perf_counter()
hillClim(data)
t1=time.perf_counter()
print(t1-t0)