import unittest

class GridTest(unittest.TestCase):

    def testExample(self):
        self.assertTrue(is_sorted(5, ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']))
        self.assertFalse(is_sorted(5, ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywcv']))

def is_sorted(N, G):
    for i, row in enumerate(G):
        G[i] = sorted(row)
    for column in xrange(N):
        for row in xrange(1, N):
            if G[row-1][column]>G[row][column]:
                return False
    return True


if __name__=='__main__':
    T = input()
    for t in xrange(T):
        N = input()
        G = []
        for n in xrange(N):
            G.append(raw_input())
        if is_sorted(N, G):
            print('YES')
        else:
            print('NO')
