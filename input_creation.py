from itertools import permutations
import random

def input_creation(amnt_clauses, amnt_variables):
    variables = [*range(1, amnt_variables + 1)] + [*range(-amnt_variables, 0)]
    all_clauses = list(permutations(variables, 2))

    file_name = 'input_' + str(amnt_clauses) + '_' + str(amnt_variables) + '.txt'
    with open(file_name, 'w') as f:
        f.write(str(amnt_clauses) + ' ' + str(amnt_variables) + '\n')

        clauses = random.choices(all_clauses, k=amnt_clauses)
        for clause in clauses:
            f.write(str(clause[0]) + ' ' + str(clause[1]) + '\n')
