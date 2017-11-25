def value(self,gameState,CurrentDepth,agentIndex):
        print "agentIndex : ", agentIndex
        print "getNumAgents : ", gameState.getNumAgents()
        print "CurrentDepth : ", CurrentDepth
        print '--------------------'
        # exit(0)
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
            # maximum value
            node = [-float("inf")]
            action_possible = []
            action_possible = gameState.getLegalActions(agentIndex)
            for action in action_possible:
                successor_state = gameState.generateSuccessor(agentIndex, action)
                successor_evalvalue = self.value(successor_state, CurrentDepth, agentIndex + 1)
                successor_evalvalue = successor_evalvalue[0]
                if (successor_evalvalue >= node[0]):
                    node = [successor_evalvalue,action]
            # print node
            # print '---'
            return node
        else:
            # minimum value
            node = [-float("inf")]
            action_list = []
            action_list = gameState.getLegalActions(agentIndex)
            for action in action_list:
                successor_state = gameState.generateSuccessor(agentIndex, action)
                successor_evalvalue = self.value(successor_state, CurrentDepth, agentIndex + 1)
                successor_evalvalue = successor_evalvalue[0]
                if (successor_evalvalue <= node[0]):
                    node = [successor_evalvalue,action]
            return node

# return self.min(gameState,CurrentDepth,agentIndex)
def max(self,gameState,CurrentDepth,agentIndex):
        node = [-float("inf")]
        actions = []
        actions = gameState.getLegalActions(agentIndex)
        # print actions
        # print '-- -- possible actions -- --'
        for each_action in actions:
            next_state = gameState.generateSuccessor(agentIndex, each_action)
            successor_evalvalue = self.get_direction_to_move(next_state, CurrentDepth, agentIndex + 1)
            successor_evalvalue = successor_evalvalue[0]
            if (successor_evalvalue >= node[0]):
                node = [successor_evalvalue,each_action]
        return node
    

# return self.max(gameState,CurrentDepth,agentIndex)
    def min(self,gameState,CurrentDepth,agentIndex):
        node_value = [float("inf")]
        actions = []
        actions = gameState.getLegalActions(agentIndex)
        for each_action in actions:
            next_state = gameState.generateSuccessor(agentIndex, each_action)
            successor_evalvalue = self.get_direction_to_move(next_state, CurrentDepth, agentIndex + 1)
            successor_evalvalue = successor_evalvalue[0]
            if (successor_evalvalue <= node_value[0]):
                node_value = [successor_evalvalue,each_action]
        return node_value