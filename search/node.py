# Defining a class Node
## Storing the current state of a node - the list of directions that need to be followed (start state) to (current state) - specific problem in which the node will be used.

class Node():

    def __init__(self, state, path, cost=0, heuristic=0, problem=None):
        self.state = state
        self.path = path
        self.cost = cost
        self.heuristic = heuristic
        self.problem = problem

    def get_next_node(self, heuristicFunction=None):
        children_node = []
        print self.problem.getSuccessors
        for next_node in self.problem.getSuccessors(self.state):
            state = next_node[0]
            path = list(self.path)
            path.append(next_node[1])
            cost = self.cost + next_node[2]
            if heuristicFunction:
                heuristic = heuristicFunction(state, self.problem)
            else:
                heuristic = 0
            node = Node(state, path, cost, heuristic, self.problem)
            children_node.append(node)
        return children_node