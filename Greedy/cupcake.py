import unittest

class MinWalkTest(unittest.TestCase):

    def testExample(self):
        self.assertEqual(min_walk(3, [1, 3, 2]), 11)

def min_walk(n, cupcakes):
    cupcakes.sort(reverse=True)
    total_walk = 0
    t = 1
    for cupcake in cupcakes:
        total_walk += t*cupcake
        t *= 2
    return total_walk

if __name__=='__main__':
    n = input()
    c = map(int, raw_input().split(' '))
    print(min_walk(n, c))
