def process_input(filename):
    """
    processes an input file for the algobowl problem to be usable in finding a result
    assumes proper formatting of the file
    :param filename: file name of the input file to process of the correct format for the algobowl problem
    :return: a tuple whose first element is the number of variables and whose second element is a list of tuples
            containing the m clauses from the input file
    """
    with open(filename, 'r') as f:
        firstline = f.readline().split(" ")
        m = int(firstline[0])
        n = int(firstline[1])
        clauses = []
        for i in range(m):
            line = f.readline().split()
            clause = (int(line[0]), int(line[1]))
            clauses.append(clause)
        result = (n, clauses)
    return result