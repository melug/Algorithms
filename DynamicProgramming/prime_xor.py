import unittest
import collections


def eratosthenes(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            for n in xrange(i*i, limit, i):
                a[n] = False
    return a


if __name__=='__main__':
    q = input()
    prime_numbers = eratosthenes(8200)
    base = 3500
    array = [0]*1001
    for i in xrange(q):
        n = input()
        for a in map(int, raw_input().split(' ')):
            array[a-base] += 1

        print(number_of_primes(n, a))
