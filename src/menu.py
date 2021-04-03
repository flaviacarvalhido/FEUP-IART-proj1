from HillClimbing import hillClim
from SimulatedAnnealing import simulatedAnnealing
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
  return file

# menu to choose the algorithm to run
def algorithmOptions(file):
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
      hillClimbingMenu(data)
      break
    elif option == 2:
      simulatedAnnealingMenu(data)
      break
    elif option == 3:
      geneticSteadyStateMenu(data)
      break
    elif option == 4: 
      geneticGenerationalMenu(data)
      break
    elif option == 5: 
      iterativeLocalSearchMenu(data)
      break
    elif option == 6:
      guidedLocalSearchMenu(data)
      break
    elif option == 7:
      tabuSearchMenu(data)
      break
    else: 
      print("Invalid input: Try again!")
      continue
  #print("------------------------------------------------")


# menu to run the hill climbing algorithm
def hillClimbingMenu(data):
  print("------------------------------------------------")
  print()
  print("                HILL CLIMBING                   ")
  print()
  hillClim(data)
  print("------------------------------------------------")

# menu to run the simulated annealing algorithm
def simulatedAnnealingMenu(data):
  print("------------------------------------------------")
  print()
  print("              SIMULATED ANNEALING               ")
  print()
  simulatedAnnealing(data)
  print("------------------------------------------------")

#menu to run the genetic steady state algorithm
def geneticSteadyStateMenu(data):
  print("------------------------------------------------")
  print()
  print("             GENETIC STEADY STATE               ")
  print()
  #chamar função
  print("------------------------------------------------")

#menu to run the genetic generational algorithm
def geneticGenerationalMenu(data):
  print("------------------------------------------------")
  print()
  print("             GENETIC GENERATIONAL               ")
  print()
  #chamar função
  print("------------------------------------------------")

#menu to run the iterative local search algorithm
def iterativeLocalSearchMenu(data):
  print("------------------------------------------------")
  print()
  print("           ITERATIVE LOCAL SEARCH               ")
  print()
  #chamar função
  print("------------------------------------------------")

#menu to run the guided local search algorithm
def guidedLocalSearchMenu(data):
  print("------------------------------------------------")
  print()
  print("             GUIDED LOCAL SEARCH                ")
  print()
  #chamar função
  print("------------------------------------------------")

#menu to run the tabu search algorithm
def tabuSearchMenu(data):
  print("------------------------------------------------")
  print()
  print("                  TABU SEARCH                   ")
  print()
  #chamar função
  print("------------------------------------------------")

initialMenu()
file = fileOptions()
algorithmOptions(file)

