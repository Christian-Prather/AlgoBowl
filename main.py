import simulated_annealing
TEMP = 2000
COOLING = 0.99
STEP_SIZE = 2

def main():
    print("AlgoBowl.......")
    global TEMP
    simulated_annealing.generate_start_state()
   
    # Not sure when to stop?
    for i in range(5):
        simulated_annealing.choose_next_node(TEMP, STEP_SIZE)
        TEMP *= COOLING

    print(simulated_annealing.get_currentNode())
if __name__== "__main__":
    main()