from itertools import permutations
import random

# Create input based on number of clauses and variables
def input_creation(amnt_clauses, amnt_variables):
    # Add both the negative and positive values of variables
    variables = [*range(1, amnt_variables + 1)] + [*range(-amnt_variables, 0)]
    clauses = list(permutations(variables, 2))
    all_clauses = []
    for clause in clauses:
        if abs(clause[0]) == abs(clause[1]):
            continue
        all_clauses.append(clause)

    # Print to a file with name corresponding to number of clauses, variables
    file_name = 'input_' + str(amnt_clauses) + '_' + str(amnt_variables) + '.txt'
    with open(file_name, 'w') as f:
        f.write(str(amnt_clauses) + ' ' + str(amnt_variables) + '\n')

        for i in range(amnt_clauses):
            random.seed()
            clause = random.choice(all_clauses)
            f.write(str(clause[0]) + ' ' + str(clause[1]) + '\n')


