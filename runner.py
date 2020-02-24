import simulated_annealing
import verification
import process_output

TEMP = 2500
COOLING = 0.99
STEP_SIZE = 30
MIN_TEMP = 5

def runInput(inputFile):
    print("Running " + inputFile)
    global TEMP

    simulated_annealing.initialSetup(inputFile)
    while TEMP > MIN_TEMP:
        simulated_annealing.choose_next_node(TEMP, STEP_SIZE)
        TEMP *= COOLING
        # print("TEMP:---------------------{}".format(TEMP))
    s = simulated_annealing.get_currentNode()
    print(s)
    variables = s[0]
    claim = s[1]
    process_output.process_output(claim, variables, "group_outputs/output_" + inputFile)
    print(verification.verification("group_inputs/" + inputFile, "group_outputs/output_" + inputFile))


