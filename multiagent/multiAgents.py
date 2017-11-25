# multiAgents.py
# --------------
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


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

from sets import Set

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        # returns as array of legal moves

        # print gameState

        # print legalMoves
        # print '-----'

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        # print action
        # print '----'
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        # raw_input('Press enter to continue..')
        # print 'best index : ', bestIndices
        # print '---------'
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best
        # print 'chosen index : ', chosenIndex
        # print 'legal move : ', legalMoves[chosenIndex]

        # "Add more of your code here if you want to"
        # sends a random move - line 61

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):

        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        
        # print currentGameState
        
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        # print 'successor game state : ', successorGameState
        # print 'new position : ', newPos
        # print 'new food : \n ', newFood
        # print 'new Ghost state : ', newGhostStates
        # print type(newFood)

        # "*** YOUR CODE HERE ***"
        # print newFood.width * newFood.height

        food_available_location = []
        food_location = []
        distance_pacman_ghost = 0
        food_distance = 0

        for ghost_state in newGhostStates:
          # calculate a heurtic based distance between the position of pacman to ghost(s)
            distance_pacman_ghost = manhattanDistance(newPos,ghost_state.getPosition())
            # if the distance between pacman and ghost is very close
            if (distance_pacman_ghost <= 1):
                return float("-inf")
        

        for i in range(0,newFood.width):
            for j in range(0,newFood.height):
                # check if the food pallets occurs
                if (newFood[i][j] == True):
                    location = (i,j)
                    # store the location in a tuple
                    food_available_location.append(location)

        # if no food is available - return infinte
        if len(food_available_location) == 0:
            return float("inf")
        
        # calculate a huristic based distance between the position of pacman to the food 
        for food_loc in food_available_location:
            # manhattan between position of pacman and food
            food_distance = manhattanDistance(newPos,food_loc)
            food_location.append(food_distance)
        
        # obtain the new number of 
        current_food_count = currentGameState.getNumFood()
        
        if (len(food_available_location) < current_food_count):
            return 1000
        
        score = 0

        # capture the smallest element in the food location array
        # score = (10*(1/min(food_location)))
        # if 1/min(food_location) is not considered - pacman ends up staying in one part of the maze for long
        # until a ghost comes nearby
        # score = 10*(1/min(food_location))
        # score = ((newFood.width * newFood.height) * (1/min(food_location)))

        score = len(food_available_location) * (1/min(food_location))
        # print 'Distance between Pacman to food : ', food_distance
        # print 'Distance between Pacman to ghost : ', distance_pacman_ghost
        # print 'Food available count : ', len(food_available_location)
        # print 'Score : ', score
        # print '---'
        return score


