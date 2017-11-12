import unittest

class Test(unittest.TestCase):

    def test_min_candes(self):
        scores = [1, 5, 6, 4, 3, 2, 1]
        print('scores', scores)
        print('candies', min_candies(scores))
        scores = [5, 5, 5, 4, 4, 2, 1, 2, 2, 3, 3, 3, 4]
        print('scores', scores)
        print('candies', min_candies(scores))

def min_candies(scores):
    candies = [1]
    for i in xrange(1, len(scores)):
        if scores[i]>scores[i-1]:
            candies.append(candies[i-1]+1)
        elif scores[i]<scores[i-1]:
            candies.append(1)
            j = i
            while j>0 and scores[j]<scores[j-1] and candies[j]==candies[j-1]:
                candies[j-1] += 1
                j -= 1
        else:
            candies.append(1)
        #print(candies)
    return sum(candies)

if __name__=='__main__':
    N = input()
    scores = []
    for i in xrange(N):
        scores.append(input())
    print(min_candies(scores))
