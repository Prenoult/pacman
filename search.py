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
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
  
def breadthFirstSearch(problem):
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
  
def uniformCostSearch(problem):
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
  
def nullHeuristic(state, problem=None):
  """
  Heuristique triviale qui renvoie 0 tout le temps.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
