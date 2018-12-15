# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

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
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    state = problem.getStartState()  # A variable that is more convenient to write state
    get = list()    # Get the information of the next step
    filo = util.Stack()    # A variable that is more convenient to write stack
    record = list()    # Record the path that we had go through

    filo.push((state, [], 0))   # Push in the initial state
    while not filo.isEmpty():   # While stack isn't empty

          # Pop and get three variables (walk to the position)
        (pos, direction, cost) = filo.pop()
        if pos in record:
            continue
        record.append(pos)    # Append position into record
          # Get the information of the successors
        get = problem.getSuccessors(pos)

        for i in get:    # Variable i will go through all list(get)
            if problem.isGoalState(i[0]):    # If the successor is goal
                print("GOAL!!")
                # Return the path as for the actions
                return (direction + [i[1]])
            else:
                if i[0] not in record:    # If the successor isn't in the record
                    # Push the successor into stack
                    filo.push((i[0], direction + [i[1]], i[2] + cost))
                else:    # If the successor is in the record
                    continue    # Continue for the next successor
    if filo.isEmpty():    # If stack is error
        print("ERROR! The Stack is empty.")
        return 0

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    "Search the shallowest nodes in the search tree first. [p 81]"
    "*** YOUR CODE HERE ***"

    state = problem.getStartState()  # a variable that is more convenient to write state
    get = list()    # get the information of the next step
    fifo = util.Queue()    # a variable that is more convenient to write queue
    record = list()    # record the path that we had go through

    fifo.push((state, [], 0))    # Push in the initial state
    while not fifo.isEmpty():   # While queue isn't empty

          # Pop and get three variables (walk to the position)
        (pos, direction, cost) = fifo.pop()
        if pos in record:
            continue
        record.append(pos)    # Append position into record
          # Get the information of the successors
        get = problem.getSuccessors(pos)

        for i in get:    # Variable i will go through all list(get)
            if problem.isGoalState(i[0]):    # If the successor is goal
                print("GOAL!!")
                # Return the path as for the actions
                return (direction + [i[1]])
            else:
                if i[0] not in record:    # If the successor isn't in the record
                    # Push the successor into queue
                    fifo.push((i[0], direction + [i[1]], i[2] + cost))
                else:     # If the successor is in the record
                    continue    # Continue for the next successor
    if fifo.isEmpty():    # If queue is error
        print("ERROR! The Queue is empty.")
        return 0
    util.raiseNotDefined()

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"

    state = problem.getStartState()  # A variable that is more convenient to write state
    get = list()    # Get the information of the next step
    priorfifo = util.PriorityQueue()    # To implement PriorityQueue
    record = list()    # record the position we've been through

    priorfifo.push((state, [], 0),0)    # Push in the initial state
    while not priorfifo.isEmpty():   # While PriorityQueue isn't empty

          # Pop and get three variables (walk to the position)
        (pos, direction, cost) = priorfifo.pop()
        if pos in record:
            continue
        record.append(pos)    # Append position into record
          # Get the information of the successors
        get = problem.getSuccessors(pos)

        for i in get:    # Variable i will go through all list(get)
            if problem.isGoalState(i[0]):    # If the successor is goal
                print("GOAL!!")
                  # Return the path as for the actions
                return (direction + [i[1]])
            else:
                if i[0] not in record:
                    # Estimate the cost to the next position
                    priority = i[2] + cost + heuristic(pos, problem)
                    # push the successors into PriorityQueue
                    priorfifo.push((i[0], direction + [i[1]], i[2] + cost), priority)
                else:           # If the successor is in the record
                    continue    # Continue for the next successor
    if priorfifo.isEmpty():    # If PriorityQueue is error
        print("ERROR! The Queue is empty.")
        return 0

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
