import os
from tqdm import tqdm
import runner

INPUT_FOLDER = "group_inputs/"

def main():
    # Generate File
    # input_creation.input_creation(25000,1000)
    with os.scandir(INPUT_FOLDER) as files:
        with tqdm(total=len(os.listdir(INPUT_FOLDER))) as pbar:
            print("AlgoBowl.......")
            for file in tqdm(files):
                print(file.name)
                pbar.update(1)
                runner.runInput(file.name)
            

    


if __name__ == "__main__":
    main()
