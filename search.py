"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
    """
     Returns the start state for the search problem 
     """
    util.raiseNotDefined()
    
  def isGoalState(self, state):
    """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
    util.raiseNotDefined()

  def getSuccessors(self, state):
    """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
    util.raiseNotDefined()

  def getCostOfActions(self, actions):
    """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
    util.raiseNotDefined()
    

def tinyMazeSearch(problem):
  """
  Retourne un sequence d'action pour le le probleme tinyMaze. 
  Ne marchera pas pour tout autre probleme.
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Pour commencer, je vous conseille de regarder ce que renvoient les fonctions
  suivantes pour bien comprendre en quoi consiste l'argument "problem": 
  
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
  #python pacman.py -l mediumMaze -p SearchAgent
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST
  t=[]
  result
  Nvisite=[]
  Nvisite.append(problem.getStartState())

  def rec(node,t,Nvisite):
    if problem.isGoalState(node):
      print node
      return 1
    else:
      pile = problem.getSuccessors(node)
      for v in pile:
        if v[0] not in Nvisite:
          Nvisite.append(v[0])
          print v
          bool = rec(v[0],t,Nvisite)
          if bool == 1:
            if v[1] == "West":
              t.append(w)
            elif v[1] == "North":
              t.append(n)
            elif v[1] == "South":
              t.append(s)
            else:
              t.append(e)
            return bool
      return 0

  vv = rec(problem.getStartState(),t,Nvisite)
  t.reverse()
  return t


  
def breadthFirstSearch(problem):
  file =[]
  file.append(problem.getStartState())
  nVisite = []
  nVisite.append(problem.getStartState())
  bool = 0
  result = []
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST

  n2 = problem.getStartState()
  tabP={}


  while len(file) !=0 and bool == 0:
    #node = file[len(file)-1]
    node = file[0]
    #print file
    #print node
    file.remove(node)
    for v in problem.getSuccessors(node):
      if v[0] not in nVisite and bool == 0:
        if problem.isGoalState(v[0]):
          bool = 1
          if v[1] == "West":
            result.append(w)
          elif v[1] == "North":
            result.append(n)
          elif v[1] == "South":
            result.append(s)
          else:
            result.append(e)
          tabP[v[0]]=node
          n2=node
          break
        else:
          tabP[v[0]] = node
          nVisite.append(v[0])
          file.append(v[0])

  #print n2
  #print "-----------"
  #print n2
  #print nVisite
  #print tabP
  #print node
  bool2 =0

  while bool2 == 0:
    if node != problem.getStartState():
      tmp = tabP[node]
      for v in problem.getSuccessors(tmp):
        if v[0] == node:
            node = tmp
            if v[1] == "West":
              result.append(w)
            elif v[1] == "North":
              result.append(n)
            elif v[1] == "South":
              result.append(s)
            else:
              result.append(e)
    else:
      bool2=1







  result.reverse()
  return result
  
def uniformCostSearch(problem):
  "*** YOUR CODE HERE ***"
  from util import PriorityQueue
  file = PriorityQueue()
  #print file.isEmpty()
  file.push(problem.getStartState(),0)
  #print file.isEmpty()
  bool = False
  #bool = True
  Nvisite = []
  Nvisite.append(problem.getStartState())
  tabP={}
  result = []

  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST

  while bool != True and file.isEmpty() != True:
    node = file.pop()
    #print node
    for v in problem.getSuccessors(node):
      if v[0] not in Nvisite:
        if problem.isGoalState(v[0]):
          bool = True
          if v[1] == "West":
            result.append(w)
          elif v[1] == "North":
            result.append(n)
          elif v[1] == "South":
            result.append(s)
          else:
            result.append(e)
        else:
          file.push(v[0],v[2])
        Nvisite.append(v[0])
        tabP[v[0]] = node





  bool2 = 0

  while bool2 == 0:
    if node != problem.getStartState():
      tmp = tabP[node]
      for v in problem.getSuccessors(tmp):
        if v[0] == node:
          node = tmp
          if v[1] == "West":
            result.append(w)
          elif v[1] == "North":
            result.append(n)
          elif v[1] == "South":
            result.append(s)
          else:
            result.append(e)
    else:
      bool2 = 1

  #print result
  result.reverse()
  return result

  
def nullHeuristic(state, problem=None):
  """
  Heuristique triviale qui renvoie 0 tout le temps.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "*** YOUR CODE HERE ***"
  from game import Directions
  from util import PriorityQueue
  s = Directions.SOUTH
  w = Directions.WEST
  n = Directions.NORTH
  e = Directions.EAST

  result = []
  Nvisite = []
  Nvisite.append(problem.getStartState())
  tabP = {}

  file = PriorityQueue()
  cout = 0 + heuristic(problem.getStartState(), problem)
  file.push(problem.getStartState(), cout)
  bool = False

  while bool != True and file.isEmpty() != True:
    node = file.pop()
    print node
    for v in problem.getSuccessors(node):
      if v[0] not in Nvisite:
        if problem.isGoalState(v[0]):
          bool = True
          #print v[0]
          #print node
          if v[1] == "West":
            result.append(w)
          elif v[1] == "North":
            result.append(n)
          elif v[1] == "South":
            result.append(s)
          else:
            result.append(e)
        else:
          cout = v[2]+heuristic(v[0],problem)
          file.push(v[0],cout)
        Nvisite.append(v[0])
        tabP[v[0]] = node

  bool2 = 0
  #print result
  while bool2 == 0:
    if node != problem.getStartState():
      tmp = tabP[node]
      for v in problem.getSuccessors(tmp):
        if v[0] == node:
          node = tmp
          if v[1] == "West":
            result.append(w)
          elif v[1] == "North":
            result.append(n)
          elif v[1] == "South":
            result.append(s)
          else:
            result.append(e)
    else:
      bool2 = 1

  #print result
  result.reverse()
  return result






  util.raiseNotDefined()
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
