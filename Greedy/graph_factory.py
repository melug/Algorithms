import unittest

class GraphTest(unittest.TestCase):

    def testTree(self):
        self.assertTrue(is_tree(3, [1, 2, 1]))

def is_tree(N, degrees):
    degrees.sort(reverse=True)
    for i in xrange(N):
        j = i+1
        while degrees[i]>0 and j<N:
            if degrees[j]>0:
                degrees[j] -= 1
                degrees[i] -= 1
            j += 1
        if degrees[i]!=0:
            return False
    return True

if __name__=='__main__':
    N = input()
    degrees = map(int, raw_input().split(' '))
    if is_tree(N, degrees):
        print('Yes')
    else:
        print('No')
