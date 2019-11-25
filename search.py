# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """

        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions

    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]




def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """


    "*** YOUR CODE HERE ***"
    st = util.Stack()
    strt = problem.getStartState()
    st.push(strt)  
    visited = []
    came_from ={}
    came_from [strt] =(None,None)

    while not st.isEmpty():
        state = st.pop()
        visited.append(state)
        if problem.isGoalState(state) :
            break
        nodes = problem.getSuccessors(state)
        for (successor,action,cost) in nodes:
            if successor not in visited :
                st.push(successor)
                came_from[successor] = (state , action)    
            
    # exit while
    actions = []
    while(state != strt) :
        (parent,action) =came_from[state]
        state = parent
        actions.append(action)
    actions.reverse()
    return actions
      


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    st = util.Queue()
    strt = problem.getStartState()
    st.push(strt)  
    visited = []
    came_from ={}
    came_from [strt] =(None,None)

    while not st.isEmpty():
        state = st.pop()
        visited.append(state)
        if problem.isGoalState(state) :
            break
        nodes = problem.getSuccessors(state)
        for (successor,action,cost) in nodes:
            if successor not in visited :
                st.push(successor)
                came_from[successor] = (state , action)    
            
    # exit while
    actions = []
    while(state != strt) :
        (parent,action) =came_from[state]
        state = parent
        actions.append(action)
    actions.reverse()
    return actions



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    pq = util.PriorityQueue()
    startState = problem.getStartState()
    pq.push(("", None, startState), 0)
    # moves[state] returns (dir, parent) the direction and the parent from which this state was reached
    moves = {}
    # Current cost to reach this state
    stateCost = {startState: 0}
    goalState = None
    while not pq.isEmpty():
        (move, parent, currentState) = pq.pop()
        if currentState in moves:  # already visited
            continue
        moves[currentState] = (move, parent)
        if problem.isGoalState(currentState):  # Found goal state
            goalState = currentState
            break
        children = problem.getSuccessors(currentState)
        for successor, action, cost in children:
            if successor not in stateCost or stateCost[successor] > stateCost[currentState] + cost:
                pq.push((action, currentState, successor), stateCost[currentState] + cost)
                stateCost[successor] = stateCost[currentState] + cost

    currentState = goalState
    path = []
    while currentState != startState:
        (move, parent) = moves[currentState]
        path.append(move)
        currentState = parent
    path.reverse()
    return path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    pq = util.PriorityQueue()
    start = problem.getStartState()
    pq.push(start,heuristic(start,problem))
    cost_so_far = {}
    cost_so_far[start] = 0
    came_from = {}
    came_from[start] = (None,None)
    actions =[]

    while not pq.isEmpty() :
        current=pq.pop()
        if problem.isGoalState(current) :
            break
        neighbours = problem.getSuccessors(current)
        for (next,action,cost) in neighbours :
            new_cost = cost_so_far[current] + cost
            if next not in cost_so_far or new_cost < cost_so_far[next] :
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(next,problem)
                pq.push(next, priority)
                came_from[next] = (current,action)

    # exiting the while loop when current == goalstate , now time to trace back !
    while current != start :
        parent,action = came_from[current]
        actions.append(action)
        current = parent
    actions.reverse()    
    return  actions

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch


