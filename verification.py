import process_input


def verification(inputfile, outputfile):
    """
    checks whether the solution given in the output file satisfies the number of clauses in the input that it claims to
    :param clauses: the clauses to be checked. a list of tuples containing integers indicating whether the numbered
            variable should be set to true or set to false
    :param numvar: the number of distinct variables in the clauses
    :param outputfile: the name of the output file that contains the number of clauses claimed and what each distinct
            variable should be set to.
    :return: true if what the variables are set to satisfy the number of clauses as indicated at the top of the output
        file.
    """
    numvar, clauses = process_input.process_input(inputfile)

    with open(outputfile, 'r') as f:
        # set the first line of the output file to the claim
        # this is the number of clauses the solution claims to satisfy
        claim = int(f.readline())
        setvar = []
        # for each of the next lines corresponding to each of the variables, add them to the end of an array to keep
        # track of how they are set for the given claim
        for i in range(numvar):
            var = int(f.readline())
            setvar.append(var)

    count = 0
    for clause in clauses:
        if check_clause(setvar, clause):
            count += 1

    # since we are checking if the number of clauses satisfied by the solution is equal to the number of
    # clauses claimed to be satisfied, return this value as a boolean
    print(count)
    print(claim)
    return count == claim


def check_clause(setvar, clause):
    """
    checks a clause for if the set variables satisfy the clause
    :param setvar: a list of what each of the variables are set to
    :param clause: the clause to check truth for
    :return: true if the clause is satisfied and false if the clause is not satisfied
    """
    var1 = clause[0]
    var2 = clause[1]
    # if the variable in the current clause is positive, then set the first variable of the clause to
    # what it was set to in setvar. since the variables in the clause start numbering at one,
    # subtract one to get the index of that variable in the array
    if var1 > 0:
        first = setvar[var1 - 1]
    # if the variable in the clause is negative, then the opposite of what it was set to in setvar is what
    # should be checked in the clause. the index of the variable in the array can be checked by removing the
    # sign and subtracting one
    elif setvar[abs(var1) - 1] == 0:
        first = 1
    else:
        first = 0

    # the same logic that was applied to var1 to set the first half of the clause is applied to the second
    if var2 > 0:
        second = setvar[var2 - 1]
    elif setvar[abs(var2) - 1] == 0:
        second = 1
    else:
        second = 0

    # if the resulting first half or second half of the clause is true, then we add one to the count of
    # clauses that the given solution satisfies
    return first or second
