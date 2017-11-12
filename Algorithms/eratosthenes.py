
def eratosthenes(limit):
    """
    returns list of boolean values up to limit,
    if number n is prime, a[n] is true otherwise false
    """
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            for n in xrange(i*i, limit, i):
                a[n] = False
    return a
