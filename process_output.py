def process_output(clauses_satisfied, setvar, filename):
    """

    :param clauses_satisfied:
    :param setvar:
    :return:
    """
    with open(filename, 'w+') as f:
        f.write(str(clauses_satisfied))
        for var in setvar:
            f.write('\n')
            f.write(str(var))
    return
