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

from node import Node


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

    def getCostOfActions(self, actions, heuristicFunction=None):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        print actions
        print '-----'
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

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
    # "*** YOUR CODE HERE ***"
    # print type(problem)
    # print problem
    # (5,5)
    # print problem.getStartState()
    # -------
    # close set is used to keep track of all visited nodes
    close = set()
    # define a fringe -  stack
    fringe = util.Stack()
    # start - instance of Node
    # problem.getStartState() - returns the coordinates of the state of Pacman
    ## Node is from the class Node - import from node - implemented in node.py
    start = Node(problem.getStartState(), [], 0, 0, problem)
    # push the start node on to the stack
    fringe.push(start)
    # print fringe.display()
    while True:
        if fringe.isEmpty():
            return False
        # pop the first node from the fringe
        node = fringe.pop()
        # if the problem is at goalState - return path
        if problem.isGoalState(node.state):
            return node.path
        # if the node is not in close set - add the node to the close set
        if node.state not in close:
            close.add(node.state)
            # expand the child node of the node - add the the nodes in the fringe
            for child_node in node.get_next_node():
                fringe.push(child_node)

    print getattr(close)
    # [method_name for method_name in dir(close) if callable(getattr(close, method_name))]
    # print close
    # util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # "*** YOUR CODE HERE ***"
    # BFS - fringe is a Queue
    close = set()
    fringe = util.Queue()

    # print problem.getStartState()
    # Assign the start node 
    start_node = Node(problem.getStartState(), [], 0, 0, problem)
    # push onto the queue (fringe)
    fringe.push(start_node)

    while True:
        # if the fringe is empty - terminate
        if fringe.isEmpty():
            return False
        node = fringe.pop()
        # if the current state = goal - return the path to the goal state
        if problem.isGoalState(node.state):
            return node.path
        # if state not present in close set - add the node state to close set
        # push every child_node into the fringe
        # print close
        if node.state not in close:
            close.add(node.state)
            for child_node in node.get_next_node():
                fringe.push(child_node)
    
    # util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    # "*** YOUR CODE HERE ***"
    # close set is a way to keep track of all visited nodes
    close = set()
    # UCS - fringe is a Priority Queue
    fringe = util.PriorityQueue()
    # assign startnode
    start_node = Node(problem.getStartState(), [], 0, 0, problem)
    # pushing - < node, cost >
    print start_node
    print start_node.cost
    # push the first node and it's cost on the fringe
    fringe.push(start_node, start_node.cost)

    while True:
        # if the fringe is empty - No more nodes to visit
        if fringe.isEmpty():
            return False
        # pull out the first node from the fringe
        node = fringe.pop()
        # if the node is the goal - return the path
        if problem.isGoalState(node.state):
            return node.path
        # if state is not in the close set - add to close
        if node.state not in close:
            close.add(node.state)
            # expand the child node of the node - and add the node to the fringe
            for child_node in node.get_next_node():
                fringe.push(child_node, child_node.cost)


    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # "*** YOUR CODE HERE ***"

    # create a fringe - priority queue + empty set
    # assign start node
    # push start node + cost to the fringe
    # start popping the fringe - and check if the state of node is the goal
    # if yes : return the node path
    # if state not available in close set - add the node   

    # A* - fringe is a PriorityQueue
    close = set()
    fringe = util.PriorityQueue()
    start_node = Node(problem.getStartState(), [], 0, 0, problem)
    fringe.push(start_node, start_node.cost + start_node.heuristic)

    while True:
        # if fringe empty - terminate
        if fringe.isEmpty():
            return False
        # pop one node from the fringe
        node = fringe.pop()
        print node.state
        print node.path
        print '-------'
        ## f(n) = g(n) + h(n)
        ## For Astar search - the computation function for considering the path is the sum of actual cost + heuristic cost
        # if the node is already in goalstate - return path
        if problem.isGoalState(node.state):
            return node.path
        # if node state is not in close set - add node.state onto the close set
        if node.state not in close:
            close.add(node.state)
            # expand all nodes and add the f(n) cost inside the fringe
            for child_node in node.get_next_node(heuristic):
                fringe.push(child_node, child_node.cost + child_node.heuristic)


    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
