def spiralize(size, n=1):
    """ Your code goes somewhere in here"""
    n = 1
    adder = 0
    rome = 2
    totl = 0

    while n <= size ** 2:
        totl += 1
        n += rome
        adder += 1
        if adder == n:
            rome += 2
            adder = 0
    return totl

    return_value = n
    return return_value
