"""
implement n-step SARSA
basic reward function
    essentially just a completed function
    basic dumbbell structure
"""

"""
Adjacency Matrix (Input)
1 <-> 2 <-> 3
1: [2]
2: [1,3]
3: [2]

then

1 <-> 2 <-> 3
1: [(2, 0, 0)]
2: [(1,0, 0), ( 3,0, 0)]
3: [(2, 0, 0)]

if 1 and 3 had an entanglement, then:

1: [(2, 0, 0), (3, 1, 1)]
2: [(1,0), (3,0)]
3: [(2, 0), (1, 1, 1)]

OR we could represent nodes as objects

node1: [ (node2 , stateConnection , age)]
"""
# Potential Idea ####
class Node:
    def __init__(self, name, connections):
        self.name = name # Which node it is (i.e. node 1, 2 or A e.c.t.)
        self.connections = [connections] # Nodes it's connected too
        pass
    
    def generateEntanglements(self, name):  
        pass
        
class Link:
    def __init__(self, node1, node2, state = 0):
        self.node1 = node1
        self.node2 = node2
        self.state = state
        pass
    
    def generateEntanglements(self):
        pass
    def destroyEntanglement(self):
        # Need to destroy all related entanglements
        pass
        
################################################


class Env():
    def ___init__(self):
        self.topology = None # Holds the main topology 
        self.currentStates = None # Convert topology into
        pass
    
    def reset(self):         # Reset the environment to the original topology
        self.currentStates = None # Reset this to nothing.
        pass

    def isEndToEndEntanglement():  # TODO - How to work for multiple users?
        pass


def nStepSARSA(env: Env, numEpisodes: int, n: int):
    for episode in range(numEpisodes):
        pass


"""
In on-policy learning, the 𝑄(𝑠,𝑎)
 function is learned from actions that we took using our current policy 𝜋(𝑎|𝑠)
.
In off-policy learning, the 𝑄(𝑠,𝑎)
 function is learned from taking different actions (for example, random actions). We don't even need a policy at all!



"""