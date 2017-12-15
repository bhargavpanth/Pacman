# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"

        states = mdp.getStates()
        # val = util.Counter()
        val = self.values.copy()
        i = 0
        
        for i in range(iterations):
          for each_state in states:
            optimum_reward = 0
            actions = mdp.getPossibleActions(each_state)

            for each_action in actions:
              reward = 0
              for each_transition in self.mdp.getTransitionStatesAndProbs(each_state, each_action):
                reward += each_transition[1] * self.mdp.getReward(each_state, each_action, each_transition[0]) + self.discount * self.values[each_transition[0]]
                # print 'Op reward : ', optimum_reward
                # print 'Reward : ', reward
                
              optimum_reward = max(optimum_reward, reward)
              # optimum_reward = max(optimum_reward, each_state)
          self.values[each_state] = val[each_state]

          #


    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """

        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"


        # util.raiseNotDefined()
        ##
        ## Utility value - qval + (prob * (reward + (discount * utility)))
        ##

        q_value = 0
        for each_transition in self.mdp.getTransitionStatesAndProbs(state, action):
          # print each_transition
          prob = each_transition[1]
          state_ = each_transition[0]
          # calculate reward
          reward = self.mdp.getReward(state, action, state_)
          q_value += prob*(reward + self.discount * self.values[state_])

        return q_value



    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        "*** YOUR CODE HERE ***"
        # util.raiseNotDefined()
        # print self.actions
        # print '----'

        optimal_Q = -1
        action = None
        for each_action in self.mdp.getPossibleActions(state):
          q_value = self.getQValue(state, each_action)
          # while (True):
          if (q_value >= optimal_Q):
            # print type(action)
            action = each_action
            
        
        return action


    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
