from HillClimbing import hillClim
from SimulatedAnnealing import simulatedAnnealing
from genetic import *
from iteratedLocalSearch import *
from GuidedLocalSearch import *
from TabuSearch import *

from structure.Structure import *
from parserfunc import *

# first menu of the application
def initialMenu():
  print("------------------------------------------------")
  print()
  print("               STREAMING VIDEOS                 ")
  print()
  print("                          by Trio de Informática")
  print()
  input("Press a key to start ")
  print()
  print("------------------------------------------------")

# menu to choose the file to get the input
# it's ordered by file size
def fileOptions():
  print("------------------------------------------------")
  print()
  print("Choose the input file: ")
  print()
  print("1: Small")
  print("2: Me at the Zoo")
  print("3: Videos Worth Spreading")
  print("4: Trending Today")
  print("5: Kittens")
  print()
  while True:
    optionStr = input("Option: ")
    option = int(optionStr)
    if option == 1:
      file = "src/input/small.in"
      break
    elif option == 2:
      file = "src/input/me_at_the_zoo.in"
      break
    elif option == 3:
      file = "src/input/videos_worth_spreading.in"
      break
    elif option == 4: 
      file = "src/input/trending_today.in"
      break
    elif option == 5: 
      file = "src/input/kittens.in"
      break
    else: 
      print("Invalid input: Try again!")
      continue
  print("------------------------------------------------")
  return file, option

# menu to choose the algorithm to run
def algorithmOptions(file, fileSize):
  print("------------------------------------------------")
  print()
  print("Choose the algorithm: ")
  print()
  print("1: Hill Climbing")
  print("2: Simulated Annealing")
  print("3: Genetic - Steady State")
  print("4: Genetic - Generational")
  print("5: Iterative Local Search")
  print("6: Guided Local Search")
  print("7: Tabu Search")
  print()
  data=readData(file)
  while True:
    optionStr = input("Option: ")
    option = int(optionStr)
    if option == 1:
      hillClimbingMenu(data, fileSize)
      break
    elif option == 2:
      simulatedAnnealingMenu(data)
      break
    elif option == 3:
      geneticSteadyStateMenu(data, fileSize)
      break
    elif option == 4: 
      geneticGenerationalMenu(data, fileSize)
      break
    elif option == 5: 
      iterativeLocalSearchMenu(data, fileSize)
      break
    elif option == 6:
      guidedLocalSearchMenu(data, fileSize)
      break
    elif option == 7:
      tabuSearchMenu(data, fileSize)
      break
    else: 
      print("Invalid input: Try again!")
      continue
  #print("------------------------------------------------")


# menu to run the hill climbing algorithm
def hillClimbingMenu(data, fileSize):
  print("------------------------------------------------")
  print()
  print("                HILL CLIMBING                   ")
  print()
  if fileSize == 1 or fileSize == 2:
    iterations = 20
  else:
    iterations = 5
  sol, time = hillClim(data, iterations)
  printSolution(data, sol, time)
  print("------------------------------------------------")

# menu to run the simulated annealing algorithm
def simulatedAnnealingMenu(data):
  print("------------------------------------------------")
  print()
  print("              SIMULATED ANNEALING               ")
  print()
  sol, time = simulatedAnnealing(data)
  printSolution(data, sol, time)
  print("------------------------------------------------")

#menu to run the genetic steady state algorithm
def geneticSteadyStateMenu(data, fileSize):
  print("------------------------------------------------")
  print()
  print("             GENETIC STEADY STATE               ")
  print()
  sol, time = steadyStateGenetic(data,50,15,0.2,0.3)
  printSolution(data, sol, time)
  print("------------------------------------------------")

#menu to run the genetic generational algorithm
def geneticGenerationalMenu(data, fileSize):
  print("------------------------------------------------")
  print()
  print("             GENETIC GENERATIONAL               ")
  print()
  sol, time = generationalGenetic(data, 50, 15, 0.3)
  printSolution(data, sol, time)
  print("------------------------------------------------")

#menu to run the iterative local search algorithm
def iterativeLocalSearchMenu(data, fileSize):
  print("------------------------------------------------")
  print()
  print("           ITERATIVE LOCAL SEARCH               ")
  print()
  sol, time = ils(30, data)
  printSolution(data, sol, time)
  print("------------------------------------------------")

#menu to run the guided local search algorithm
def guidedLocalSearchMenu(data, fileSize):
  print("------------------------------------------------")
  print()
  print("             GUIDED LOCAL SEARCH                ")
  print()
  sol, time = gls(data, 10, -1000)
  printSolution(data, sol, time)
  print("------------------------------------------------")

#menu to run the tabu search algorithm
def tabuSearchMenu(data, fileSize):
  print("------------------------------------------------")
  print()
  print("                  TABU SEARCH                   ")
  print()
  sol, time = tabuSearchStatic(data,10)
  printSolution(data, sol, time)
  print("------------------------------------------------")

initialMenu()
file, size = fileOptions()
algorithmOptions(file, size)

