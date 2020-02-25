import os
from tqdm import tqdm
import runner
import exhaustive2
import verification
import process_input

INPUT_FOLDER = "group_inputs/"


def main():
    # # Generate File
    # # input_creation.input_creation(25000,1000)
    # with os.scandir(INPUT_FOLDER) as files:
    #     with tqdm(total=len(os.listdir(INPUT_FOLDER))) as pbar:
    #         print("AlgoBowl.......")
    #         for file in tqdm(files):
    #             print(file.name)
    #             pbar.update(1)
    #             runner.runInput(file.name)

    runner.runInput("input_group181.txt")

    # print(verification.verification("group_inputs/input_group162.txt", "best_group_outputs/output_input_group162.txt"))
    # print(verification.verification("group_inputs/input_group163.txt", "best_group_outputs/output_input_group163.txt"))
    # print(verification.verification("group_inputs/input_group164.txt", "best_group_outputs/output_input_group164.txt"))
    # print(verification.verification("group_inputs/input_group165.txt", "best_group_outputs/output_input_group165.txt"))
    # print(verification.verification("group_inputs/input_group167.txt", "best_group_outputs/output_input_group167.txt"))
    # print(verification.verification("group_inputs/input_group168.txt", "best_group_outputs/output_input_group168.txt"))
    # print(verification.verification("group_inputs/input_group169.txt", "best_group_outputs/output_input_group169.txt"))
    # print(verification.verification("group_inputs/input_group170.txt", "best_group_outputs/output_input_group170.txt"))
    # print(verification.verification("group_inputs/input_group171.txt", "best_group_outputs/output_input_group171.txt"))
    # print(verification.verification("group_inputs/input_group172.txt", "best_group_outputs/output_input_group172.txt"))
    # print(verification.verification("group_inputs/input_group173.txt", "best_group_outputs/output_input_group173.txt"))
    # print(verification.verification("group_inputs/input_group174.txt", "best_group_outputs/output_input_group174.txt"))
    # print(verification.verification("group_inputs/input_group175.txt", "best_group_outputs/output_input_group175.txt"))
    # print(verification.verification("group_inputs/input_group176.txt", "best_group_outputs/output_input_group176.txt"))
    # print(verification.verification("group_inputs/input_group177.txt", "best_group_outputs/output_input_group177.txt"))
    # print(verification.verification("group_inputs/input_group178.txt", "best_group_outputs/output_input_group178.txt"))
    # print(verification.verification("group_inputs/input_group180.txt", "best_group_outputs/output_input_group180.txt"))
    # print(verification.verification("group_inputs/input_group181.txt", "best_group_outputs/output_input_group181.txt"))
    # print(verification.verification("group_inputs/input_group183.txt", "best_group_outputs/output_input_group183.txt"))


if __name__ == "__main__":
    main()
