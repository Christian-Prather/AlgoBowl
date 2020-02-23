from itertools import permutations
import process_input
import process_output

def exhaustive(input_file):
    """
    goes through every possible combination of variables (true or false) to find the ideal
    solution with the greatest number satisfied
    """
    
    result = process_input.process_input(input_file)
    variables = result[0]
    clauses = result[1]

    # Find all possible solutions depending on number of variables
    # ex. 2 variables provides [0, 0], [0, 1], etc.
    solution_set = [1] * variables + [0] * variables
    solutions = set(permutations(solution_set, variables))

    greatest_satisfied = -1
    ideal_solution = []
    
    for solution in solutions:
        satisfied = 0
        for clause in clauses:
            temp_clause = []
            for variable in clause:
                if solution[abs(variable) - 1] == 1:
                    if variable < 0:
                        temp_clause.append(0)
                    else:
                        temp_clause.append(1)
                else:
                    if variable < 0:
                        temp_clause.append(1)
                    else:
                        temp_clause.append(0)
            
            if temp_clause[0] == 1 or temp_clause[1] == 1:
                satisfied += 1
        
        if satisfied > greatest_satisfied:
            greatest_satisfied = satisfied
            ideal_solution = solution

    # Put results into output file
    process_output.process_output(greatest_satisfied, ideal_solution, 'output.txt')
