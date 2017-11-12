import unittest

class TestMaxNo(unittest.TestCase):

    def testMaxNo(self):
        self.assertEqual(max_no_activities([[3, 9], [2, 8], [6, 9]]), 1)
        self.assertEqual(max_no_activities([[1, 7], [5, 8], [7, 8], [1, 8]]), 2)
        self.assertEqual(max_no_activities([[7, 9], [0, 10], [4, 5], [8, 9], [4, 10], [5, 7]]), 3)


def max_no_activities(intervals):
    intervals.sort(key=lambda e:e[1])
    previous_interval = intervals[0]
    count = 1
    for i in xrange(1, len(intervals)):
        if previous_interval[1]<=intervals[i][0]:
            previous_interval = intervals[i]
            count += 1
    return count

if __name__=='__main__':
    T = input()
    for t in xrange(T):
        intervals = []
        N = input()
        for i in xrange(N):
            intervals.append(map(int, raw_input().split(' ')))
        print(max_no_activities(intervals))

