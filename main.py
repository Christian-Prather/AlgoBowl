import simulated_annealing
import exhaustive2
import input_creation
import process_output
import verification

TEMP = 2500
COOLING = 0.99
STEP_SIZE = 30
MIN_TEMP = 5


def main():
    # Generate File
    # input_creation.input_creation(25000,1000)
    print("AlgoBowl.......")
    global TEMP
    simulated_annealing.generate_start_state()
    # Not sure when to stop?
    while TEMP > MIN_TEMP:
        simulated_annealing.choose_next_node(TEMP, STEP_SIZE)
        TEMP *= COOLING
        print("TEMP:---------------------{}".format(TEMP))

    s = simulated_annealing.get_currentNode()
    print(s)
    variables = s[0]
    claim = s[1]
    process_output.process_output(claim, variables, "outputs/output_25000_1000.txt")
    print(verification.verification("inputs/input_25000_1000.txt", "outputs/output_25000_1000.txt"))
    # print("Exhaustive Comp......")
    # exhaustive2.exhaustive("inputs/input_100_10.txt")
    # print("Done")


if __name__ == "__main__":
    main()
