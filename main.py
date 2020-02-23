import simulated_annealing
import exhaustive2
import input_creation


TEMP = 2500
COOLING = 0.99
STEP_SIZE = 30
MIN_TEMP = 5
def main():
    #Generate File
    # input_creation.input_creation(25000,1000)
    print("AlgoBowl.......")
    global TEMP
    simulated_annealing.generate_start_state()
    # Not sure when to stop?
    while TEMP > MIN_TEMP:
        simulated_annealing.choose_next_node(TEMP, STEP_SIZE)
        TEMP *= COOLING
        print("TEMP:---------------------{}".format(TEMP))

    print(simulated_annealing.get_currentNode())
    # print("Exhaustive Comp......")
    # exhaustive2.exhaustive("inputs/input_100_10.txt")
    # print("Done")
if __name__== "__main__":
    main()