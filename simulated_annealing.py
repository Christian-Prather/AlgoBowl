# Utilize the simulated annealing method to find next selection
# This whole file should be structured as a class


import process_input
import random
import time
import math
import verification

variables = 0
clauses =0 
startState = []
currentNode = []
currentScore = 0

def initialSetup(inputFile):
    global startState
    global currentNode
    global currentScore
    global variables
    global clauses

    variables = 0
    clauses =0 
    startState.clear()
    currentNode.clear()
    currentScore = 0


    variables, clauses = process_input.process_input("group_inputs/"+ inputFile)
    generate_start_state()




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
    return currentNode, currentScore

def convert(varSet):
    conversion = []
    for variable in varSet:
        if variable == 'T':
            conversion.append(1)
        else:
            conversion.append(0)
    return conversion
# Loop through all nodes in neighbor and compute their funciton
# value for selection
# Choose random high probability state as next option
def choose_next_node(temp, stepSize):
    global currentNode
    global currentScore

    acceptableWorseStates = []
    neigbors = generate_neighbor_nodes(stepSize)
    for option in neigbors:
        #option = [T,F] etc
        conversion = convert(option)
        #print(conversion)
        potentialScore = check_clauses(conversion)
        if potentialScore > currentScore:
            currentScore = potentialScore
            # Always select this new state
            currentNode = option
            return 0
        else:
            loss = abs(currentScore - potentialScore)
            probability = math.exp(-(loss/temp))
            # print ("Loss: {} Probability: {}".format(loss, probability))
            if (random.random() < probability):
                acceptableWorseStates.append(option)
 
    if len(acceptableWorseStates) > 0:
        currentNode = acceptableWorseStates[random.randint(0, len(acceptableWorseStates) -1)]
        # TODO: clp 2-21 Fix this store it dont just recalculate it
        currentNodeConversion = convert(currentNode)
        currentScore = check_clauses(currentNodeConversion)
        #print(currentScore)

# Variable set = [T, F] etc...
def check_clauses(variableSet):
    # Map into 1 T 0 False for Validation
    score = 0
    for clause in clauses:
        score += verification.check_clause(variableSet, clause)
    return score

def generate_neighbor_nodes(stepSize):
# variables a list of t f for current state [T, T]
# variable is a sigle one
# neighbors = random adjustment of variables
    neighbors = []
    for i in range(stepSize):
        neighbor = currentNode.copy()
        randomIndex = random.randint(0, len(currentNode)-1)
        if neighbor[randomIndex] == 'T':
            neighbor[randomIndex] = 'F'
        else:
            neighbor[randomIndex] = 'T'
        neighbors.append(neighbor)

    # for i in range(len(currentNode)):
    #     # Get a copy of current node state
    #     neighbor = currentNode.copy()
        
    #     if neighbor[i] == 'T':
    #         # change it to F and dont touch the rest 
    #         neighbor[i] = 'F'
    #     else:
    #         neighbor[i] = 'T'
    #     neighbors.append(neighbor)  
    return neighbors

   







