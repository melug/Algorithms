import unittest

class Test(unittest.TestCase):

    def test1(self):
        self.assertEqual(number_of_candies([1, 6]), 23)

    def test2(self):
        self.assertEqual(number_of_candies([1, 2, 3]), 164)

def number_of_candies(N):
    S = N[0]
    T = S
    for i in xrange(1, len(N)):
        S = N[i]*(i+1)+S*10
        T += S
    return T

if __name__=='__main__':
    N = raw_input()
    print(number_of_candies(map(int, N)))
