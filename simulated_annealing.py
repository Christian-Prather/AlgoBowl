# Utilize the simulated annealing method to find next selection
# This whole file should be structured as a class


import process_input
import random
import time
import math

variables, clauses = process_input.process_input("inputs/input_4_2.txt")
startState = []
currentNode = []
currentScore = 0

def generate_start_state():
    # Pick a random state
    global currentNode
    print("Running....")
    random.seed(time.time())
    for variable in range(variables):
        if random.random() > 0.5:
            startState.insert(variable, 'T')
        else:
            startState.insert(variable, 'F')
    print(*startState, sep = ", ")  
    currentNode = startState.copy()

def get_currentNode():
    return currentNode

# Loop through all nodes in neighbor and compute their funciton
# value for selection
# Choose random high probability state as next option
def choose_next_node(temp, stepSize):
    global currentNode
    acceptableWorseStates = []
    neigbors = generate_neighbor_nodes()
    for option in neigbors:
        #option = [T,F] etc
        potentialScore = check_clauses(option)
        if potentialScore > currentScore:
            # Always select this new state
            currentNode = option
            break
        else:
            loss = abs(currentScore - potentialScore)
            probability = math.exp(-(loss/temp))
            if (random.random() < probability):
                acceptableWorseStates.append(option)
    
    currentNode = acceptableWorseStates[random.randint(0, len(acceptableWorseStates) -1)]

# Varaible set = [T, F] etc...
def check_clauses(variableSet):
    score = 0
    for claus in clauses:
        # if solvable with vairable state add to score
        #return score
        pass
    return 0



def generate_neighbor_nodes():
# variables a list of t f for current state [T, T]
# variable is a sigle one
# neighbors = {['T', 'F'], ['F', 'T']}
    neighbors = []

    for i in range(len(currentNode)):
        # Get a copy of current node state
        neighbor = currentNode.copy()
        
        if neighbor[i] == 'T':
            # change it to F and dont touch the rest 
            neighbor[i] = 'F'
        else:
            neighbor[i] = 'T'
            
        # add to neigbors set
        #print("Neighbor: {}".format(neighbor))
        neighbors.append(neighbor)  
    print("Neighbors: {}".format(neighbors))
    return neighbors

   







