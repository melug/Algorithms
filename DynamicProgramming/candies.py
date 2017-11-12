import unittest

class Test(unittest.TestCase):

    def testSections(self):
        self.assertEqual(split_into_sections([1, 2, 2]), [[0, 1], [2, 2]])
        self.assertEqual(split_into_sections([9, 8, 6, 6, 1]), [[0, 2], [3, 4]])
        self.assertEqual(split_into_sections([1, 2, 3]), [[0, 2]])

    def test_min_candies(self):
        self.assertEqual(_min_candies([1, 2], 0, 1), 3)
        self.assertEqual(_min_candies([9, 8, 6], 0, 2), 6)
        self.assertEqual(_min_candies([1, 2, 3], 0, 2), 6)

    def testMinCandies(self):
        self.assertEqual(min_candies([1, 2, 2]), 4)
        self.assertEqual(min_candies([9, 8, 6, 6, 1]), 9)
        self.assertEqual(min_candies([1, 2, 3]), 6)

def split_into_sections(scores):
    sections = []
    start = 0
    for i in xrange(1, len(scores)):
        if scores[i-1]==scores[i]:
            sections.append([start, i-1])
            start = i
    sections.append([start, i])
    return sections

def _min_candies(scores, start, end):
    ''' two adjacent kids cannot have same score '''
    candies = [1]
    min_encounter = 1
    for i in xrange(start+1, end+1):
        j = i-(start+1)
        if scores[i-1]<scores[i]:
            candies.append(candies[j]+1)
        else:
            candies.append(candies[j]-1)
            min_encounter = min(min_encounter, candies[j]-1)
    print('distribution', scores[start:end+1], candies)
    total_candies = sum(candies)
    return total_candies+(end-start+1)*(1-min_encounter)

def min_candies(scores):
    ''' two adjacent kids can have same score '''
    number_of_candies = 0
    for start, end in split_into_sections(scores):
        number_of_candies += _min_candies(scores, start, end)
    return number_of_candies

if __name__=='__main__':
    N = input()
    scores = []
    for i in xrange(N):
        scores.append(input())
    print(min_candies(scores))