def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        # "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        
        # print self
        # print gameState
        # print gameState.getNumAgents()
        root_value = self.get_direction_to_move(gameState,0,self.index)
        # action = root_value[1]
        return root_value[1]


    def get_direction_to_move(self,gameState,CurrentDepth,agentIndex):
        # print "getNumAgents : ",gameState.getNumAgents()
        # print "gameState : ", gameState # instance
        # print "CurrentDepth : ",CurrentDepth
        # print "agentIndex : ",agentIndex
        # print "-----------------"
        if agentIndex == gameState.getNumAgents():
            CurrentDepth = CurrentDepth + 1
            agentIndex = agentIndex = 0
            
        legal_action = []
        legal_action = gameState.getLegalActions(agentIndex)
        
        if len(legal_action) == 0:
            eval_value =  self.evaluationFunction(gameState)
            print '0'
            return [eval_value]
        
        if CurrentDepth == self.depth:
            eval_value =  self.evaluationFunction(gameState)
            print self.depth
            return [eval_value]
        
        if agentIndex == 0:
            # defining another method to obtain max
            # Bug: Suboptimal moves ? (not sure where)
            # Student Move:['Stop']
            # Optimal Move:East
            node = [-float("inf")]
            actions = []
            actions = gameState.getLegalActions(agentIndex)
            for each_action in actions:
                next_state = gameState.generateSuccessor(agentIndex, each_action)
                # print self.get_direction_to_move()
                successor_evalvalue = self.get_direction_to_move(next_state, CurrentDepth, agentIndex + 1)
                successor_evalvalue = successor_evalvalue[0]
                if (successor_evalvalue >= node[0]):
                    node = [successor_evalvalue,each_action]
            return node
        else:
            # defining another method to obtain min
            # Bug: Suboptimal moves ? (not sure where)
            # Bug resolved - was not passing the successor_eval
            # Student Move:['Stop']
            # Optimal Move:East
            node = [float("inf")]
            action_list = []
            action_list = gameState.getLegalActions(agentIndex)
            for each_action in action_list:
                next_state = gameState.generateSuccessor(agentIndex, each_action)
                successor_evalvalue = self.get_direction_to_move(next_state, CurrentDepth, agentIndex + 1)
                successor_evalvalue = successor_evalvalue[0]
                if (successor_evalvalue <= node[0]):
                    node = [successor_evalvalue,each_action]
            return node



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
      Your minimax agent with alpha-beta pruning (question 3)
    """
        

    def get_value(self,gameState,CurrentDepth,agentIndex,alpha,beta):
        # print "gameState : ", gameState
        # print "CurrentDepth : ", CurrentDepth
        # print "------------------"
        if agentIndex == gameState.getNumAgents():
            CurrentDepth = CurrentDepth + 1
            agentIndex = agentIndex = 0
        
        if CurrentDepth == self.depth:
            eval_value =  self.evaluationFunction(gameState)
            return [eval_value]
        
        legal_action = []
        legal_action = gameState.getLegalActions(agentIndex)
        
        if len(legal_action) == 0:
            eval_value =  self.evaluationFunction(gameState)
            return [eval_value]
        
        if agentIndex == 0:
            node = [-float("inf")]
            action_list = []
            action_list = gameState.getLegalActions(agentIndex)
            for action in action_list:
                successor_state = gameState.generateSuccessor(agentIndex, action)
                successor_evalvalue = self.get_value(successor_state, CurrentDepth, agentIndex + 1,alpha,beta)
                successor_evalvalue = successor_evalvalue[0]
                if (successor_evalvalue >= node[0]):
                    node = [successor_evalvalue,action]
                max_value = node[0]
                if max_value > beta:
                    return node
                alpha = max(max_value,alpha)
            return node
        else:
            node = [float("inf")]
            action_list = []
            action_list = gameState.getLegalActions(agentIndex)
            for action in action_list:
                successor_state = gameState.generateSuccessor(agentIndex, action)
                successor_evalvalue = self.get_value(successor_state, CurrentDepth, agentIndex + 1,alpha,beta)
                successor_evalvalue = successor_evalvalue[0]
                if (successor_evalvalue <= node[0]):
                    node = [successor_evalvalue,action]
                min_value = node[0]
                if min_value < alpha:
                    return node
                beta = min(min_value,beta)
            return node


    def getAction(self, gameState):
        """
          Returns the minimax action using self.depth and self.evaluationFunction
        """
        # "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        value = self.get_value(gameState,0,self.index,-float("inf"),float("inf"))
        return value[1]


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        # "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        value = self.value(gameState,0,self.index)
        return value[1]
        
    def value(self, gameState, CurrentDepth, agentIndex):
        if agentIndex == gameState.getNumAgents():
            CurrentDepth = CurrentDepth + 1
            agentIndex = agentIndex = 0
        legal_action = []
        legal_action = gameState.getLegalActions(agentIndex)
        
        if len(legal_action) == 0:
            eval_value =  self.evaluationFunction(gameState)
            return [eval_value]

        if CurrentDepth == self.depth:
            eval_value =  self.evaluationFunction(gameState)
            return [eval_value]
        
        if agentIndex == 0:
            node_value = [-float("inf")]
            action_possible = []
            action_possible = gameState.getLegalActions(agentIndex)
            for action in action_possible:
                successor_state = gameState.generateSuccessor(agentIndex, action)
                successor_evalvalue = self.value(successor_state, CurrentDepth, agentIndex + 1)
                successor_evalvalue = successor_evalvalue[0]
                if (successor_evalvalue >= node_value[0]):
                    node_value = [successor_evalvalue,action]
            return node_value
        else:
            node_value = [float("inf")]
            action_list = []
            action_list = gameState.getLegalActions(agentIndex)
            for action in action_list:
                successor_state = gameState.generateSuccessor(agentIndex, action)
                successor_evalvalue = self.value(successor_state, CurrentDepth, agentIndex + 1)
                successor_evalvalue = successor_evalvalue[0]
                if (successor_evalvalue <= node_value[0]):
                    node_value = [successor_evalvalue,action]
            return node_value



def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function (question 5).

      DESCRIPTION: <write something here so we know what you did>
    """
    # "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()
    food_count = currentGameState.getNumFood()
    
    if food_count == 0:
        return float("inf")
    
    dist_from_ghost = 0
    
    current_ghost_state = currentGameState.getGhostStates()
    new_pos = currentGameState.getPacmanPosition()
    new_food = currentGameState.getFood()
        
    for ghostState in current_ghost_state:
        dist_from_ghost = manhattanDistance(new_pos,ghostState.getPosition())
        if (dist_from_ghost <= 1):
            return float("-inf")
        
    food_available = []
    food_data = []
    food_distance = 0
    
    for i in range(0,new_food.width):
        for j in range(0,new_food.height):
            if (new_food[i][j] == True):
                food_location = (i,j)
                food_available.append(food_location)
                
    for food_loc in food_available:
        food_distance = manhattanDistance(new_pos,food_loc)
        food_data.append(food_distance)
    
    closest_food_dist = min(food_data)
        
    score = 0
    
    score = (10*(-closest_food_dist)+(100*(-food_count)))
    
    return score

# Abbreviation
better = betterEvaluationFunction

