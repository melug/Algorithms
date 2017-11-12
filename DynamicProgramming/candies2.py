import unittest

class Test(unittest.TestCase):
    pass

def min_candies(scores):
    s, e = 0, len(scores)-1
    if e==0:
        return 1
    local_minimas = []
    if scores[s]<=scores[s+1]:
        local_minimas.append(s)
    if scores[e]<=scores[e-1]:
        local_minimas.append(e)
    for i in xrange(1, e):
        if scores[i-1]>=scores[i]<=scores[i+1]:
            local_minimas.append(i)
    candies = [-1]*len(scores)
    #print('local_minimas', local_minimas)
    for minima in local_minimas:
        candies[minima] = 1
        while minima>0 and scores[minima-1]>scores[minima] and candies[minima]>=candies[minima-1]:
            candies[minima-1] = candies[minima]+1
            minima -= 1
        while minima<e and scores[minima+1]>scores[minima] and candies[minima]>=candies[minima+1]:
            candies[minima+1] = candies[minima]+1
            minima += 1
        #print('candies', candies)
    return sum(candies)

if __name__=='__main__':
    N = input()
    scores = []
    for i in xrange(N):
        scores.append(input())
    print(min_candies(scores))
